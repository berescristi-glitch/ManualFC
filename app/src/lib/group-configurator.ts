/**
 * TASK-2705 — Group Configurator: deterministic field logistics for a target
 * player count, derived exclusively from canonical exercise data
 * (`GoldStandardExercise`, see `content-bridge.ts`). No group size, space
 * value or equipment count here is invented — every number either comes
 * directly from canonical fields (`players.total`, `field`, `equipment_items`)
 * or is an explicit, labelled `PRACTICE_HEURISTIC` for how those canonical
 * numbers combine at a player count the exercise wasn't individually authored
 * for. The exercise's `numerical_relation` (e.g. "2v1") is never altered —
 * changing group size would change what the exercise actually trains.
 */
import type { GoldStandardEquipmentItem, GoldStandardExercise } from './content-bridge';

export const SUPPORTED_PLAYER_COUNTS = [8, 10, 12, 14, 16, 18] as const;
export type SupportedPlayerCount = (typeof SUPPORTED_PLAYER_COUNTS)[number];
export type CoachCount = 1 | 2;

export type GroupConfiguratorEquipmentTotal = GoldStandardEquipmentItem;

export interface GroupConfiguratorResult {
  exerciseId: string;
  exerciseTitle: string;
  totalPlayers: SupportedPlayerCount;
  coachCount: CoachCount;
  groupSize: number;
  numericalRelation: string;
  feasible: boolean;
  feasibilityNote?: string;
  numberOfGroups: number;
  activePlayers: number;
  waitingPlayers: number;
  rotationNote: string;
  playingAreas: number;
  areaDimensions: { length_m: number; width_m: number; safety_margin_m: number };
  totalSpace: { combined_width_m: number; length_m: number };
  equipmentTotals: GroupConfiguratorEquipmentTotal[];
  coachPositioning: string;
}

function readGroupSize(exercise: GoldStandardExercise): number {
  const total = (exercise.players as Record<string, unknown>)?.total;
  const groupSize = Number(total);
  if (!Number.isFinite(groupSize) || groupSize <= 0) {
    throw new Error(`[FAIL_CLOSED] [group-configurator] [${exercise.id}] players.total lipsește sau este invalid.`);
  }
  return groupSize;
}

function computeCoachPositioning(numberOfGroups: number, coachCount: CoachCount): string {
  if (numberOfGroups <= 1) {
    return coachCount === 1
      ? 'Un grup activ — antrenorul observă direct, fără nevoie de rotație de atenție.'
      : 'Un grup activ — al doilea antrenor este disponibil pentru feedback individual sau pentru grupul de așteptare, nu este nevoie de acoperire separată.';
  }
  if (coachCount === 1) {
    return numberOfGroups === 2
      ? 'PRACTICE_HEURISTIC: un antrenor circulă între cele două grupe, alternând atenția la fiecare set; niciun grup nu rămâne neobservat mai mult de un set întreg.'
      : `PRACTICE_HEURISTIC: cu ${numberOfGroups} grupe și un singur antrenor, observarea directă simultană a tuturor nu este posibilă — antrenorul prioritizează 1-2 grupe pe rând (rotație explicită), celelalte rulează cu auto-verificare între coechipieri folosind întrebările de la "coach_questions".`;
  }
  const first = Math.ceil(numberOfGroups / 2);
  const second = numberOfGroups - first;
  return `PRACTICE_HEURISTIC: împărțire pe doi antrenori — primul acoperă ${first} grup${first === 1 ? '' : 'e'}, al doilea acoperă ${second} grup${second === 1 ? '' : 'e'}; reevaluează împărțirea dacă o grupă are nevoie vizibil de mai multă atenție.`;
}

function computeRotationNote(exercise: GoldStandardExercise, waitingPlayers: number): string {
  const base = typeof exercise.duration?.format === 'string' ? exercise.duration.format as string : '';
  if (waitingPlayers <= 0) {
    return base || 'Fără rotație suplimentară — toți copiii sunt activi simultan în grupele formate.';
  }
  return `${base ? base + ' ' : ''}PRACTICE_HEURISTIC: cei ${waitingPlayers} copii rămași în afara unei grupe complete de ${exercise.players && (exercise.players as Record<string, unknown>).total} intră prin rotație cu grupele active la fiecare schimbare de set, ca nimeni să nu aștepte întreaga durată a exercițiului.`;
}

/**
 * Deterministic logistics for one exercise at one target player count.
 * Group size always equals the exercise's canonical `players.total` — never
 * inflated or shrunk, since that would silently change `numerical_relation`.
 */
export function computeGroupConfiguration(
  exercise: GoldStandardExercise,
  totalPlayers: SupportedPlayerCount,
  coachCount: CoachCount,
): GroupConfiguratorResult {
  const groupSize = readGroupSize(exercise);
  const numberOfGroups = Math.floor(totalPlayers / groupSize);
  const feasible = numberOfGroups >= 1;
  const activePlayers = numberOfGroups * groupSize;
  const waitingPlayers = totalPlayers - activePlayers;

  const equipmentTotals: GroupConfiguratorEquipmentTotal[] = exercise.equipment_items.map((eq) => ({
    item: eq.item,
    quantity: feasible ? eq.quantity * numberOfGroups : 0,
    ...(eq.quantity_max ? { quantity_max: feasible ? eq.quantity_max * numberOfGroups : 0 } : {}),
  }));

  return {
    exerciseId: exercise.id,
    exerciseTitle: exercise.title,
    totalPlayers,
    coachCount,
    groupSize,
    numericalRelation: exercise.numerical_relation,
    feasible,
    feasibilityNote: feasible
      ? undefined
      : `Cu ${totalPlayers} copii nu se poate forma niciun grup complet de ${groupSize} (${exercise.numerical_relation}) fără să schimbi relația numerică a exercițiului. Folosește regresia exercițiului sau alege un alt exercițiu din familie pentru acest efectiv.`,
    numberOfGroups,
    activePlayers,
    waitingPlayers,
    rotationNote: computeRotationNote(exercise, waitingPlayers),
    playingAreas: numberOfGroups,
    areaDimensions: exercise.field,
    totalSpace: {
      combined_width_m: feasible ? Number((numberOfGroups * (exercise.field.width_m + exercise.field.safety_margin_m)).toFixed(1)) : 0,
      length_m: exercise.field.length_m + exercise.field.safety_margin_m,
    },
    equipmentTotals,
    coachPositioning: feasible ? computeCoachPositioning(numberOfGroups, coachCount) : 'N/A — niciun grup format la acest efectiv.',
  };
}

export function computeGroupConfigurations(
  exercises: GoldStandardExercise[],
  totalPlayers: SupportedPlayerCount,
  coachCount: CoachCount,
): GroupConfiguratorResult[] {
  return exercises.map((exercise) => computeGroupConfiguration(exercise, totalPlayers, coachCount));
}

export const TOTAL_SPACE_LABEL =
  'PRACTICE_HEURISTIC: suprafață totală pentru un aranjament simplu, grupele așezate una lângă alta pe un singur rând, cu marja de siguranță proprie fiecărei grupe inclusă. Nu este singurul aranjament posibil — adaptează la forma reală a terenului disponibil.';
