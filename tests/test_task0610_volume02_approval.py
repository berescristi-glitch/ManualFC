import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class Task0610Tests(unittest.TestCase):
    def test_all_volume02_chapters_exist_and_have_valid_frontmatter(self):
        for number in range(1, 9):
            path = ROOT / f"content/volume-02/chapter-{number:02d}.mdx"
            self.assertTrue(path.exists(), f"Missing chapter-{number:02d}.mdx")
            text = path.read_text(encoding="utf-8")
            self.assertIn(f'chapter_id: "CH-02{number:02d}"', text)
            self.assertGreater(len(text), 2500)

    def test_all_eight_volume02_principles_are_registered_in_content_bridge(self):
        bridge_text = (ROOT / "app/src/lib/content-bridge.ts").read_text(encoding="utf-8")
        expected_files = [
            "principle-jocul-ca-sistem-de-probleme.json",
            "principle-spatiu-si-unghiuri.json",
            "principle-progresie-si-sprijin.json",
            "principle-protejarea-centrului.json",
            "principle-presiune-si-acoperire.json",
            "principle-tranzitia-la-pierderea-mingii.json",
            "principle-tranzitia-la-castigarea-mingii.json",
            "principle-superioritate-egalitate-inferioritate-numerica.json"
        ]
        for filename in expected_files:
            self.assertIn(filename, bridge_text, f"Principle file {filename} is not registered in content-bridge.ts")

    def test_volume02_manifest_is_valid_and_complete(self):
        manifest_path = ROOT / "content/volume-02/manifest.json"
        self.assertTrue(manifest_path.exists(), "content/volume-02/manifest.json must exist")
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        self.assertEqual(manifest["volume_id"], "VOLUME-02")
        self.assertEqual(manifest["status"], "FIELD_REVIEW_READY")
        self.assertEqual(len(manifest["chapters"]), 8)
        routes = [ch["route"] for ch in manifest["chapters"]]
        self.assertEqual(len(set(routes)), 8)
        for i, route in enumerate(routes, 1):
            self.assertEqual(route, f"/volum/02/ch-02{i:02d}")

    def test_volume02_static_routes_exist_and_render_all_chapters(self):
        index_astro = ROOT / "app/src/pages/volum/02/index.astro"
        chapter_astro = ROOT / "app/src/pages/volum/02/[chapter].astro"
        self.assertTrue(index_astro.exists(), "app/src/pages/volum/02/index.astro must exist")
        self.assertTrue(chapter_astro.exists(), "app/src/pages/volum/02/[chapter].astro must exist")
        
        index_text = index_astro.read_text(encoding="utf-8")
        chapter_text = chapter_astro.read_text(encoding="utf-8")
        
        for number in range(1, 9):
            slug = f"ch-02{number:02d}"
            self.assertIn(slug, index_text)
            self.assertIn(slug, chapter_text)

    def test_volume02_field_review_package_exists_and_references_all_tools(self):
        pkg_path = ROOT / "docs/field-review/VOLUME_02_FIELD_REVIEW_PACKAGE.md"
        self.assertTrue(pkg_path.exists(), "VOLUME_02_FIELD_REVIEW_PACKAGE.md must exist")
        pkg_text = pkg_path.read_text(encoding="utf-8")
        
        required_headers = [
            "SCOPUL PILOTULUI",
            "CE TESTĂM",
            "CE NU TESTĂM / CE NU PUTEM CONCLUZIONA",
            "UNITĂȚILE/CAPITOLELE TESTATE",
            "FIELD TOOLS TESTATE",
            "CE OBSERVĂ ANTRENORUL",
            "CE ÎI SPUNE COPILULUI",
            "CE COMPORTAMENTE URMĂREȘTE",
            "CE MODIFICĂ",
            "CE ÎNREGISTREAZĂ",
            "SEMNALE POZITIVE",
            "SEMNALE DE PROBLEMĂ",
            "TRANSFER ÎN JOC",
            "FEEDBACKUL ANTRENORULUI",
            "LIMITE",
            "DECIZIE DUPĂ PILOT"
        ]
        pkg_upper = pkg_text.upper()
        for header in required_headers:
            self.assertIn(header, pkg_upper, f"Field review package missing header: {header}")

        expected_tools = [
            "CH_0201_GAME_PROBLEM_CANVAS.md",
            "CH_0202_SPACE_ANGLE_OBSERVATION_CARD.md",
            "CH_0203_PROGRESSION_SUPPORT_CARD.md",
            "CH_0204_PROTECT_CENTRE_CARD.md",
            "CH_0205_PRESSURE_COVER_CARD.md",
            "CH_0206_TRANSITION_LOSS_CARD.md",
            "CH_0207_TRANSITION_WIN_CARD.md",
            "CH_0208_NUMERICAL_SITUATIONS_CARD.md"
        ]
        for tool in expected_tools:
            self.assertIn(tool, pkg_text, f"Field review package missing tool reference: {tool}")


if __name__ == "__main__":
    unittest.main()
