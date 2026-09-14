import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXERCISE_DIR = ROOT / "data" / "exercises"
SESSION_DIR = ROOT / "data" / "sessions"
ASSESSMENT_PATH = ROOT / "data" / "assessments" / "assessment-sprijin-si-unghi-de-pasa.json"
PROBLEM_LIBRARY_PATH = ROOT / "data" / "problems" / "problem-library.json"


def load(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def load_exercise(filename):
    return json.loads((EXERCISE_DIR / filename).read_text(encoding="utf-8"))


def load_session(filename):
    return json.loads((SESSION_DIR / filename).read_text(encoding="utf-8"))


class Task3712NewExerciseTests(unittest.TestCase):
    EXERCISE_FILES = [
        "exercise-unghiul-de-sprijin-din-spate.json",
        "exercise-unu-doi-pentru-a-iesi-din-umbra.json",
        "exercise-al-treilea-jucator-de-sprijin.json",
        "exercise-receptie-sub-presiune-completa.json",
        "exercise-momentul-potrivit-de-plecare.json",
        "exercise-patru-sprijiniri-o-singura-minge.json",
        "exercise-prima-privire-dupa-recuperare.json",
        "exercise-sprijin-pe-culoar-lateral.json",
        "exercise-joc-mic-3v3-doua-porti.json",
        "exercise-joc-mic-5v5-zona-de-finalizare.json",
    ]
    EXPECTED_IDS = [f"EX-{n:04d}" for n in range(6, 16)]

    def test_ten_new_exercise_files_exist(self):
        for filename in self.EXERCISE_FILES:
            self.assertTrue((EXERCISE_DIR / filename).exists(), filename)

    def test_ids_are_unique_and_sequential(self):
        ids = [load_exercise(f)["id"] for f in self.EXERCISE_FILES]
        self.assertEqual(ids, self.EXPECTED_IDS)

    def test_all_stay_in_the_existing_theme(self):
        # TASK-3712 explicitly forbids introducing a second training theme.
        for filename in self.EXERCISE_FILES:
            ex = load_exercise(filename)
            self.assertEqual(ex["theme"], "sprijin-si-unghi-de-pasa", filename)

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

    def test_rationales_have_all_seven_dimensions_and_are_non_empty(self):
        dims = {"tactical", "perceptual", "decisional", "cognitive", "psychological", "technical", "social"}
        for filename in self.EXERCISE_FILES:
            ex = load_exercise(filename)
            self.assertEqual(set(ex["rationales"].keys()), dims, filename)
            for v in ex["rationales"].values():
                self.assertTrue(v.strip(), filename)

    def test_v2_fields_present_per_validator_contract(self):
        # Mirrors the fields scripts/validate_gold_standard_v2.py enforces for
        # any exercise declaring gold_standard_v2.status == "V2".
        required_v2 = [
            "pedagogical_principle_ids", "pedagog_competency_ids", "coach_competency_ids",
            "child_action", "coach_focus", "do_not_assume", "when_to_intervene",
            "when_not_to_intervene", "coach_common_errors", "coach_reflection",
            "evidence_boundary", "assessment_ref",
        ]
        for filename in self.EXERCISE_FILES:
            ex = load_exercise(filename)
            self.assertEqual(ex.get("gold_standard_v2", {}).get("status"), "V2", filename)
            for field in required_v2:
                value = ex.get(field)
                self.assertTrue(value not in (None, "", []), f"{filename} missing/empty {field}")

    def test_assessment_ref_points_to_real_assessment(self):
        for filename in self.EXERCISE_FILES:
            ex = load_exercise(filename)
            self.assertEqual(ex["assessment_ref"], "ASM-0001", filename)

    def test_no_withdrawn_source_referenced(self):
        sources = {s["source_id"]: s for s in load("research/sources.json")["sources"]}
        for filename in self.EXERCISE_FILES:
            ex = load_exercise(filename)
            for sid in ex["sources"]:
                self.assertIn(sid, sources, f"{filename} references unknown {sid}")
                self.assertFalse(sources[sid]["withdrawn"], f"{filename} references withdrawn {sid}")

    def test_message_related_claims_referenced_are_real(self):
        claims = {c["claim_id"] for c in load("research/claims.json")["claims"]}
        for filename in self.EXERCISE_FILES:
            ex = load_exercise(filename)
            text = json.dumps(ex, ensure_ascii=False)
            for clm in re.findall(r"CLM-\d{4,}", text):
                self.assertIn(clm, claims, f"{filename} references unknown {clm}")

    def test_visual_assets_remain_pending_no_design_freeze_violation(self):
        for filename in self.EXERCISE_FILES:
            ex = load_exercise(filename)
            for key in ("static_svg", "animation_or_storyboard", "pdf_frames"):
                self.assertIn("PENDING", ex["visual_assets"][key], f"{filename}.{key}")

    def test_dimension_rationale_labels_numbers_as_exercise_specific(self):
        for filename in self.EXERCISE_FILES:
            ex = load_exercise(filename)
            rationale = ex["dimension_rationale"]
            self.assertNotIn("EXERCISE_SPECIFIC_PARAMETER", rationale, filename)
            self.assertTrue(
                "prag" in rationale or "validat" in rationale,
                f"{filename}: expected a not-a-research-threshold caveat in: {rationale}",
            )

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
                self.assertGreaterEqual(len(err["possible_causes"]), 1)

    def test_no_invented_exact_angle_presented_as_validated(self):
        for filename in self.EXERCISE_FILES:
            ex = load_exercise(filename)
            self.assertNotIn("45°", json.dumps(ex, ensure_ascii=False))


class Task3712NewSessionTests(unittest.TestCase):
    SESSION_FILES = [
        "session-sprijin-din-spate-si-combinatie.json",
        "session-al-treilea-jucator-si-presiune.json",
        "session-recuperare-si-sprijin-lateral.json",
        "session-transfer-complet-jocuri-variate.json",
    ]
    EXPECTED_IDS = ["SES-0003", "SES-0004", "SES-0005", "SES-0006"]

    def test_four_new_session_files_exist(self):
        for filename in self.SESSION_FILES:
            self.assertTrue((SESSION_DIR / filename).exists(), filename)

    def test_ids_are_sequential(self):
        ids = [load_session(f)["id"] for f in self.SESSION_FILES]
        self.assertEqual(ids, self.EXPECTED_IDS)

    def test_duration_matches_schema_enum(self):
        for filename in self.SESSION_FILES:
            ses = load_session(filename)
            self.assertIn(ses["duration_min"], (60, 75, 90))

    def test_segments_are_contiguous_and_cover_full_duration(self):
        for filename in self.SESSION_FILES:
            ses = load_session(filename)
            segments = sorted(ses["segments"], key=lambda s: s["start_min"])
            self.assertEqual(segments[0]["start_min"], 0)
            self.assertEqual(segments[-1]["end_min"], ses["duration_min"])
            for a, b in zip(segments, segments[1:]):
                self.assertEqual(a["end_min"], b["start_min"], f"{filename}: gap/overlap between segments")

    def test_60min_variant_is_contiguous_and_matches_segment_count(self):
        for filename in self.SESSION_FILES:
            ses = load_session(filename)
            v60 = sorted(ses["duration_variant_60min"]["segments"], key=lambda s: s["start_min"])
            self.assertEqual(len(v60), len(ses["segments"]), filename)
            self.assertEqual(v60[0]["start_min"], 0, filename)
            self.assertEqual(v60[-1]["end_min"], 60, filename)
            for a, b in zip(v60, v60[1:]):
                self.assertEqual(a["end_min"], b["start_min"], f"{filename}: 60min gap/overlap")

    def test_at_least_three_segments(self):
        for filename in self.SESSION_FILES:
            ses = load_session(filename)
            self.assertGreaterEqual(len(ses["segments"]), 3)

    def test_every_segment_answers_why_now(self):
        for filename in self.SESSION_FILES:
            ses = load_session(filename)
            for seg in ses["segments"]:
                self.assertTrue(seg["why_now"].strip(), f"{filename}: {seg['title']}")

    def test_exercise_ids_referenced_exist(self):
        known_ids = {json.loads(f.read_text(encoding="utf-8"))["id"] for f in EXERCISE_DIR.glob("exercise-*.json")}
        for filename in self.SESSION_FILES:
            ses = load_session(filename)
            for seg in ses["segments"]:
                for eid in seg["exercise_ids"]:
                    self.assertIn(eid, known_ids, f"{filename}: unknown {eid}")

    def test_expected_exercise_progression_per_session(self):
        expected = {
            "SES-0003": ["EX-0006", "EX-0007"],
            "SES-0004": ["EX-0008", "EX-0009", "EX-0010"],
            "SES-0005": ["EX-0011", "EX-0012", "EX-0013"],
            "SES-0006": ["EX-0014", "EX-0015"],
        }
        for filename in self.SESSION_FILES:
            ses = load_session(filename)
            ids = [eid for seg in ses["segments"] for eid in seg["exercise_ids"]]
            self.assertEqual(ids, expected[ses["id"]], filename)

    def test_v2_fields_present_per_validator_contract(self):
        for filename in self.SESSION_FILES:
            ses = load_session(filename)
            self.assertEqual(ses.get("gold_standard_v2", {}).get("status"), "V2", filename)
            self.assertTrue(ses.get("child_objectives"), filename)
            self.assertTrue(ses.get("coach_objectives"), filename)
            rv2 = ses.get("reflection_v2") or {}
            self.assertTrue(rv2.get("child_game_dimension"), filename)
            self.assertTrue(rv2.get("coach_dimension"), filename)

    def test_reflection_present_and_no_fabricated_duration(self):
        for filename in self.SESSION_FILES:
            ses = load_session(filename)
            self.assertGreaterEqual(len(ses["reflection"]), 1)
            text = json.dumps(ses, ensure_ascii=False)
            self.assertNotIn("3-5 minute", text)
            self.assertNotIn("3–5 minute", text)

    def test_no_withdrawn_source_referenced(self):
        sources = {s["source_id"]: s for s in load("research/sources.json")["sources"]}
        for filename in self.SESSION_FILES:
            ses = load_session(filename)
            for sid in ses["sources"]:
                self.assertIn(sid, sources, f"{filename} references unknown {sid}")
                self.assertFalse(sources[sid]["withdrawn"], f"{filename} references withdrawn {sid}")

    def test_capstone_session_ties_whole_arc_together(self):
        ses6 = load_session("session-transfer-complet-jocuri-variate.json")
        self.assertIn("EX-0014", json.dumps(ses6))
        self.assertIn("EX-0015", json.dumps(ses6))
        self.assertIn("arc", ses6["session_rationale"])


class Task3712AssessmentExtensionTests(unittest.TestCase):
    def load_assessment(self):
        return json.loads(ASSESSMENT_PATH.read_text(encoding="utf-8"))

    def test_three_new_criteria_added(self):
        asm = self.load_assessment()
        ids = {c["id"] for c in asm["criteria"]}
        for new_id in ("ASM-0001-C6", "ASM-0001-C7", "ASM-0001-C8"):
            self.assertIn(new_id, ids)

    def test_eight_criteria_total(self):
        asm = self.load_assessment()
        self.assertEqual(len(asm["criteria"]), 8)

    def test_new_criteria_reference_new_exercises(self):
        asm = self.load_assessment()
        by_id = {c["id"]: c for c in asm["criteria"]}
        self.assertIn("EX-0006", by_id["ASM-0001-C6"]["observable_behaviour"])
        self.assertIn("EX-0007", by_id["ASM-0001-C6"]["observable_behaviour"])
        self.assertIn("EX-0009", by_id["ASM-0001-C7"]["observable_behaviour"])
        self.assertIn("EX-0012", by_id["ASM-0001-C8"]["observable_behaviour"])

    def test_new_criteria_have_at_least_two_levels_and_autonomy_worded_top(self):
        asm = self.load_assessment()
        for cid in ("ASM-0001-C6", "ASM-0001-C7", "ASM-0001-C8"):
            criterion = next(c for c in asm["criteria"] if c["id"] == cid)
            self.assertGreaterEqual(len(criterion["levels"]), 2)
            top = criterion["levels"][-1]
            self.assertTrue(any(w in top for w in ("autonom", "fără comandă", "fără reper extern")), cid)

    def test_assessment_still_valid_against_schema(self):
        from jsonschema import Draft202012Validator
        schema = json.loads((ROOT / "schemas/assessment.schema.json").read_text(encoding="utf-8"))
        errors = list(Draft202012Validator(schema).iter_errors(self.load_assessment()))
        self.assertEqual(errors, [], [e.message for e in errors])


class Task3712ProblemGraphStrengtheningTests(unittest.TestCase):
    def load_problems(self):
        return {p["problem_id"]: p for p in json.load(open(PROBLEM_LIBRARY_PATH, encoding="utf-8"))["problems"]}

    def test_previously_orphaned_prb0005_now_linked(self):
        problems = self.load_problems()
        prb5 = problems["PRB-0005"]
        self.assertIn("EX-0012", prb5["related_exercises"])
        self.assertIn("ASM-0001", prb5["assessment_links"])

    def test_deliberately_untouched_defensive_problems(self):
        # TASK-3712 explicitly does not link PRB-0004/PRB-0006 (defensive
        # organization — a different theme) to any new exercise/session.
        problems = self.load_problems()
        self.assertEqual(problems["PRB-0004"]["related_exercises"], [])
        self.assertEqual(problems["PRB-0004"]["related_sessions"], [])
        self.assertEqual(problems["PRB-0006"]["related_exercises"], [])
        self.assertEqual(problems["PRB-0006"]["related_sessions"], [])

    def test_strengthened_problems_reference_only_real_exercises_and_sessions(self):
        exercise_ids = {json.loads(f.read_text(encoding="utf-8"))["id"] for f in EXERCISE_DIR.glob("exercise-*.json")}
        session_ids = {json.loads(f.read_text(encoding="utf-8"))["id"] for f in SESSION_DIR.glob("session-*.json")}
        for pid in ("PRB-0001", "PRB-0002", "PRB-0003", "PRB-0005", "PRB-0007", "PRB-0008"):
            problem = self.load_problems()[pid]
            for eid in problem["related_exercises"]:
                self.assertIn(eid, exercise_ids, f"{pid}: unknown exercise {eid}")
            for sid in problem["related_sessions"]:
                self.assertIn(sid, session_ids, f"{pid}: unknown session {sid}")


if __name__ == "__main__":
    unittest.main()
