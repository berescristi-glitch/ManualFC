import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def load(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))

class Task0607Tests(unittest.TestCase):
    def test_chapter_publishable(self):
        text = (ROOT / "content/volume-02/chapter-07.mdx").read_text(encoding="utf-8")
        self.assertIn('chapter_id: "CH-0207"', text)
        self.assertGreater(len(text), 9000)
        for marker in ("Ce susțin dovezile", "Ce îi spui copilului", "Transfer în meci", "Ce nu putem concluziona"):
            self.assertIn(marker, text)

    def test_partial_claim_chain(self):
        claims = {x["claim_id"]: x for x in load("research/claims.json")["claims"]}
        citations = load("research/citations.json")["citations"]
        self.assertEqual(claims["CLM-0048"]["u11_applicability"], "PARTIAL")
        self.assertEqual(claims["CLM-0049"]["u11_applicability"], "PARTIAL")
        for claim_id in ("CLM-0048", "CLM-0049"):
            self.assertTrue([c for c in citations if c["claim_id"] == claim_id])

    def test_no_fixed_speed_rule(self):
        text = (ROOT / "content/volume-02/chapter-07.mdx").read_text(encoding="utf-8")
        self.assertIn("nu recomandă „atacă imediat de fiecare dată când câștigi mingea”", text)
        self.assertIn("Atacă imediat!", text)

    def test_decision_test_caution(self):
        text = (ROOT / "content/volume-02/chapter-07.mdx").read_text(encoding="utf-8")
        self.assertIn("nu s-a corelat cu succesul lor real într-un joc redus de posesie", text)
        self.assertIn("nu presupune că un exercițiu izolat de decizie măsoară", text)

    def test_field_card_safe_and_feasible(self):
        text = (ROOT / "docs/content/CH_0207_TRANSITION_WIN_CARD.md").read_text(encoding="utf-8")
        for marker in ("25 × 18 m", "3v3 + portari", "Test anti-tipar", "Ce nu faci"):
            self.assertIn(marker, text)

    def test_message_foundation(self):
        p = load("data/principles/principle-tranzitia-la-castigarea-mingii.json")
        self.assertEqual(len(p["rationales"]), 7)
        for key in ("child_message", "coach_meaning", "why_this_message", "understanding_check", "response_if_not_understood", "match_transfer"):
            self.assertTrue(p[key])

    def test_control_look_decide_sequence(self):
        text = (ROOT / "content/volume-02/chapter-07.mdx").read_text(encoding="utf-8")
        self.assertIn("Ai câștigat mingea. Uită-te: ai loc să mergi înainte sau ai nevoie de un coleg aproape?", text)
        self.assertIn("Primul control, apoi decizia", text)

    def test_combined_age_and_transfer_limit(self):
        text = (ROOT / "content/volume-02/chapter-07.mdx").read_text(encoding="utf-8")
        self.assertIn("Grupele 2015 și 2016 rămân împreună", text)
        self.assertIn("nu demonstrează transfer direct în meci complet", text)

    def test_audits_distinct(self):
        self.assertTrue((ROOT / "reports/audits/TASK-0607-factual-pedagogical-audit.md").exists())
        self.assertTrue((ROOT / "reports/audits/TASK-0607-editorial-audit.md").exists())

if __name__ == "__main__":
    unittest.main()
