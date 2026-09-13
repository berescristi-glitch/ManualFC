from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ProductPivotTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.registry = json.loads((ROOT / "TASK_REGISTRY.json").read_text(encoding="utf-8"))
        cls.tasks = {x["task_id"]: x for x in cls.registry["tasks"]}
        cls.project = json.loads((ROOT / "config/project.json").read_text(encoding="utf-8"))

    def test_01_done_preserved(self):
        for tid in ("TASK-0001", "TASK-0002", "TASK-0101", "TASK-0102", "TASK-0103", "TASK-0104"):
            self.assertEqual(self.tasks[tid]["status"], "DONE")

    def test_02_task_0104_done(self): self.assertEqual(self.tasks["TASK-0104"]["status"], "DONE")
    def test_03_registry_reproducible_marker(self): self.assertEqual(self.registry["generator"], "scripts/generate_task_registry.py")
    def test_04_weights_sum_100(self): self.assertAlmostEqual(sum(x["weight_percent"] for x in self.tasks.values()), 100, places=6)
    def test_05_prior_progress_preserved(self):
        ids=("TASK-0001","TASK-0002","TASK-0101","TASK-0102","TASK-0103","TASK-0104")
        self.assertAlmostEqual(sum(self.tasks[x]["weight_percent"] for x in ids), 2.462, places=6)

    def test_06_dependencies_exist(self):
        self.assertFalse([(x["task_id"],d) for x in self.tasks.values() for d in x["dependencies"] if d not in self.tasks])

    def test_07_no_cycles(self):
        visiting=set(); done=set()
        def visit(t):
            if t in visiting: raise AssertionError(t)
            if t in done: return
            visiting.add(t)
            for dep in self.tasks[t]["dependencies"]: visit(dep)
            visiting.remove(t); done.add(t)
        for tid in self.tasks: visit(tid)

    def test_08_multimedia_outputs(self):
        for tid in ("TASK-0303","TASK-0304","TASK-0403","TASK-0404","TASK-0411"):
            self.assertTrue(self.tasks[tid]["outputs"])

    def test_09_content_pedagogical_audit(self):
        self.assertTrue(all("pedagogic" in " ".join(x["acceptance_criteria"]).lower() for x in self.tasks.values() if x["title"].startswith("Capitol —")))

    def test_10_content_editorial_audit(self):
        self.assertTrue(all("editorial" in " ".join(x["acceptance_criteria"]).lower() for x in self.tasks.values() if x["title"].startswith("Capitol —")))

    def test_11_tactical_static_diagram(self): self.assertIn("diagramă statică", " ".join(self.tasks["TASK-0411"]["acceptance_criteria"]))
    def test_12_selected_animation(self): self.assertIn("animație", " ".join(self.tasks["TASK-0411"]["acceptance_criteria"]))
    def test_13_pdf_fallback(self): self.assertIn("fallbackul PDF", " ".join(self.tasks["TASK-0415"]["acceptance_criteria"]))
    def test_14_accessibility(self): self.assertIn("accesibil", (ROOT/"PRODUCT_REQUIREMENTS.md").read_text(encoding="utf-8").lower())
    def test_15_field_test_no_personal_data(self): self.assertIn("Nu se stochează date personale", " ".join(self.tasks["TASK-0413"]["acceptance_criteria"]))
    def test_16_other_ages_not_produced(self): self.assertEqual(self.project["future_age_architecture"]["production_scope"], "10–11")
    def test_17_single_2015_2016_category(self): self.assertEqual(self.project["age_category"]["birth_years"], [2015, 2016])
    def test_18_no_premature_monetization(self): self.assertIn("nu include\nautentificare", (ROOT/"COMMERCIALIZATION_ROADMAP.md").read_text(encoding="utf-8"))
    def test_19_next_ready(self): self.assertEqual(sorted([x["task_id"] for x in self.tasks.values() if x["status"]=="READY"]), [])
    def test_20_every_task_migrated(self): self.assertTrue(all(x.get("migration_disposition") for x in self.tasks.values()))


if __name__ == "__main__": unittest.main()
