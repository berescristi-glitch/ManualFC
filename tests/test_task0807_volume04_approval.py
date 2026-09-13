import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class Task0807Tests(unittest.TestCase):
    def test_volume_04_approval_audit_exists(self):
        path = ROOT / "reports/audits/volume-04-approval.md"
        self.assertTrue(path.exists())
        text = path.read_text(encoding="utf-8")
        self.assertIn("PASS_FIELD_REVIEW_READY", text)
        self.assertIn("VOLUME-04", text)

    def test_volume_04_field_review_package_exists(self):
        path = ROOT / "docs/field-review/VOLUME_04_FIELD_REVIEW_PACKAGE.md"
        self.assertTrue(path.exists())
        text = path.read_text(encoding="utf-8")
        # The original "COMPLETE_FOR_FIELD_REVIEW = YES" verdict was cancelled by the
        # forensic audit (DEC-0040), then re-earned through remediation (TASK-0809) and
        # a genuinely independent re-audit (TASK-0810) — the string is legitimate again.
        self.assertIn("VOLUME_04_COMPLETE_FOR_FIELD_REVIEW = YES", text)
        self.assertIn("TASK-0810", text)

    def test_volume_04_manifest_exists(self):
        path = ROOT / "content/volume-04/manifest.json"
        self.assertTrue(path.exists())

    def test_volume_04_web_routes_exist(self):
        self.assertTrue((ROOT / "app/src/pages/volum/04/index.astro").exists())
        self.assertTrue((ROOT / "app/src/pages/volum/04/[chapter].astro").exists())


if __name__ == "__main__":
    unittest.main()
