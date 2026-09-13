import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def load(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))

class Task0605Tests(unittest.TestCase):
    def test_chapter_publishable(self):
        text = (ROOT / "content/volume-02/chapter-05.mdx").read_text(encoding="utf-8")
        self.assertIn('chapter_id: "CH-0205"', text)
        self.assertGreater(len(text), 9000)
        for marker in ("Ce susțin dovezile", "Ce îi spui copilului", "Transfer în meci", "Ce nu putem concluziona"):
            self.assertIn(marker, text)

    def test_indirect_claim_chain(self):
        claims = {x["claim_id"]: x for x in load("research/claims.json")["claims"]}
        citations = load("research/citations.json")["citations"]
        self.assertEqual(claims["CLM-0044"]["u11_applicability"], "INDIRECT")
        self.assertTrue([x for x in citations if x["claim_id"] == "CLM-0044"])

    def test_tackling_not_quality_proxy(self):
        text = (ROOT / "content/volume-02/chapter-05.mdx").read_text(encoding="utf-8")
        self.assertIn("Mai multe tacklinguri nu înseamnă automat presiune mai bună", text)
        self.assertIn("Un tackling reușit poate veni după o presiune necontrolată", text)

    def test_field_card_safe_and_feasible(self):
        text = (ROOT / "docs/content/CH_0205_PRESSURE_COVER_CARD.md").read_text(encoding="utf-8")
        for marker in ("24 × 18 m", "minimum 2 m", "două terenuri", "Test anti-pereche"):
            self.assertIn(marker, text)

    def test_message_foundation(self):
        p = load("data/principles/principle-presiune-si-acoperire.json")
        self.assertEqual(len(p["rationales"]), 7)
        for key in ("child_message", "coach_meaning", "why_this_message", "understanding_check", "response_if_not_understood", "match_transfer"):
            self.assertTrue(p[key])

    def test_roles_change(self):
        text = (ROOT / "content/volume-02/chapter-05.mdx").read_text(encoding="utf-8")
        self.assertIn("Rolurile se schimbă", text)
        self.assertIn("nu după o pereche fixă", text)

    def test_combined_age_and_transfer_limit(self):
        text = (ROOT / "content/volume-02/chapter-05.mdx").read_text(encoding="utf-8")
        self.assertIn("Grupele 2015 și 2016 rămân împreună", text)
        self.assertIn("nu demonstrează transfer", text)

    def test_audits_distinct(self):
        self.assertTrue((ROOT / "reports/audits/TASK-0605-factual-pedagogical-audit.md").exists())
        self.assertTrue((ROOT / "reports/audits/TASK-0605-editorial-audit.md").exists())

if __name__ == "__main__":
    unittest.main()
