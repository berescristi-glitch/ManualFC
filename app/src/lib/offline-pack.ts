/**
 * TASK-2805 — offline field pack: resource-graph computation and service-worker
 * orchestration. Deliberately free of any content-bridge/problem-library import
 * so this module stays cheap to include in any client <script> — the canonical
 * lookup table (which routes/media a given exercise or session maps to) is built
 * server-side in Astro frontmatter (see app/src/pages/spatiul-meu/index.astro)
 * and passed in, mirroring the existing data-embedding pattern already used by
 * the session builder and reflection pages.
 *
 * Domain vs. cache separation (see docs/architecture/OFFLINE_ACCOUNT_ENTITLEMENT.md):
 * the pack MANIFEST (which session, which routes, which content version) is user
 * state and lives in CoachState/localStorage via coach-state.ts. The actual bytes
 * for those routes live in the Service Worker's Cache Storage, named per pack.
 * Reflections and saved sessions are never written into Cache Storage.
 */
import contentVersionData from '../../../data/platform/content-version.json';
import type { OfflineCanonicalRef, WorkspaceSession } from './coach-state';

export const CONTENT_VERSION: string = contentVersionData.version;

export interface ExerciseResourceInfo { id: string; route: string; mediaIds: string[]; }
export interface SessionResourceInfo { id: string; route: string; fieldModeRoutes: string[]; }
export interface ResourceLookup {
  exercises: Record<string, ExerciseResourceInfo>;
  sessions: Record<string, SessionResourceInfo>;
  sharedRoutes: string[];
}

export interface ResourceGraph {
  routes: string[];
  canonicalRefs: OfflineCanonicalRef[];
  mediaRefs: string[];
  unresolvedRefs: string[];
}

const ALWAYS_INCLUDED_ROUTES = ['/spatiul-meu', '/spatiul-meu/sedinta', '/spatiul-meu/reflectie'];

/** Rezolvă determinist ce rute/media sunt necesare pentru o ședință — nu întreține liste duplicate manual. */
export function computeResourceGraph(session: WorkspaceSession, lookup: ResourceLookup): ResourceGraph {
  const routes = new Set<string>(ALWAYS_INCLUDED_ROUTES);
  const canonicalRefs: OfflineCanonicalRef[] = [];
  const mediaRefs = new Set<string>();
  const unresolvedRefs: string[] = [];
  let hasExercise = false;

  for (const item of session.items) {
    if (item.ref.kind === 'exercise') {
      const info = lookup.exercises[item.ref.id];
      if (!info) { unresolvedRefs.push(item.ref.id); continue; }
      hasExercise = true;
      routes.add(info.route);
      info.mediaIds.forEach((m) => mediaRefs.add(m));
      canonicalRefs.push({ kind: 'exercise', id: item.ref.id });
    } else if (item.ref.kind === 'session') {
      const info = lookup.sessions[item.ref.id];
      if (!info) { unresolvedRefs.push(item.ref.id); continue; }
      routes.add(info.route);
      info.fieldModeRoutes.forEach((r) => routes.add(r));
      canonicalRefs.push({ kind: 'session', id: item.ref.id });
    }
  }
  if (hasExercise) lookup.sharedRoutes.forEach((r) => routes.add(r));

  return { routes: Array.from(routes), canonicalRefs, mediaRefs: Array.from(mediaRefs), unresolvedRefs };
}

export interface PrepareResult { ok: boolean; cachedRoutes: string[]; failedRoutes: string[]; reason?: string; }

/** Cere Service Worker-ului sa precacheze exact rutele grafului; fail-closed daca SW nu e disponibil sau activ. */
export async function prepareOfflinePack(graph: ResourceGraph, timeoutMs = 20000): Promise<PrepareResult> {
  if (typeof navigator === 'undefined' || !('serviceWorker' in navigator)) {
    return { ok: false, cachedRoutes: [], failedRoutes: graph.routes, reason: 'SERVICE_WORKER_UNSUPPORTED' };
  }
  let registration: ServiceWorkerRegistration;
  try {
    registration = await navigator.serviceWorker.ready;
  } catch {
    return { ok: false, cachedRoutes: [], failedRoutes: graph.routes, reason: 'SERVICE_WORKER_NOT_READY' };
  }
  const controller = navigator.serviceWorker.controller ?? registration.active;
  if (!controller) {
    return { ok: false, cachedRoutes: [], failedRoutes: graph.routes, reason: 'SERVICE_WORKER_NOT_CONTROLLING' };
  }
  return new Promise((resolve) => {
    const channel = new MessageChannel();
    const timer = setTimeout(() => {
      resolve({ ok: false, cachedRoutes: [], failedRoutes: graph.routes, reason: 'TIMEOUT' });
    }, timeoutMs);
    channel.port1.onmessage = (event) => {
      clearTimeout(timer);
      const data = event.data as { cachedRoutes?: string[]; failedRoutes?: string[] };
      const cachedRoutes = Array.isArray(data.cachedRoutes) ? data.cachedRoutes : [];
      const failedRoutes = Array.isArray(data.failedRoutes) ? data.failedRoutes : graph.routes;
      resolve({ ok: failedRoutes.length === 0, cachedRoutes, failedRoutes });
    };
    controller.postMessage({ type: 'MANUALFC_CACHE_URLS', urls: graph.routes, version: CONTENT_VERSION }, [channel.port2]);
  });
}
