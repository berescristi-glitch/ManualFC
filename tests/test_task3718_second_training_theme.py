import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXERCISE_DIR = ROOT / "data" / "exercises"
SESSION_DIR = ROOT / "data" / "sessions"
ASSESSMENT_PATH = ROOT / "data" / "assessments" / "assessment-apararea-presiune-si-acoperire.json"
PROBLEM_LIBRARY_PATH = ROOT / "data" / "problems" / "problem-library.json"
CONTENT_BRIDGE_PATH = ROOT / "app" / "src" / "lib" / "content-bridge.ts"
THEME = "apararea-presiune-si-acoperire"


def load_exercise(filename):
    return json.loads((EXERCISE_DIR / filename).read_text(encoding="utf-8"))


def load_session(filename):
    return json.loads((SESSION_DIR / filename).read_text(encoding="utf-8"))


class Task3718NewExerciseTests(unittest.TestCase):
    EXERCISE_FILES = [
        "exercise-incetineste-nu-ataca-mingea.json",
        "exercise-unul-incetineste-celalalt-protejeaza.json",
        "exercise-schimba-rolul-cand-mingea-se-muta.json",
        "exercise-nu-va-eliminati-amandoi.json",
        "exercise-al-doilea-aparator-acopera-drumul.json",
        "exercise-primele-doua-secunde-dupa-pierdere.json",
        "exercise-cine-e-aproape-cine-protejeaza-centrul.json",
        "exercise-recupereaza-forma-nu-doar-mingea.json",
        "exercise-joc-mic-4v4-observare-defensiva.json",
        "exercise-joc-mic-6v6-zona-de-protejat.json",
    ]
    EXPECTED_IDS = [f"EX-{n:04d}" for n in range(16, 26)]

    def test_ten_new_exercise_files_exist(self):
        for filename in self.EXERCISE_FILES:
            self.assertTrue((EXERCISE_DIR / filename).exists(), f"missing {filename}")

    def test_exercise_ids_are_sequential_and_unique(self):
        ids = [load_exercise(f)["id"] for f in self.EXERCISE_FILES]
        self.assertEqual(sorted(ids), self.EXPECTED_IDS)
        self.assertEqual(len(ids), len(set(ids)))

    def test_all_new_exercises_belong_to_second_theme(self):
        for filename in self.EXERCISE_FILES:
            ex = load_exercise(filename)
            self.assertEqual(ex["theme"], THEME, f"{filename}: unexpected theme")

    def test_all_new_exercises_reference_the_new_assessment(self):
        for filename in self.EXERCISE_FILES:
            ex = load_exercise(filename)
            self.assertEqual(ex.get("assessment_ref"), "ASM-0002", f"{filename}: assessment_ref")

    def test_all_new_exercises_have_gold_standard_v2_rationales(self):
        expected_rationale_keys = {
            "tactical", "perceptual", "decisional", "cognitive",
            "psychological", "technical", "social",
        }
        for filename in self.EXERCISE_FILES:
            ex = load_exercise(filename)
            self.assertEqual(ex["gold_standard_v2"]["status"], "V2", filename)
            self.assertEqual(set(ex["rationales"].keys()), expected_rationale_keys, filename)

    def test_all_new_exercises_have_pending_visual_assets(self):
        # Design freeze convention: no real graphics produced for exercises
        # beyond the original EX-0001-EX-0005 set (see TASK-3712 for the same rule).
        for filename in self.EXERCISE_FILES:
            ex = load_exercise(filename)
            for key in ("static_svg", "animation_or_storyboard", "pdf_frames"):
                self.assertIn("PENDING", ex["visual_assets"][key], f"{filename}: {key}")

    def test_all_new_exercises_reference_only_real_non_withdrawn_sources(self):
        sources_registry = json.loads((ROOT / "research" / "sources.json").read_text(encoding="utf-8"))
        by_id = {s["source_id"]: s for s in sources_registry["sources"]}
        for filename in self.EXERCISE_FILES:
            ex = load_exercise(filename)
            for src_id in ex.get("sources", []):
                self.assertIn(src_id, by_id, f"{filename}: unknown source {src_id}")
                self.assertFalse(by_id[src_id].get("withdrawn", False), f"{filename}: withdrawn source {src_id}")


class Task3718NewSessionTests(unittest.TestCase):
    SESSION_FILES = {
        "session-incetinire-si-schimb-de-rol.json": "SES-0007",
        "session-coordonare-defensiva-2v2.json": "SES-0008",
        "session-tranzitie-negativa-si-echipa.json": "SES-0009",
        "session-transfer-defensiv-complet.json": "SES-0010",
    }

    def test_four_new_session_files_exist_with_expected_ids(self):
        for filename, expected_id in self.SESSION_FILES.items():
            self.assertTrue((SESSION_DIR / filename).exists(), f"missing {filename}")
            self.assertEqual(load_session(filename)["id"], expected_id)

    def test_every_new_exercise_appears_in_at_least_one_new_session(self):
        referenced = set()
        for filename in self.SESSION_FILES:
            session = load_session(filename)
            for segment in session["segments"]:
                referenced.update(segment["exercise_ids"])
        expected_ids = {f"EX-{n:04d}" for n in range(16, 26)}
        self.assertEqual(expected_ids - referenced, set(), "orphaned new exercise(s) not in any new session")

    def test_duration_variant_60min_covers_every_segment(self):
        # Regression guard for the TASK-3718 authoring bug where SES-0008/SES-0009
        # initially omitted the final "joc liber" segment from the 60-minute variant.
        for filename in self.SESSION_FILES:
            session = load_session(filename)
            full_indices = set(range(len(session["segments"])))
            variant_indices = {s["segment_index"] for s in session["duration_variant_60min"]["segments"]}
            self.assertEqual(full_indices, variant_indices, filename)

    def test_sessions_progress_through_the_defense_chain_in_order(self):
        # SES-0007 introduces individual/pair defending, SES-0008 adds 2v2 risk of
        # simultaneous elimination, SES-0009 extends to team transition, SES-0010
        # is the pure-transfer capstone with no new exercises.
        ses10 = load_session("session-transfer-defensiv-complet.json")
        capstone_exercise_ids = {eid for seg in ses10["segments"] for eid in seg["exercise_ids"]}
        self.assertEqual(capstone_exercise_ids, {"EX-0024", "EX-0025"})


class Task3718AssessmentTests(unittest.TestCase):
    def test_asm_0002_exists_with_five_criteria(self):
        assessment = json.loads(ASSESSMENT_PATH.read_text(encoding="utf-8"))
        self.assertEqual(assessment["id"], "ASM-0002")
        self.assertEqual(len(assessment["criteria"]), 5)
        for criterion in assessment["criteria"]:
            self.assertEqual(len(criterion["levels"]), 3)

    def test_asm_0002_criteria_reference_only_real_exercise_ids(self):
        assessment = json.loads(ASSESSMENT_PATH.read_text(encoding="utf-8"))
        exercise_ids = {json.loads(f.read_text(encoding="utf-8"))["id"] for f in EXERCISE_DIR.glob("exercise-*.json")}
        for criterion in assessment["criteria"]:
            for ex_id in re.findall(r"EX-\d{4}", criterion["observable_behaviour"]):
                self.assertIn(ex_id, exercise_ids, f"{criterion['id']}: unknown exercise {ex_id}")

    def test_asm_0002_principle_ids_resolve_to_real_principle_files(self):
        assessment = json.loads(ASSESSMENT_PATH.read_text(encoding="utf-8"))
        principle_dir = ROOT / "data" / "principles"
        for principle_id in assessment["principle_ids"]:
            slug = principle_id.split(".", 1)[-1]
            self.assertTrue((principle_dir / f"principle-{slug}.json").exists(), principle_id)


class Task3718ProblemLibraryStrengtheningTests(unittest.TestCase):
    def load_problems(self):
        data = json.loads(PROBLEM_LIBRARY_PATH.read_text(encoding="utf-8"))
        return {p["problem_id"]: p for p in data["problems"]}

    def test_prb_0004_links_to_transition_and_transfer_content(self):
        problem = self.load_problems()["PRB-0004"]
        self.assertIn("EX-0021", problem["related_exercises"])
        self.assertIn("SES-0009", problem["related_sessions"])
        self.assertIn("ASM-0002", problem["assessment_links"])

    def test_prb_0006_links_to_pressure_and_cover_content(self):
        problem = self.load_problems()["PRB-0006"]
        self.assertIn("EX-0018", problem["related_exercises"])
        self.assertIn("SES-0007", problem["related_sessions"])
        self.assertIn("ASM-0002", problem["assessment_links"])

    def test_strengthened_links_reference_only_real_content(self):
        exercise_ids = {json.loads(f.read_text(encoding="utf-8"))["id"] for f in EXERCISE_DIR.glob("exercise-*.json")}
        session_ids = {json.loads(f.read_text(encoding="utf-8"))["id"] for f in SESSION_DIR.glob("session-*.json")}
        for pid in ("PRB-0004", "PRB-0006"):
            problem = self.load_problems()[pid]
            for eid in problem["related_exercises"]:
                self.assertIn(eid, exercise_ids, f"{pid}: unknown exercise {eid}")
            for sid in problem["related_sessions"]:
                self.assertIn(sid, session_ids, f"{pid}: unknown session {sid}")


class Task3718ContentBridgeRegistrationTests(unittest.TestCase):
    """content-bridge.ts is TypeScript; these tests check the static import/array
    wiring by text inspection rather than executing the module."""

    def setUp(self):
        self.source = CONTENT_BRIDGE_PATH.read_text(encoding="utf-8")

    def test_all_new_exercises_are_imported_and_registered(self):
        exercise_files = [
            "exercise-incetineste-nu-ataca-mingea.json",
            "exercise-unul-incetineste-celalalt-protejeaza.json",
            "exercise-schimba-rolul-cand-mingea-se-muta.json",
            "exercise-nu-va-eliminati-amandoi.json",
            "exercise-al-doilea-aparator-acopera-drumul.json",
            "exercise-primele-doua-secunde-dupa-pierdere.json",
            "exercise-cine-e-aproape-cine-protejeaza-centrul.json",
            "exercise-recupereaza-forma-nu-doar-mingea.json",
            "exercise-joc-mic-4v4-observare-defensiva.json",
            "exercise-joc-mic-6v6-zona-de-protejat.json",
        ]
        for filename in exercise_files:
            self.assertIn(filename, self.source, f"{filename} not imported in content-bridge.ts")
            self.assertIn(f"parseGoldStandardExercise", self.source)

    def test_all_new_sessions_are_imported_and_registered(self):
        for filename in ("session-incetinire-si-schimb-de-rol.json", "session-coordonare-defensiva-2v2.json",
                         "session-tranzitie-negativa-si-echipa.json", "session-transfer-defensiv-complet.json"):
            self.assertIn(filename, self.source, f"{filename} not imported in content-bridge.ts")

    def test_new_assessment_is_imported_and_registered(self):
        self.assertIn("assessment-apararea-presiune-si-acoperire.json", self.source)

    def test_assessment_getter_is_backward_compatible(self):
        # Must remain callable with zero arguments (existing theme-1 call sites)
        # while also accepting an explicit id for theme-2 lookups.
        self.assertRegex(self.source, r"DEFAULT_ASSESSMENT_ID\s*=\s*['\"]ASM-0001['\"]")
        self.assertRegex(self.source, r"getGoldStandardAssessment\(id: string = DEFAULT_ASSESSMENT_ID\)")
        self.assertIn("getGoldStandardAssessments", self.source)


if __name__ == "__main__":
    unittest.main()
