import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT_DIR = ROOT / "data" / "communication-scripts"
CONTENT_BRIDGE_PATH = ROOT / "app" / "src" / "lib" / "content-bridge.ts"

EXPECTED_CATEGORIES = {
    "observare-inainte-de-corectie",
    "receptie-si-scanare",
    "sprijin-si-unghiuri-de-pasa",
    "miscare-dupa-pasa",
    "tranzitia-la-pierderea-mingii",
    "tranzitia-la-castigarea-mingii",
    "cooperare-defensiva",
    "decizie-sub-presiune",
    "greseala-ca-informatie",
    "reflectie-si-autoevaluare",
    "conflict-frustrare-si-reglare-emotionala",
    "incluziune-echitate-si-participare-respectuoasa",
    "explicarea-constrangerilor-si-schimbarea-sarcinii",
    "inchiderea-sedintei-si-transferul-in-meci",
}

RATIONALE_KEYS = {"tactical", "perceptual", "decisional", "cognitive", "psychological", "technical", "social"}


def load_scripts():
    return [json.loads(f.read_text(encoding="utf-8")) for f in sorted(SCRIPT_DIR.glob("script-*.json"))]


class Task3719ScriptCountAndIdentityTests(unittest.TestCase):
    def test_between_twenty_and_thirty_scripts_exist(self):
        scripts = load_scripts()
        self.assertGreaterEqual(len(scripts), 20)
        self.assertLessEqual(len(scripts), 30)

    def test_ids_are_sequential_unique_and_well_formed(self):
        scripts = load_scripts()
        ids = [s["id"] for s in scripts]
        self.assertEqual(len(ids), len(set(ids)), "duplicate script ids")
        for sid in ids:
            self.assertRegex(sid, r"^SCR-\d{4,}$")
        expected = [f"SCR-{n:04d}" for n in range(1, len(scripts) + 1)]
        self.assertEqual(sorted(ids), expected)

    def test_slugs_are_unique(self):
        scripts = load_scripts()
        slugs = [s["slug"] for s in scripts]
        self.assertEqual(len(slugs), len(set(slugs)), "duplicate script slugs")

    def test_every_script_uses_a_canonical_category(self):
        for s in load_scripts():
            self.assertIn(s["category"], EXPECTED_CATEGORIES, s["id"])

    def test_all_fourteen_categories_are_covered(self):
        used = {s["category"] for s in load_scripts()}
        self.assertEqual(used, EXPECTED_CATEGORIES, "not every required category has at least one script")


class Task3719PedagogicalDepthTests(unittest.TestCase):
    def test_rationales_have_exactly_the_seven_required_dimensions(self):
        for s in load_scripts():
            self.assertEqual(set(s["rationales"].keys()), RATIONALE_KEYS, s["id"])
            for dim, text in s["rationales"].items():
                self.assertGreaterEqual(len(text.strip()), 24, f"{s['id']}: rationales.{dim} too short")

    def test_short_and_expanded_versions_are_distinct_and_nonempty(self):
        for s in load_scripts():
            self.assertTrue(s["short_version"].strip(), s["id"])
            self.assertTrue(s["expanded_version"].strip(), s["id"])
            self.assertNotEqual(s["short_version"].strip(), s["expanded_version"].strip(), s["id"])

    def test_understanding_check_avoids_the_weak_did_you_understand_pattern(self):
        weak_pattern = re.compile(r"(?i)ai\s+înțeles\??\s*$")
        for s in load_scripts():
            for question in s["understanding_check"]:
                self.assertFalse(weak_pattern.match(question.strip()), f"{s['id']}: weak understanding_check {question!r}")

    def test_phrases_to_avoid_have_a_reason_each(self):
        for s in load_scripts():
            self.assertTrue(s["phrases_to_avoid"], s["id"])
            for entry in s["phrases_to_avoid"]:
                self.assertTrue(entry["phrase"].strip(), s["id"])
                self.assertTrue(entry["reason"].strip(), s["id"])

    def test_evidence_boundary_is_present_and_nontrivial(self):
        for s in load_scripts():
            self.assertGreaterEqual(len(s["evidence_boundary"].strip()), 30, s["id"])

    def test_when_to_and_when_not_to_intervene_are_both_present_and_distinct(self):
        for s in load_scripts():
            self.assertTrue(s["when_to_intervene"], s["id"])
            self.assertTrue(s["when_not_to_intervene"], s["id"])
            self.assertNotEqual(set(s["when_to_intervene"]), set(s["when_not_to_intervene"]), s["id"])


class Task3719CrossReferenceIntegrityTests(unittest.TestCase):
    """Mirrors scripts/validate_communication_scripts.py at the test-suite level."""

    def load_real_ids(self):
        principle_ids = set()
        for f in (ROOT / "data" / "principles").glob("*.json"):
            data = json.loads(f.read_text(encoding="utf-8"))
            if "id" in data:
                principle_ids.add(data["id"])
        exercise_ids = {json.loads(f.read_text(encoding="utf-8"))["id"] for f in (ROOT / "data" / "exercises").glob("exercise-*.json")}
        session_ids = {json.loads(f.read_text(encoding="utf-8"))["id"] for f in (ROOT / "data" / "sessions").glob("session-*.json")}
        problems = json.loads((ROOT / "data" / "problems" / "problem-library.json").read_text(encoding="utf-8"))
        problem_ids = {p["problem_id"] for p in problems["problems"]}
        claims = json.loads((ROOT / "research" / "claims.json").read_text(encoding="utf-8"))
        claim_ids = {c["claim_id"] for c in claims["claims"] if not c.get("withdrawn", False)}
        return principle_ids, exercise_ids, session_ids, problem_ids, claim_ids

    def test_every_reference_resolves_to_real_non_withdrawn_content(self):
        principle_ids, exercise_ids, session_ids, problem_ids, claim_ids = self.load_real_ids()
        for s in load_scripts():
            for pid in s["principle_ids"]:
                self.assertIn(pid, principle_ids, f"{s['id']}: unknown principle {pid}")
            for eid in s.get("related_exercise_ids", []):
                self.assertIn(eid, exercise_ids, f"{s['id']}: unknown exercise {eid}")
            for sid in s.get("related_session_ids", []):
                self.assertIn(sid, session_ids, f"{s['id']}: unknown session {sid}")
            for prb in s.get("related_problem_ids", []):
                self.assertIn(prb, problem_ids, f"{s['id']}: unknown problem {prb}")
            for clm in s.get("source_claim_ids", []):
                self.assertIn(clm, claim_ids, f"{s['id']}: unknown or withdrawn claim {clm}")

    def test_both_training_themes_are_reachable_from_the_script_library(self):
        theme1_exercise_ids = {f"EX-{n:04d}" for n in range(1, 16)}
        theme2_exercise_ids = {f"EX-{n:04d}" for n in range(16, 26)}
        referenced = {eid for s in load_scripts() for eid in s.get("related_exercise_ids", [])}
        self.assertTrue(referenced & theme1_exercise_ids, "no script links into theme 1 (sprijin-si-unghi-de-pasa)")
        self.assertTrue(referenced & theme2_exercise_ids, "no script links into theme 2 (apararea-presiune-si-acoperire)")

    def test_no_orphaned_script_every_script_links_to_at_least_one_principle(self):
        for s in load_scripts():
            self.assertTrue(s["principle_ids"], f"{s['id']}: has no principle_ids at all")


class Task3719ContentBridgeRegistrationTests(unittest.TestCase):
    def setUp(self):
        self.source = CONTENT_BRIDGE_PATH.read_text(encoding="utf-8")

    def test_all_scripts_are_imported_and_registered(self):
        for f in sorted(SCRIPT_DIR.glob("script-*.json")):
            self.assertIn(f.name, self.source, f"{f.name} not imported in content-bridge.ts")

    def test_getters_are_exported(self):
        for fn in ("getCommunicationScripts", "getCommunicationScript", "getScriptsForExercise", "getScriptsForSession", "getScriptsForPrinciple"):
            self.assertIn(f"export function {fn}", self.source, fn)


if __name__ == "__main__":
    unittest.main()
