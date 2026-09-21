export const COACH_STATE_KEY = 'manualfc.coach-state.v1';

export type CanonicalKind = 'problem' | 'principle' | 'exercise' | 'session' | 'assessment' | 'chapter' | 'script';
export interface CanonicalRef { id: string; kind: CanonicalKind; href: string; title: string; }
export interface RecentRef extends CanonicalRef { visitedAt: string; }
export interface WorkspaceItem { ref: CanonicalRef; minutes: number; }
export interface WorkspaceSession {
  id: string;
  title: string;
  problemId?: string;
  duration: 60 | 75;
  players: number;
  coaches: 1 | 2;
  items: WorkspaceItem[];
  notes: string;
  updatedAt: string;
}
export interface CoachProfile { experience: 'incepator' | 'intermediar' | 'experimentat'; defaultPlayers: number; defaultDuration: 60 | 75; onboardingDone: boolean; }

export type ObservedState = 'not_observed' | 'emerging' | 'partial' | 'consistent_in_task';
export type TransferState = 'transfer_unconfirmed' | 'transfer_seen';
export interface SessionReflection {
  id: string;
  createdAt: string;
  updatedAt: string;
  workspaceSessionId?: string;
  canonicalSessionId?: string;
  problemId?: string;
  exerciseIds: string[];
  observedState: ObservedState;
  transferState: TransferState;
  whatWorked?: string;
  whyItHappened?: string;
  whatToChange?: string;
  coachNote?: string;
}

export type OfflinePackStatus = 'READY' | 'NOT_READY' | 'UPDATE_AVAILABLE';
export interface OfflineCanonicalRef { kind: 'exercise' | 'session'; id: string; }
export interface OfflinePackManifest {
  id: string;
  workspaceSessionId: string;
  routes: string[];
  mediaRefs: string[];
  canonicalRefs: OfflineCanonicalRef[];
  contentVersion: string;
  createdAt: string;
  updatedAt: string;
  status: OfflinePackStatus;
}

export interface CoachState {
  version: 1;
  profile: CoachProfile;
  saved: CanonicalRef[];
  favorites: CanonicalRef[];
  recents: RecentRef[];
  sessions: WorkspaceSession[];
  reflections: SessionReflection[];
  offlinePacks: OfflinePackManifest[];
  activeSessionId?: string;
}

const defaults = (): CoachState => ({
  version: 1,
  profile: { experience: 'incepator', defaultPlayers: 12, defaultDuration: 75, onboardingDone: false },
  saved: [], favorites: [], recents: [], sessions: [], reflections: [], offlinePacks: []
});

const VALID_KINDS: readonly CanonicalKind[] = ['problem', 'principle', 'exercise', 'session', 'assessment', 'chapter', 'script'];
const isKind = (v: unknown): v is CanonicalKind => typeof v === 'string' && (VALID_KINDS as readonly string[]).includes(v);

export function clampPlayers(v: unknown): number {
  const n = Number(v);
  return Number.isFinite(n) ? Math.min(18, Math.max(8, Math.round(n))) : 12;
}
const sanitizeDuration = (v: unknown): 60 | 75 => (Number(v) === 60 ? 60 : 75);
const sanitizeCoaches = (v: unknown): 1 | 2 => (Number(v) === 2 ? 2 : 1);

function sanitizeRef(v: unknown): CanonicalRef | null {
  if (!v || typeof v !== 'object') return null;
  const r = v as Record<string, unknown>;
  if (typeof r.id !== 'string' || !r.id || !isKind(r.kind) || typeof r.href !== 'string' || !r.href || typeof r.title !== 'string' || !r.title) return null;
  return { id: r.id, kind: r.kind, href: r.href, title: r.title };
}
const sanitizeRefList = (v: unknown): CanonicalRef[] => Array.isArray(v) ? v.map(sanitizeRef).filter((x): x is CanonicalRef => x !== null) : [];

function sanitizeRecent(v: unknown): RecentRef | null {
  const ref = sanitizeRef(v);
  if (!ref) return null;
  const visitedAt = (v as Record<string, unknown>).visitedAt;
  return { ...ref, visitedAt: typeof visitedAt === 'string' ? visitedAt : new Date(0).toISOString() };
}
const sanitizeRecents = (v: unknown): RecentRef[] => Array.isArray(v) ? v.map(sanitizeRecent).filter((x): x is RecentRef => x !== null).slice(0, 12) : [];

function sanitizeItem(v: unknown): WorkspaceItem | null {
  if (!v || typeof v !== 'object') return null;
  const r = v as Record<string, unknown>;
  const ref = sanitizeRef(r.ref);
  if (!ref) return null;
  const minutes = Number(r.minutes);
  return { ref, minutes: Number.isFinite(minutes) && minutes > 0 ? minutes : 15 };
}
const sanitizeItems = (v: unknown): WorkspaceItem[] => Array.isArray(v) ? v.map(sanitizeItem).filter((x): x is WorkspaceItem => x !== null) : [];

function sanitizeSession(v: unknown): WorkspaceSession | null {
  if (!v || typeof v !== 'object') return null;
  const r = v as Record<string, unknown>;
  if (typeof r.id !== 'string' || !r.id) return null;
  return {
    id: r.id,
    title: typeof r.title === 'string' && r.title ? r.title : 'Ședința mea',
    problemId: typeof r.problemId === 'string' ? r.problemId : undefined,
    duration: sanitizeDuration(r.duration),
    players: clampPlayers(r.players),
    coaches: sanitizeCoaches(r.coaches),
    items: sanitizeItems(r.items),
    notes: typeof r.notes === 'string' ? r.notes : '',
    updatedAt: typeof r.updatedAt === 'string' ? r.updatedAt : new Date(0).toISOString()
  };
}
const sanitizeSessions = (v: unknown): WorkspaceSession[] => Array.isArray(v) ? v.map(sanitizeSession).filter((x): x is WorkspaceSession => x !== null) : [];

const OBSERVED_STATES: readonly ObservedState[] = ['not_observed', 'emerging', 'partial', 'consistent_in_task'];
const isObservedState = (v: unknown): v is ObservedState => typeof v === 'string' && (OBSERVED_STATES as readonly string[]).includes(v);
const TRANSFER_STATES: readonly TransferState[] = ['transfer_unconfirmed', 'transfer_seen'];
const isTransferState = (v: unknown): v is TransferState => typeof v === 'string' && (TRANSFER_STATES as readonly string[]).includes(v);

function sanitizeReflection(v: unknown): SessionReflection | null {
  if (!v || typeof v !== 'object') return null;
  const r = v as Record<string, unknown>;
  if (typeof r.id !== 'string' || !r.id || !isObservedState(r.observedState)) return null;
  const str = (x: unknown): string | undefined => typeof x === 'string' && x ? x : undefined;
  return {
    id: r.id,
    createdAt: typeof r.createdAt === 'string' ? r.createdAt : new Date(0).toISOString(),
    updatedAt: typeof r.updatedAt === 'string' ? r.updatedAt : new Date(0).toISOString(),
    workspaceSessionId: str(r.workspaceSessionId),
    canonicalSessionId: str(r.canonicalSessionId),
    problemId: str(r.problemId),
    exerciseIds: Array.isArray(r.exerciseIds) ? r.exerciseIds.filter((x): x is string => typeof x === 'string') : [],
    observedState: r.observedState,
    transferState: isTransferState(r.transferState) ? r.transferState : 'transfer_unconfirmed',
    whatWorked: str(r.whatWorked),
    whyItHappened: str(r.whyItHappened),
    whatToChange: str(r.whatToChange),
    coachNote: str(r.coachNote)
  };
}
const sanitizeReflections = (v: unknown): SessionReflection[] => Array.isArray(v) ? v.map(sanitizeReflection).filter((x): x is SessionReflection => x !== null) : [];

const OFFLINE_PACK_STATUSES: readonly OfflinePackStatus[] = ['READY', 'NOT_READY', 'UPDATE_AVAILABLE'];
const isOfflinePackStatus = (v: unknown): v is OfflinePackStatus => typeof v === 'string' && (OFFLINE_PACK_STATUSES as readonly string[]).includes(v);
function sanitizeOfflineCanonicalRef(v: unknown): OfflineCanonicalRef | null {
  if (!v || typeof v !== 'object') return null;
  const r = v as Record<string, unknown>;
  if ((r.kind !== 'exercise' && r.kind !== 'session') || typeof r.id !== 'string' || !r.id) return null;
  return { kind: r.kind, id: r.id };
}
function sanitizeOfflinePack(v: unknown): OfflinePackManifest | null {
  if (!v || typeof v !== 'object') return null;
  const r = v as Record<string, unknown>;
  if (typeof r.id !== 'string' || !r.id || typeof r.workspaceSessionId !== 'string' || !r.workspaceSessionId) return null;
  return {
    id: r.id,
    workspaceSessionId: r.workspaceSessionId,
    routes: Array.isArray(r.routes) ? r.routes.filter((x): x is string => typeof x === 'string') : [],
    mediaRefs: Array.isArray(r.mediaRefs) ? r.mediaRefs.filter((x): x is string => typeof x === 'string') : [],
    canonicalRefs: Array.isArray(r.canonicalRefs) ? r.canonicalRefs.map(sanitizeOfflineCanonicalRef).filter((x): x is OfflineCanonicalRef => x !== null) : [],
    contentVersion: typeof r.contentVersion === 'string' ? r.contentVersion : '',
    createdAt: typeof r.createdAt === 'string' ? r.createdAt : new Date(0).toISOString(),
    updatedAt: typeof r.updatedAt === 'string' ? r.updatedAt : new Date(0).toISOString(),
    status: isOfflinePackStatus(r.status) ? r.status : 'NOT_READY'
  };
}
const sanitizeOfflinePacks = (v: unknown): OfflinePackManifest[] => Array.isArray(v) ? v.map(sanitizeOfflinePack).filter((x): x is OfflinePackManifest => x !== null) : [];

function sanitizeProfile(v: unknown): CoachProfile {
  const d = defaults().profile;
  if (!v || typeof v !== 'object') return d;
  const r = v as Record<string, unknown>;
  const experience = r.experience === 'incepator' || r.experience === 'intermediar' || r.experience === 'experimentat' ? r.experience : d.experience;
  return {
    experience,
    defaultPlayers: clampPlayers(r.defaultPlayers ?? d.defaultPlayers),
    defaultDuration: sanitizeDuration(r.defaultDuration ?? d.defaultDuration),
    onboardingDone: typeof r.onboardingDone === 'boolean' ? r.onboardingDone : d.onboardingDone
  };
}

function sanitizeState(parsed: unknown): CoachState {
  if (!parsed || typeof parsed !== 'object') return defaults();
  const r = parsed as Record<string, unknown>;
  if (r.version !== 1) return defaults();
  const sessions = sanitizeSessions(r.sessions);
  const activeSessionId = typeof r.activeSessionId === 'string' && sessions.some(s => s.id === r.activeSessionId) ? r.activeSessionId : undefined;
  return {
    version: 1,
    profile: sanitizeProfile(r.profile),
    saved: sanitizeRefList(r.saved),
    favorites: sanitizeRefList(r.favorites),
    recents: sanitizeRecents(r.recents),
    sessions,
    reflections: sanitizeReflections(r.reflections),
    offlinePacks: sanitizeOfflinePacks(r.offlinePacks),
    activeSessionId
  };
}

export interface CoachStatePort { read(): CoachState; write(state: CoachState): void; }
export const browserCoachStatePort: CoachStatePort = {
  read() {
    if (typeof localStorage === 'undefined') return defaults();
    try {
      const raw = localStorage.getItem(COACH_STATE_KEY);
      if (!raw) return defaults();
      return sanitizeState(JSON.parse(raw));
    } catch { return defaults(); }
  },
  write(state) { if (typeof localStorage !== 'undefined') localStorage.setItem(COACH_STATE_KEY, JSON.stringify(state)); }
};

export function updateCoachState(change: (state: CoachState) => CoachState, port = browserCoachStatePort) {
  const next = change(port.read()); port.write(next); window.dispatchEvent(new CustomEvent('manualfc:state')); return next;
}
export function toggleRef(list: CanonicalRef[], ref: CanonicalRef) {
  return list.some(item => item.id === ref.id && item.kind === ref.kind)
    ? list.filter(item => !(item.id === ref.id && item.kind === ref.kind)) : [ref, ...list];
}
export function recordRecent(ref: CanonicalRef, port = browserCoachStatePort) {
  return updateCoachState(state => ({ ...state, recents: [{ ...ref, visitedAt: new Date().toISOString() }, ...state.recents.filter(x => !(x.id === ref.id && x.kind === ref.kind))].slice(0, 12) }), port);
}
export function makeSession(state: CoachState): WorkspaceSession {
  const now = new Date().toISOString();
  return { id: `ws-${Date.now()}`, title: 'Ședința mea', duration: state.profile.defaultDuration, players: state.profile.defaultPlayers, coaches: 1, items: [], notes: '', updatedAt: now };
}

export const OBSERVED_STATE_LABELS: Record<ObservedState, string> = {
  not_observed: 'Nu a apărut', emerging: 'Abia apare', partial: 'Apare parțial', consistent_in_task: 'Apare constant, autonom'
};
export const TRANSFER_STATE_LABELS: Record<TransferState, string> = {
  transfer_unconfirmed: 'Doar în exercițiu', transfer_seen: 'Și în joc liber'
};

/** Recomandarea este calculată determinist din stare, niciodată generată liber. */
export function computeNextAction(observed: ObservedState, transfer: TransferState): string {
  if (observed === 'not_observed') return 'Reconsideră ipoteza: încearcă o regresie sau un test diferit.';
  if (observed === 'emerging') return 'Repetă sarcina cu același reper; comportamentul abia apare.';
  if (observed === 'partial') return 'Repetă sau ajustează o singură variabilă a sarcinii.';
  return transfer === 'transfer_seen'
    ? 'Crește dificultatea sau verifică transferul într-un context diferit.'
    : 'Păstrează reperul și testează dacă apare și în joc mai liber.';
}

export type ReflectionInput = Omit<SessionReflection, 'id' | 'createdAt' | 'updatedAt'> & { id?: string };
export function saveReflection(input: ReflectionInput, port = browserCoachStatePort): SessionReflection {
  const state = port.read();
  const now = new Date().toISOString();
  const existing = input.id ? state.reflections.find(r => r.id === input.id) : undefined;
  const reflection: SessionReflection = { ...input, id: existing?.id ?? `refl-${Date.now()}`, createdAt: existing?.createdAt ?? now, updatedAt: now };
  updateCoachState(s => ({
    ...s,
    reflections: existing ? s.reflections.map(r => r.id === reflection.id ? reflection : r) : [reflection, ...s.reflections]
  }), port);
  return reflection;
}
export function deleteReflection(id: string, port = browserCoachStatePort) {
  return updateCoachState(state => ({ ...state, reflections: state.reflections.filter(r => r.id !== id) }), port);
}
export function deleteWorkspaceSession(id: string, port = browserCoachStatePort) {
  return updateCoachState(state => ({
    ...state,
    sessions: state.sessions.filter(s => s.id !== id),
    offlinePacks: state.offlinePacks.filter(p => p.workspaceSessionId !== id),
    activeSessionId: state.activeSessionId === id ? undefined : state.activeSessionId
  }), port);
}
/** O ședință construită, ne-activă, fără nicio reflecție legată încă — candidat pentru Continue V2 prioritatea 2. */
export function findUnreflectedSession(state: CoachState): WorkspaceSession | undefined {
  return state.sessions.find(s => s.id !== state.activeSessionId && !state.reflections.some(r => r.workspaceSessionId === s.id));
}

export type OfflinePackInput = Omit<OfflinePackManifest, 'id' | 'createdAt' | 'updatedAt'>;
export function saveOfflinePack(input: OfflinePackInput, port = browserCoachStatePort): OfflinePackManifest {
  const state = port.read();
  const now = new Date().toISOString();
  const existing = state.offlinePacks.find(p => p.workspaceSessionId === input.workspaceSessionId);
  const pack: OfflinePackManifest = { ...input, id: existing?.id ?? `pack-${Date.now()}`, createdAt: existing?.createdAt ?? now, updatedAt: now };
  updateCoachState(s => ({
    ...s,
    offlinePacks: existing ? s.offlinePacks.map(p => p.id === pack.id ? pack : p) : [pack, ...s.offlinePacks]
  }), port);
  return pack;
}
export function deleteOfflinePack(id: string, port = browserCoachStatePort) {
  return updateCoachState(state => ({ ...state, offlinePacks: state.offlinePacks.filter(p => p.id !== id) }), port);
}
export function findOfflinePackForSession(state: CoachState, workspaceSessionId: string): OfflinePackManifest | undefined {
  return state.offlinePacks.find(p => p.workspaceSessionId === workspaceSessionId);
}
/** Recalculeaza starea pachetului fata de versiunea curenta a continutului canonic, fara sa presupuna READY implicit. */
export function resolveOfflinePackStatus(pack: OfflinePackManifest, currentContentVersion: string): OfflinePackStatus {
  if (pack.status === 'NOT_READY') return 'NOT_READY';
  return pack.contentVersion === currentContentVersion ? 'READY' : 'UPDATE_AVAILABLE';
}
