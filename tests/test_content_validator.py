from __future__ import annotations

import contextlib
import io
import json
import shutil
import tempfile
import unittest
from pathlib import Path

from scripts.validate_content import ContentValidator, main
from scripts.validation.codes import ERROR_CODES


ROOT = Path(__file__).resolve().parents[1]
CASES = json.loads((ROOT / "tests/fixtures/validation/cases.json").read_text(encoding="utf-8"))


class ValidatorFixtureTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        shutil.copytree(ROOT / "schemas", self.root / "schemas")
        for folder in ("config", "research", "data/principles", "data/exercises", "data/sessions",
                       "assets/manifests", "assets/diagrams", "reports/task-reports"):
            (self.root / folder).mkdir(parents=True, exist_ok=True)
        self.write_json("config/project.json", {
            "$schema": "../schemas/project.schema.json",
            "project_id": "manual-u11", "product_kind": "platformă web pedagogică profesională",
            "primary_delivery": "static_web", "pedagogical_first": True, "language": "ro",
            "age_category": {
                "label": "10–11 ani, grupele 2015 și 2016 tratate împreună",
                "birth_years": [2015, 2016], "single_curriculum": True,
                "individual_adaptation_dimensions": ["experiență"]
            },
            "future_age_architecture": {
                "production_scope": "10–11",
                "expansion_order": ["8–9", "6–7", "4–5", "12–13", "14–15", "16–18"]
            },
            "minimum_deliverables": {
                "volumes": 10, "exercises": 60, "sessions": 36,
                "communication_scripts": 50, "case_studies": 15
            },
            "canonical_registries": {
                "tasks": "TASK_REGISTRY.json", "task_history": "TASK_HISTORY.jsonl",
                "sources": "research/sources.json", "claims": "research/claims.json",
                "citations": "research/citations.json"
            }
        })
        self.write_json("config/visual-tokens.json", {
            "$schema": "../schemas/visual-tokens.schema.json", "version": "1.0.0",
            "roles": {"possession": {}, "opponent": {}, "neutral": {}, "goalkeeper": {}, "coach": {}},
            "paths": {"pass": "dashed", "off_ball_run": "solid", "dribble": "double", "change_of_direction": "curved"},
            "accessibility": {
                "color_is_never_the_only_signal": True, "svg_requires_title_and_description": True,
                "reduced_motion_required": True, "black_and_white_profile_required": True
            }
        })
        self.write_json("research/sources.json", {"$schema": "../schemas/source-registry.schema.json", "schema_version": "2.0.0", "sources": []})
        self.write_json("research/claims.json", {"$schema": "../schemas/claim-registry.schema.json", "schema_version": "2.0.0", "claims": []})
        self.write_json("research/citations.json", {"$schema": "../schemas/citation-registry.schema.json", "schema_version": "2.0.0", "citations": []})
        self.write_json("research/questions.json", {"$schema": "../schemas/research-question.schema.json", "schema_version": "1.0.0", "questions": []})
        self.write_json("research/archive-manifests.json", {"$schema": "../schemas/archive-manifest.schema.json", "schema_version": "1.0.0", "archives": []})
        (self.root / "research/search-logs.jsonl").write_text("", encoding="utf-8")
        self.write_json("TASK_REGISTRY.json", {"schema_version": "2.0.0", "tasks": []})
        (self.root / "TASK_HISTORY.jsonl").write_text("", encoding="utf-8")

    def tearDown(self):
        self.temp.cleanup()

    def write_json(self, relative: str, value):
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(value, ensure_ascii=False, indent=2), encoding="utf-8")

    def read_json(self, relative: str):
        return json.loads((self.root / relative).read_text(encoding="utf-8"))

    def source(self, source_id="SRC-0001"):
        return {
            "source_id": source_id, "title": "Ghid oficial pentru formare", "authors": ["Autor Test"],
            "organisation": "Organizație", "source_type": "OFFICIAL_GUIDANCE", "year": 2025,
            "published_at": "2025-01-01", "updated_at": None, "version": "1.0", "edition": None,
            "url": "https://example.invalid/document", "doi": None, "isbn": None, "language": "ro",
            "country": "RO", "accessed_at": "2026-07-30", "verified_at": "2026-07-30",
            "next_review_at": "2027-07-30", "archive": None, "sha256": None, "licence": "fixture",
            "usage_rights": {"store_snapshot": False, "public_distribution": False, "source_package": False,
                             "pdf": False, "web": False, "editable_package": False,
                             "commercial_use": None, "modification": None, "attribution": None},
            "access_status": "OPEN", "currency_status": "CURRENT", "confidence": "MODERATE",
            "population": "10–11 ani", "age_range": "10–11", "sport": "fotbal",
            "research_question_ids": [], "claim_ids": [],
            "limitations": ["Fixture, nu sursă editorială."], "researcher_notes": "Fixture sintetic.",
            "local_file": None, "supersedes_source_id": None, "superseded_by_source_id": None,
            "withdrawn": False, "visual_rights": None
        }

    def claim(self, source_ids=None):
        return {
            "claim_id": "CLM-0001", "statement": "Afirmație sintetică suficient de precisă pentru fixture.",
            "claim_type": "FACT", "domain": "TEST", "volume_id": "VOLUME-01", "chapter_id": None,
            "source_ids": ["SRC-0001"] if source_ids is None else source_ids,
            "source_locators": [{"kind": "SECTION", "value": "Fixture"}],
            "confidence": "MODERATE", "population": "10–11 ani", "limitations": [],
            "allowed_wording": "Formulare prudentă pentru test.",
            "forbidden_overstatements": ["Dovedește în toate cazurile."],
            "verified_at": "2026-07-30", "next_review_at": None, "status": "PROPOSED",
            "replacement_claim_id": None
        }

    def task(self, task_id="TASK-9001", status="PENDING"):
        return {
            "task_id": task_id, "title": "Task valid pentru fixture", "phase": "TEST",
            "volume": None, "status": status, "priority": "LOW", "dependencies": [],
            "outputs": ["config/project.json"], "acceptance_criteria": ["Criteriu verificabil."],
            "validation_commands": ["python scripts/validate_content.py"], "weight_percent": 1,
            "attempts": 0, "max_attempts": 1, "last_error": None,
            "created_at": "2026-07-30", "started_at": None, "completed_at": None
        }

    def message(self, msg_id="MSG-0001"):
        rationales = {
            "tactical": "Mesajul creează un unghi de sprijin pentru continuarea posesiei.",
            "perceptual": "Copilul caută adversarul și spațiul liber înainte să primească mingea.",
            "decisional": "Copilul alege unghiul care menține două opțiuni de continuare.",
            "cognitive": "Copilul compară două opțiuni și alege traseul cu presiune mai redusă.",
            "psychological": "Formularea lasă loc alegerii și protejează curajul de a încerca.",
            "technical": "Orientarea corpului permite primul control spre spațiul disponibil.",
            "social": "Mișcarea oferă colegului o opțiune clară și susține cooperarea."
        }
        return {
            "$schema": "../../schemas/message-foundation.schema.json", "id": msg_id,
            "message_type": "instruction", "child_wording": "Privește și oferă-i colegului un unghi.",
            "coach_meaning": "Jucătorul se repoziționează pentru a deschide o linie de pasă.",
            "why_this_wording": "Verbele indică informația și acțiunea fără a dicta poziția exactă.",
            "problem_being_solved": "Purtătorul mingii rămâne fără opțiune sigură de progresie.",
            "information_to_notice": ["poziția adversarului", "linia de pasă"],
            "interpretation": "Spațiul lateral este liber și poate fi ocupat.",
            "decision_to_learn": "Alege poziția care deschide linia de pasă.",
            "execution_support": "Schimbă viteza și orientează corpul spre teren.",
            "observable_behaviours": ["se deplasează din umbra adversarului"],
            "rationales": rationales, "age_appropriateness": "Un singur reper vizual și o alegere sunt gestionabile la 10–11 ani.",
            "phrases_to_avoid": [{"phrase": "Stai exact aici.", "reason": "Elimină observarea și alegerea."}],
            "misinterpretation_risks": ["Copilul se poate apropia prea mult de minge."],
            "task_risks": ["Apropierea excesivă poate reduce spațiul și timpul colegului."],
            "understanding_check": ["Arată două poziții și explică pe care o alegi."],
            "response_if_not_working": ["Oprește scurt și reduce numărul adversarilor."],
            "match_transfer": "Comportamentul reapare când purtătorul mingii este presat lateral.",
            "source_claim_ids": []
        }

    def apply_case(self, name: str):
        if name == "valid_document":
            return
        if name == "invalid_json":
            (self.root / "config/project.json").write_text("{", encoding="utf-8")
        elif name == "missing_schema":
            (self.root / "schemas/project.schema.json").unlink()
        elif name == "unknown_schema_version":
            schema = self.read_json("schemas/project.schema.json")
            schema["$schema"] = "https://json-schema.org/draft/2099-01/schema"
            self.write_json("schemas/project.schema.json", schema)
        elif name == "missing_required_field":
            data = self.read_json("config/project.json"); data.pop("project_id"); self.write_json("config/project.json", data)
        elif name == "empty_required_value":
            data = self.read_json("TASK_REGISTRY.json"); task = self.task(); task["title"] = ""; data["tasks"] = [task]; self.write_json("TASK_REGISTRY.json", data)
        elif name == "wrong_type":
            data = self.read_json("TASK_REGISTRY.json"); task = self.task(); task["dependencies"] = "TASK-0001"; data["tasks"] = [task]; self.write_json("TASK_REGISTRY.json", data)
        elif name == "duplicate_id":
            data = self.read_json("research/sources.json"); data["sources"] = [self.source(), self.source()]; self.write_json("research/sources.json", data)
        elif name == "duplicate_slug":
            item = {"$schema": "../../schemas/case-study.schema.json", "id": "CASE-0001", "slug": "acelasi-slug", "title": "Caz didactic", "scenario_type": "didactic", "principle_ids": ["PRI-9999"], "exercise_ids": [], "script_ids": [], "analysis": "Analiză suficient de lungă pentru a descrie problema didactică observată."}
            self.write_json("data/case-studies/batch.json", [item, {**item, "id": "CASE-0002"}])
        elif name == "broken_reference":
            data = self.read_json("research/claims.json"); data["claims"] = [self.claim(["SRC-9999"])]; self.write_json("research/claims.json", data)
        elif name == "reference_type_mismatch":
            data = self.read_json("research/claims.json"); data["claims"] = [self.claim(["CLM-0001"])]; self.write_json("research/claims.json", data)
        elif name == "forbidden_cycle":
            a, b = self.task("TASK-9001"), self.task("TASK-9002"); a["dependencies"] = ["TASK-9002"]; b["dependencies"] = ["TASK-9001"]; self.write_json("TASK_REGISTRY.json", {"schema_version": "2.0.0", "tasks": [a, b]})
        elif name == "missing_output":
            task = self.task(status="DONE"); task["outputs"] = ["missing.file"]; task["completed_at"] = "2026-07-30"; self.write_json("TASK_REGISTRY.json", {"schema_version": "2.0.0", "tasks": [task]}); (self.root / "TASK_HISTORY.jsonl").write_text(json.dumps({"task_id": "TASK-9001", "event": "COMPLETED"}) + "\n", encoding="utf-8"); (self.root / "reports/task-reports/TASK-9001.md").write_text("# raport", encoding="utf-8")
        elif name == "missing_report":
            task = self.task(status="DONE"); task["completed_at"] = "2026-07-30"; self.write_json("TASK_REGISTRY.json", {"schema_version": "2.0.0", "tasks": [task]}); (self.root / "TASK_HISTORY.jsonl").write_text(json.dumps({"task_id": "TASK-9001", "event": "COMPLETED"}) + "\n", encoding="utf-8")
        elif name == "placeholder":
            data = self.read_json("TASK_REGISTRY.json"); task = self.task(); task["title"] = "TODO validare"; data["tasks"] = [task]; self.write_json("TASK_REGISTRY.json", data)
        elif name == "pedagogy_missing":
            self.write_json("data/principles/item.json", {"id": "PRI-0001", "title": "Principiu incomplet"})
        elif name == "pedagogy_empty":
            item = self.message(); item["rationales"]["tactical"] = " "; self.write_json("data/principles/message.json", item)
        elif name == "claim_without_source":
            data = self.read_json("research/claims.json"); data["claims"] = [self.claim([])]; self.write_json("research/claims.json", data)
        elif name == "incomplete_source":
            data = self.read_json("research/sources.json"); item = self.source(); item.pop("title"); data["sources"] = [item]; self.write_json("research/sources.json", data)
        elif name == "citation_target_missing":
            data = self.read_json("research/citations.json"); data["citations"] = [{"citation_id": "CIT-0001", "claim_id": "CLM-9999", "source_id": "SRC-9999", "locator": {"kind": "PHYSICAL_PAGE", "value": "1", "physical_page": 1, "printed_page": None, "section_title": None, "anchor": None, "snapshot_sha256": None}, "document_version": "1.0", "usage_location": "content/lipsa.mdx", "support_type": "DIRECT", "direct_quote": None, "verified_at": "2026-07-30"}]; self.write_json("research/citations.json", data)
        elif name == "unregistered_asset":
            (self.root / "assets/diagrams/orphan.svg").write_text("<svg/>", encoding="utf-8")
        elif name == "asset_file_missing":
            self.write_json("assets/manifests/item.json", {"id": "VIS-0001", "subject_id": "EX-0001", "asset_type": "static", "editable_source": "assets/editable/missing.svg", "static_svg": "assets/diagrams/missing.svg", "dimensions": {"length_m": 20, "width_m": 15}, "safety_margin_m": 2, "attack_direction": "nord", "roles": [{"id": "A1"}], "ball_start": "A1", "coach_position": "lateral", "legend": [{"key": "A"}], "animation_data": None, "states": [], "accessibility": {"title": "Diagramă", "description": "Descriere accesibilă suficient de clară.", "non_color_cues": ["formă"], "keyboard_controlled": False, "reduced_motion": True}, "pdf_equivalent": {"frames": ["assets/diagrams/missing.svg"], "equivalent_information": True}})
        elif name == "exercise_missing_principle":
            self.write_json("data/exercises/item.json", {"id": "EX-0001", "principle_ids": ["PRI-9999"]})
        elif name == "session_missing_exercise":
            self.write_json("data/sessions/item.json", {"id": "SES-0001", "exercise_ids": ["EX-9999"]})
        elif name == "duplicate_content":
            item = self.message(); repeated = "Aceeași explicație contextuală este copiată identic în două câmpuri diferite."; item["rationales"]["tactical"] = repeated; item["rationales"]["perceptual"] = repeated; self.write_json("data/principles/message.json", item)
        else:
            raise AssertionError(name)

    def test_manifest_contains_25_required_cases(self):
        self.assertEqual(len(CASES), 25)

    def test_all_declared_cases(self):
        for case in CASES:
            with self.subTest(case=case["name"]):
                self.tearDown(); self.setUp()
                self.apply_case(case["name"])
                diagnostics = ContentValidator(self.root).run()
                codes = {item.code for item in diagnostics if item.severity == "ERROR"}
                if case["expected"] is None:
                    self.assertEqual(codes, set(), [item.to_dict() for item in diagnostics])
                else:
                    self.assertIn(case["expected"], codes, [item.to_dict() for item in diagnostics])
                    match = next(item for item in diagnostics if item.code == case["expected"])
                    self.assertEqual(match.severity, "ERROR")
                    self.assertTrue(match.file)
                    self.assertTrue(match.json_path)
                    with contextlib.redirect_stdout(io.StringIO()):
                        exit_code = main(["--root", str(self.root), "--format", "json"])
                    self.assertNotEqual(exit_code, 0)

    def test_cli_exit_codes_and_json_output(self):
        with contextlib.redirect_stdout(io.StringIO()) as output:
            valid_code = main(["--root", str(self.root), "--format", "json"])
        self.assertEqual(valid_code, 0)
        self.assertTrue(json.loads(output.getvalue())["valid"])
        self.apply_case("invalid_json")
        with contextlib.redirect_stdout(io.StringIO()) as output:
            invalid_code = main(["--root", str(self.root), "--format", "json"])
        self.assertEqual(invalid_code, 1)
        self.assertFalse(json.loads(output.getvalue())["valid"])

    def test_file_and_type_modes(self):
        self.assertEqual(ContentValidator(self.root).run("config/project.json"), [])
        items = ContentValidator(self.root).run(selected_type="source")
        self.assertEqual([item for item in items if item.severity == "ERROR"], [])

    def test_diagnostics_are_deterministic(self):
        self.apply_case("citation_target_missing")
        first = [item.to_dict() for item in ContentValidator(self.root).run()]
        second = [item.to_dict() for item in ContentValidator(self.root).run()]
        self.assertEqual(first, second)

    def test_required_error_codes_are_centralized(self):
        required = {
            "JSON_PARSE_ERROR", "SCHEMA_NOT_FOUND", "SCHEMA_VERSION_UNSUPPORTED", "SCHEMA_INVALID",
            "REQUIRED_FIELD_MISSING", "EMPTY_REQUIRED_VALUE", "INVALID_IDENTIFIER", "DUPLICATE_ID",
            "DUPLICATE_SLUG", "BROKEN_REFERENCE", "REFERENCE_TYPE_MISMATCH",
            "FORBIDDEN_REFERENCE_CYCLE", "OUTPUT_MISSING", "REPORT_MISSING",
            "UNREGISTERED_ASSET", "ASSET_FILE_MISSING", "UNUSED_REQUIRED_ASSET",
            "CLAIM_WITHOUT_SOURCE", "SOURCE_WITHOUT_REQUIRED_METADATA", "CITATION_TARGET_MISSING",
            "PLACEHOLDER_DETECTED", "PEDAGOGICAL_RATIONALE_MISSING",
            "PEDAGOGICAL_RATIONALE_INCOMPLETE", "DUPLICATE_CONTENT_DETECTED",
            "TASK_STATE_INCONSISTENT"
        }
        self.assertTrue(required <= ERROR_CODES)

    def test_strict_mode_promotes_warnings(self):
        data = self.read_json("research/sources.json")
        source = self.source()
        source["source_type"] = "OFFICIAL_REGULATION"
        source["version"] = None
        data["sources"] = [source]
        self.write_json("research/sources.json", data)
        normal = ContentValidator(self.root).run()
        strict = ContentValidator(self.root, strict=True).run()
        self.assertIn("WARNING", {item.severity for item in normal})
        self.assertNotIn("WARNING", {item.severity for item in strict})
        self.assertIn("ERROR", {item.severity for item in strict})

    def _install_production_evidence_fixture(self, include_citation=True, complete_metadata=True):
        source = self.source()
        claim = self.claim()
        if complete_metadata:
            claim.update({
                "epistemic_level": "MODERATE", "participant_age": "10–11 ani",
                "context": "FOOTBALL", "u11_applicability": "DIRECT",
                "practical_implication": "Antrenorul observă din nou înainte de concluzie."
            })
        self.write_json("research/sources.json", {"$schema": "../schemas/source-registry.schema.json", "schema_version": "2.0.0", "sources": [source]})
        self.write_json("research/claims.json", {"$schema": "../schemas/claim-registry.schema.json", "schema_version": "2.0.0", "claims": [claim]})
        citations = []
        if include_citation:
            citations.append({
                "citation_id": "CIT-0001", "claim_id": "CLM-0001", "source_id": "SRC-0001",
                "locator": {"kind": "SECTION", "value": "Fixture"}, "document_version": "1.0",
                "usage_location": "data/principles/production.json", "support_type": "DIRECT",
                "direct_quote": None, "verified_at": "2026-08-09"
            })
        self.write_json("research/citations.json", {"$schema": "../schemas/citation-registry.schema.json", "schema_version": "2.0.0", "citations": citations})
        principle = json.loads((ROOT / "data/principles/principle-variabilitatea-dezvoltarii-u11.json").read_text(encoding="utf-8"))
        principle["evidence_claim_ids"] = ["CLM-0001"]
        self.write_json("data/principles/production.json", principle)

    def test_production_claim_without_citation_is_rejected(self):
        self._install_production_evidence_fixture(include_citation=False)
        codes = {item.code for item in ContentValidator(self.root).run() if item.severity == "ERROR"}
        self.assertIn("CANONICAL_EVIDENCE_CHAIN_BROKEN", codes)

    def test_production_claim_without_epistemic_metadata_is_rejected(self):
        self._install_production_evidence_fixture(complete_metadata=False)
        codes = {item.code for item in ContentValidator(self.root).run() if item.severity == "ERROR"}
        self.assertIn("CANONICAL_EVIDENCE_METADATA_MISSING", codes)

    def test_citation_source_must_be_declared_by_claim(self):
        self._install_production_evidence_fixture()
        second = self.source("SRC-0002")
        data = self.read_json("research/sources.json")
        data["sources"].append(second)
        self.write_json("research/sources.json", data)
        citations = self.read_json("research/citations.json")
        citations["citations"][0]["source_id"] = "SRC-0002"
        self.write_json("research/citations.json", citations)
        codes = {item.code for item in ContentValidator(self.root).run() if item.severity == "ERROR"}
        self.assertIn("CITATION_SOURCE_MISMATCH", codes)


if __name__ == "__main__":
    unittest.main()
