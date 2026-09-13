import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def load(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))

class Task0602Tests(unittest.TestCase):
    def test_chapter_is_publishable(self):
        text = (ROOT / "content/volume-02/chapter-02.mdx").read_text(encoding="utf-8")
        self.assertIn('chapter_id: "CH-0202"', text)
        self.assertGreater(len(text), 9000)
        for marker in ("Ce susțin dovezile", "Ce îi spui copilului", "Transfer în meci", "Ce nu putem concluziona"):
            self.assertIn(marker, text)

    def test_claim_chains(self):
        claims = {x["claim_id"]: x for x in load("research/claims.json")["claims"]}
        citations = load("research/citations.json")["citations"]
        for cid in ("CLM-0040", "CLM-0041"):
            self.assertIn(cid, claims)
            self.assertTrue([x for x in citations if x["claim_id"] == cid])
            self.assertTrue(claims[cid]["limitations"])

    def test_no_optimal_pitch_overstatement(self):
        text = (ROOT / "content/volume-02/chapter-02.mdx").read_text(encoding="utf-8")
        self.assertIn("nu au arătat o dimensiune optimă", text)
        self.assertIn("ipoteză ManualFC", text)

    def test_field_card_is_actionable_and_safe(self):
        text = (ROOT / "docs/content/CH_0202_SPACE_ANGLE_OBSERVATION_CARD.md").read_text(encoding="utf-8")
        for marker in ("28 × 22 m", "minimum 2 m", "o singură variabilă", "Test anti-poziție"):
            self.assertIn(marker, text)

    def test_child_message_foundation(self):
        p = load("data/principles/principle-spatiu-si-unghiuri.json")
        self.assertEqual(len(p["rationales"]), 7)
        for key in ("child_message", "coach_meaning", "why_this_message", "understanding_check", "response_if_not_understood", "match_transfer"):
            self.assertTrue(p[key])

    def test_combined_age_group(self):
        text = (ROOT / "content/volume-02/chapter-02.mdx").read_text(encoding="utf-8")
        self.assertIn("Grupele 2015 și 2016 rămân împreună", text)

    def test_transfer_is_not_same_position(self):
        text = (ROOT / "content/volume-02/chapter-02.mdx").read_text(encoding="utf-8")
        self.assertIn("nu înseamnă să reproduci poziția", text)
        self.assertIn("nu demonstrează singură transferul tactic", text)

    def test_audits_are_distinct(self):
        self.assertTrue((ROOT / "reports/audits/TASK-0602-factual-pedagogical-audit.md").exists())
        self.assertTrue((ROOT / "reports/audits/TASK-0602-editorial-audit.md").exists())

if __name__ == "__main__":
    unittest.main()
