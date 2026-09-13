import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


class Task0802Tests(unittest.TestCase):
    def test_chapter_mdx_exists_and_contains_pedagogical_loop(self):
        path = ROOT / "content/volume-04/chapter-02.mdx"
        self.assertTrue(path.exists())
        text = path.read_text(encoding="utf-8")
        self.assertIn('chapter_id: "CH-0402"', text)
        for marker in ("Formularea exactă", "Tactic", "Perceptiv", "Psihologic", "verificare", "înțelegerii", "Transferul în joc"):
            self.assertIn(marker.lower(), text.lower())

    def test_no_fabricated_chow_2016_source(self):
        text = (ROOT / "content/volume-04/chapter-02.mdx").read_text(encoding="utf-8")
        self.assertNotIn("Chow et al. 2016", text)
        self.assertNotIn("Chow et al. (2016)", text)

    def test_avoids_cla_always_superior_dogma(self):
        text = (ROOT / "content/volume-04/chapter-02.mdx").read_text(encoding="utf-8")
        self.assertIn("Despre limitele metodei", text)
        self.assertIn("Nu există dovadă că manipularea constrângerilor e superioară în orice situație instrucției directe", text)

    def test_no_unsupported_hard_number_presented_as_evidence(self):
        text = (ROOT / "content/volume-04/chapter-02.mdx").read_text(encoding="utf-8")
        card = (ROOT / "docs/content/CH_0402_CONSTRAINTS_MATRIX_CARD.md").read_text(encoding="utf-8")
        self.assertNotIn("5 secunde pentru finalizare", card)
        self.assertIn("euristică practică ManualFC", card)

    def test_old_claim_replaced_not_silently_dropped(self):
        claims = {x["claim_id"]: x for x in load("research/claims.json")["claims"]}
        self.assertEqual(claims["CLM-0060"]["status"], "REPLACED")
        self.assertEqual(claims["CLM-0060"]["replacement_claim_id"], "CLM-0090")
        sources = {s["source_id"]: s for s in load("research/sources.json")["sources"]}
        self.assertTrue(sources["SRC-0059"]["withdrawn"])

    def test_claim_chain_and_no_withdrawn_source_in_use(self):
        claims = {x["claim_id"]: x for x in load("research/claims.json")["claims"]}
        citations = load("research/citations.json")["citations"]
        sources = {s["source_id"]: s for s in load("research/sources.json")["sources"]}
        for claim_id in ("CLM-0089", "CLM-0090", "CLM-0091"):
            self.assertEqual(claims[claim_id]["status"], "VERIFIED")
            self.assertTrue([c for c in citations if c["claim_id"] == claim_id])
            for sid in claims[claim_id]["source_ids"]:
                self.assertFalse(sources[sid]["withdrawn"], f"{sid} is withdrawn but still cited by {claim_id}")
        principle = load("data/principles/principle-manipularea-si-dozarea-constrangerilor.json")
        withdrawn_ids = {s["source_id"] for s in load("research/sources.json")["sources"] if s["withdrawn"]}
        for sid in principle["sources"]:
            self.assertNotIn(sid, withdrawn_ids)

    def test_principle_json_exists(self):
        path = ROOT / "data/principles/principle-manipularea-si-dozarea-constrangerilor.json"
        self.assertTrue(path.exists())

    def test_field_tool_card_exists(self):
        path = ROOT / "docs/content/CH_0402_CONSTRAINTS_MATRIX_CARD.md"
        self.assertTrue(path.exists())


if __name__ == "__main__":
    unittest.main()
