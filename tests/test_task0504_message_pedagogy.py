import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
load = lambda p: json.loads((ROOT / p).read_text(encoding="utf-8"))


class Task0504Tests(unittest.TestCase):
    def test_chapter_preserves_architecture_and_task_theme(self):
        text = (ROOT / "content/volume-01/chapter-04.mdx").read_text(encoding="utf-8")
        self.assertIn('chapter_id: "CH-0104"', text)
        for term in ("Formularea mesajului pedagogic", "motiva", "autonomi", "încredere"):
            self.assertIn(term, text)

    def test_claim_chains_and_metadata(self):
        claims = {x["claim_id"]: x for x in load("research/claims.json")["claims"]}
        citations = load("research/citations.json")["citations"]
        sources = {x["source_id"] for x in load("research/sources.json")["sources"]}
        for cid in ("CLM-0034", "CLM-0035"):
            claim = claims[cid]
            links = [x for x in citations if x["claim_id"] == cid]
            self.assertTrue(links)
            self.assertEqual(claim["u11_applicability"], "INDIRECT")
            self.assertTrue(claim["limitations"] and claim["practical_implication"])
            self.assertTrue(all(x["source_id"] in sources for x in links))

    def test_protocol_is_actionable_and_non_diagnostic(self):
        text = (ROOT / "docs/content/CH_0104_MESSAGE_COMPRESSION_PROTOCOL.md").read_text(encoding="utf-8")
        for marker in ("CE AI VĂZUT", "REPER", "ALEGERE", "REIA", "Nu este o scală psihologică"):
            self.assertIn(marker, text)

    def test_child_message_has_complete_foundation(self):
        p = load("data/principles/principle-mesaj-pedagogic-observabil.json")
        self.assertTrue(p["child_message"] and p["coach_meaning"] and p["why_this_message"])
        self.assertTrue(p["understanding_check"] and p["response_if_not_understood"] and p["match_transfer"])
        self.assertEqual(len(p["rationales"]), 7)

    def test_dossier_separates_support_limits_and_translation(self):
        text = (ROOT / "research/dossiers/ch-0104-message-pedagogy.md").read_text(encoding="utf-8")
        for section in ("What the evidence supports", "does NOT support", "U11 applicability", "Limitations", "Practical translation", "Citation map"):
            self.assertIn(section, text)

    def test_audits_are_separate(self):
        self.assertTrue((ROOT / "reports/audits/TASK-0504-factual-pedagogical-audit.md").exists())
        self.assertTrue((ROOT / "reports/audits/TASK-0504-editorial-audit.md").exists())

    def test_report_references_real_task(self):
        registry = load("TASK_REGISTRY.json")
        self.assertTrue(any(x["task_id"] == "TASK-0504" for x in registry["tasks"]))
        self.assertTrue((ROOT / "reports/task-reports/TASK-0504.md").exists())


if __name__ == "__main__":
    unittest.main()
