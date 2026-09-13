from __future__ import annotations

import argparse
import copy
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from datetime import date
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

from scripts.research_tool import (
    ResearchError,
    add_search,
    add_source,
    duplicate_matches,
    duplicate_report,
    freshness_report,
    prepare_source,
)
from scripts.validate_content import ContentValidator

ROOT = Path(__file__).resolve().parents[1]


def rights(store=True, public=True):
    return {
        "store_snapshot": store, "public_distribution": public,
        "source_package": public, "pdf": public, "web": public,
        "editable_package": public, "commercial_use": False,
        "modification": False, "attribution": "Fixture attribution",
    }


def source_payload(**changes):
    item = {
        "title": "Synthetic research fixture",
        "authors": ["Fixture Author"],
        "organisation": "Fixture Organisation",
        "source_type": "OFFICIAL_GUIDANCE",
        "year": 2026,
        "published_at": "2026-01-01",
        "updated_at": None,
        "version": "1.0",
        "edition": None,
        "url": "https://example.invalid/research",
        "doi": None,
        "isbn": None,
        "language": "en",
        "country": "RO",
        "accessed_at": "2026-07-30",
        "verified_at": "2026-07-30",
        "next_review_at": "2027-07-30",
        "archive": None,
        "sha256": None,
        "licence": "Fixture licence",
        "usage_rights": rights(),
        "access_status": "OPEN",
        "currency_status": "CURRENT",
        "confidence": "MODERATE",
        "population": "Synthetic U11 fixture",
        "age_range": "10–11",
        "sport": "football",
        "research_question_ids": [],
        "claim_ids": [],
        "limitations": ["Synthetic fixture; no factual use."],
        "researcher_notes": "Test only.",
        "local_file": None,
        "supersedes_source_id": None,
        "superseded_by_source_id": None,
        "withdrawn": False,
        "visual_rights": None,
    }
    item.update(changes)
    return item


class ResearchProtocolTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        shutil.copytree(ROOT / "schemas", self.root / "schemas")
        (self.root / "research").mkdir()
        (self.root / "research" / "sources.json").write_text(
            '{"schema_version":"2.0.0","sources":[]}\n', encoding="utf-8")
        (self.root / "research" / "questions.json").write_text(
            '{"schema_version":"1.0.0","questions":[]}\n', encoding="utf-8")
        (self.root / "research" / "search-logs.jsonl").write_text("", encoding="utf-8")

    def tearDown(self):
        self.temp.cleanup()

    def input_file(self, data, name="input.json"):
        path = self.root / name
        path.write_text(json.dumps(data), encoding="utf-8")
        return path

    def add(self, data):
        return add_source(argparse.Namespace(
            root=self.root, input=self.input_file(data), file=None))

    def source_schema(self):
        schema = json.loads((self.root / "schemas/source-registry.schema.json").read_text(encoding="utf-8"))
        return schema["properties"]["sources"]["items"]

    def assert_schema_rejected(self, item, schema_name, item_path):
        schema = json.loads((self.root / "schemas" / schema_name).read_text(encoding="utf-8"))
        for key in item_path:
            schema = schema[key]
        errors = list(Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(item))
        self.assertTrue(errors)

    def test_01_valid_source_registration(self):
        self.assertEqual(self.add(source_payload()), {"added": "SRC-0001"})

    def test_02_source_without_title_is_rejected(self):
        item = source_payload(title="")
        with self.assertRaises(ResearchError):
            self.add(item)

    def test_03_source_without_type_is_rejected(self):
        item = source_payload()
        del item["source_type"]
        with self.assertRaises(ResearchError):
            self.add(item)

    def test_04_duplicate_doi_is_detected(self):
        first = prepare_source(source_payload(doi="10.9999/FIXTURE", url=None), [], None)
        second = prepare_source(source_payload(doi="https://doi.org/10.9999/fixture", url=None), [first], None)
        self.assertEqual(duplicate_matches(second, [first])[0]["exact_identifiers"], ["DOI"])

    def test_05_normalized_url_duplicate_is_detected(self):
        first = prepare_source(source_payload(url="HTTPS://EXAMPLE.INVALID/a/?utm_source=x"), [], None)
        second = prepare_source(source_payload(url="https://example.invalid/a"), [first], None)
        self.assertIn("URL", duplicate_matches(second, [first])[0]["exact_identifiers"])

    def test_06_duplicate_hash_is_detected(self):
        first = prepare_source(source_payload(sha256="a" * 64), [], None)
        second = prepare_source(source_payload(sha256="a" * 64), [first], None)
        self.assertIn("SHA256", duplicate_matches(second, [first])[0]["exact_identifiers"])

    def test_07_two_valid_editions_remain_separate(self):
        first = prepare_source(source_payload(url=None, edition="1"), [], None)
        second = prepare_source(source_payload(url=None, edition="2"), [first], None)
        self.assertEqual(duplicate_matches(second, [first]), [])

    def test_08_circular_version_relation_is_rejected(self):
        self.assertIn("VERSION_CYCLE", (ROOT / "scripts/validation/codes.py").read_text(encoding="utf-8"))
        graph = {"SRC-0001": ["SRC-0002"], "SRC-0002": ["SRC-0001"]}
        self.assertIsNotNone(ContentValidator._find_cycle(graph))

    def test_09_expired_source_is_reported(self):
        item = prepare_source(source_payload(next_review_at="2025-01-01"), [], None)
        data = {"schema_version": "2.0.0", "sources": [item]}
        (self.root / "research/sources.json").write_text(json.dumps(data), encoding="utf-8")
        result = freshness_report(argparse.Namespace(root=self.root, as_of="2026-01-01"))
        self.assertEqual(result["expired"], ["SRC-0001"])

    def test_10_claim_without_source_is_rejected(self):
        schema = json.loads((self.root / "schemas/claim-registry.schema.json").read_text(encoding="utf-8"))
        item_schema = schema["properties"]["claims"]["items"]
        self.assertTrue(list(Draft202012Validator(item_schema).iter_errors({"claim_id": "CLM-0001"})))

    def test_11_citation_without_locator_is_rejected(self):
        item = {"citation_id": "CIT-0001", "claim_id": "CLM-0001", "source_id": "SRC-0001"}
        self.assert_schema_rejected(item, "citation-registry.schema.json", ["properties", "citations", "items"])

    def test_12_visual_source_without_licence_is_rejected(self):
        item = prepare_source(source_payload(source_type="VISUAL_ASSET_SOURCE", licence=None), [], None)
        self.assertTrue(list(Draft202012Validator(self.source_schema()).iter_errors(item)))

    def test_13_archive_without_manifest_code_is_integrated(self):
        snapshots = self.root / "research/source-snapshots"
        snapshots.mkdir()
        (snapshots / "orphan.bin").write_bytes(b"fixture")
        validator = ContentValidator(self.root)
        validator._validate_assets()
        self.assertIn("ARCHIVE_MANIFEST_MISSING", {item.code for item in validator.diagnostics})

    def test_14_restricted_public_asset_code_is_integrated(self):
        manifest = {
            "archive_id": "ARCH-0001", "source_id": "SRC-0001",
            "path": "research/source-snapshots/missing.bin", "sha256": "a" * 64,
            "size_bytes": 1, "archived_at": "2026-07-30T10:00:00Z",
            "licence": "Restricted fixture", "storage_level": "C_REFERENCE_ONLY",
            "distribution_status": "PUBLIC",
        }
        validator = ContentValidator(self.root)
        validator.documents = [("research/archive-manifests.json", "archive-manifest",
                                {"archives": [manifest]})]
        validator.ids_by_type["source"].add("SRC-0001")
        validator._validate_assets()
        codes = {item.code for item in validator.diagnostics}
        self.assertIn("RESTRICTED_ASSET_IN_PUBLIC_DISTRIBUTION", codes)

    def test_15_search_without_query_is_rejected(self):
        item = self.valid_search(query="")
        self.assert_schema_rejected(item, "search-log.schema.json", [])

    def test_16_exclusion_without_reason_is_rejected(self):
        item = self.valid_search(excluded_results=[{"title_or_id": "fixture"}])
        self.assert_schema_rejected(item, "search-log.schema.json", [])

    def valid_search(self, **changes):
        item = {
            "search_id": "SEARCH-0001", "research_question_id": "RQ-0001",
            "platform": "Fixture Index", "query": "fixture", "filters": {},
            "searched_at": "2026-07-30T10:00:00Z", "language": "en",
            "date_range": None, "results_count": 0, "screened_count": 0,
            "included_source_ids": [], "excluded_results": [], "notes": "",
            "performed_by": "test-suite",
        }
        item.update(changes)
        return item

    def test_17_withdrawn_source_is_reported(self):
        item = prepare_source(source_payload(withdrawn=True, currency_status="WITHDRAWN"), [], None)
        (self.root / "research/sources.json").write_text(
            json.dumps({"schema_version": "2.0.0", "sources": [item]}), encoding="utf-8")
        result = freshness_report(argparse.Namespace(root=self.root, as_of="2026-07-30"))
        self.assertEqual(result["withdrawn"], ["SRC-0001"])

    def test_18_duplicate_report_is_deterministic(self):
        first = prepare_source(source_payload(), [], None)
        second = prepare_source(source_payload(), [first], None)
        (self.root / "research/sources.json").write_text(
            json.dumps({"schema_version": "2.0.0", "sources": [first, second]}), encoding="utf-8")
        args = argparse.Namespace(root=self.root)
        self.assertEqual(duplicate_report(args), duplicate_report(args))

    def test_19_general_validator_compatibility(self):
        result = subprocess.run(
            [sys.executable, "scripts/validate_project.py"],
            cwd=ROOT, text=True, capture_output=True, check=False)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_20_fixture_tests_do_not_change_real_registries(self):
        paths = [ROOT / "research/sources.json", ROOT / "research/claims.json",
                 ROOT / "research/citations.json"]
        before = {p: hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
        self.add(source_payload())
        after = {p: hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
        self.assertEqual(before, after)


if __name__ == "__main__":
    unittest.main()
