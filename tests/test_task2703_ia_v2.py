import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class InformationArchitectureV2Tests(unittest.TestCase):
    def test_header_maps_real_routes_to_coach_jobs(self):
        text = (ROOT / "app/src/components/AppHeader.astro").read_text(encoding="utf-8")
        expected = {
            "/incepe-aici": "Începe aici",
            "/volum": "Învață",
            "/principii": "Principii aplicate",
            "/gold-standard/rapid": "Rezolvă pe teren",
            "/gold-standard": "Modul complet",
        }
        for route, label in expected.items():
            self.assertIn(f"'{route}': '{label}'", text)

    def test_footer_exposes_same_five_destinations(self):
        text = (ROOT / "app/src/components/AppFooter.astro").read_text(encoding="utf-8")
        for route in ("/incepe-aici", "/volum", "/principii", "/gold-standard/rapid", "/gold-standard"):
            self.assertIn(f'href="{route}"', text)

    def test_primary_surfaces_use_plain_language_titles(self):
        principle_index = (ROOT / "app/src/pages/principii/index.astro").read_text(encoding="utf-8")
        rapid = (ROOT / "app/src/pages/gold-standard/rapid.astro").read_text(encoding="utf-8")
        module = (ROOT / "app/src/pages/gold-standard/index.astro").read_text(encoding="utf-8")
        self.assertIn("Principii pentru joc și antrenament", principle_index)
        self.assertIn("Rezolvă pe teren", rapid)
        self.assertIn("Modul complet", module)


if __name__ == "__main__":
    unittest.main()
