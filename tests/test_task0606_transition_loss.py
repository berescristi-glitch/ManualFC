import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def load(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))

class Task0606Tests(unittest.TestCase):
    def test_chapter_publishable(self):
        text = (ROOT / "content/volume-02/chapter-06.mdx").read_text(encoding="utf-8")
        self.assertIn('chapter_id: "CH-0206"', text)
        self.assertGreater(len(text), 9000)
        for marker in ("Ce susțin dovezile", "Ce îi spui copilului", "Transfer în meci", "Ce nu putem concluziona"):
            self.assertIn(marker, text)

    def test_indirect_and_partial_claim_chain(self):
        claims = {x["claim_id"]: x for x in load("research/claims.json")["claims"]}
        citations = load("research/citations.json")["citations"]
        self.assertEqual(claims["CLM-0045"]["u11_applicability"], "INDIRECT")
        self.assertEqual(claims["CLM-0046"]["u11_applicability"], "PARTIAL")
        self.assertEqual(claims["CLM-0047"]["u11_applicability"], "INDIRECT")
        for claim_id in ("CLM-0045", "CLM-0046", "CLM-0047"):
            self.assertTrue([c for c in citations if c["claim_id"] == claim_id])

    def test_no_universal_time_threshold(self):
        text = (ROOT / "content/volume-02/chapter-06.mdx").read_text(encoding="utf-8")
        self.assertIn("Nu am găsit niciun studiu, la nicio vârstă, care testează sau validează un asemenea prag", text)
        self.assertIn("Aveți 5 secunde", text)

    def test_no_block_pressing_prescribed(self):
        text = (ROOT / "content/volume-02/chapter-06.mdx").read_text(encoding="utf-8")
        self.assertIn("De ce nu pornim cu presing în bloc", text)
        self.assertIn("PRACTICE_ONLY", text)

    def test_field_card_safe_and_feasible(self):
        text = (ROOT / "docs/content/CH_0206_TRANSITION_LOSS_CARD.md").read_text(encoding="utf-8")
        for marker in ("30 × 20 m", "3v3 + portari", "Test anti-tipar", "Ce nu faci"):
            self.assertIn(marker, text)

    def test_message_foundation(self):
        p = load("data/principles/principle-tranzitia-la-pierderea-mingii.json")
        self.assertEqual(len(p["rationales"]), 7)
        for key in ("child_message", "coach_meaning", "why_this_message", "understanding_check", "response_if_not_understood", "match_transfer"):
            self.assertTrue(p[key])

    def test_two_distinct_decisions(self):
        text = (ROOT / "content/volume-02/chapter-06.mdx").read_text(encoding="utf-8")
        self.assertIn("Cine e aproape, încetinește. Restul, închideți drumul spre poartă.", text)
        self.assertIn("Cine decide ce, în primele secunde", text)

    def test_combined_age_and_transfer_limit(self):
        text = (ROOT / "content/volume-02/chapter-06.mdx").read_text(encoding="utf-8")
        self.assertIn("Grupele 2015 și 2016 rămân împreună", text)
        self.assertIn("nu demonstrează transfer direct în meci complet", text)

    def test_audits_distinct(self):
        self.assertTrue((ROOT / "reports/audits/TASK-0606-factual-pedagogical-audit.md").exists())
        self.assertTrue((ROOT / "reports/audits/TASK-0606-editorial-audit.md").exists())

if __name__ == "__main__":
    unittest.main()
