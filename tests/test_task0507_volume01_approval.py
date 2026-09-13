import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class Task0507Tests(unittest.TestCase):
    def test_all_chapters_have_uniform_identity_and_substance(self):
        for number in range(1, 11):
            path = ROOT / f"content/volume-01/chapter-{number:02d}.mdx"
            text = path.read_text(encoding="utf-8")
            self.assertIn(f'chapter_id: "CH-01{number:02d}"', text)
            self.assertGreater(len(text), 2500)

    def test_chapter_one_contains_full_pedagogical_loop(self):
        text = (ROOT / "content/volume-01/chapter-01.mdx").read_text(encoding="utf-8")
        for marker in ("Formularea exactă", "Tactic", "Perceptiv", "Psihologic", "Verificarea înțelegerii", "Transfer în joc", "Limite"):
            self.assertIn(marker, text)

    def test_all_canonical_principles_are_loaded_by_web_bridge(self):
        bridge = (ROOT / "app/src/lib/content-bridge.ts").read_text(encoding="utf-8")
        for filename in (
            "principle-variabilitatea-dezvoltarii-u11.json",
            "principle-adaptarea-sarcinii-u11.json",
            "principle-eroarea-ca-informatie.json",
            "principle-mesaj-pedagogic-observabil.json",
            "principle-transfer-autonom-cooperare.json",
        ):
            self.assertIn(filename, bridge)

    def test_manifest_declares_ten_static_routes(self):
        manifest = json.loads((ROOT / "content/volume-01/manifest.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest["status"], "FIELD_REVIEW_READY")
        self.assertEqual(len(manifest["chapters"]), 10)
        self.assertEqual(len({item["route"] for item in manifest["chapters"]}), 10)

    def test_field_review_package_is_non_diagnostic(self):
        text = (ROOT / "docs/field-review/VOLUME_01_FIELD_REVIEW_PACKAGE.md").read_text(encoding="utf-8")
        for marker in ("nu testează copilul", "NO_OPPORTUNITY", "joystick coaching", "DEFERRED_BY_DESIGN_FREEZE"):
            self.assertIn(marker, text)

    def test_static_volume_pages_exist(self):
        self.assertTrue((ROOT / "app/src/pages/volum/01/index.astro").exists())
        dynamic = (ROOT / "app/src/pages/volum/01/[chapter].astro").read_text(encoding="utf-8")
        for number in range(1, 11):
            self.assertIn(f"ch-01{number:02d}", dynamic)


if __name__ == "__main__":
    unittest.main()
