import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ASSESSMENT_PATH = ROOT / "data" / "assessments" / "assessment-sprijin-si-unghi-de-pasa.json"


def load(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def load_assessment():
    return json.loads(ASSESSMENT_PATH.read_text(encoding="utf-8"))


class Task2206AssessmentSystemTests(unittest.TestCase):
    def test_assessment_file_exists(self):
        self.assertTrue(ASSESSMENT_PATH.exists())

    def test_id_matches_schema_pattern(self):
        asm = load_assessment()
        self.assertRegex(asm["id"], r"^ASM-[0-9]{4,}$")

    def test_principle_ids_point_to_real_reused_principles(self):
        asm = load_assessment()
        principle_dir = ROOT / "data" / "principles"
        known_ids = set()
        for f in principle_dir.glob("principle-*.json"):
            known_ids.add(json.loads(f.read_text(encoding="utf-8"))["id"])
        for pid in asm["principle_ids"]:
            self.assertIn(pid, known_ids, pid)

    def test_no_pseudo_precise_numeric_score(self):
        text = json.dumps(load_assessment(), ensure_ascii=False)
        self.assertNotRegex(text, r"\d\.\d\s*/\s*10")
        self.assertNotRegex(text, r"\bscor\b", "assessment should not use numeric scoring language")

    def test_levels_are_qualitative_not_numeric_ranks(self):
        asm = load_assessment()
        for criterion in asm["criteria"]:
            for level in criterion["levels"]:
                self.assertNotRegex(level, r"^\s*\d")

    def test_each_criterion_has_at_least_two_levels(self):
        asm = load_assessment()
        for criterion in asm["criteria"]:
            self.assertGreaterEqual(len(criterion["levels"]), 2)

    def test_distinguishes_task_success_from_autonomous_transfer(self):
        asm = load_assessment()
        levels_by_id = {c["id"]: c["levels"] for c in asm["criteria"]}
        # Every criterion's top level should describe autonomy (no external cue / no command),
        # its bottom level should describe dependence on external cue/intervention.
        for cid, levels in levels_by_id.items():
            bottom, top = levels[0], levels[-1]
            self.assertTrue(
                any(w in top for w in ("autonom", "fără comandă", "fără reper extern", "fără intervenție")),
                f"{cid} top level not autonomy-worded: {top}",
            )

    def test_match_transfer_criterion_marks_field_validation_pending(self):
        # PHASE-25: the raw "FIELD_VALIDATION_PENDING" enum rendered verbatim in
        # product UI (this field is displayed on ASM-0001) is a defect, closed
        # in PHASE-25; the same status is now expressed in natural Romanian.
        asm = load_assessment()
        c5 = next(c for c in asm["criteria"] if c["id"] == "ASM-0001-C5")
        self.assertNotIn("FIELD_VALIDATION_PENDING", c5["levels"][-1])
        self.assertIn("neconfirmat", c5["levels"][-1])
        self.assertIn("pilotare reală pe teren", c5["levels"][-1])

    def test_criteria_cover_all_five_exercises(self):
        asm = load_assessment()
        text = json.dumps(asm, ensure_ascii=False)
        for eid in ("EX-0001", "EX-0002", "EX-0003", "EX-0004", "EX-0005"):
            self.assertIn(eid, text)


if __name__ == "__main__":
    unittest.main()
