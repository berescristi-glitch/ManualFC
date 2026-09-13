import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def load(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))

class Task0701Tests(unittest.TestCase):
    def test_chapter_publishable(self):
        text = (ROOT / "content/volume-03/chapter-01.mdx").read_text(encoding="utf-8")
        self.assertIn('chapter_id: "CH-0301"', text)
        self.assertGreater(len(text), 6500)
        for marker in ("Ce știm din cercetare", "Ce le spun și de ce", "Transferul în meci", "Ce nu putem concluziona"):
            self.assertIn(marker, text)

    def test_no_fabricated_15_second_rule(self):
        text = (ROOT / "content/volume-03/chapter-01.mdx").read_text(encoding="utf-8")
        card = (ROOT / "docs/content/CH_0301_CONCISE_LANGUAGE_CARD.md").read_text(encoding="utf-8")
        for bad in ("regula celor 15 secunde", "10–15 secunde", "10-15 secunde", "maximum 15 secunde"):
            self.assertNotIn(bad, text)
            self.assertNotIn(bad, card)
        self.assertIn("Nu există nicio astfel de cifră", text)

    def test_claim_chain_and_directness(self):
        claims = {x["claim_id"]: x for x in load("research/claims.json")["claims"]}
        citations = load("research/citations.json")["citations"]
        sources = {s["source_id"]: s for s in load("research/sources.json")["sources"]}
        for claim_id in ("CLM-0065", "CLM-0066", "CLM-0067", "CLM-0068"):
            self.assertEqual(claims[claim_id]["status"], "VERIFIED")
            self.assertTrue([c for c in citations if c["claim_id"] == claim_id])
            for sid in claims[claim_id]["source_ids"]:
                self.assertFalse(sources[sid]["withdrawn"], f"{sid} is withdrawn but still cited by {claim_id}")
        self.assertEqual(claims["CLM-0067"]["u11_applicability"], "PARTIAL")

    def test_no_withdrawn_source_used_in_chapter(self):
        sources = load("research/sources.json")["sources"]
        withdrawn_ids = {s["source_id"] for s in sources if s["withdrawn"]}
        principle = load("data/principles/principle-limbaj-scurt-si-relevanta.json")
        for sid in principle["sources"]:
            self.assertNotIn(sid, withdrawn_ids)

    def test_external_focus_and_timing_content(self):
        text = (ROOT / "content/volume-03/chapter-01.mdx").read_text(encoding="utf-8")
        self.assertIn("64%", text)
        self.assertIn("reper extern", text)
        self.assertIn("Împinge mingea unde nu e adversar", text)

    def test_field_tool_no_stopwatch(self):
        card = (ROOT / "docs/content/CH_0301_CONCISE_LANGUAGE_CARD.md").read_text(encoding="utf-8")
        self.assertIn("Nu impune un cronometru", card)
        self.assertIn("Test anti-monolog", card)

    def test_message_foundation(self):
        p = load("data/principles/principle-limbaj-scurt-si-relevanta.json")
        self.assertEqual(len(p["rationales"]), 7)
        for key in ("child_message", "coach_meaning", "why_this_message", "understanding_check", "response_if_not_understood", "match_transfer"):
            self.assertTrue(p[key])

    def test_principle_json_exists(self):
        path = ROOT / "data/principles/principle-limbaj-scurt-si-relevanta.json"
        self.assertTrue(path.exists())

    def test_field_tool_card_exists(self):
        path = ROOT / "docs/content/CH_0301_CONCISE_LANGUAGE_CARD.md"
        self.assertTrue(path.exists())


if __name__ == "__main__":
    unittest.main()
