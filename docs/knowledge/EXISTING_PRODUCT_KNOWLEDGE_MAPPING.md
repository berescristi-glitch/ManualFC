# Maparea cunoașterii pe produsul existent

**Versiune:** 1.0.0 · **Task de referință:** TASK-2908 · **Statut:** Architecture

Stări posibile: `ALREADY_COMPATIBLE`, `NEEDS_METADATA_EXTENSION` (câmp opțional nou, aditiv), `NEEDS_CONTENT_EXTENSION` (conținut de scris, schema neschimbată), `NEEDS_SCHEMA_CHANGE` (schema JSON se extinde), `NEEDS_REFACTOR` (schimbare structurală). Niciun runtime nu se modifică în PHASE-29 — acesta e doar inventarul.

## 1. Cele 8 probleme (`data/problems/problem-library.json`)

| Obiect | Stare | Motiv |
|---|---|---|
| PRB-0001–PRB-0008 (structura de bază) | `ALREADY_COMPATIBLE` | `observable_behavior`/`possible_explanations` deja separă observație de ipoteză, exact modelul cerut |
| Legătură spre `PEDAGOG_COMPETENCY`/`COACH_COMPETENCY` | `NEEDS_SCHEMA_CHANGE` | câmp nou `related_pedagog_competencies`/`related_coach_competencies`, opțional, aditiv |
| Legătură spre `PEDAGOG_DOMAIN`/`COACH_DOMAIN` | `NEEDS_SCHEMA_CHANGE` | câmp nou opțional, similar cu `related_exercises` existent |

## 2. Cele 25 de principii (`data/principles/`)

| Obiect | Stare | Motiv |
|---|---|---|
| Structura de bază | `ALREADY_COMPATIBLE` | deja urmează cele 18 întrebări din `PEDAGOGICAL_PRODUCT_PRINCIPLES.md` |
| Clasificare Pedagog vs. Coach vs. Practică | `NEEDS_METADATA_EXTENSION` | azi toate principiile trăiesc sub `cat.principii-joc`; unele (ex. „greșeala ca informație") sunt de fapt concepte Pedagogul, nu principii tactice — necesită un câmp `pillar: PEDAGOGUL|ANTRENORUL|PRACTICA` |
| Legătură spre competențe | `NEEDS_SCHEMA_CHANGE` | ca la probleme |

## 3. EX-0001–EX-0005

| Obiect | Stare | Motiv |
|---|---|---|
| Structura curentă completă (`primary_objective`, `exact_cue`, `observable_behaviours`, `rationales`, `progression`/`regression`) | `ALREADY_COMPATIBLE` | acoperă deja marea majoritate a Practice Contract V2 (§5, `THEORY_TO_PRACTICE_CONTRACT.md`) |
| `PEDAGOGICAL_PRINCIPLE_IDS`, `PEDAGOG_COMPETENCY_IDS`, `COACH_COMPETENCY_IDS` | `NEEDS_SCHEMA_CHANGE` | complet absente azi |
| `DO_NOT_ASSUME`, `WHEN_NOT_TO_INTERVENE`, `COMMON_COACH_ERROR` | `NEEDS_SCHEMA_CHANGE` + `NEEDS_CONTENT_EXTENSION` | câmp nou + text de scris pentru cele 5 exerciții |
| `COACH_REFLECTION` | `NEEDS_SCHEMA_CHANGE` | depinde de Reflection V2, neimplementat |

**Concluzie:** cele 5 exerciții sunt candidați direcți pentru migrarea Gold Standard V2 (§`KNOWLEDGE_SCHEMA_IMPACT_ANALYSIS.md`) — sunt deja aproape de contract, lipsesc doar câmpurile de legătură explicită.

## 4. SES-0001–SES-0002

| Obiect | Stare | Motiv |
|---|---|---|
| Coloana „CHILD OBJECTIVES" (Session Contract V2) | `ALREADY_COMPATIBLE` (parțial) | `problemId`, `items`, Group Configurator, Field Mode — deja implementate |
| Coloana „COACH OBJECTIVES" | `NEEDS_REFACTOR` | complet absentă — necesită `coach_competency_ids`, `coach_focus_cues` per segment, o structură nouă |

## 5. ASM-0001

| Obiect | Stare | Motiv |
|---|---|---|
| Criterii comportamentale existente | `ALREADY_COMPATIBLE` | deja per-comportament, deja legate de exerciții |
| Legătură spre competențe | `NEEDS_METADATA_EXTENSION` | opțională, aditivă |

## 6. Decision Engine

| Obiect | Stare | Motiv |
|---|---|---|
| Fluxul observație→ipoteză→test→cue→exercițiu | `ALREADY_COMPATIBLE` | e deja implementarea funcțională a lanțului din `THEORY_TO_PRACTICE_CONTRACT.md` §1, minus pasul de competență |
| Afișarea competenței de coaching aplicate | `NEEDS_CONTENT_EXTENSION` (UI) | nu se implementează în PHASE-29 |

## 7. Field Mode

| Obiect | Stare | Motiv |
|---|---|---|
| Cronometru, navigare pe segmente, cue/observă | `ALREADY_COMPATIBLE` | funcțional, offline-capabil (TASK-2805) |
| „Focus de antrenor" per segment (Field Mode V2) | `NEEDS_REFACTOR` | necesită Session Contract V2 înainte |

## 8. Reflecție (`SessionReflection`)

| Obiect | Stare | Motiv |
|---|---|---|
| Dimensiunea copil/joc (`observedState`, `transferState`) | `ALREADY_COMPATIBLE` | deja implementat, testat, offline-capabil |
| Dimensiunea antrenor (Reflection V2 §8) | `NEEDS_SCHEMA_CHANGE` | extensie aditivă v1 a `CoachState`, exact tiparul deja folosit de 3 ori (`reflections`, `offlinePacks`) |

## 9. Registrul media (`data/media/media-registry.json`)

| Obiect | Stare | Motiv |
|---|---|---|
| Structura curentă (`canonical_refs`, `evidence_boundary`) | `ALREADY_COMPATIBLE` | `canonical_refs` poate referi deja orice ID canonic nou fără schimbare de schemă |

## 10. Registrul de cercetare (`research/`, `schemas/claim-registry.schema.json` etc.)

| Obiect | Stare | Motiv |
|---|---|---|
| Toată infrastructura | `ALREADY_COMPATIBLE` | vezi `EVIDENCE_CLASSIFICATION_SYSTEM.md` — nicio schimbare necesară |
| Dosare ancorate pe `PED-Dxx`/`COACH-Dxx` | `NEEDS_METADATA_EXTENSION` | câmp `domain_id` opțional alături de `chapter_id` |

## Rezumat

| Stare | Câte obiecte |
|---|---|
| `ALREADY_COMPATIBLE` | 6 din 10 zone (probleme-bază, principii-bază, exerciții-bază, sesiuni copil, Decision Engine, Field Mode-bază, reflecție-copil, media, cercetare) |
| `NEEDS_METADATA_EXTENSION` | principii (pilon), dosare cercetare |
| `NEEDS_SCHEMA_CHANGE` | probleme/principii/exerciții (legături competență), reflecție (dimensiune antrenor) |
| `NEEDS_REFACTOR` | ședințe (coloana coach), Field Mode V2 |

Niciun obiect nu cere `NEEDS_REFACTOR` distructiv — cel mai amplu caz (Session Contract V2) e o **adăugire** de coloană nouă, nu o rescriere a celei existente.
