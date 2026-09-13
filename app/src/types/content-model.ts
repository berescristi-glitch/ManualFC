/**
 * Content Model TypeScript API — ManualFC (TASK-0402)
 * Reprezentare complet tipizată a entităților de conținut, relațiilor și contractelor epistemice.
 * Autoritatea canonică rămâne validatorul Python (scripts/validate_content.py) și JSON Schemas.
 */

/* 1. Branded Types with Centralized Construction */

export type CanonicalId = string & { readonly __brand: unique symbol };
export type EntitySlug = string & { readonly __brand: unique symbol };
export type CategoryId = string & { readonly __brand: unique symbol };
export type EvidenceClaimId = string & { readonly __brand: unique symbol };
export type SourceId = string & { readonly __brand: unique symbol };

export function parseCanonicalId(id: string): CanonicalId {
  if (!id || typeof id !== 'string' || !/^[a-z0-9_]+\.[a-z0-9-]+$/.test(id)) {
    throw new Error(`[FAIL_CLOSED] ID canonic invalid: "${id}". Format așteptat: "type_prefix.slug" (ex: principle.scanning-before-receive)`);
  }
  return id as CanonicalId;
}

export function parseEntitySlug(slug: string): EntitySlug {
  if (!slug || typeof slug !== 'string' || !/^[a-z0-9]+(-[a-z0-9]+)*$/.test(slug)) {
    throw new Error(`[FAIL_CLOSED] Slug invalid: "${slug}". Must be lowercase ASCII kebab-case fără diacritice.`);
  }
  return slug as EntitySlug;
}

export function parseCategoryId(catId: string): CategoryId {
  if (!catId || typeof catId !== 'string' || !catId.startsWith('cat.')) {
    throw new Error(`[FAIL_CLOSED] ID categorie invalid: "${catId}". Format așteptat: "cat.name"`);
  }
  return catId as CategoryId;
}

export function parseEvidenceClaimId(claimId: string): EvidenceClaimId {
  if (!claimId || typeof claimId !== 'string' || !/^CLM-[A-Z0-9_-]+$/.test(claimId)) {
    throw new Error(`[FAIL_CLOSED] Evidence Claim ID invalid: "${claimId}". Format așteptat: "CLM-XXXX"`);
  }
  return claimId as EvidenceClaimId;
}

export function parseSourceId(sourceId: string): SourceId {
  if (!sourceId || typeof sourceId !== 'string' || !/^SRC-[A-Z0-9_-]+$/.test(sourceId)) {
    throw new Error(`[FAIL_CLOSED] Source ID invalid: "${sourceId}". Format așteptat: "SRC-XXXX"`);
  }
  return sourceId as SourceId;
}

/* 2. Entity Classes & Epistemic Mapping */

export type EntityClass =
  | 'PRIMARY_CONTENT_ENTITY'
  | 'SUPPORTING_ENTITY'
  | 'RESEARCH_ENTITY'
  | 'VISUAL_ENTITY'
  | 'SYSTEM_ENTITY';

export type EpistemicLevel = 'HIGH' | 'MODERATE' | 'LOW' | 'PRACTICE_ONLY' | 'UNRESOLVED';

export interface EpistemicDisplayInfo {
  level: EpistemicLevel;
  label_ro: string;
  badge_color: string;
  accessible_symbol: string;
}

export const EPISTEMIC_MAP: Record<EpistemicLevel, EpistemicDisplayInfo> = {
  HIGH: { level: 'HIGH', label_ro: "Evidență Puternică", badge_color: "#166534", accessible_symbol: "[EVIDENȚĂ RĂSPÂNDITĂ]" },
  MODERATE: { level: 'MODERATE', label_ro: "Evidență Moderată", badge_color: "#075985", accessible_symbol: "[STUDIU EXPERIMENTAL]" },
  LOW: { level: 'LOW', label_ro: "Evidență Limitată", badge_color: "#854D0E", accessible_symbol: "[DATE RESTRÂNSE]" },
  PRACTICE_ONLY: { level: 'PRACTICE_ONLY', label_ro: "Practică de Academie", badge_color: "#6B21A8", accessible_symbol: "[CONSENS EXPERȚI]" },
  UNRESOLVED: { level: 'UNRESOLVED', label_ro: "Neconfirmat", badge_color: "#991B1B", accessible_symbol: "[ÎN VERIFICARE]" }
};

/* 3. Type-Aware Visual References */

export type VisualAssetKind = 'diagram' | 'animation' | 'video_export' | 'print_fallback';

export interface TacticalVisualRef {
  kind: VisualAssetKind;
  asset_id: string;
}

export interface TacticalVisualHooks {
  diagram_ref?: string | null;
  animation_ref?: string | null;
  video_export_ref?: string | null;
  print_fallback_ref?: string | null;
}

/* 4. Problem Model — Discriminated Semantics */

export type ObservationText = string & { readonly __brand: unique symbol };
export type PossibleCauseText = string & { readonly __brand: unique symbol };

export function parseObservation(text: string): ObservationText {
  if (!text || typeof text !== 'string' || text.trim().length === 0) {
    throw new Error("[FAIL_CLOSED] Semantica OBSERVATION invalidă: trebuie să descrie ce observă antrenorul pe teren.");
  }
  return text as ObservationText;
}

export function parsePossibleCause(text: string): PossibleCauseText {
  if (!text || typeof text !== 'string' || text.trim().length === 0) {
    throw new Error("[FAIL_CLOSED] Semantica POSSIBLE_CAUSE invalidă: trebuie să fie o ipoteză metodologică.");
  }
  return text as PossibleCauseText;
}

export interface ProblemInterventionModel {
  things_to_check: string;
  what_to_say: string;
  why_explanation: string;
  exercise_ids: CanonicalId[];
  adaptation_note: string;
  verification_check: string;
}

export interface ProblemEntity {
  entity_class: 'PRIMARY_CONTENT_ENTITY';
  development_fixture?: boolean;
  fixture_type?: string;
  id: CanonicalId;
  slug: EntitySlug;
  category_id: CategoryId;
  title: string;
  observation: ObservationText;
  possible_causes: PossibleCauseText[];
  intervention: ProblemInterventionModel;
  principle_ids: CanonicalId[];
  evidence_claim_ids: EvidenceClaimId[];
}

/* 5. Primary Entities */

export interface PrincipleEntity {
  entity_class: 'PRIMARY_CONTENT_ENTITY';
  development_fixture?: boolean;
  fixture_type?: string;
  id: CanonicalId;
  slug: EntitySlug;
  category_id: CategoryId;
  title: string;
  summary: string;
  concept_text: string;
  why_it_matters: string;
  child_wording: string;
  coach_explanation: string;
  target_behavior: string;
  exercise_ids: CanonicalId[];
  evidence_claim_ids: EvidenceClaimId[];
  tactical_visual_hooks?: TacticalVisualHooks;
}

export interface ExerciseEntity {
  entity_class: 'PRIMARY_CONTENT_ENTITY';
  development_fixture?: boolean;
  fixture_type?: string;
  id: CanonicalId;
  slug: EntitySlug;
  category_id: CategoryId;
  title: string;
  objective: string;
  players: string;
  area: string;
  duration: string;
  setup: string;
  rules: string;
  coach_cues: string;
  child_cues: string;
  principle_ids: CanonicalId[];
  tactical_visual_hooks?: TacticalVisualHooks;
}

export interface SessionEntity {
  entity_class: 'PRIMARY_CONTENT_ENTITY';
  development_fixture?: boolean;
  fixture_type?: string;
  id: CanonicalId;
  slug: EntitySlug;
  category_id: CategoryId;
  title: string;
  objectives: string[];
  duration_minutes: number;
  exercise_ids: CanonicalId[];
}

/* 6. Content Bridge Resolution Types */

export interface ResolvedPrinciple {
  principle: PrincipleEntity;
  exercises: ExerciseEntity[];
}

export interface ResolvedExercise {
  exercise: ExerciseEntity;
  principles: PrincipleEntity[];
}

export interface ResolvedProblem {
  problem: ProblemEntity;
  exercises: ExerciseEntity[];
  principles: PrincipleEntity[];
}
