import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class BootstrapTests(unittest.TestCase):
    def test_registry_is_reproducible(self):
        result = subprocess.run(
            [sys.executable, "scripts/generate_task_registry.py", "--check"],
            cwd=ROOT, capture_output=True, text=True
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_registry_weights_sum_to_100(self):
        registry = json.loads((ROOT / "TASK_REGISTRY.json").read_text(encoding="utf-8"))
        self.assertAlmostEqual(sum(task["weight_percent"] for task in registry["tasks"]), 100.0)

    def test_single_age_category_is_canonical(self):
        config = json.loads((ROOT / "config/project.json").read_text(encoding="utf-8"))
        self.assertEqual(config["age_category"]["birth_years"], [2015, 2016])
        self.assertTrue(config["age_category"]["single_curriculum"])

    def test_research_registries_are_valid_containers(self):
        for name, key, id_key in (
            ("sources", "sources", "source_id"),
            ("claims", "claims", "claim_id"),
            ("citations", "citations", "citation_id"),
        ):
            data = json.loads((ROOT / f"research/{name}.json").read_text(encoding="utf-8"))
            self.assertIsInstance(data[key], list)
            ids = [item[id_key] for item in data[key]]
            self.assertEqual(len(ids), len(set(ids)))


if __name__ == "__main__":
    unittest.main()
