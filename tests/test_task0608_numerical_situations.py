import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def load(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))

class Task0608Tests(unittest.TestCase):
    def test_chapter_publishable(self):
        text = (ROOT / "content/volume-02/chapter-08.mdx").read_text(encoding="utf-8")
        self.assertIn('chapter_id: "CH-0208"', text)
        self.assertGreater(len(text), 9000)
        for marker in ("Ce susțin dovezile", "Ce îi spui copilului", "Transfer în meci", "Ce nu putem concluziona"):
            self.assertIn(marker, text)

    def test_claim_chain_and_directness(self):
        claims = {x["claim_id"]: x for x in load("research/claims.json")["claims"]}
        citations = load("research/citations.json")["citations"]
        self.assertEqual(claims["CLM-0050"]["u11_applicability"], "DIRECT")
        self.assertEqual(claims["CLM-0051"]["u11_applicability"], "DIRECT")
        self.assertEqual(claims["CLM-0052"]["u11_applicability"], "INDIRECT")
        for claim_id in ("CLM-0050", "CLM-0051", "CLM-0052"):
            self.assertTrue([c for c in citations if c["claim_id"] == claim_id])

    def test_skill_level_conditional_benefit(self):
        text = (ROOT / "content/volume-02/chapter-08.mdx").read_text(encoding="utf-8")
        self.assertIn("dovada arată exact opusul pentru copiii cu nivel tehnic mai scăzut", text)
        self.assertIn("antrenamentul pe superioritate numerică ajută automat orice copil, indiferent de nivelul lui tehnic actual", text)

    def test_no_guaranteed_advantage_framing(self):
        text = (ROOT / "content/volume-02/chapter-08.mdx").read_text(encoding="utf-8")
        self.assertIn("Sunteți în plus, faceți gol!", text)
        self.assertIn("nu este un gol garantat", text)

    def test_field_card_safe_and_feasible(self):
        text = (ROOT / "docs/content/CH_0208_NUMERICAL_SITUATIONS_CARD.md").read_text(encoding="utf-8")
        for marker in ("30 × 20 m", "2v1", "Test anti-tipar", "Ce nu faci"):
            self.assertIn(marker, text)

    def test_message_foundation(self):
        p = load("data/principles/principle-superioritate-egalitate-inferioritate-numerica.json")
        self.assertEqual(len(p["rationales"]), 7)
        for key in ("child_message", "coach_meaning", "why_this_message", "understanding_check", "response_if_not_understood", "match_transfer"):
            self.assertTrue(p[key])

    def test_dual_role_message(self):
        text = (ROOT / "content/volume-02/chapter-08.mdx").read_text(encoding="utf-8")
        self.assertIn("Sunteți mai mulți aici? Folosește-i pe amândoi. Sunteți mai puțini? Alege ce aperi primul.", text)

    def test_combined_age_and_transfer_limit(self):
        text = (ROOT / "content/volume-02/chapter-08.mdx").read_text(encoding="utf-8")
        self.assertIn("Grupele 2015 și 2016 rămân împreună", text)
        self.assertIn("nu demonstrează transfer direct în meci complet", text)

    def test_audits_distinct(self):
        self.assertTrue((ROOT / "reports/audits/TASK-0608-factual-pedagogical-audit.md").exists())
        self.assertTrue((ROOT / "reports/audits/TASK-0608-editorial-audit.md").exists())

if __name__ == "__main__":
    unittest.main()
