import {
  parseCanonicalId,
  parseEntitySlug,
  parseCategoryId,
  parseEvidenceClaimId,
  parseObservation,
  parsePossibleCause,
  type PrincipleEntity,
  type ExerciseEntity,
  type ProblemEntity,
  type CanonicalId,
  type EvidenceClaimId
} from '../types/content-model';

/**
 * JSON Boundary & Data Integrity Layer — ManualFC
 * Asigură parsarea și narrowing-ul fail-closed la citirea fișierelor JSON de către aplicația Astro.
 */

export function validateAndParsePrinciple(raw: any, sourceContext: string = "principles.json"): PrincipleEntity {
  if (!raw || typeof raw !== 'object') {
    throw new Error(`[FAIL_CLOSED] [${sourceContext}] Obiectul principiului este invalid.`);
  }

  const rawId = raw.id || (sourceContext.includes('principle-') ? 'principle.' + sourceContext.replace('principle-', '').replace('.json', '') : 'principle.unknown');
  const id = parseCanonicalId(rawId);
  if (!id.startsWith('principle.')) {
    throw new Error(`[FAIL_CLOSED] [${sourceContext}] [${rawId}] ID-ul trebuie să aibă prefixul "principle."`);
  }

  const rawSlug = raw.slug || (sourceContext.includes('principle-') ? sourceContext.replace('principle-', '').replace('.json', '') : 'variabilitatea-dezvoltarii-u11');
  const slug = parseEntitySlug(rawSlug);
  const category_id = parseCategoryId(raw.category_id || 'cat.copilul-10-11');
  
  const title = raw.title || raw.name;
  if (!title || typeof title !== 'string') {
    throw new Error(`[FAIL_CLOSED] [${sourceContext}] [${id}] Titlul lipsește.`);
  }

  const exercise_ids: CanonicalId[] = (raw.exercise_ids || []).map((exId: string) => {
    const parsed = parseCanonicalId(exId);
    if (!parsed.startsWith('exercise.')) {
      throw new Error(`[FAIL_CLOSED] [${sourceContext}] [${id}] Câmpul exercise_ids conține un ID ${parsed} care nu este de tip "exercise." (Actual: "${parsed}")`);
    }
    return parsed;
  });

  const rawClaims = raw.evidence_claim_ids || [];
  const evidence_claim_ids: EvidenceClaimId[] = rawClaims.map((clId: string) => parseEvidenceClaimId(clId));

  return {
    entity_class: 'PRIMARY_CONTENT_ENTITY',
    development_fixture: Boolean(raw.development_fixture),
    fixture_type: raw.fixture_type,
    id,
    slug,
    category_id,
    title,
    summary: raw.summary || raw.professional_definition || '',
    concept_text: raw.concept_text || raw.coach_meaning || '',
    why_it_matters: raw.why_it_matters || raw.why_this_message || '',
    child_wording: raw.child_wording || raw.child_message || '',
    coach_explanation: raw.coach_explanation || raw.coach_meaning || '',
    target_behavior: raw.target_behavior || raw.decision_children_must_learn || '',
    exercise_ids,
    evidence_claim_ids,
    tactical_visual_hooks: raw.tactical_visual_hooks
  };
}

export function validateAndParseExercise(raw: any, sourceContext: string = "exercises.json"): ExerciseEntity {
  if (!raw || typeof raw !== 'object') {
    throw new Error(`[FAIL_CLOSED] [${sourceContext}] Obiectul exercițiului este invalid.`);
  }

  const id = parseCanonicalId(raw.id);
  if (!id.startsWith('exercise.')) {
    throw new Error(`[FAIL_CLOSED] [${sourceContext}] [${raw.id}] ID-ul trebuie să aibă prefixul "exercise."`);
  }

  const slug = parseEntitySlug(raw.slug);
  const category_id = parseCategoryId(raw.category_id);

  if (!raw.title || typeof raw.title !== 'string') {
    throw new Error(`[FAIL_CLOSED] [${sourceContext}] [${id}] Titlul exercițiului lipsește.`);
  }

  const principle_ids: CanonicalId[] = (raw.principle_ids || []).map((pId: string) => {
    const parsed = parseCanonicalId(pId);
    if (!parsed.startsWith('principle.')) {
      throw new Error(`[FAIL_CLOSED] [${sourceContext}] [${id}] Câmpul principle_ids conține un ID ${parsed} care nu este de tip "principle." (Actual: "${parsed}")`);
    }
    return parsed;
  });

  return {
    entity_class: 'PRIMARY_CONTENT_ENTITY',
    development_fixture: Boolean(raw.development_fixture),
    fixture_type: raw.fixture_type,
    id,
    slug,
    category_id,
    title: raw.title,
    objective: raw.objective || '',
    players: raw.players || '',
    area: raw.area || '',
    duration: raw.duration || '',
    setup: raw.setup || '',
    rules: raw.rules || '',
    coach_cues: raw.coach_cues || '',
    child_cues: raw.child_cues || '',
    principle_ids,
    tactical_visual_hooks: raw.tactical_visual_hooks
  };
}

export function validateAndParseProblem(raw: any, sourceContext: string = "problems.json"): ProblemEntity {
  if (!raw || typeof raw !== 'object') {
    throw new Error(`[FAIL_CLOSED] [${sourceContext}] Obiectul problemei este invalid.`);
  }

  const id = parseCanonicalId(raw.id);
  if (!id.startsWith('problem.')) {
    throw new Error(`[FAIL_CLOSED] [${sourceContext}] [${raw.id}] ID-ul trebuie să aibă prefixul "problem."`);
  }

  const slug = parseEntitySlug(raw.slug);
  const category_id = parseCategoryId(raw.category_id);

  const observation = parseObservation(raw.observation);
  const possible_causes = (raw.possible_causes || []).map((c: string) => parsePossibleCause(c));

  if (!raw.intervention || typeof raw.intervention !== 'object') {
    throw new Error(`[FAIL_CLOSED] [${sourceContext}] [${id}] Câmpul "intervention" lipsește sau este invalid.`);
  }

  const exercise_ids: CanonicalId[] = (raw.intervention.exercise_ids || []).map((exId: string) => {
    const parsed = parseCanonicalId(exId);
    if (!parsed.startsWith('exercise.')) {
      throw new Error(`[FAIL_CLOSED] [${sourceContext}] [${id}] Câmpul intervention.exercise_ids conține un ID ${parsed} care nu este de tip "exercise." (Actual: "${parsed}")`);
    }
    return parsed;
  });

  const principle_ids: CanonicalId[] = (raw.principle_ids || []).map((pId: string) => {
    const parsed = parseCanonicalId(pId);
    if (!parsed.startsWith('principle.')) {
      throw new Error(`[FAIL_CLOSED] [${sourceContext}] [${id}] Câmpul principle_ids conține un ID ${parsed} care nu este de tip "principle." (Actual: "${parsed}")`);
    }
    return parsed;
  });

  const evidence_claim_ids: EvidenceClaimId[] = (raw.evidence_claim_ids || []).map((clId: string) => parseEvidenceClaimId(clId));

  return {
    entity_class: 'PRIMARY_CONTENT_ENTITY',
    development_fixture: Boolean(raw.development_fixture),
    fixture_type: raw.fixture_type,
    id,
    slug,
    category_id,
    title: raw.title || '',
    observation,
    possible_causes,
    intervention: {
      things_to_check: raw.intervention.things_to_check || '',
      what_to_say: raw.intervention.what_to_say || '',
      why_explanation: raw.intervention.why_explanation || '',
      exercise_ids,
      adaptation_note: raw.intervention.adaptation_note || '',
      verification_check: raw.intervention.verification_check || ''
    },
    principle_ids,
    evidence_claim_ids
  };
}
