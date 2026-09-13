import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


class Task0804Tests(unittest.TestCase):
    def test_chapter_mdx_exists_and_contains_pedagogical_loop(self):
        path = ROOT / "content/volume-04/chapter-04.mdx"
        self.assertTrue(path.exists())
        text = path.read_text(encoding="utf-8")
        self.assertIn('chapter_id: "CH-0404"', text)
        for marker in ("Formularea exactă", "Tactic", "Perceptiv", "Psihologic", "verificare", "înțelegerii", "Transferul în joc"):
            self.assertIn(marker.lower(), text.lower())

    def test_no_fabricated_cushion_2012_source(self):
        text = (ROOT / "content/volume-04/chapter-04.mdx").read_text(encoding="utf-8")
        self.assertNotIn("Cushion et al. 2012", text)
        self.assertNotIn("Cushion et al. (2012)", text)

    def test_no_unsupported_timing_number(self):
        text = (ROOT / "content/volume-04/chapter-04.mdx").read_text(encoding="utf-8")
        card = (ROOT / "docs/content/CH_0404_OBSERVATION_INTERVENTION_CARD.md").read_text(encoding="utf-8")
        for bad in ("15 secunde", "Regula celor 3", "sub 15 secunde"):
            self.assertNotIn(bad, text)
            self.assertNotIn(bad, card)
        self.assertIn("fără un cronometru exact validat de cercetare", text)

    def test_safety_exception_kept(self):
        text = (ROOT / "content/volume-04/chapter-04.mdx").read_text(encoding="utf-8")
        self.assertIn("Siguranța și respectul cer intervenție imediată", text)

    def test_old_claim_replaced_not_silently_dropped(self):
        claims = {x["claim_id"]: x for x in load("research/claims.json")["claims"]}
        self.assertEqual(claims["CLM-0062"]["status"], "REPLACED")
        self.assertEqual(claims["CLM-0062"]["replacement_claim_id"], "CLM-0094")
        sources = {s["source_id"]: s for s in load("research/sources.json")["sources"]}
        self.assertTrue(sources["SRC-0061"]["withdrawn"])

    def test_claim_chain_and_no_withdrawn_source_in_use(self):
        claims = {x["claim_id"]: x for x in load("research/claims.json")["claims"]}
        citations = load("research/citations.json")["citations"]
        sources = {s["source_id"]: s for s in load("research/sources.json")["sources"]}
        clm = claims["CLM-0094"]
        self.assertEqual(clm["status"], "VERIFIED")
        self.assertTrue([c for c in citations if c["claim_id"] == "CLM-0094"])
        for sid in clm["source_ids"]:
            self.assertFalse(sources[sid]["withdrawn"], f"{sid} is withdrawn but still cited by CLM-0094")
        principle = load("data/principles/principle-focalizarea-observatiei-si-criterii-de-interventie.json")
        withdrawn_ids = {s["source_id"] for s in load("research/sources.json")["sources"] if s["withdrawn"]}
        for sid in principle["sources"]:
            self.assertNotIn(sid, withdrawn_ids)

    def test_principle_json_exists(self):
        path = ROOT / "data/principles/principle-focalizarea-observatiei-si-criterii-de-interventie.json"
        self.assertTrue(path.exists())

    def test_field_tool_card_exists(self):
        path = ROOT / "docs/content/CH_0404_OBSERVATION_INTERVENTION_CARD.md"
        self.assertTrue(path.exists())


if __name__ == "__main__":
    unittest.main()
