import libraryRaw from '../../../data/problems/problem-library.json';
import { getAllPrinciples, getGoldStandardAssessment, getGoldStandardExercises, getGoldStandardSessions } from './content-bridge';

export type ProblemEvidenceState = 'VERIFIED_FACT'|'CONSENSUS'|'STUDY_RESULT'|'PRACTICE_HEURISTIC'|'HYPOTHESIS'|'NEEDS_RESEARCH'|'NEEDS_FIELD_VALIDATION';
export type CanonicalProblem = (typeof libraryRaw.problems)[number];

const problems = libraryRaw.problems as CanonicalProblem[];

export function getProblems(): CanonicalProblem[] { return problems; }
export function getProblem(slugOrId: string): CanonicalProblem {
  const problem = problems.find(item => item.slug === slugOrId || item.problem_id === slugOrId);
  if (!problem) throw new Error(`[FAIL_CLOSED] Problema canonică "${slugOrId}" nu există.`);
  return problem;
}

export function validateProblemGraph(): true {
  const principleIds = new Set<string>(getAllPrinciples().filter(item => !item.development_fixture).map(item => item.id));
  const exerciseIds = new Set(getGoldStandardExercises().map(item => item.id));
  const sessionIds = new Set(getGoldStandardSessions().map(item => item.id));
  const assessmentIds = new Set([getGoldStandardAssessment().id]);
  const ids = new Set<string>();
  const relationIds = new Set<string>();
  for (const problem of problems) {
    if (ids.has(problem.problem_id)) throw new Error(`[FAIL_CLOSED] Problem ID duplicat: ${problem.problem_id}`);
    ids.add(problem.problem_id);
    for (const id of [...problem.possible_explanations.map(x=>x.id), ...problem.quick_tests.map(x=>x.id), ...problem.child_cues.map(x=>x.id), ...problem.transfer_checks.map(x=>x.id)]) {
      if (relationIds.has(id)) throw new Error(`[FAIL_CLOSED] ID relație duplicat: ${id}`);
      relationIds.add(id);
    }
    for (const id of problem.related_principles) if (!principleIds.has(id)) throw new Error(`[FAIL_CLOSED] ${problem.problem_id}: principiu lipsă ${id}`);
    for (const id of problem.related_exercises) if (!exerciseIds.has(id)) throw new Error(`[FAIL_CLOSED] ${problem.problem_id}: exercițiu lipsă ${id}`);
    for (const id of problem.related_sessions) if (!sessionIds.has(id)) throw new Error(`[FAIL_CLOSED] ${problem.problem_id}: ședință lipsă ${id}`);
    for (const id of problem.assessment_links) if (!assessmentIds.has(id)) throw new Error(`[FAIL_CLOSED] ${problem.problem_id}: evaluare lipsă ${id}`);
    if (problem.media.some(item => item.status === 'AVAILABLE' && !problem.flagship)) throw new Error(`[FAIL_CLOSED] Media disponibilă declarată fără implementare flagship: ${problem.problem_id}`);
  }
  if (problems.length < 8 || problems.filter(p => p.flagship).length !== 3) throw new Error('[FAIL_CLOSED] Biblioteca Wave-3 trebuie să conțină minimum 8 probleme și exact 3 flagship.');
  return true;
}

validateProblemGraph();

export const problemFamilyLabels: Record<string,string> = {
  POSSESSION:'Posesie', TRANSITION_AFTER_LOSS:'După pierdere', TRANSITION_AFTER_WIN:'După recuperare',
  DEFENDING:'Apărare', PERCEPTION_DECISION:'Percepție și decizie', PEDAGOGICAL_BEHAVIOURAL:'Implicare și siguranță'
};
