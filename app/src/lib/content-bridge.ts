import type { ProjectConfig } from '../types';
import {
  parseCanonicalId,
  parseEntitySlug,
  parseCategoryId,
  type PrincipleEntity,
  type ExerciseEntity,
  type ProblemEntity,
  type ResolvedPrinciple,
  type ResolvedExercise,
  type ResolvedProblem,
  type EntitySlug,
  type CategoryId
} from '../types/content-model';
import {
  validateAndParsePrinciple,
  validateAndParseExercise,
  validateAndParseProblem
} from './json-boundary';

import registryData from '../../../data/taxonomy/registry.json';
import principlesFixtureRaw from '../../../data/fixtures/principles.json';
import exercisesFixtureRaw from '../../../data/fixtures/exercises.json';
import problemsFixtureRaw from '../../../data/fixtures/problems.json';
import principleVariabilitateRaw from '../../../data/principles/principle-variabilitatea-dezvoltarii-u11.json';
import principleAdaptareRaw from '../../../data/principles/principle-adaptarea-sarcinii-u11.json';
import principleEroareRaw from '../../../data/principles/principle-eroarea-ca-informatie.json';
import principleMesajRaw from '../../../data/principles/principle-mesaj-pedagogic-observabil.json';
import principleTransferRaw from '../../../data/principles/principle-transfer-autonom-cooperare.json';
import principleJoculCaSistemRaw from '../../../data/principles/principle-jocul-ca-sistem-de-probleme.json';
import principleSpatiuUnghiuriRaw from '../../../data/principles/principle-spatiu-si-unghiuri.json';
import principleProgresieSprijinRaw from '../../../data/principles/principle-progresie-si-sprijin.json';
import principleProtejareaCentruluiRaw from '../../../data/principles/principle-protejarea-centrului.json';
import principlePresiuneAcoperireRaw from '../../../data/principles/principle-presiune-si-acoperire.json';
import principleTranzitiaPierdereRaw from '../../../data/principles/principle-tranzitia-la-pierderea-mingii.json';
import principleTranzitiaCastigareRaw from '../../../data/principles/principle-tranzitia-la-castigarea-mingii.json';
import principleSuperioritateNumericaRaw from '../../../data/principles/principle-superioritate-egalitate-inferioritate-numerica.json';
import principleLimbajScurtRaw from '../../../data/principles/principle-limbaj-scurt-si-relevanta.json';
import principleIntrebariIntelegereRaw from '../../../data/principles/principle-intrebari-si-verificarea-intelegerii.json';
import principleGresealaSigurantaRaw from '../../../data/principles/principle-greseala-ca-informatie-si-siguranta.json';
import principleDisciplinaFaraUmilireRaw from '../../../data/principles/principle-disciplina-fara-umilire.json';
import principleTacetFaraJoystickRaw from '../../../data/principles/principle-tacet-si-observa-fara-joystick.json';
import principleConversatiiEchitateRaw from '../../../data/principles/principle-conversatii-individuale-si-echitate.json';
import principleProiectareaSituatiilorRaw from '../../../data/principles/principle-proiectarea-situatiilor-reprezentative.json';
import principleManipulareaDozareaRaw from '../../../data/principles/principle-manipularea-si-dozarea-constrangerilor.json';
import principleProgresieRegresieRaw from '../../../data/principles/principle-progresie-si-regresie-cu-conservarea-intentiei.json';
import principleFocalizareaObservatieiRaw from '../../../data/principles/principle-focalizarea-observatiei-si-criterii-de-interventie.json';
import principleMaximizareaTimpuluiActivRaw from '../../../data/principles/principle-maximizarea-timpului-activ-si-organizarea-sigura.json';
import principleReflectiaGhidataRaw from '../../../data/principles/principle-reflectia-ghidata-si-transferul-in-joc.json';
import claimsRegistryRaw from '../../../research/claims.json';
import citationsRegistryRaw from '../../../research/citations.json';
import sourcesRegistryRaw from '../../../research/sources.json';

import gsExercise1Raw from '../../../data/exercises/exercise-recunoasterea-umbrei-defensive.json';
import gsExercise2Raw from '../../../data/exercises/exercise-creeaza-optiunea-sub-presiune.json';
import gsExercise3Raw from '../../../data/exercises/exercise-primeste-gata-sa-continui.json';
import gsExercise4Raw from '../../../data/exercises/exercise-sprijin-cu-doi-coechipieri.json';
import gsExercise5Raw from '../../../data/exercises/exercise-transferul-in-joc-mic.json';
import gsSession1Raw from '../../../data/sessions/session-introducere.json';
import gsSession2Raw from '../../../data/sessions/session-coordonare-si-transfer.json';
import gsAssessmentRaw from '../../../data/assessments/assessment-sprijin-si-unghi-de-pasa.json';

/**
 * Content Bridge 2.0 — Puntea de citire fail-closed complet tipizată pentru datele canonice ale proiectului.
 * Autoritatea de validare canonică rămâne validatorul Python (scripts/validate_content.py).
 */

export interface TaxonomyCategory {
  id: CategoryId;
  label_ro: string;
  slug: EntitySlug;
  order: number;
  route_base: string;
}

export type EvidenceLevel = 'HIGH' | 'MODERATE' | 'LOW' | 'PRACTICE_ONLY' | 'UNRESOLVED';
export type U11Applicability = 'DIRECT' | 'PARTIAL' | 'INDIRECT';

export interface ResolvedEvidenceSource {
  source_id: string;
  title: string;
  authors: string[];
  year: number | null;
  doi: string | null;
  url: string | null;
  citation_id: string;
  locator: string;
  support_type: string;
}

export interface ResolvedEvidenceClaim {
  claim_id: string;
  statement: string;
  epistemic_level: EvidenceLevel;
  u11_applicability: U11Applicability;
  practical_implication: string;
  limitations: string[];
  sources: ResolvedEvidenceSource[];
}

export function getProjectConfig(): ProjectConfig {
  return {
    project_id: "manual-u11",
    product_kind: "platformă web pedagogică profesională",
    primary_delivery: "static_web",
    pedagogical_first: true,
    language: "ro",
    age_category: {
      label: "10–11 ani, grupele 2015 și 2016 tratate împreună",
      birth_years: [2015, 2016],
      single_curriculum: true,
      individual_adaptation_dimensions: [
        "experiență",
        "dezvoltare tehnică",
        "înțelegerii jocului",
        "maturizare fizică",
        "încredere",
        "nevoi cognitive, emoționale și sociale",
        "ritm de învățare"
      ]
    }
  };
}

export function getPrimaryNavigation() {
  // NOTE (product-implementation-parity repair): previously pointed at dev-fixture
  // routes (/principii/orientare-corporala-scanare, /probleme/lipsa-unghi-de-pasa,
  // /exercitii/2v1-unghi-de-suport) instead of any real canonical content. Now
  // points at real production surfaces: the principle index, the one real Quick
  // Mode instance (Gold Standard), and Gold Standard Deep Mode.
  return [
    { label: "Acasă", href: "/" },
    { label: "Începe aici", href: "/incepe-aici" },
    { label: "Volume", href: "/volum" },
    { label: "Principii", href: "/principii" },
    { label: "Rezolvă pe teren", href: "/rezolva-pe-teren" },
    { label: "Caută", href: "/cauta" },
    { label: "Gold Standard", href: "/gold-standard" }
  ];
}

/* Taxonomy Registry */

export function getTaxonomyRegistry() {
  return registryData;
}

export function getTaxonomyCategories(): TaxonomyCategory[] {
  return registryData.categories.map(c => ({
    id: parseCategoryId(c.id),
    label_ro: c.label_ro,
    slug: parseEntitySlug(c.slug),
    order: c.order,
    route_base: c.route_base
  }));
}

export function getCategoryById(id: string): TaxonomyCategory | undefined {
  const parsed = parseCategoryId(id);
  return getTaxonomyCategories().find(c => c.id === parsed);
}

export function getCategoryBySlug(slug: string): TaxonomyCategory | undefined {
  const parsed = parseEntitySlug(slug);
  return getTaxonomyCategories().find(c => c.slug === parsed);
}

/* Entity Parsers & Loaders */

let cachedPrinciples: PrincipleEntity[] | null = null;
let cachedExercises: ExerciseEntity[] | null = null;
let cachedProblems: ProblemEntity[] | null = null;

export function getAllPrinciples(): PrincipleEntity[] {
  if (!cachedPrinciples) {
    const fixtures = principlesFixtureRaw.map(raw => validateAndParsePrinciple(raw, "principles.json"));
    const canonical1 = validateAndParsePrinciple(principleVariabilitateRaw, "principle-variabilitatea-dezvoltarii-u11.json");
    const canonical2 = validateAndParsePrinciple(principleAdaptareRaw, "principle-adaptarea-sarcinii-u11.json");
    const canonical3 = validateAndParsePrinciple(principleEroareRaw, "principle-eroarea-ca-informatie.json");
    const canonical4 = validateAndParsePrinciple(principleMesajRaw, "principle-mesaj-pedagogic-observabil.json");
    const canonical5 = validateAndParsePrinciple(principleTransferRaw, "principle-transfer-autonom-cooperare.json");
    const canonical6 = validateAndParsePrinciple(principleJoculCaSistemRaw, "principle-jocul-ca-sistem-de-probleme.json");
    const canonical7 = validateAndParsePrinciple(principleSpatiuUnghiuriRaw, "principle-spatiu-si-unghiuri.json");
    const canonical8 = validateAndParsePrinciple(principleProgresieSprijinRaw, "principle-progresie-si-sprijin.json");
    const canonical9 = validateAndParsePrinciple(principleProtejareaCentruluiRaw, "principle-protejarea-centrului.json");
    const canonical10 = validateAndParsePrinciple(principlePresiuneAcoperireRaw, "principle-presiune-si-acoperire.json");
    const canonical11 = validateAndParsePrinciple(principleTranzitiaPierdereRaw, "principle-tranzitia-la-pierderea-mingii.json");
    const canonical12 = validateAndParsePrinciple(principleTranzitiaCastigareRaw, "principle-tranzitia-la-castigarea-mingii.json");
    const canonical13 = validateAndParsePrinciple(principleSuperioritateNumericaRaw, "principle-superioritate-egalitate-inferioritate-numerica.json");
    const canonical14 = validateAndParsePrinciple(principleLimbajScurtRaw, "principle-limbaj-scurt-si-relevanta.json");
    const canonical15 = validateAndParsePrinciple(principleIntrebariIntelegereRaw, "principle-intrebari-si-verificarea-intelegerii.json");
    const canonical16 = validateAndParsePrinciple(principleGresealaSigurantaRaw, "principle-greseala-ca-informatie-si-siguranta.json");
    const canonical17 = validateAndParsePrinciple(principleDisciplinaFaraUmilireRaw, "principle-disciplina-fara-umilire.json");
    const canonical18 = validateAndParsePrinciple(principleTacetFaraJoystickRaw, "principle-tacet-si-observa-fara-joystick.json");
    const canonical19 = validateAndParsePrinciple(principleConversatiiEchitateRaw, "principle-conversatii-individuale-si-echitate.json");
    const canonical20 = validateAndParsePrinciple(principleProiectareaSituatiilorRaw, "principle-proiectarea-situatiilor-reprezentative.json");
    const canonical21 = validateAndParsePrinciple(principleManipulareaDozareaRaw, "principle-manipularea-si-dozarea-constrangerilor.json");
    const canonical22 = validateAndParsePrinciple(principleProgresieRegresieRaw, "principle-progresie-si-regresie-cu-conservarea-intentiei.json");
    const canonical23 = validateAndParsePrinciple(principleFocalizareaObservatieiRaw, "principle-focalizarea-observatiei-si-criterii-de-interventie.json");
    const canonical24 = validateAndParsePrinciple(principleMaximizareaTimpuluiActivRaw, "principle-maximizarea-timpului-activ-si-organizarea-sigura.json");
    const canonical25 = validateAndParsePrinciple(principleReflectiaGhidataRaw, "principle-reflectia-ghidata-si-transferul-in-joc.json");
    cachedPrinciples = [
      ...fixtures,
      canonical1, canonical2, canonical3, canonical4, canonical5,
      canonical6, canonical7, canonical8, canonical9, canonical10, canonical11, canonical12, canonical13,
      canonical14, canonical15, canonical16, canonical17, canonical18, canonical19,
      canonical20, canonical21, canonical22, canonical23, canonical24, canonical25
    ];
  }
  return cachedPrinciples;
}

export function getAllExercises(): ExerciseEntity[] {
  if (!cachedExercises) {
    cachedExercises = exercisesFixtureRaw.map(raw => validateAndParseExercise(raw, "exercises.json"));
  }
  return cachedExercises;
}

export function getAllProblems(): ProblemEntity[] {
  if (!cachedProblems) {
    cachedProblems = problemsFixtureRaw.map(raw => validateAndParseProblem(raw, "problems.json"));
  }
  return cachedProblems;
}

/* Fixture Separation */

export function getDevelopmentFixtures<T extends { development_fixture?: boolean }>(entities: T[]): T[] {
  return entities.filter(e => e.development_fixture === true);
}

export function getCanonicalProductionContent<T extends { development_fixture?: boolean }>(entities: T[]): T[] {
  return entities.filter(e => !e.development_fixture);
}

export function resolveEvidenceClaims(entity: { evidence_claim_ids: readonly string[] }): ResolvedEvidenceClaim[] {
  return entity.evidence_claim_ids.map(claimId => {
    const claim = claimsRegistryRaw.claims.find(item => item.claim_id === claimId);
    if (!claim) {
      throw new Error(`[FAIL_CLOSED] Claim-ul "${claimId}" lipsește din registrul canonic.`);
    }

    const epistemicLevel = claim.epistemic_level as EvidenceLevel | undefined;
    const applicability = claim.u11_applicability as U11Applicability | undefined;
    if (!epistemicLevel || !applicability || !claim.practical_implication) {
      throw new Error(`[FAIL_CLOSED] Claim-ul "${claimId}" nu are metadata epistemică completă.`);
    }

    const citations = citationsRegistryRaw.citations.filter(item => item.claim_id === claimId);
    if (citations.length === 0) {
      throw new Error(`[FAIL_CLOSED] Claim-ul "${claimId}" nu are nicio citare canonică.`);
    }

    const sources = citations.map(citation => {
      const source = sourcesRegistryRaw.sources.find(item => item.source_id === citation.source_id);
      if (!source) {
        throw new Error(`[FAIL_CLOSED] Citarea "${citation.citation_id}" indică sursa lipsă "${citation.source_id}".`);
      }
      return {
        source_id: source.source_id,
        title: source.title,
        authors: source.authors,
        year: source.year,
        doi: source.doi,
        url: source.url,
        citation_id: citation.citation_id,
        locator: citation.locator.value,
        support_type: citation.support_type
      };
    });

    return {
      claim_id: claim.claim_id,
      statement: claim.statement,
      epistemic_level: epistemicLevel,
      u11_applicability: applicability,
      practical_implication: claim.practical_implication,
      limitations: claim.limitations,
      sources
    };
  });
}

/* Typed Lookups */

export function lookupByCanonicalId(id: string): PrincipleEntity | ExerciseEntity | ProblemEntity | undefined {
  const parsed = parseCanonicalId(id);
  if (parsed.startsWith('principle.')) return getAllPrinciples().find(p => p.id === parsed);
  if (parsed.startsWith('exercise.')) return getAllExercises().find(e => e.id === parsed);
  if (parsed.startsWith('problem.')) return getAllProblems().find(pr => pr.id === parsed);
  return undefined;
}

export function lookupBySlug(slug: string): PrincipleEntity | ExerciseEntity | ProblemEntity | undefined {
  const parsed = parseEntitySlug(slug);
  const p = getAllPrinciples().find(x => x.slug === parsed);
  if (p) return p;
  const e = getAllExercises().find(x => x.slug === parsed);
  if (e) return e;
  const pr = getAllProblems().find(x => x.slug === parsed);
  if (pr) return pr;
  return undefined;
}

/* Relation Resolvers with Target Type Checking & Fail-Closed Errors */

export function getResolvedPrinciple(idOrSlug: string): ResolvedPrinciple {
  const p = getAllPrinciples().find(x => x.id === idOrSlug || x.slug === idOrSlug);
  if (!p) {
    throw new Error(`[FAIL_CLOSED] Principiul "${idOrSlug}" nu a fost găsit în registrul de conținut.`);
  }

  const exercises = p.exercise_ids.map(exId => {
    const target = lookupByCanonicalId(exId);
    if (!target) {
      throw new Error(`[FAIL_CLOSED] [Source: ${p.id}] [Field: exercise_ids] Referința lipsă "${exId}". Expected entity type: "ExerciseEntity".`);
    }
    if (!exId.startsWith('exercise.')) {
      throw new Error(`[FAIL_CLOSED] [Source: ${p.id}] [Field: exercise_ids] Referința "${exId}" indică un tip de entitate incompatibil. Expected entity type: "ExerciseEntity", Actual: "${target.id.split('.')[0]}".`);
    }
    return target as ExerciseEntity;
  });

  return { principle: p, exercises };
}

export function getResolvedExercise(idOrSlug: string): ResolvedExercise {
  const ex = getAllExercises().find(x => x.id === idOrSlug || x.slug === idOrSlug);
  if (!ex) {
    throw new Error(`[FAIL_CLOSED] Exercițiul "${idOrSlug}" nu a fost găsit în registrul de conținut.`);
  }

  const principles = ex.principle_ids.map(pId => {
    const target = lookupByCanonicalId(pId);
    if (!target) {
      throw new Error(`[FAIL_CLOSED] [Source: ${ex.id}] [Field: principle_ids] Referința lipsă "${pId}". Expected entity type: "PrincipleEntity".`);
    }
    if (!pId.startsWith('principle.')) {
      throw new Error(`[FAIL_CLOSED] [Source: ${ex.id}] [Field: principle_ids] Referința "${pId}" indică un tip de entitate incompatibil. Expected entity type: "PrincipleEntity", Actual: "${target.id.split('.')[0]}".`);
    }
    return target as PrincipleEntity;
  });

  return { exercise: ex, principles };
}

export function getResolvedProblem(idOrSlug: string): ResolvedProblem {
  const pr = getAllProblems().find(x => x.id === idOrSlug || x.slug === idOrSlug);
  if (!pr) {
    throw new Error(`[FAIL_CLOSED] Problema "${idOrSlug}" nu a fost găsită în registrul de conținut.`);
  }

  const exercises = pr.intervention.exercise_ids.map(exId => {
    const target = lookupByCanonicalId(exId);
    if (!target) {
      throw new Error(`[FAIL_CLOSED] [Source: ${pr.id}] [Field: intervention.exercise_ids] Referința lipsă "${exId}". Expected entity type: "ExerciseEntity".`);
    }
    if (!exId.startsWith('exercise.')) {
      throw new Error(`[FAIL_CLOSED] [Source: ${pr.id}] [Field: intervention.exercise_ids] Referința "${exId}" indică un tip de entitate incompatibil. Expected entity type: "ExerciseEntity", Actual: "${target.id.split('.')[0]}".`);
    }
    return target as ExerciseEntity;
  });

  const principles = pr.principle_ids.map(pId => {
    const target = lookupByCanonicalId(pId);
    if (!target) {
      throw new Error(`[FAIL_CLOSED] [Source: ${pr.id}] [Field: principle_ids] Referința lipsă "${pId}". Expected entity type: "PrincipleEntity".`);
    }
    if (!pId.startsWith('principle.')) {
      throw new Error(`[FAIL_CLOSED] [Source: ${pr.id}] [Field: principle_ids] Referința "${pId}" indică un tip de entitate incompatibil. Expected entity type: "PrincipleEntity", Actual: "${target.id.split('.')[0]}".`);
    }
    return target as PrincipleEntity;
  });

  return { problem: pr, exercises, principles };
}

export function validateNoDuplicateIds(): void {
  const allIds = [
    ...getAllPrinciples().map(p => p.id),
    ...getAllExercises().map(e => e.id),
    ...getAllProblems().map(pr => pr.id)
  ];
  const set = new Set(allIds);
  if (set.size !== allIds.length) {
    throw new Error("[FAIL_CLOSED] Au fost detectate ID-uri canonice duplicate în registrul de conținut!");
  }
}

/**
 * Gold Standard Bridge — Sprijinul și unghiul de pasă (TASK-2208).
 *
 * `data/exercises/*.json`, `data/sessions/*.json` și `data/assessments/*.json` folosesc
 * schemele bogate de producție (`schemas/exercise.schema.json`, `session.schema.json`,
 * `assessment.schema.json`), validate canonic de `scripts/validate_content.py` — un format
 * complet diferit de fixture-ul îngust `ExerciseEntity`/`validateAndParseExercise` de mai sus
 * (construit pentru un singur exercițiu de test, TASK-0402). Nu forțăm conținutul Gold
 * Standard prin acel adaptor îngust — l-am fi trunchiat ireversibil. În schimb, adăugăm
 * tipuri și loadere dedicate, aditive, fără să atingem loaderele de principii/exerciții/
 * probleme existente.
 */

export interface GoldStandardRationales {
  tactical: string; perceptual: string; decisional: string; cognitive: string;
  psychological: string; technical: string; social: string;
}

export interface GoldStandardCommonError { observation: string; possible_causes: string[]; }
export interface GoldStandardPhraseToAvoid { phrase: string; reason: string; }
export interface GoldStandardEquipmentItem { item: string; quantity: number; quantity_max?: number; }
export interface GoldStandardCoachCommonError { observation: string; why_it_happens: string; }
export interface GoldStandardV2Marker { status: 'V1' | 'V2'; version: string; }

export interface GoldStandardExercise {
  id: string;
  title: string;
  level: string;
  theme: string;
  game_moment: string;
  primary_objective: string;
  observable_behaviours: string[];
  players: Record<string, unknown>;
  numerical_relation: string;
  equipment: string[];
  equipment_items: GoldStandardEquipmentItem[];
  field: { length_m: number; width_m: number; safety_margin_m: number };
  duration: Record<string, unknown>;
  rules: { rule: string; why: string }[];
  step_by_step: string[];
  rotation: string;
  transition: string;
  child_message: string;
  why_this_message: string;
  problem_being_solved: string;
  information_children_must_notice: string[];
  decision_children_must_learn: string;
  rationales: GoldStandardRationales;
  age_appropriateness: string;
  possible_misinterpretations: string[];
  task_risks: string[];
  phrases_to_avoid: GoldStandardPhraseToAvoid[];
  understanding_check: string[];
  response_if_not_understood: string[];
  dimension_rationale: string;
  too_small_signs: string[];
  too_large_signs: string[];
  regression: string[];
  progression: string[];
  coach_questions: { question: string; when: string }[];
  coach_feedback: { type: string; cue: string }[];
  common_errors: GoldStandardCommonError[];
  success_criteria: string[];
  match_transfer: string;
  visual_assets: { static_svg: string; animation_or_storyboard: string; pdf_frames: string };
  sources: string[];
  gold_standard_v2?: GoldStandardV2Marker;
  pedagogical_principle_ids?: string[];
  pedagog_competency_ids?: string[];
  coach_competency_ids?: string[];
  related_pedagog_lesson_ids?: string[];
  related_coach_lesson_ids?: string[];
  child_action?: string;
  coach_focus?: string;
  do_not_assume?: string[];
  when_to_intervene?: string[];
  when_not_to_intervene?: string[];
  coach_common_errors?: GoldStandardCoachCommonError[];
  coach_reflection?: string[];
  evidence_boundary?: string;
  group_configuration_note?: string;
  assessment_ref?: string;
}

export interface GoldStandardSessionSegment {
  start_min: number; end_min: number; title: string; exercise_ids: string[];
  coach_message: string; why_now: string; methodological_rationale: string;
  observation_focus: string[]; intervention_criteria: string[]; transition_logistics: string;
  non_intervention_criteria?: string[]; coach_focus?: string; verification_method?: string;
}

export interface GoldStandardOperationalContingency { scenario: string; guidance: string; }
export interface GoldStandardDurationVariantSegment { segment_index: number; start_min: number; end_min: number; reduction_note: string; }
export interface GoldStandardDurationVariant60Min { total_minutes: 60; policy_note: string; segments: GoldStandardDurationVariantSegment[]; }

export interface GoldStandardSession {
  id: string;
  title: string;
  duration_min: number;
  primary_objective: string;
  observable_behaviours: string[];
  players_range: Record<string, unknown>;
  operational_contingencies: GoldStandardOperationalContingency[];
  duration_variant_60min: GoldStandardDurationVariant60Min;
  equipment: string[];
  surface_plan: Record<string, unknown>;
  segments: GoldStandardSessionSegment[];
  message_foundations: Record<string, unknown>[];
  session_rationale: string;
  match_theme: string;
  reflection: string[];
  sources: string[];
  gold_standard_v2?: GoldStandardV2Marker;
  child_objectives?: string[];
  coach_objectives?: { objective: string; coach_competency_id: string }[];
  reflection_v2?: { child_game_dimension: string[]; coach_dimension: string[] };
}

export interface GoldStandardAssessmentCriterion { id: string; observable_behaviour: string; levels: string[]; }
export interface GoldStandardAssessment { id: string; title: string; principle_ids: string[]; criteria: GoldStandardAssessmentCriterion[]; }

function requireField<T>(value: T | undefined | null, entityId: string, field: string): T {
  if (value === undefined || value === null) {
    throw new Error(`[FAIL_CLOSED] [Gold Standard] [${entityId}] Câmpul "${field}" lipsește.`);
  }
  return value;
}

function parseGoldStandardExercise(raw: any, sourceContext: string): GoldStandardExercise {
  const id = requireField(raw?.id, sourceContext, 'id');
  requireField(raw?.title, id, 'title');
  requireField(raw?.rationales, id, 'rationales');
  for (const dim of ['tactical', 'perceptual', 'decisional', 'cognitive', 'psychological', 'technical', 'social']) {
    requireField(raw.rationales[dim], id, `rationales.${dim}`);
  }
  requireField(raw?.dimension_rationale, id, 'dimension_rationale');
  requireField(raw?.visual_assets, id, 'visual_assets');
  const equipmentItems = requireField(raw?.equipment_items, id, 'equipment_items');
  if (!Array.isArray(equipmentItems) || equipmentItems.length === 0) {
    throw new Error(`[FAIL_CLOSED] [Gold Standard] [${id}] "equipment_items" nu poate fi gol.`);
  }
  return raw as GoldStandardExercise;
}

function parseGoldStandardSession(raw: any, sourceContext: string): GoldStandardSession {
  const id = requireField(raw?.id, sourceContext, 'id');
  requireField(raw?.title, id, 'title');
  const segments = requireField(raw?.segments, id, 'segments');
  if (!Array.isArray(segments) || segments.length < 3) {
    throw new Error(`[FAIL_CLOSED] [Gold Standard] [${id}] "segments" trebuie să aibă minimum 3 elemente.`);
  }
  const contingencies = requireField(raw?.operational_contingencies, id, 'operational_contingencies');
  if (!Array.isArray(contingencies) || contingencies.length === 0) {
    throw new Error(`[FAIL_CLOSED] [Gold Standard] [${id}] "operational_contingencies" nu poate fi gol.`);
  }
  const variant60 = requireField(raw?.duration_variant_60min, id, 'duration_variant_60min');
  const variant60Segments = requireField(variant60?.segments, id, 'duration_variant_60min.segments');
  if (!Array.isArray(variant60Segments) || variant60Segments.length !== segments.length) {
    throw new Error(`[FAIL_CLOSED] [Gold Standard] [${id}] "duration_variant_60min.segments" trebuie să acopere fiecare segment din "segments" (${segments.length}).`);
  }
  return raw as GoldStandardSession;
}

function parseGoldStandardAssessment(raw: any, sourceContext: string): GoldStandardAssessment {
  const id = requireField(raw?.id, sourceContext, 'id');
  const criteria = requireField(raw?.criteria, id, 'criteria');
  if (!Array.isArray(criteria) || criteria.length === 0) {
    throw new Error(`[FAIL_CLOSED] [Gold Standard] [${id}] "criteria" nu poate fi gol.`);
  }
  return raw as GoldStandardAssessment;
}

let cachedGoldStandardExercises: GoldStandardExercise[] | null = null;
let cachedGoldStandardSessions: GoldStandardSession[] | null = null;
let cachedGoldStandardAssessment: GoldStandardAssessment | null = null;

export function getGoldStandardExercises(): GoldStandardExercise[] {
  if (!cachedGoldStandardExercises) {
    cachedGoldStandardExercises = [
      parseGoldStandardExercise(gsExercise1Raw, 'exercise-recunoasterea-umbrei-defensive.json'),
      parseGoldStandardExercise(gsExercise2Raw, 'exercise-creeaza-optiunea-sub-presiune.json'),
      parseGoldStandardExercise(gsExercise3Raw, 'exercise-primeste-gata-sa-continui.json'),
      parseGoldStandardExercise(gsExercise4Raw, 'exercise-sprijin-cu-doi-coechipieri.json'),
      parseGoldStandardExercise(gsExercise5Raw, 'exercise-transferul-in-joc-mic.json'),
    ];
  }
  return cachedGoldStandardExercises;
}

export function getGoldStandardExercise(id: string): GoldStandardExercise {
  const ex = getGoldStandardExercises().find(e => e.id === id);
  if (!ex) {
    throw new Error(`[FAIL_CLOSED] [Gold Standard] Exercițiul "${id}" nu a fost găsit.`);
  }
  return ex;
}

export function getGoldStandardSessions(): GoldStandardSession[] {
  if (!cachedGoldStandardSessions) {
    cachedGoldStandardSessions = [
      parseGoldStandardSession(gsSession1Raw, 'session-introducere.json'),
      parseGoldStandardSession(gsSession2Raw, 'session-coordonare-si-transfer.json'),
    ];
  }
  return cachedGoldStandardSessions;
}

export function getGoldStandardSession(id: string): GoldStandardSession {
  const ses = getGoldStandardSessions().find(s => s.id === id);
  if (!ses) {
    throw new Error(`[FAIL_CLOSED] [Gold Standard] Ședința "${id}" nu a fost găsită.`);
  }
  return ses;
}

export function getGoldStandardSessionExercises(session: GoldStandardSession): GoldStandardExercise[] {
  const ids = session.segments.flatMap(seg => seg.exercise_ids);
  return ids.map(exId => {
    const target = getGoldStandardExercises().find(e => e.id === exId);
    if (!target) {
      throw new Error(`[FAIL_CLOSED] [Gold Standard] [${session.id}] Referința la exercițiul "${exId}" nu a fost găsită.`);
    }
    return target;
  });
}

export function getGoldStandardAssessment(): GoldStandardAssessment {
  if (!cachedGoldStandardAssessment) {
    cachedGoldStandardAssessment = parseGoldStandardAssessment(gsAssessmentRaw, 'assessment-sprijin-si-unghi-de-pasa.json');
  }
  return cachedGoldStandardAssessment;
}

export function getGoldStandardAssessmentPrinciples(): PrincipleEntity[] {
  const assessment = getGoldStandardAssessment();
  return assessment.principle_ids.map(pId => {
    const target = getAllPrinciples().find(p => p.id === pId);
    if (!target) {
      throw new Error(`[FAIL_CLOSED] [Gold Standard] [${assessment.id}] Referința la principiul "${pId}" nu a fost găsită.`);
    }
    return target;
  });
}
