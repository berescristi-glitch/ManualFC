import json
import re
import unittest
from pathlib import Path

try:
    import jsonschema
except ImportError:  # pragma: no cover
    jsonschema = None


ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = ROOT / "data/media/media-registry.json"
SCHEMA_PATH = ROOT / "schemas/media-registry.schema.json"
PROBLEM_LIBRARY_PATH = ROOT / "data/problems/problem-library.json"

EXERCISE_IDS = {"EX-0001", "EX-0002", "EX-0003", "EX-0004", "EX-0005"}


def load_registry():
    return json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))


def load_problem_ids():
    data = json.loads(PROBLEM_LIBRARY_PATH.read_text(encoding="utf-8"))
    return {p["problem_id"] for p in data["problems"]}


class MediaRegistrySchemaTests(unittest.TestCase):
    def test_registry_validates_against_schema(self):
        if jsonschema is None:
            self.skipTest("jsonschema not installed")
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        data = load_registry()
        jsonschema.validate(data, schema)

    def test_media_ids_are_unique(self):
        data = load_registry()
        ids = [m["media_id"] for m in data["media"]]
        self.assertEqual(len(ids), len(set(ids)), "duplicate media_id found")

    def test_canonical_refs_resolve_to_real_exercises_or_problems(self):
        data = load_registry()
        problem_ids = load_problem_ids()
        for entry in data["media"]:
            for ref in entry["canonical_refs"]:
                if entry["canonical_subject"] == "exercise":
                    self.assertIn(ref, EXERCISE_IDS, f"{entry['media_id']}: unknown exercise ref {ref}")
                else:
                    self.assertIn(ref, problem_ids, f"{entry['media_id']}: unknown problem ref {ref}")

    def test_animated_available_media_has_reduced_motion_fallback(self):
        data = load_registry()
        for entry in data["media"]:
            if entry["media_type"] in ("TACTICAL_LOOP", "EXERCISE_ANIMATION") and entry["status"] == "AVAILABLE":
                self.assertTrue(
                    entry.get("reduced_motion_fallback"),
                    f"{entry['media_id']}: animated AVAILABLE media without reduced_motion_fallback",
                )

    def test_coach_explainer_script_ready_entries_have_script(self):
        data = load_registry()
        for entry in data["media"]:
            if entry["media_type"] == "COACH_EXPLAINER" and entry["status"] == "SCRIPT_READY":
                self.assertIn("script", entry)
                script = entry["script"]
                for key in (
                    "ce_vezi", "de_ce_conteaza", "ce_ii_spui_copilului",
                    "ce_urmaresti", "greseala_frecventa_a_antrenorului", "ce_faci_mai_departe",
                ):
                    self.assertTrue(script.get(key), f"{entry['media_id']}: empty script.{key}")

    def test_no_media_claims_real_footage(self):
        data = load_registry()
        for entry in data["media"]:
            self.assertNotEqual(entry["evidence_boundary"], "REAL_FOOTAGE", f"{entry['media_id']}: fabricated real footage claim")

    def test_static_only_exercises_document_why(self):
        data = load_registry()
        by_ref = {}
        for entry in data["media"]:
            for ref in entry["canonical_refs"]:
                by_ref.setdefault(ref, []).append(entry["media_type"])
        for ex_id in ("EX-0004", "EX-0005"):
            types = by_ref.get(ex_id, [])
            self.assertNotIn("TACTICAL_LOOP", types)
            self.assertNotIn("EXERCISE_ANIMATION", types)
        static_entries = {e["media_id"]: e for e in data["media"] if e["media_type"] == "STATIC_TACTICAL_IMAGE"}
        self.assertTrue(static_entries["MED-STATIC-EX-0004"]["reason_not_animated"])
        self.assertTrue(static_entries["MED-STATIC-EX-0005"]["reason_not_animated"])

    def test_gold_standard_flagship_coverage_present(self):
        data = load_registry()
        by_type_ref = {(e["media_type"], ref) for e in data["media"] for ref in e["canonical_refs"]}
        for ex_id in EXERCISE_IDS:
            self.assertIn(("STATIC_TACTICAL_IMAGE", ex_id), by_type_ref, f"missing static visual for {ex_id}")
        for ex_id in ("EX-0001", "EX-0002", "EX-0003"):
            self.assertIn(("TACTICAL_LOOP", ex_id), by_type_ref, f"missing tactical loop for {ex_id}")
        self.assertIn(("EXERCISE_ANIMATION", "EX-0001"), by_type_ref)
        for prb_id in ("PRB-0001", "PRB-0002", "PRB-0003"):
            self.assertIn(("COACH_EXPLAINER", prb_id), by_type_ref, f"missing coach explainer for {prb_id}")


class MediaLoaderIntegrationTests(unittest.TestCase):
    def test_loader_registers_fail_closed_validation(self):
        source = (ROOT / "app/src/lib/media-registry.ts").read_text(encoding="utf-8")
        self.assertIn("export function validateMediaRegistry(): true", source)
        self.assertIn("FAIL_CLOSED", source)
        self.assertIn("validateMediaRegistry();", source)

    def test_concept_loop_component_covers_three_new_variants(self):
        source = (ROOT / "app/src/components/ConceptLoop.astro").read_text(encoding="utf-8")
        for variant in ("ex-0002", "ex-0003", "prb-0003"):
            self.assertIn(f"'{variant}'", source)
        self.assertIn("prefers-reduced-motion", source)
        self.assertIn("data-concept-loop", source)

    def test_concept_loop_uses_distinct_toggle_attribute_from_tactical_loop(self):
        concept = (ROOT / "app/src/components/ConceptLoop.astro").read_text(encoding="utf-8")
        tactical = (ROOT / "app/src/components/TacticalLoop.astro").read_text(encoding="utf-8")
        self.assertNotIn("data-tactical-loop", concept)
        self.assertIn("data-tactical-loop", tactical)

    def test_exercise_sequence_animation_has_restart_and_transcript(self):
        source = (ROOT / "app/src/components/ExerciseSequenceAnimation.astro").read_text(encoding="utf-8")
        self.assertIn("data-loop-restart", source)
        self.assertIn("exseq-transcript", source)
        self.assertIn("prefers-reduced-motion", source)
        self.assertIn("reprezentare comprimată", source)

    def test_gold_standard_exercise_page_wires_media_by_id(self):
        source = (ROOT / "app/src/pages/gold-standard/exercitii/[id].astro").read_text(encoding="utf-8")
        self.assertIn("ExerciseSequenceAnimation", source)
        self.assertIn("ConceptLoop", source)
        self.assertIn("ex-0002", source)
        self.assertIn("ex-0003", source)

    def test_problem_page_wires_explainer_and_prb0003_loop(self):
        source = (ROOT / "app/src/pages/rezolva-pe-teren/[slug].astro").read_text(encoding="utf-8")
        self.assertIn("CoachExplainerScript", source)
        self.assertIn("getCoachExplainer", source)
        self.assertIn("prb-0003", source)


if __name__ == "__main__":
    unittest.main()
