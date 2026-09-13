import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def load(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))

class Task0603Tests(unittest.TestCase):
    def test_chapter_is_publishable(self):
        text = (ROOT / "content/volume-02/chapter-03.mdx").read_text(encoding="utf-8")
        self.assertIn('chapter_id: "CH-0203"', text)
        self.assertGreater(len(text), 9000)
        for marker in ("Ce susțin dovezile", "Ce îi spui copilului", "Transfer în meci", "Ce nu putem concluziona"):
            self.assertIn(marker, text)

    def test_claim_chain_complete(self):
        claims = {x["claim_id"]: x for x in load("research/claims.json")["claims"]}
        citations = load("research/citations.json")["citations"]
        self.assertIn("CLM-0042", claims)
        self.assertTrue([x for x in citations if x["claim_id"] == "CLM-0042"])
        self.assertEqual(claims["CLM-0042"]["u11_applicability"], "INDIRECT")

    def test_progression_not_direction_only(self):
        text = (ROOT / "content/volume-02/chapter-03.mdx").read_text(encoding="utf-8")
        self.assertIn("nu înseamnă „mingea înainte cu orice preț”", text)
        self.assertIn("O pasă înapoi poate pregăti progresia", text)

    def test_field_card_safe_and_adjustable(self):
        text = (ROOT / "docs/content/CH_0203_PROGRESSION_SUPPORT_CARD.md").read_text(encoding="utf-8")
        for marker in ("30 × 22 m", "minimum 2 m", "o singură dimensiune", "Test anti-coregrafie"):
            self.assertIn(marker, text)

    def test_message_foundation_complete(self):
        p = load("data/principles/principle-progresie-si-sprijin.json")
        self.assertEqual(len(p["rationales"]), 7)
        for key in ("child_message", "coach_meaning", "why_this_message", "understanding_check", "response_if_not_understood", "match_transfer"):
            self.assertTrue(p[key])

    def test_combined_age_group(self):
        text = (ROOT / "content/volume-02/chapter-03.mdx").read_text(encoding="utf-8")
        self.assertIn("Grupele 2015 și 2016 rămân o singură categorie", text)

    def test_transfer_not_assumed(self):
        text = (ROOT / "content/volume-02/chapter-03.mdx").read_text(encoding="utf-8")
        self.assertIn("nu este dovadă suficientă de transfer", text)

    def test_audits_distinct(self):
        self.assertTrue((ROOT / "reports/audits/TASK-0603-factual-pedagogical-audit.md").exists())
        self.assertTrue((ROOT / "reports/audits/TASK-0603-editorial-audit.md").exists())

if __name__ == "__main__":
    unittest.main()
