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
            "/rezolva-pe-teren": "Rezolvă pe teren",
            "/gold-standard": "Modul complet",
        }
        for route, label in expected.items():
            self.assertIn(f"'{route}': '{label}'", text)

    def test_footer_exposes_same_five_destinations(self):
        # TASK-3721: the footer no longer hardcodes <a href="..."> markup for each
        # destination -- it renders dynamically from getPrimaryNavigation(), the
        # same single source of truth the header uses (avoiding the duplicate,
        # divergence-prone route lists this test originally guarded against).
        # The five original destinations remain configured, just via a label map
        # instead of static markup.
        text = (ROOT / "app/src/components/AppFooter.astro").read_text(encoding="utf-8")
        self.assertIn("getPrimaryNavigation", text)
        for route in ("/incepe-aici", "/volum", "/principii", "/rezolva-pe-teren", "/gold-standard"):
            self.assertIn(f"'{route}':", text)

    def test_primary_surfaces_use_plain_language_titles(self):
        principle_index = (ROOT / "app/src/pages/principii/index.astro").read_text(encoding="utf-8")
        rezolva = (ROOT / "app/src/pages/rezolva-pe-teren/index.astro").read_text(encoding="utf-8")
        module = (ROOT / "app/src/pages/gold-standard/index.astro").read_text(encoding="utf-8")
        self.assertIn("Principii pentru joc și antrenament", principle_index)
        self.assertIn("Rezolvă pe teren", rezolva)
        self.assertIn("Modul complet", module)


if __name__ == "__main__":
    unittest.main()
