import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class Task0707Tests(unittest.TestCase):
    def test_audit_report_exists_and_contains_verdict(self):
        path = ROOT / "reports/audits/volume-03-audit.md"
        self.assertTrue(path.exists())
        text = path.read_text(encoding="utf-8")
        self.assertIn("REPAIR_REQUIRED", text)
        self.assertIn("V03-M01", text)
        self.assertIn("V03-M02", text)
        self.assertIn("V03-M03", text)


if __name__ == "__main__":
    unittest.main()
