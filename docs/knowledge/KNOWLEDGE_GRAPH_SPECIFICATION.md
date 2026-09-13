# Specificația grafului de cunoaștere

**Versiune:** 2.0.0 (extensie a graf-ului v1 Wave-3) · **Task de referință:** TASK-2906 · **Statut:** Architecture

Extinde explicit `docs/architecture/PROBLEM_KNOWLEDGE_GRAPH.md` (graful canonic `problem → observation → hypothesis → test → cue → principle → exercise → session → assessment → transfer → evidence → media`, deja implementat prin `app/src/lib/problem-library.ts`). Nu se creează un al doilea graf paralel — se adaugă noduri și relații noi pe același graf.

## 1. Regula fără legături decorative (§25 din prompt)

Fiecare relație de mai jos există pentru unul din patru motive: **înțelegere** (ajută un antrenor să vadă de ce), **descoperire** (ajută căutarea/navigarea), **practică** (activează un comportament concret) sau **validare** (permite unui script să verifice completitudinea). O relație care nu servește niciunul din aceste patru scopuri nu se adaugă — regulă explicit inspirată de tiparul deja aplicat de `problem-library.ts` (relațiile spre exercițiu/ședință pot fi goale, dar interfața spune asta, nu inventează).

## 2. Tipuri de entități

| Entitate | Stare | ID prefix |
|---|---|---|
| `KNOWLEDGE_CONCEPT` | NOU | `ped.*` / `coach.*` |
| `PEDAGOG_DOMAIN` | NOU (formalizare) | `PED-D` |
| `COACH_DOMAIN` | NOU (formalizare) | `COACH-D` |
| `PEDAGOG_COMPETENCY` | NOU | `PED-C` |
| `COACH_COMPETENCY` | NOU | `COACH-C` |
| `FOOTBALL_PRINCIPLE` | EXISTENT | `principle.*` |
| `PROBLEM` | EXISTENT | `PRB-####` |
| `INTERVENTION` | EXISTENT (implicit în `Problem.possible_explanations`) | — |
| `CUE` | EXISTENT (`exact_cue` în exercițiu) | — |
| `EXERCISE` | EXISTENT | `EX-####` |
| `SESSION` | EXISTENT | `SES-####` |
| `ASSESSMENT` | EXISTENT | `ASM-####` |
| `TRANSFER_CHECK` | EXISTENT (`SessionReflection.transferState`) | — |
| `REFLECTION_PROMPT` | EXISTENT (parțial — copil/joc), NOU (dimensiune antrenor) | — |
| `EVIDENCE_CLAIM` | EXISTENT | `CLM-####` |
| `MEDIA` | EXISTENT | `MED-*` |

## 3. Relații — extensie a graf-ului existent

```
CONCEPT           → SUPPORTS      → PEDAGOG_COMPETENCY
CONCEPT           → SUPPORTS      → COACH_COMPETENCY
PEDAGOG_COMPETENCY → APPLIED_IN   → EXERCISE
COACH_COMPETENCY  → PRACTICED_IN  → SESSION
COACH_COMPETENCY  → PRACTICED_IN  → EXERCISE
PROBLEM           → EXPLAINED_BY  → CONCEPT
PROBLEM           → TESTED_BY     → INTERVENTION       (deja implicit, acum explicit)
INTERVENTION      → USES          → CUE                (deja implicit prin exact_cue)
INTERVENTION      → REQUIRES      → COACH_COMPETENCY
EXERCISE          → TRAINS        → FOOTBALL_PRINCIPLE (deja implementat, related_principles)
EXERCISE          → APPLIES       → PEDAGOG_COMPETENCY
EXERCISE          → APPLIES       → COACH_COMPETENCY
SESSION           → DEVELOPS_CHILD → FOOTBALL_PRINCIPLE (deja implicit prin items)
SESSION           → DEVELOPS_COACH → COACH_COMPETENCY
PEDAGOG_DOMAIN    → CONTAINS      → CONCEPT
COACH_DOMAIN      → CONTAINS      → CONCEPT
CONCEPT           → GROUNDED_IN   → EVIDENCE_CLAIM      (deja implicit, `research/dossiers/*` → CLM-*)
COMPETENCY        → REFLECTED_IN  → REFLECTION_PROMPT
```

Toate relațiile marcate „deja implicit" există azi ca legături de date fără nume formal de relație — PHASE-29 le numește, nu le creează.

## 4. Direcție bidirecțională (§9 arhitectură master)

Fiecare relație e navigabilă în ambele sensuri prin construcție (ID canonic + index invers, exact tiparul `content-bridge.ts` deja folosit pentru `Principle↔Exercise↔Problem`). Nu se duplică date — indexul invers se calculează, nu se stochează separat (regulă deja aplicată de `getResolvedProblem`/`getResolvedExercise`).

## 5. Cardinalități

| Relație | Cardinalitate | Obligatorie? |
|---|---|---|
| `PROBLEM → EXPLAINED_BY → CONCEPT` | many-to-many | recomandată, nu obligatorie (o problemă poate rămâne `NEEDS_FIELD_VALIDATION` fără concept confirmat) |
| `EXERCISE → APPLIES → PEDAGOG_COMPETENCY` | many-to-many | obligatorie doar pentru Gold Standard V2 (vezi `KNOWLEDGE_SCHEMA_IMPACT_ANALYSIS.md`) |
| `EXERCISE → APPLIES → COACH_COMPETENCY` | many-to-many, minim 1 | obligatorie doar pentru Gold Standard V2 |
| `CONCEPT → GROUNDED_IN → EVIDENCE_CLAIM` | many-to-many | recomandată; un concept fără claim rămâne `HYPOTHESIS`/`RESEARCH_REQUIRED`, vizibil ca atare |
| `SESSION → DEVELOPS_COACH → COACH_COMPETENCY` | many-to-many | opțională în V1, obligatorie în Session Contract V2 |

## 6. Mapare pe produsul curent

| Nod din graf | Obiect runtime actual |
|---|---|
| `PROBLEM` | `data/problems/problem-library.json`, tipizat prin `problem.schema.json` |
| `EXERCISE`, `SESSION`, `ASSESSMENT` | `data/exercises/`, `data/sessions/`, `data/assessments/` |
| `EVIDENCE_CLAIM` | `research/claims.json`, `schemas/claim-registry.schema.json` |
| `MEDIA` | `data/media/media-registry.json` (TASK-2804) |
| `TRANSFER_CHECK` | `SessionReflection.transferState` (`app/src/lib/coach-state.ts`) |
| `PEDAGOG_DOMAIN`, `COACH_DOMAIN`, `PEDAGOG_COMPETENCY`, `COACH_COMPETENCY` | încă documente Markdown (`docs/knowledge/*`), nu obiecte JSON validate — pasul următor e formalizarea în schemă (`KNOWLEDGE_SCHEMA_IMPACT_ANALYSIS.md`) |

## 7. Ce nu se construiește acum

Fără implementare de motor de graf (bază de date de tip graph). Relațiile rămân, ca și azi, ID-uri și array-uri rezolvate la build-time prin `content-bridge.ts` — „Knowledge Graph Light", exact termenul deja folosit în `CONTENT_TAXONOMY.md` §1.3. Fără UI nou de explorare a grafului în PHASE-29.
