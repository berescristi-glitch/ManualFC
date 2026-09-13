import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class Task0708Tests(unittest.TestCase):
    def test_volume03_manifest_exists(self):
        path = ROOT / "content/volume-03/manifest.json"
        self.assertTrue(path.exists())

    def test_field_review_package_exists(self):
        path = ROOT / "docs/field-review/VOLUME_03_FIELD_REVIEW_PACKAGE.md"
        self.assertTrue(path.exists())

    def test_approval_report_exists(self):
        path = ROOT / "reports/audits/volume-03-approval.md"
        self.assertTrue(path.exists())
        text = path.read_text(encoding="utf-8")
        self.assertIn("PASS_FIELD_REVIEW_READY", text)
        self.assertIn("VOLUME_03_COMPLETE_FOR_FIELD_REVIEW = YES", text)

    def test_web_routes_exist(self):
        self.assertTrue((ROOT / "app/src/pages/volum/03/index.astro").exists())
        self.assertTrue((ROOT / "app/src/pages/volum/03/[chapter].astro").exists())


if __name__ == "__main__":
    unittest.main()
