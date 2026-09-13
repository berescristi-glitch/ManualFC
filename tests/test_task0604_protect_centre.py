import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def load(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))

class Task0604Tests(unittest.TestCase):
    def test_chapter_publishable(self):
        text = (ROOT / "content/volume-02/chapter-04.mdx").read_text(encoding="utf-8")
        self.assertIn('chapter_id: "CH-0204"', text)
        self.assertGreater(len(text), 9000)
        for marker in ("Ce susțin dovezile", "Ce îi spui copilului", "Transfer în meci", "Ce nu putem concluziona"):
            self.assertIn(marker, text)

    def test_direct_u11_claim_chain(self):
        claims = {x["claim_id"]: x for x in load("research/claims.json")["claims"]}
        citations = load("research/citations.json")["citations"]
        claim = claims["CLM-0043"]
        self.assertEqual(claim["u11_applicability"], "DIRECT")
        self.assertTrue([x for x in citations if x["claim_id"] == "CLM-0043"])
        self.assertTrue(claim["limitations"])

    def test_centre_is_relational(self):
        text = (ROOT / "content/volume-02/chapter-04.mdx").read_text(encoding="utf-8")
        self.assertIn("nu este o bandă fixă", text)
        self.assertIn("nu înseamnă retragere pasivă", text)

    def test_field_card_safe(self):
        text = (ROOT / "docs/content/CH_0204_PROTECT_CENTRE_CARD.md").read_text(encoding="utf-8")
        for marker in ("30 × 22 m", "minimum 2 m", "porți fixate", "Test anti-bloc"):
            self.assertIn(marker, text)

    def test_message_foundation(self):
        p = load("data/principles/principle-protejarea-centrului.json")
        self.assertEqual(len(p["rationales"]), 7)
        for key in ("child_message", "coach_meaning", "why_this_message", "understanding_check", "response_if_not_understood", "match_transfer"):
            self.assertTrue(p[key])

    def test_combined_age(self):
        text = (ROOT / "content/volume-02/chapter-04.mdx").read_text(encoding="utf-8")
        self.assertIn("Grupele 2015 și 2016 sunt tratate împreună", text)

    def test_no_format_overclaim(self):
        text = (ROOT / "content/volume-02/chapter-04.mdx").read_text(encoding="utf-8")
        self.assertIn("nu demonstrează că 6v6", text)
        self.assertIn("nu demonstrează transfer stabil", text)

    def test_audits_distinct(self):
        self.assertTrue((ROOT / "reports/audits/TASK-0604-factual-pedagogical-audit.md").exists())
        self.assertTrue((ROOT / "reports/audits/TASK-0604-editorial-audit.md").exists())

if __name__ == "__main__":
    unittest.main()
