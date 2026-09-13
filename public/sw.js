/**
 * TASK-2805 — ManualFC service worker. Plain vanilla JS, no build step, no
 * external library (see docs/architecture/OFFLINE_ACCOUNT_ENTITLEMENT.md for
 * why: a simple tactical/field caching need does not justify Workbox).
 *
 * Two caches, both versioned so an app update can clean up stale assets
 * without ever touching personal state (reflections/sessions live in
 * localStorage via coach-state.ts, never in Cache Storage):
 *   - SHELL_CACHE: the minimal app shell (Workspace/Builder/Reflection shells,
 *     icons, manifest, offline fallback, hashed build assets under /_astro/).
 *   - PACK_CACHE: routes explicitly requested by a coach's "Disponibil pe
 *     teren" action (see offline-pack.ts) plus opportunistically-cached
 *     navigations, so a route visited once while online tends to stay usable.
 *
 * Conservative update policy: the install handler does not force immediate
 * activation, so an updated worker waits until the coach naturally closes
 * and reopens the app instead of forcing a reload mid-session (explicit
 * TASK-2805 requirement: never interrupt an active Field Mode segment).
 */
const SW_VERSION = 'v2';
const SHELL_CACHE = `manualfc-shell-${SW_VERSION}`;
const PACK_CACHE = `manualfc-pack-${SW_VERSION}`;
const OFFLINE_FALLBACK_URL = '/offline/';

const APP_SHELL_URLS = [
  '/',
  '/spatiul-meu/',
  '/spatiul-meu/sedinta/',
  '/spatiul-meu/reflectie/',
  OFFLINE_FALLBACK_URL,
  '/manifest.webmanifest',
  '/brand/manualfc/logo/manualfc-icon-192.png',
  '/brand/manualfc/logo/manualfc-icon-512.png'
];

/**
 * Precaching only the HTML document of a route (what MANUALFC_CACHE_URLS does)
 * is not enough: the page still references hashed /_astro/*.css and *.js files
 * that were never fetched if the coach hadn't already visited that exact page
 * online. astro-assets-manifest.json is generated at build time (see
 * scripts/generate_astro_manifest.mjs) and lists every hashed asset in the
 * build, so every page's CSS/JS is guaranteed present offline regardless of
 * which pages were actually visited before going offline.
 */
async function precacheHashedAssets(cache) {
  try {
    const res = await fetch('/astro-assets-manifest.json', { cache: 'reload' });
    if (!res.ok) return;
    const data = await res.json();
    const routes = Array.isArray(data.routes) ? data.routes : [];
    await Promise.all(routes.map((r) => cache.add(r).catch(() => {})));
  } catch {
    /* offline-first install: a missing manifest must not break shell precache */
  }
}

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(SHELL_CACHE).then(async (cache) => {
      await cache.addAll(APP_SHELL_URLS).catch(() => {});
      await precacheHashedAssets(cache);
    })
  );
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    (async () => {
      const keys = await caches.keys();
      await Promise.all(
        keys
          .filter((key) => key.startsWith('manualfc-') && key !== SHELL_CACHE && key !== PACK_CACHE)
          .map((key) => caches.delete(key))
      );
      await self.clients.claim();
    })()
  );
});

function isNavigationRequest(request) {
  return request.mode === 'navigate' || (request.method === 'GET' && (request.headers.get('accept') || '').includes('text/html'));
}

async function networkFirstNavigation(request) {
  try {
    const response = await fetch(request);
    if (response && response.ok) {
      const cache = await caches.open(PACK_CACHE);
      cache.put(request, response.clone()).catch(() => {});
    }
    return response;
  } catch {
    const cached =
      (await caches.match(request, { ignoreVary: true })) ||
      (await caches.match(request, { ignoreSearch: true, ignoreVary: true }));
    if (cached) return cached;
    const fallback = await caches.match(OFFLINE_FALLBACK_URL, { ignoreVary: true });
    if (fallback) return fallback;
    return new Response(
      'ManualFC este offline si aceasta pagina nu a fost pregatita pentru teren.',
      { status: 503, headers: { 'Content-Type': 'text/plain; charset=utf-8' } }
    );
  }
}

async function cacheFirstAsset(request) {
  // ignoreVary: true — the server sends `Vary: Origin`, and module-script fetches
  // (always CORS-mode per spec) can carry a subtly different Origin header than the
  // one used when this file was precached at install time, causing caches.match()
  // to sporadically miss a genuinely cached entry. Safe here because these are
  // content-hashed filenames: identical URL already guarantees identical bytes.
  const cached = await caches.match(request, { ignoreVary: true });
  if (cached) return cached;
  try {
    const response = await fetch(request);
    if (response && response.ok) {
      const cache = await caches.open(SHELL_CACHE);
      cache.put(request, response.clone()).catch(() => {});
    }
    return response;
  } catch {
    return new Response('', { status: 504 });
  }
}

self.addEventListener('fetch', (event) => {
  const { request } = event;
  let url;
  try { url = new URL(request.url); } catch { return; }
  if (url.origin !== self.location.origin || request.method !== 'GET') return;

  if (isNavigationRequest(request)) {
    event.respondWith(networkFirstNavigation(request));
    return;
  }
  if (
    url.pathname.startsWith('/_astro/') ||
    url.pathname.startsWith('/brand/') ||
    url.pathname === '/manifest.webmanifest'
  ) {
    event.respondWith(cacheFirstAsset(request));
  }
});

self.addEventListener('message', (event) => {
  const data = event.data;
  if (!data || data.type !== 'MANUALFC_CACHE_URLS') return;
  const urls = Array.isArray(data.urls) ? data.urls : [];
  const port = event.ports && event.ports[0];
  event.waitUntil(
    (async () => {
      const cache = await caches.open(PACK_CACHE);
      const cachedRoutes = [];
      const failedRoutes = [];
      for (const requestUrl of urls) {
        try {
          const response = await fetch(requestUrl, { cache: 'reload' });
          if (response && response.ok) {
            await cache.put(requestUrl, response.clone());
            cachedRoutes.push(requestUrl);
          } else {
            failedRoutes.push(requestUrl);
          }
        } catch {
          failedRoutes.push(requestUrl);
        }
      }
      if (port) port.postMessage({ cachedRoutes, failedRoutes });
    })()
  );
});
