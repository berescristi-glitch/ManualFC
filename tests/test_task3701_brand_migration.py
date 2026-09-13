import json
import unittest
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
LOGO_DIR = ROOT_DIR / "public" / "brand" / "manualfc" / "logo"

OLD_BRAND_FILENAMES = [
    "manualfc-logo-master.png",
    "manualfc-mark-master.png",
    "manualfc-logo-light-web.png",
    "manualfc-logo-dark-web.png",
    "manualfc-mark-web.png",
    "manualfc-favicon-128.png",
]


class BrandMigrationTests(unittest.TestCase):
    def test_canonical_master_asset_exists(self):
        master = LOGO_DIR / "manualfc-brand-master.png"
        self.assertTrue(master.exists(), "manualfc-brand-master.png (canonical V2 master) lipseste.")

    def test_required_derivative_assets_exist(self):
        required = [
            "manualfc-logo-full.png",
            "manualfc-logo-horizontal.png",
            "manualfc-mark.png",
            "manualfc-icon-512.png",
            "manualfc-icon-192.png",
            "manualfc-apple-touch-icon.png",
            "manualfc-favicon-48.png",
            "manualfc-favicon-32.png",
            "manualfc-favicon-16.png",
            "manualfc-social.png",
        ]
        for name in required:
            self.assertTrue((LOGO_DIR / name).exists(), f"Derivat de brand V2 lipseste: {name}")

    def test_old_shield_identity_assets_removed(self):
        for name in OLD_BRAND_FILENAMES:
            self.assertFalse((LOGO_DIR / name).exists(), f"Asset din identitatea V1 (shield) inca prezent: {name}")
        self.assertFalse((ROOT_DIR / "public" / "icons" / "icon-192.png").exists())
        self.assertFalse((ROOT_DIR / "public" / "icons" / "icon-512.png").exists())

    def test_logo_assets_manifest_matches_files_on_disk(self):
        manifest_path = LOGO_DIR / "logo-assets.json"
        self.assertTrue(manifest_path.exists())
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        self.assertEqual(manifest.get("status"), "MANUALFC_CANONICAL_LOGO_IDENTITY_V2")
        for entry in manifest.get("assets", []):
            asset_path = LOGO_DIR / entry["asset"]
            self.assertTrue(asset_path.exists(), f"logo-assets.json referentiaza un fisier inexistent: {entry['asset']}")

    def test_manualfc_logo_component_has_no_surface_prop(self):
        component = (ROOT_DIR / "app" / "src" / "components" / "ManualFCLogo.astro").read_text(encoding="utf-8")
        self.assertNotIn("surface?:", component, "ManualFCLogo.astro nu ar trebui sa mai expuna prop-ul 'surface' (nu exista varianta oficiala light/inversata).")
        self.assertNotIn("showTagline", component)
        self.assertIn("'full' | 'horizontal' | 'mark'", component)

    def test_header_uses_new_horizontal_lockup(self):
        header = (ROOT_DIR / "app" / "src" / "components" / "AppHeader.astro").read_text(encoding="utf-8")
        self.assertIn('variant="horizontal"', header)
        self.assertNotIn("showTagline", header)
        self.assertNotIn("surface=", header)

    def test_footer_uses_new_lockup(self):
        footer = (ROOT_DIR / "app" / "src" / "components" / "AppFooter.astro").read_text(encoding="utf-8")
        self.assertIn("ManualFCLogo", footer)
        self.assertNotIn("showTagline", footer)
        self.assertNotIn("surface=", footer)
        self.assertNotIn("logo-tagline-size", footer)

    def test_base_layout_favicon_and_social_meta_reference_new_assets(self):
        layout = (ROOT_DIR / "app" / "src" / "layouts" / "BaseLayout.astro").read_text(encoding="utf-8")
        self.assertIn("manualfc-favicon-16.png", layout)
        self.assertIn("manualfc-favicon-32.png", layout)
        self.assertIn("manualfc-favicon-48.png", layout)
        self.assertIn("manualfc-apple-touch-icon.png", layout)
        self.assertIn('property="og:image"', layout)
        self.assertIn("manualfc-social.png", layout)
        self.assertIn('name="twitter:image"', layout)
        for old_name in OLD_BRAND_FILENAMES:
            self.assertNotIn(old_name, layout)
        self.assertNotIn("/icons/icon-192.png", layout)

    def test_manifest_webmanifest_uses_new_icons(self):
        manifest_path = ROOT_DIR / "public" / "manifest.webmanifest"
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        icon_srcs = [icon["src"] for icon in manifest.get("icons", [])]
        self.assertIn("/brand/manualfc/logo/manualfc-icon-192.png", icon_srcs)
        self.assertIn("/brand/manualfc/logo/manualfc-icon-512.png", icon_srcs)
        for src in icon_srcs:
            self.assertFalse(src.startswith("/icons/"), f"manifest.webmanifest inca refera vechea locatie /icons/: {src}")

    def test_service_worker_precaches_new_icons_only(self):
        sw = (ROOT_DIR / "public" / "sw.js").read_text(encoding="utf-8")
        self.assertIn("manualfc-icon-192.png", sw)
        self.assertIn("manualfc-icon-512.png", sw)
        self.assertNotIn("/icons/icon-192.png", sw)
        self.assertNotIn("/icons/icon-512.png", sw)

    def test_design_system_lab_has_no_obsolete_surface_usage(self):
        design_system = (ROOT_DIR / "app" / "src" / "internal-pages" / "design-system.astro").read_text(encoding="utf-8")
        self.assertNotIn("surface=", design_system)
        self.assertNotIn("showTagline", design_system)

    def test_brand_system_v2_doc_exists(self):
        doc = ROOT_DIR / "docs" / "brand" / "MANUALFC_BRAND_SYSTEM_V2.md"
        self.assertTrue(doc.exists())
        content = doc.read_text(encoding="utf-8")
        self.assertIn("ȘTIINȚĂ. PEDAGOGIE. PRACTICĂ.", content)
        self.assertIn("DEC-0080", content)


if __name__ == "__main__":
    unittest.main()
