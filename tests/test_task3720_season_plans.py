import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CURRICULUM_DIR = ROOT / "data" / "curriculum"
PLAN_DIR = ROOT / "data" / "season-plans"
CONTENT_BRIDGE_PATH = ROOT / "app" / "src" / "lib" / "content-bridge.ts"

REQUIRED_BLOCK_FIELDS = [
    "problem_context", "perceptual_decisional_progression", "representative_game_context",
    "expected_observable_behaviour", "coach_watch_for", "do_not_assume",
    "constraint_variation", "progression_decision_criteria",
    "too_difficult_adjustment", "too_easy_adjustment",
]
REQUIRED_PLAN_FIELDS = [
    "scope", "starting_problem", "related_problem_ids", "assumptions_and_prerequisites",
    "overall_learning_intention", "principle_ids", "related_exercise_ids", "related_session_ids",
    "related_script_ids", "observation_criteria", "when_to_intervene", "when_not_to_intervene",
    "reflection_questions", "match_transfer_checkpoints", "adaptation_rules",
    "progression_logic", "regression_logic", "review_points", "continuation_signals", "evidence_boundary",
]
REQUIRED_MICROCYCLE_FIELDS = [
    "title", "session_ids", "learning_intention", "target_behaviour", "coach_observation_focus",
    "related_script_ids", "reflection_prompts", "match_transfer", "review_notes",
    "adaptation_options", "safety_and_workload_notes",
]


def load_curricula():
    return [json.loads(f.read_text(encoding="utf-8")) for f in sorted(CURRICULUM_DIR.glob("curriculum-*.json"))]


def load_plans():
    return [json.loads(f.read_text(encoding="utf-8")) for f in sorted(PLAN_DIR.glob("season-plan-*.json"))]


class Task3720CountAndIdentityTests(unittest.TestCase):
    def test_three_to_four_season_plans_exist(self):
        plans = load_plans()
        self.assertGreaterEqual(len(plans), 3)
        self.assertLessEqual(len(plans), 4)

    def test_six_to_ten_blocks_exist(self):
        blocks = [b for c in load_curricula() for b in c["blocks"]]
        self.assertGreaterEqual(len(blocks), 6)
        self.assertLessEqual(len(blocks), 10)

    def test_twelve_to_twenty_microcycles_exist(self):
        microcycles = [m for p in load_plans() for m in p["microcycles"]]
        self.assertGreaterEqual(len(microcycles), 12)
        self.assertLessEqual(len(microcycles), 20)

    def test_plan_ids_are_unique_and_well_formed(self):
        plans = load_plans()
        ids = [p["id"] for p in plans]
        self.assertEqual(len(ids), len(set(ids)), "duplicate plan ids")
        for pid in ids:
            self.assertRegex(pid, r"^PLAN-\d{4,}$")

    def test_curriculum_ids_are_unique_and_well_formed(self):
        curricula = load_curricula()
        ids = [c["id"] for c in curricula]
        self.assertEqual(len(ids), len(set(ids)), "duplicate curriculum ids")
        for cid in ids:
            self.assertRegex(cid, r"^CUR-\d{4,}$")

    def test_block_and_microcycle_ids_are_globally_unique(self):
        block_ids = [b["id"] for c in load_curricula() for b in c["blocks"]]
        self.assertEqual(len(block_ids), len(set(block_ids)), "duplicate BLK ids across curricula")
        mic_ids = [m["id"] for p in load_plans() for m in p["microcycles"]]
        self.assertEqual(len(mic_ids), len(set(mic_ids)), "duplicate MIC ids across plans")

    def test_plan_slugs_are_unique(self):
        slugs = [p["slug"] for p in load_plans()]
        self.assertEqual(len(slugs), len(set(slugs)), "duplicate plan slugs")


class Task3720PedagogicalCompletenessTests(unittest.TestCase):
    def test_every_block_has_all_required_fields_nonempty(self):
        for curriculum in load_curricula():
            for block in curriculum["blocks"]:
                for field in REQUIRED_BLOCK_FIELDS:
                    value = block.get(field)
                    self.assertTrue(value, f"{curriculum['id']}/{block['id']}: {field} missing or empty")

    def test_every_plan_has_all_required_fields_nonempty(self):
        for plan in load_plans():
            for field in REQUIRED_PLAN_FIELDS:
                value = plan.get(field)
                self.assertTrue(value, f"{plan['id']}: {field} missing or empty")

    def test_every_microcycle_has_all_required_fields_nonempty(self):
        for plan in load_plans():
            for mic in plan["microcycles"]:
                for field in REQUIRED_MICROCYCLE_FIELDS:
                    value = mic.get(field)
                    self.assertTrue(value, f"{plan['id']}/{mic['id']}: {field} missing or empty")

    def test_continuation_signals_have_all_four_categories(self):
        for plan in load_plans():
            signals = plan["continuation_signals"]
            for key in ("continue", "adjust", "slow_down", "abandon"):
                self.assertTrue(signals.get(key), f"{plan['id']}: continuation_signals.{key} missing or empty")

    def test_evidence_boundary_declares_this_is_not_sports_periodization(self):
        # Explicit pedagogical decision (see plans/TASK-3720-season-planning-pillar.md
        # decision log): this pillar must not be presented as sports-science
        # periodization, per CLM-0371/CLM-0372.
        for plan in load_plans():
            boundary = plan["evidence_boundary"].lower()
            self.assertIn("periodizare", boundary, f"{plan['id']}: evidence_boundary should address periodization framing")

    def test_evidence_boundary_states_transfer_remains_unconfirmed(self):
        for plan in load_plans():
            boundary = plan["evidence_boundary"].lower()
            self.assertIn("neconfirmat", boundary, f"{plan['id']}: evidence_boundary should state transfer remains unconfirmed")


class Task3720CrossReferenceIntegrityTests(unittest.TestCase):
    """Mirrors scripts/validate_season_plans.py at the test-suite level."""

    def load_real_ids(self):
        principle_ids = {json.loads(f.read_text(encoding="utf-8"))["id"] for f in (ROOT / "data" / "principles").glob("*.json")}
        exercise_ids = {json.loads(f.read_text(encoding="utf-8"))["id"] for f in (ROOT / "data" / "exercises").glob("exercise-*.json")}
        session_ids = {json.loads(f.read_text(encoding="utf-8"))["id"] for f in (ROOT / "data" / "sessions").glob("session-*.json")}
        script_ids = {json.loads(f.read_text(encoding="utf-8"))["id"] for f in (ROOT / "data" / "communication-scripts").glob("script-*.json")}
        problems = json.loads((ROOT / "data" / "problems" / "problem-library.json").read_text(encoding="utf-8"))
        problem_ids = {p["problem_id"] for p in problems["problems"]}
        curriculum_ids = {c["id"] for c in load_curricula()}
        return principle_ids, exercise_ids, session_ids, script_ids, problem_ids, curriculum_ids

    def test_every_block_reference_resolves(self):
        principle_ids, _, session_ids, _, problem_ids, _ = self.load_real_ids()
        for curriculum in load_curricula():
            for block in curriculum["blocks"]:
                for pid in block["principle_ids"]:
                    self.assertIn(pid, principle_ids, f"{block['id']}: unknown principle {pid}")
                for sid in block["session_ids"]:
                    self.assertIn(sid, session_ids, f"{block['id']}: unknown session {sid}")
                for prb in block.get("related_problem_ids", []):
                    self.assertIn(prb, problem_ids, f"{block['id']}: unknown problem {prb}")

    def test_every_plan_reference_resolves(self):
        principle_ids, exercise_ids, session_ids, script_ids, problem_ids, curriculum_ids = self.load_real_ids()
        for plan in load_plans():
            for cur in plan["curriculum_ids"]:
                self.assertIn(cur, curriculum_ids, f"{plan['id']}: unknown curriculum {cur}")
            for pid in plan["principle_ids"]:
                self.assertIn(pid, principle_ids, f"{plan['id']}: unknown principle {pid}")
            for prb in plan["related_problem_ids"]:
                self.assertIn(prb, problem_ids, f"{plan['id']}: unknown problem {prb}")
            for ex in plan["related_exercise_ids"]:
                self.assertIn(ex, exercise_ids, f"{plan['id']}: unknown exercise {ex}")
            for ses in plan["related_session_ids"]:
                self.assertIn(ses, session_ids, f"{plan['id']}: unknown session {ses}")
            for scr in plan["related_script_ids"]:
                self.assertIn(scr, script_ids, f"{plan['id']}: unknown script {scr}")

    def test_every_microcycle_reference_resolves(self):
        _, _, session_ids, script_ids, _, _ = self.load_real_ids()
        for plan in load_plans():
            for mic in plan["microcycles"]:
                for sid in mic["session_ids"]:
                    self.assertIn(sid, session_ids, f"{mic['id']}: unknown session {sid}")
                for scr in mic["related_script_ids"]:
                    self.assertIn(scr, script_ids, f"{mic['id']}: unknown script {scr}")

    def test_both_training_themes_are_reachable_from_the_plan_library(self):
        theme1_exercise_ids = {f"EX-{n:04d}" for n in range(1, 16)}
        theme2_exercise_ids = {f"EX-{n:04d}" for n in range(16, 26)}
        referenced = {ex for p in load_plans() for ex in p["related_exercise_ids"]}
        self.assertTrue(referenced & theme1_exercise_ids, "no plan links into theme 1 (sprijin-si-unghi-de-pasa)")
        self.assertTrue(referenced & theme2_exercise_ids, "no plan links into theme 2 (apararea-presiune-si-acoperire)")

    def test_communication_scripts_are_reachable_from_the_plan_library(self):
        referenced = {scr for p in load_plans() for scr in p["related_script_ids"]}
        self.assertGreaterEqual(len(referenced), 5, "season plans should draw on a meaningful subset of the script library")

    def test_no_plan_is_orphaned_every_plan_has_a_curriculum(self):
        for plan in load_plans():
            self.assertTrue(plan["curriculum_ids"], f"{plan['id']}: has no curriculum_ids")

    def test_microcycle_sessions_are_declared_at_plan_level(self):
        for plan in load_plans():
            declared = set(plan["related_session_ids"])
            used = {sid for mic in plan["microcycles"] for sid in mic["session_ids"]}
            self.assertTrue(used <= declared, f"{plan['id']}: microcycles reference sessions not declared in related_session_ids: {used - declared}")


class Task3720ContentBridgeRegistrationTests(unittest.TestCase):
    def setUp(self):
        self.source = CONTENT_BRIDGE_PATH.read_text(encoding="utf-8")

    def test_all_curricula_and_plans_are_imported(self):
        for f in sorted(CURRICULUM_DIR.glob("curriculum-*.json")):
            self.assertIn(f.name, self.source, f"{f.name} not imported in content-bridge.ts")
        for f in sorted(PLAN_DIR.glob("season-plan-*.json")):
            self.assertIn(f.name, self.source, f"{f.name} not imported in content-bridge.ts")

    def test_getters_are_exported(self):
        for fn in (
            "getCurricula", "getCurriculum", "getSeasonPlans", "getSeasonPlan", "getCurriculaForPlan",
            "getSeasonPlansForProblem", "getSeasonPlansForExercise", "getSeasonPlansForSession",
            "getSeasonPlansForPrinciple", "getSeasonPlansForScript", "getSeasonPlansForTheme",
        ):
            self.assertIn(f"export function {fn}", self.source, fn)

    def test_canonical_kind_includes_season_plan(self):
        coach_state = (ROOT / "app" / "src" / "lib" / "coach-state.ts").read_text(encoding="utf-8")
        self.assertIn("'season-plan'", coach_state)


if __name__ == "__main__":
    unittest.main()
