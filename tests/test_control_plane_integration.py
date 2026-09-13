import unittest
import json
import tempfile
from pathlib import Path
from scripts.control_plane_integration import (
    load_registry,
    get_completed_task_ids,
    get_ready_tasks,
    get_next_ready_task,
    evaluate_automation_budget_gate,
    verify_task_outputs,
    audit_control_plane_status,
    ControlPlaneIntegrationError
)

class TestControlPlaneIntegration(unittest.TestCase):
    def setUp(self):
        self.mock_registry = {
            "tasks": [
                {
                    "task_id": "TASK-0001",
                    "title": "Task 1",
                    "status": "DONE",
                    "priority": "HIGH",
                    "dependencies": [],
                    "outputs": ["file1.txt"]
                },
                {
                    "task_id": "TASK-0002",
                    "title": "Task 2",
                    "status": "READY",
                    "priority": "CRITICAL",
                    "dependencies": ["TASK-0001"],
                    "outputs": ["file2.txt"]
                },
                {
                    "task_id": "TASK-0003",
                    "title": "Task 3",
                    "status": "PENDING",
                    "priority": "HIGH",
                    "dependencies": ["TASK-0002"],
                    "outputs": []
                }
            ]
        }

    def test_load_registry_valid(self):
        with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, encoding="utf-8") as f:
            json.dump(self.mock_registry, f)
            f_path = Path(f.name)
        try:
            reg = load_registry(f_path)
            self.assertEqual(len(reg["tasks"]), 3)
        finally:
            if f_path.exists():
                f_path.unlink()

    def test_load_registry_missing_file(self):
        with self.assertRaises(ControlPlaneIntegrationError):
            load_registry(Path("non_existent_registry.json"))

    def test_get_completed_task_ids(self):
        completed = get_completed_task_ids(self.mock_registry)
        self.assertIn("TASK-0001", completed)
        self.assertNotIn("TASK-0002", completed)

    def test_get_ready_tasks(self):
        ready = get_ready_tasks(self.mock_registry)
        self.assertEqual(len(ready), 1)
        self.assertEqual(ready[0]["task_id"], "TASK-0002")

    def test_get_next_ready_task(self):
        next_task = get_next_ready_task(self.mock_registry)
        self.assertIsNotNone(next_task)
        self.assertEqual(next_task["task_id"], "TASK-0002")

    def test_evaluate_budget_gate_none_gap(self):
        res = evaluate_automation_budget_gate("NONE", interventions_used=1)
        self.assertTrue(res["proceed_to_product"])
        self.assertFalse(res["abandon_automation"])
        self.assertEqual(res["next_product_task"], "TASK-0401")
        self.assertEqual(res["status"], "CLEAN_INTEGRATION")

    def test_evaluate_budget_gate_small_adapter(self):
        res = evaluate_automation_budget_gate("SMALL_ADAPTER", interventions_used=1)
        self.assertFalse(res["proceed_to_product"])
        self.assertEqual(res["allowed_extra_tasks"], 1)

    def test_evaluate_budget_gate_moderate_gap(self):
        res = evaluate_automation_budget_gate("MODERATE_GAP", interventions_used=1)
        self.assertTrue(res["proceed_to_product"])
        self.assertTrue(res["abandon_automation"])
        self.assertEqual(res["next_product_task"], "TASK-0401")

    def test_evaluate_budget_gate_major_rework(self):
        res = evaluate_automation_budget_gate("MAJOR_REWORK", interventions_used=1)
        self.assertTrue(res["proceed_to_product"])
        self.assertTrue(res["abandon_automation"])

    def test_evaluate_budget_gate_exceeded(self):
        res = evaluate_automation_budget_gate("NONE", interventions_used=3)
        self.assertTrue(res["proceed_to_product"])
        self.assertTrue(res["abandon_automation"])
        self.assertEqual(res["status"], "BUGET_EXCEEDED")

    def test_evaluate_budget_gate_invalid_gap(self):
        with self.assertRaises(ControlPlaneIntegrationError):
            evaluate_automation_budget_gate("INVALID_GAP_TYPE")

    def test_verify_task_outputs(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            tmp_path = Path(tmp_dir)
            (tmp_path / "file1.txt").write_text("content", encoding="utf-8")
            ok, missing = verify_task_outputs("TASK-0001", self.mock_registry, base_dir=tmp_path)
            self.assertTrue(ok)
            self.assertEqual(missing, [])

            ok_missing, missing_list = verify_task_outputs("TASK-0002", self.mock_registry, base_dir=tmp_path)
            self.assertFalse(ok_missing)
            self.assertIn("file2.txt", missing_list)

    def test_audit_control_plane_status_runs(self):
        audit = audit_control_plane_status()
        self.assertIn("total_tasks", audit)
        self.assertIn("completed_tasks", audit)
        self.assertIn("automation_budget_used", audit)

if __name__ == "__main__":
    unittest.main()
