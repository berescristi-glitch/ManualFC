import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


class Task0601Tests(unittest.TestCase):
    def test_chapter_is_publishable_and_canonical(self):
        text = (ROOT / "content/volume-02/chapter-01.mdx").read_text(encoding="utf-8")
        self.assertIn('chapter_id: "CH-0201"', text)
        self.assertGreater(len(text), 9000)
        for marker in ("Ce susțin dovezile", "Ce îi spui copilului", "Transfer în meci", "Ce nu putem concluziona"):
            self.assertIn(marker, text)

    def test_new_claim_chains_are_complete(self):
        claims = {x["claim_id"]: x for x in load("research/claims.json")["claims"]}
        citations = load("research/citations.json")["citations"]
        sources = {x["source_id"] for x in load("research/sources.json")["sources"]}
        for claim_id in ("CLM-0038", "CLM-0039"):
            links = [x for x in citations if x["claim_id"] == claim_id]
            self.assertTrue(links)
            self.assertTrue(claims[claim_id]["limitations"])
            self.assertTrue(all(x["source_id"] in sources for x in links))

    def test_representativeness_is_not_overstated(self):
        claim = next(x for x in load("research/claims.json")["claims"] if x["claim_id"] == "CLM-0038")
        self.assertEqual(claim["epistemic_level"], "PRACTICE_ONLY")
        self.assertEqual(claim["u11_applicability"], "INDIRECT")
        self.assertIn("nu validează", claim["statement"])

    def test_game_problem_has_required_elements(self):
        text = (ROOT / "docs/content/CH_0201_GAME_PROBLEM_CANVAS.md").read_text(encoding="utf-8")
        for marker in ("Obiectiv", "Opoziție", "Informație", "Opțiuni", "Consecință", "Testul anti-coregrafie"):
            self.assertIn(marker, text)

    def test_field_setup_is_safe_and_adjustable(self):
        text = (ROOT / "docs/content/CH_0201_GAME_PROBLEM_CANVAS.md").read_text(encoding="utf-8")
        self.assertIn("30 × 22 m", text)
        self.assertIn("minimum 2 m", text)
        self.assertIn("o singură dimensiune", text)
        self.assertIn("Nu este valoare oficială", text)

    def test_message_foundation_is_complete(self):
        principle = load("data/principles/principle-jocul-ca-sistem-de-probleme.json")
        self.assertEqual(len(principle["rationales"]), 7)
        for key in ("child_message", "coach_meaning", "why_this_message", "understanding_check", "response_if_not_understood", "match_transfer"):
            self.assertTrue(principle[key])

    def test_transfer_is_solution_variable(self):
        text = (ROOT / "content/volume-02/chapter-01.mdx").read_text(encoding="utf-8")
        self.assertIn("fără aceeași soluție", text)
        self.assertIn("Fluența în sarcina de antrenament nu este dovadă suficientă", text)

    def test_audits_are_distinct(self):
        self.assertTrue((ROOT / "reports/audits/TASK-0601-factual-pedagogical-audit.md").exists())
        self.assertTrue((ROOT / "reports/audits/TASK-0601-editorial-audit.md").exists())


if __name__ == "__main__":
    unittest.main()
