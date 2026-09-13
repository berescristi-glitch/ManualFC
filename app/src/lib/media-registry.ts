import registryRaw from '../../../data/media/media-registry.json';
import { getGoldStandardExercises } from './content-bridge';
import { getProblems } from './problem-library';

export type MediaType = 'STATIC_TACTICAL_IMAGE' | 'TACTICAL_LOOP' | 'EXERCISE_ANIMATION' | 'COACH_EXPLAINER' | 'BEFORE_AFTER' | 'REAL_FIELD_EXAMPLE' | 'MATCH_TRANSFER_EXAMPLE';
export type MediaSubject = 'exercise' | 'problem';
export type MediaStatus = 'AVAILABLE' | 'SCRIPT_READY' | 'NOT_STARTED' | 'FIELD_INPUT_REQUIRED' | 'NOT_APPLICABLE';

export interface CoachExplainerScript {
  ce_vezi: string;
  de_ce_conteaza: string;
  ce_ii_spui_copilului: string;
  ce_urmaresti: string;
  greseala_frecventa_a_antrenorului: string;
  ce_faci_mai_departe: string;
}

export type MediaEntry = (typeof registryRaw.media)[number];

const media = registryRaw.media as MediaEntry[];

export function validateMediaRegistry(): true {
  const exerciseIds = new Set(getGoldStandardExercises().map(e => e.id));
  const problemIds = new Set(getProblems().map(p => p.problem_id));
  const seenIds = new Set<string>();
  for (const entry of media) {
    if (seenIds.has(entry.media_id)) throw new Error(`[FAIL_CLOSED] media_id duplicat: ${entry.media_id}`);
    seenIds.add(entry.media_id);
    if (entry.canonical_refs.length === 0) throw new Error(`[FAIL_CLOSED] ${entry.media_id}: fara canonical_refs`);
    for (const ref of entry.canonical_refs) {
      const resolved = entry.canonical_subject === 'exercise' ? exerciseIds.has(ref) : problemIds.has(ref);
      if (!resolved) throw new Error(`[FAIL_CLOSED] ${entry.media_id}: referinta canonica lipsa (${entry.canonical_subject} ${ref})`);
    }
    if (entry.media_type === 'TACTICAL_LOOP' || entry.media_type === 'EXERCISE_ANIMATION') {
      if (entry.status === 'AVAILABLE' && !entry.reduced_motion_fallback) {
        throw new Error(`[FAIL_CLOSED] ${entry.media_id}: media animata AVAILABLE fara reduced_motion_fallback`);
      }
    }
    if (entry.media_type === 'COACH_EXPLAINER' && entry.status === 'SCRIPT_READY' && !entry.script) {
      throw new Error(`[FAIL_CLOSED] ${entry.media_id}: COACH_EXPLAINER SCRIPT_READY fara script`);
    }
  }
  return true;
}

validateMediaRegistry();

export function getMediaRegistry(): MediaEntry[] { return media; }
export function getMediaForExercise(exerciseId: string): MediaEntry[] {
  return media.filter(m => m.canonical_subject === 'exercise' && m.canonical_refs.includes(exerciseId));
}
export function getMediaForProblem(problemId: string): MediaEntry[] {
  return media.filter(m => m.canonical_subject === 'problem' && m.canonical_refs.includes(problemId));
}
export function getCoachExplainer(problemId: string): MediaEntry | undefined {
  return getMediaForProblem(problemId).find(m => m.media_type === 'COACH_EXPLAINER');
}
