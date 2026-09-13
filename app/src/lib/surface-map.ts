/**
 * TASK-2706 residual A — Session Surface Map: a deterministic bird's-eye
 * layout derived directly from `GroupConfiguratorResult` (TASK-2705).
 *
 * Architecture decision (§6 of the Wave-2.1 spec): fully dynamic, not a
 * canonical layout plus hand-drawn variants. A surface map is generated
 * for whichever player count and coach count the coach actually has, by
 * laying out `playingAreas` rectangles side by side at `areaDimensions`
 * and placing coach markers using the same split logic already computed
 * in `computeCoachPositioning`. Six hand-authored diagrams per exercise
 * per coach count (60+ static variants) would drift from the
 * configurator's numbers the moment either changed; a shared renderer
 * cannot drift, because it has no numbers of its own.
 */
import type { GroupConfiguratorResult } from './group-configurator';

export interface SurfaceMapAreaRect {
  x: number;
  y: number;
  width: number;
  height: number;
  label: string;
}

export interface SurfaceMapCoachMarker {
  x: number;
  y: number;
  label: string;
}

export interface SurfaceMapSpec {
  areas: SurfaceMapAreaRect[];
  totalWidth: number;
  totalHeight: number;
  coachMarkers: SurfaceMapCoachMarker[];
  equipmentMarker: { x: number; y: number };
  bufferNote: string;
  waitingNote?: string;
}

/** Builds a surface-map layout, or null if the count doesn't form any group (mirrors `computeGroupConfiguration`'s `feasible` flag). */
export function buildSurfaceMap(config: GroupConfiguratorResult): SurfaceMapSpec | null {
  if (!config.feasible || config.playingAreas <= 0) return null;

  const { playingAreas, areaDimensions, coachCount } = config;
  const gap = areaDimensions.safety_margin_m;
  const areaWidth = areaDimensions.width_m;
  const areaHeight = areaDimensions.length_m;

  const areas: SurfaceMapAreaRect[] = [];
  for (let i = 0; i < playingAreas; i += 1) {
    areas.push({
      x: i * (areaWidth + gap),
      y: 0,
      width: areaWidth,
      height: areaHeight,
      label: `Grupa ${i + 1}`,
    });
  }
  const totalWidth = playingAreas * areaWidth + Math.max(0, playingAreas - 1) * gap;
  const totalHeight = areaHeight;

  const coachMarkers: SurfaceMapCoachMarker[] = [];
  if (coachCount === 1 || playingAreas <= 2) {
    coachMarkers.push({ x: totalWidth / 2, y: totalHeight + gap, label: coachCount === 1 ? 'Antrenor' : 'Antrenor 1+2' });
  } else {
    const firstCount = Math.ceil(playingAreas / 2);
    const firstSpan = firstCount * areaWidth + Math.max(0, firstCount - 1) * gap;
    const secondSpan = totalWidth - firstSpan - gap;
    coachMarkers.push({ x: firstSpan / 2, y: totalHeight + gap, label: 'Antrenor 1' });
    coachMarkers.push({ x: firstSpan + gap + secondSpan / 2, y: totalHeight + gap, label: 'Antrenor 2' });
  }

  return {
    areas,
    totalWidth,
    totalHeight,
    coachMarkers,
    equipmentMarker: { x: -gap * 1.5, y: totalHeight / 2 },
    bufferNote: `PRACTICE_HEURISTIC: ${gap} m marjă de siguranță între grupe, egală cu marja canonică a exercițiului — nu un standard separat validat.`,
    waitingNote: config.waitingPlayers > 0
      ? `${config.waitingPlayers} copii în așteptare rotesc cu grupele active (vezi „Rotație / așteptare” din configurator).`
      : undefined,
  };
}
