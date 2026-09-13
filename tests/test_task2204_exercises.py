import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXERCISE_DIR = ROOT / "data" / "exercises"


def load(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def load_exercise(filename):
    return json.loads((EXERCISE_DIR / filename).read_text(encoding="utf-8"))


class Task2204ExerciseSystemTests(unittest.TestCase):
    EXERCISE_FILES = [
        "exercise-recunoasterea-umbrei-defensive.json",
        "exercise-creeaza-optiunea-sub-presiune.json",
        "exercise-primeste-gata-sa-continui.json",
        "exercise-sprijin-cu-doi-coechipieri.json",
        "exercise-transferul-in-joc-mic.json",
    ]

    def test_five_exercise_files_exist(self):
        for filename in self.EXERCISE_FILES:
            self.assertTrue((EXERCISE_DIR / filename).exists(), filename)

    def test_ids_are_unique_and_sequential(self):
        ids = [load_exercise(f)["id"] for f in self.EXERCISE_FILES]
        self.assertEqual(ids, ["EX-0001", "EX-0002", "EX-0003", "EX-0004", "EX-0005"])

    def test_age_category_matches_schema_const(self):
        for filename in self.EXERCISE_FILES:
            ex = load_exercise(filename)
            self.assertEqual(ex["age_category"], "10–11 ani, grupe 2015 și 2016 tratate împreună")

    def test_required_schema_fields_present(self):
        schema = json.loads((ROOT / "schemas/exercise.schema.json").read_text(encoding="utf-8"))
        required = schema["required"]
        for filename in self.EXERCISE_FILES:
            ex = load_exercise(filename)
            for field in required:
                self.assertIn(field, ex, f"{filename} missing {field}")

    def test_rationales_have_all_seven_dimensions(self):
        dims = {"tactical", "perceptual", "decisional", "cognitive", "psychological", "technical", "social"}
        for filename in self.EXERCISE_FILES:
            ex = load_exercise(filename)
            self.assertEqual(set(ex["rationales"].keys()), dims, filename)
            for v in ex["rationales"].values():
                self.assertTrue(v.strip(), filename)

    def test_no_unsupported_exact_angle_presented_as_validated(self):
        # "45 de grade" may appear only inside phrases_to_avoid (an explicit
        # debunked example), never presented as a validated instruction elsewhere.
        for filename in self.EXERCISE_FILES:
            ex = load_exercise(filename)
            avoid_text = json.dumps(ex.get("phrases_to_avoid", []), ensure_ascii=False)
            rest = dict(ex)
            rest.pop("phrases_to_avoid", None)
            rest_text = json.dumps(rest, ensure_ascii=False)
            self.assertNotIn("45°", rest_text)
            if "45 de grade" in avoid_text + rest_text:
                self.assertNotIn("45 de grade", rest_text, f"{filename}: exact angle presented outside phrases_to_avoid")

    def test_dimension_rationale_labels_numbers_as_exercise_specific(self):
        # PHASE-25: the internal "EXERCISE_SPECIFIC_PARAMETER" token was rendered
        # verbatim in product UI (a real defect, closed in PHASE-25). The epistemic
        # guarantee this test protects — field dimensions are labeled as a choice
        # specific to the exercise, not a research-validated threshold — is now
        # expressed in natural Romanian instead of a raw internal marker.
        for filename in self.EXERCISE_FILES:
            ex = load_exercise(filename)
            rationale = ex["dimension_rationale"]
            self.assertNotIn("EXERCISE_SPECIFIC_PARAMETER", rationale, filename)
            self.assertIn("acestui exercițiu", rationale, filename)
            self.assertTrue(
                "prag" in rationale or "validat" in rationale,
                f"{filename}: expected a not-a-research-threshold caveat in: {rationale}"
            )

    def test_no_withdrawn_source_referenced(self):
        sources = {s["source_id"]: s for s in load("research/sources.json")["sources"]}
        for filename in self.EXERCISE_FILES:
            ex = load_exercise(filename)
            for sid in ex["sources"]:
                self.assertIn(sid, sources, f"{filename} references unknown {sid}")
                self.assertFalse(sources[sid]["withdrawn"], f"{filename} references withdrawn {sid}")

    def test_progression_reuses_v02_and_v04_frameworks_not_reinvented(self):
        # PHASE-25: bare "CH-0404" chapter codes rendered verbatim in product UI
        # (meaningless to a coach with no link) are a defect, closed in
        # PHASE-25 — the source is now named in plain language instead.
        # PHASE-25: a bare internal slug ("principle-spatiu-si-unghiuri") rendered
        # verbatim in product UI is a defect, closed in PHASE-25 — the principle
        # is now named in plain language instead.
        ex1 = load_exercise("exercise-recunoasterea-umbrei-defensive.json")
        self.assertNotIn("principle-spatiu-si-unghiuri", ex1["why_this_message"])
        self.assertIn("Spațiu și unghiuri", ex1["why_this_message"])
        ex4 = load_exercise("exercise-sprijin-cu-doi-coechipieri.json")
        self.assertNotIn("CH-0404", ex4["rules"][1]["why"])
        self.assertIn("observare și criteriile de intervenție", ex4["rules"][1]["why"])

    def test_technical_dimension_exercise_avoids_single_correct_technique_claim(self):
        # PHASE-25: raw internal claim codes (CLM-xxxx) rendered verbatim in
        # product UI are a defect, closed in PHASE-25. The guarantee this test
        # protects — no single "correct" reception technique is claimed — is
        # checked via the natural-language statement itself.
        ex3 = load_exercise("exercise-primeste-gata-sa-continui.json")
        text = json.dumps(ex3, ensure_ascii=False)
        self.assertNotIn("CLM-0103", text)
        self.assertIn("nu există o tehnică de recepție «corectă» unică validată", text)
        self.assertIn("focus atențional extern", text)

    def test_transfer_exercise_marks_field_validation_pending(self):
        # PHASE-25: the raw "FIELD_VALIDATION_PENDING" enum rendered verbatim in
        # product UI is a defect, closed in PHASE-25; the same status is now
        # expressed in natural Romanian.
        ex5 = load_exercise("exercise-transferul-in-joc-mic.json")
        self.assertNotIn("FIELD_VALIDATION_PENDING", ex5["match_transfer"])
        self.assertIn("neconfirmat", ex5["match_transfer"])
        self.assertIn("pilotare reală pe teren", ex5["match_transfer"])

    def test_observable_behaviours_within_schema_limits(self):
        for filename in self.EXERCISE_FILES:
            ex = load_exercise(filename)
            self.assertGreaterEqual(len(ex["observable_behaviours"]), 1)
            self.assertLessEqual(len(ex["observable_behaviours"]), 3)

    def test_common_errors_separate_observation_from_causes(self):
        for filename in self.EXERCISE_FILES:
            ex = load_exercise(filename)
            for err in ex["common_errors"]:
                self.assertIn("observation", err)
                self.assertIn("possible_causes", err)
                self.assertIsInstance(err["possible_causes"], list)
                self.assertGreaterEqual(len(err["possible_causes"]), 1)


if __name__ == "__main__":
    unittest.main()
