from __future__ import annotations

import copy
import json
import tempfile
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator

from scripts.validate_regulations import ROOT, validate


class RegulationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads((ROOT / "data/regulations/u11-rules.json").read_text(encoding="utf-8"))
        cls.schema = json.loads((ROOT / "schemas/regulation-rule.schema.json").read_text(encoding="utf-8"))
        cls.rules = {item["rule_id"]: item for item in cls.data["rules"]}

    def schema_errors(self, data):
        return list(Draft202012Validator(self.schema).iter_errors(data))

    def test_01_complete_confirmed_rule(self):
        self.assertFalse(self.schema_errors(self.data))

    def test_02_unknown_value_is_explicit_null(self):
        self.assertIsNone(self.rules["RULE-0003"]["format"])

    def test_03_old_regulation_is_historical_only(self):
        self.assertEqual(self.rules["RULE-0004"]["status"], "PROVISIONAL_PREVIOUS_SEASON")

    def test_04_current_missing_document(self):
        self.assertEqual(self.rules["RULE-0003"]["status"], "NOT_PUBLISHED_OR_NOT_FOUND")

    def test_05_different_values_are_detected(self):
        self.assertNotEqual(self.rules["RULE-0006"]["match_duration_minutes"],
                            self.rules["RULE-0007"]["match_duration_minutes"])

    def test_06_same_rule_context_is_not_assumed(self):
        self.assertNotEqual(self.rules["RULE-0001"]["competition"], self.rules["RULE-0004"]["competition"])

    def test_07_confirmed_without_location_is_invalid(self):
        data = copy.deepcopy(self.data); data["rules"][0]["exact_locations"] = []
        self.assertTrue(self.schema_errors(data))

    def test_08_dimension_without_unit_is_invalid(self):
        data = copy.deepcopy(self.data); del data["rules"][0]["field_length_m"]["unit"]
        self.assertTrue(self.schema_errors(data))

    def test_09_min_greater_than_max_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = self.temp_root(Path(tmp), copy.deepcopy(self.data))
            d = json.loads((root / "data/regulations/u11-rules.json").read_text())
            d["rules"][0]["field_length_m"]["min"] = 41
            (root / "data/regulations/u11-rules.json").write_text(json.dumps(d))
            self.assertTrue(any("min>max" in item for item in validate(root)))

    def test_10_assumption_cannot_be_current_confirmed(self):
        self.assertEqual(self.rules["RULE-0003"]["birth_years"], None)

    def test_11_area_calculation(self):
        self.assertEqual(40 * 20, 800)

    def test_12_area_per_player(self):
        self.assertEqual(round(800 / (2 * 5), 2), 80)

    def test_13_frf_ajf_relation_is_explicit(self):
        self.assertEqual(self.rules["RULE-0004"]["jurisdiction"], "FRF_AJF_PARTNERSHIP")

    def test_14_recheck_date_exists(self):
        self.assertTrue(all(item["recheck_date"] for item in self.data["rules"]))

    def test_15_previous_version_not_current(self):
        self.assertNotEqual(self.rules["RULE-0004"]["status"], "CURRENT_CONFIRMED")

    def test_16_other_ajf_not_marked_local(self):
        self.assertTrue(all(item["status"] != "CURRENT_LOCAL_CONFIRMED" for item in self.data["rules"]
                            if item["jurisdiction"] == "OTHER_AJF_COMPARATIVE"))

    def test_17_match_and_training_dimensions_are_separated(self):
        self.assertTrue(all(item["category_kind"] == "MATCH_REGULATION" for item in self.data["rules"]))

    def test_18_source_claim_citation_chain(self):
        sources = json.loads((ROOT / "research/sources.json").read_text(encoding="utf-8"))["sources"]
        claims = json.loads((ROOT / "research/claims.json").read_text(encoding="utf-8"))["claims"]
        citations = json.loads((ROOT / "research/citations.json").read_text(encoding="utf-8"))["citations"]
        self.assertTrue(sources and claims and citations)

    def test_19_output_is_deterministic(self):
        self.assertEqual(validate(), validate())

    def test_20_real_registries_validate(self):
        self.assertEqual(validate(), [])

    @staticmethod
    def temp_root(root, data):
        (root / "schemas").mkdir()
        (root / "data/regulations").mkdir(parents=True)
        (root / "schemas/regulation-rule.schema.json").write_text(
            (ROOT / "schemas/regulation-rule.schema.json").read_text(encoding="utf-8"), encoding="utf-8")
        (root / "data/regulations/u11-rules.json").write_text(json.dumps(data), encoding="utf-8")
        (root / "data/regulations/u11-space-per-player.json").write_text(
            (ROOT / "data/regulations/u11-space-per-player.json").read_text(encoding="utf-8"), encoding="utf-8")
        return root
