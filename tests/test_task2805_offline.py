import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class CoachStateOfflinePackTests(unittest.TestCase):
    def setUp(self):
        self.source = (ROOT / "app/src/lib/coach-state.ts").read_text(encoding="utf-8")

    def test_offline_pack_extends_v1_without_breaking_existing_fields(self):
        self.assertIn("offlinePacks: OfflinePackManifest[]", self.source)
        self.assertIn("saved: [], favorites: [], recents: [], sessions: [], reflections: [], offlinePacks: []", self.source)
        self.assertIn("offlinePacks: sanitizeOfflinePacks(r.offlinePacks)", self.source)

    def test_offline_pack_sanitizer_is_fail_closed(self):
        self.assertIn("function sanitizeOfflinePack(v: unknown): OfflinePackManifest | null", self.source)
        self.assertIn("isOfflinePackStatus(r.status) ? r.status : 'NOT_READY'", self.source)

    def test_offline_pack_status_never_defaults_to_ready(self):
        # A malformed/unknown status must fail closed to NOT_READY, never READY.
        self.assertNotIn("isOfflinePackStatus(r.status) ? r.status : 'READY'", self.source)

    def test_deleting_session_also_removes_its_offline_pack(self):
        self.assertIn("offlinePacks: state.offlinePacks.filter(p => p.workspaceSessionId !== id)", self.source)

    def test_resolve_offline_pack_status_detects_content_version_mismatch(self):
        self.assertIn("export function resolveOfflinePackStatus(pack: OfflinePackManifest, currentContentVersion: string): OfflinePackStatus", self.source)
        self.assertIn("pack.contentVersion === currentContentVersion ? 'READY' : 'UPDATE_AVAILABLE'", self.source)


class OfflinePackLibTests(unittest.TestCase):
    def setUp(self):
        self.source = (ROOT / "app/src/lib/offline-pack.ts").read_text(encoding="utf-8")

    def test_no_content_bridge_import_keeps_module_client_cheap(self):
        self.assertNotIn("from './content-bridge'", self.source)
        self.assertNotIn("from './problem-library'", self.source)

    def test_computes_resource_graph_deterministically_from_lookup(self):
        self.assertIn("export function computeResourceGraph(session: WorkspaceSession, lookup: ResourceLookup): ResourceGraph", self.source)
        self.assertIn("unresolvedRefs.push(item.ref.id)", self.source)

    def test_shared_routes_only_included_when_exercise_present(self):
        self.assertIn("if (hasExercise) lookup.sharedRoutes.forEach", self.source)

    def test_prepare_offline_pack_is_fail_closed_without_service_worker(self):
        self.assertIn("SERVICE_WORKER_UNSUPPORTED", self.source)
        self.assertIn("SERVICE_WORKER_NOT_CONTROLLING", self.source)
        self.assertIn("ok: failedRoutes.length === 0", self.source)

    def test_content_version_sourced_from_platform_data_not_hardcoded_twice(self):
        self.assertIn("import contentVersionData from '../../../data/platform/content-version.json'", self.source)


class ServiceWorkerTests(unittest.TestCase):
    def setUp(self):
        self.source = (ROOT / "public/sw.js").read_text(encoding="utf-8")

    def test_cache_names_are_versioned(self):
        self.assertIn("SW_VERSION", self.source)
        self.assertIn("manualfc-shell-", self.source)
        self.assertIn("manualfc-pack-", self.source)

    def test_activate_cleans_up_stale_caches_only(self):
        self.assertIn("key.startsWith('manualfc-') && key !== SHELL_CACHE && key !== PACK_CACHE", self.source)

    def test_does_not_force_immediate_activation_mid_session(self):
        self.assertNotIn("skipWaiting()", self.source)

    def test_navigation_falls_back_to_offline_page_not_blank(self):
        self.assertIn("OFFLINE_FALLBACK_URL", self.source)
        self.assertIn("/offline/", self.source)

    def test_precached_manifest_is_actually_served_from_cache_when_offline(self):
        # manifest.webmanifest is precached into SHELL_CACHE at install, but the fetch
        # handler only matched a few hardcoded path prefixes — an offline request for
        # it fell through with no respondWith(), producing a real (not handled)
        # net::ERR_INTERNET_DISCONNECTED instead of being served from cache.
        self.assertIn("url.pathname === '/manifest.webmanifest'", self.source)

    def test_precaches_hashed_astro_assets_so_unvisited_pages_still_work_offline(self):
        # MANUALFC_CACHE_URLS only fetches a route's HTML document. A canonical
        # session added to a workspace but never actually visited online would
        # otherwise 504 on its own CSS/JS bundle the moment it's opened offline.
        self.assertIn("astro-assets-manifest.json", self.source)
        self.assertIn("precacheHashedAssets", self.source)

    def test_asset_cache_lookups_ignore_vary_for_hash_named_files(self):
        # Server responses carry `Vary: Origin`; module-script fetches (always
        # CORS-mode per spec) can present a subtly different Origin than the SW's
        # own install-time fetch, making caches.match() spuriously miss a genuinely
        # cached, content-hashed file. Safe to ignore since the hash already
        # guarantees byte-identical content for a given URL.
        self.assertIn("caches.match(request, { ignoreVary: true })", self.source)
        self.assertIn("ignoreSearch: true, ignoreVary: true", self.source)

    def test_only_same_origin_get_requests_are_intercepted(self):
        self.assertIn("url.origin !== self.location.origin || request.method !== 'GET'", self.source)

    def test_message_handler_reports_cached_and_failed_routes(self):
        self.assertIn("MANUALFC_CACHE_URLS", self.source)
        self.assertIn("cachedRoutes.push", self.source)
        self.assertIn("failedRoutes.push", self.source)


class AstroAssetsManifestTests(unittest.TestCase):
    def test_build_script_generates_the_manifest_after_astro_build(self):
        pkg = json.loads((ROOT / "package.json").read_text(encoding="utf-8"))
        self.assertIn("generate_astro_manifest.mjs", pkg["scripts"]["build"])
        self.assertLess(
            pkg["scripts"]["build"].index("astro build"),
            pkg["scripts"]["build"].index("generate_astro_manifest.mjs"),
        )

    def test_manifest_generator_writes_into_dist_not_public(self):
        source = (ROOT / "scripts/generate_astro_manifest.mjs").read_text(encoding="utf-8")
        self.assertIn("dist", source)
        self.assertIn("astro-assets-manifest.json", source)


class ManifestAndFallbackTests(unittest.TestCase):
    def test_manifest_is_valid_json_with_required_installability_fields(self):
        data = json.loads((ROOT / "public/manifest.webmanifest").read_text(encoding="utf-8"))
        for field in ("name", "short_name", "start_url", "display", "background_color", "theme_color", "icons"):
            self.assertIn(field, data)
        self.assertGreaterEqual(len(data["icons"]), 2)
        sizes = {icon["sizes"] for icon in data["icons"]}
        self.assertIn("192x192", sizes)
        self.assertIn("512x512", sizes)

    def test_manifest_start_url_targets_workspace_not_generic_home(self):
        data = json.loads((ROOT / "public/manifest.webmanifest").read_text(encoding="utf-8"))
        self.assertEqual(data["start_url"], "/spatiul-meu/")

    def test_offline_fallback_page_exists_and_does_not_overclaim(self):
        source = (ROOT / "app/src/pages/offline.astro").read_text(encoding="utf-8")
        self.assertIn("nu a fost pregătită pentru teren", source)
        self.assertNotIn("Funcționează complet offline", source)

    def test_content_version_file_is_valid_and_documented(self):
        data = json.loads((ROOT / "data/platform/content-version.json").read_text(encoding="utf-8"))
        self.assertIn("version", data)
        self.assertIsInstance(data["version"], str)


class BaseLayoutRegistrationTests(unittest.TestCase):
    def test_registers_manifest_and_service_worker_progressively(self):
        source = (ROOT / "app/src/layouts/BaseLayout.astro").read_text(encoding="utf-8")
        self.assertIn('rel="manifest"', source)
        self.assertIn("navigator.serviceWorker.register('/sw.js')", source)
        # Progressive enhancement: a failed registration must not throw uncaught.
        self.assertIn(".catch(() => {", source)


class SessionBuilderCanonicalSessionTests(unittest.TestCase):
    def setUp(self):
        self.source = (ROOT / "app/src/pages/spatiul-meu/sedinta.astro").read_text(encoding="utf-8")

    def test_builder_can_add_a_canonical_session_not_only_exercises(self):
        # Field Mode (timer, segments) only exists on canonical Gold Standard sessions,
        # never on individual exercise pages — so preparing a workspace session for
        # offline field use is only meaningful end-to-end if a canonical session can
        # be linked in, not just its component exercises.
        self.assertIn("data-session-catalog", self.source)
        self.assertIn("data-add-session", self.source)
        self.assertIn("kind:'session'", self.source)

    def test_reconciliation_is_kind_aware_for_both_exercises_and_sessions(self):
        self.assertIn("catalogFor(x.ref.kind).has(x.ref.id)", self.source)

    def test_minutes_input_upper_bound_accommodates_full_canonical_sessions(self):
        # A canonical session item can carry up to ~90 minutes; a max sized only for
        # individual exercises (45) silently blocks native form submission with no
        # visible error the moment a session item is added.
        self.assertNotIn('max="45"', self.source)
        self.assertIn('data-minutes type="number" min="5" max="90"', self.source)


class WorkspaceOfflineUiTests(unittest.TestCase):
    def setUp(self):
        self.source = (ROOT / "app/src/pages/spatiul-meu/index.astro").read_text(encoding="utf-8")

    def test_prepare_button_checks_online_state_before_attempting(self):
        self.assertIn("if(!navigator.onLine){", self.source)

    def test_never_claims_ready_without_successful_result(self):
        self.assertIn("status:'NOT_READY'", self.source)
        self.assertIn("status:'READY'", self.source)
        self.assertIn("graph.unresolvedRefs.length||!result.ok", self.source)

    def test_connectivity_feedback_uses_precise_language(self):
        self.assertIn("Offline — ședințele pregătite pentru teren rămân disponibile.", self.source)
        self.assertNotIn("Funcționează complet offline", self.source)

    def test_task2802_2803_surfaces_still_present_no_regression(self):
        for marker in ("data-saved", "data-favorites", "data-recents", "data-continue-link", "data-onboarding", "data-sessions", "data-reflections"):
            self.assertIn(marker, self.source)


if __name__ == "__main__":
    unittest.main()
