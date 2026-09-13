# Analiza de impact asupra schemei

**Versiune:** 1.0.0 · **Task de referință:** TASK-2908 · **Statut:** Architecture — propunere, nu implementare

Regulă absolută (§53 din specificația PHASE-29): **runtime-ul Wave-4 acceptat (`560e27c`) nu se modifică în PHASE-29.** Acest document e o propunere de schimbări viitoare, cu strategie explicită de migrare fără destabilizare — nu un plan de execuție imediată.

## 1. Entități noi propuse

| Entitate | Schemă nouă propusă | Impact asupra schemelor existente |
|---|---|---|
| `PEDAGOG_DOMAIN`, `COACH_DOMAIN` | `pedagog-domain.schema.json`, `coach-domain.schema.json` (schemă nouă, independentă) | ZERO — sunt fișiere noi, nu ating `exercise.schema.json` etc. |
| `PEDAGOG_COMPETENCY`, `COACH_COMPETENCY` | `pedagog-competency.schema.json`, `coach-competency.schema.json` | ZERO direct; alte scheme le pot referi opțional (§2) |

## 2. Extensii propuse la scheme existente

Toate aditive, toate opționale, toate `NEEDS_SCHEMA_CHANGE` conform `EXISTING_PRODUCT_KNOWLEDGE_MAPPING.md`:

| Schemă | Câmp nou propus | Tip | Obligatoriu? | Impact retroactiv |
|---|---|---|---|---|
| `exercise.schema.json` | `pedagog_competency_ids` | array de string, pattern `PED-C##` | opțional în V1, obligatoriu doar pentru `gold_standard_version: "V2"` | NICIUN exercițiu existent nu invalidează |
| `exercise.schema.json` | `coach_competency_ids` | array, pattern `COACH-C##` | idem | idem |
| `exercise.schema.json` | `do_not_assume` | array de string | opțional | idem |
| `exercise.schema.json` | `when_not_to_intervene` | string | opțional | idem |
| `exercise.schema.json` | `common_coach_error` | string | opțional | idem |
| `exercise.schema.json` | `gold_standard_version` | enum `"V1" | "V2"`, implicit `"V1"` | nou câmp, implicit retroactiv pe tot ce există | NICIUN regres |
| `problem.schema.json` | `related_pedagog_competencies`, `related_coach_competencies` | array opțional | opțional | zero impact |
| `session.schema.json` | `coach_competency_ids`, `coach_focus_cues` | array opțional | opțional | zero impact |
| `research-question.schema.json` | `domain_id` | string opțional, pattern `PED-D##`/`COACH-D##` | opțional, alături de `chapter_id` existent | zero impact |
| `CoachState` (`coach-state.ts`, nu JSON Schema — TypeScript runtime) | `SessionReflection.coachReflection` | obiect opțional nou | opțional, exact tiparul aditiv v1 deja folosit de 3 ori | zero impact — `sanitizeState()` tratează câmpul lipsă ca `undefined`, nu ca eroare |

## 3. Impact asupra validatorului canonic (`scripts/validate_content.py`)

`SCHEMA_TYPES` primește două intrări noi (`pedagog-domain`, `coach-domain`, `pedagog-competency`, `coach-competency`) — extensie aditivă a unui dicționar Python, exact tiparul deja folosit quando s-a adăugat `media-registry` (TASK-2804). Validarea câmpurilor noi opționale pe scheme existente nu schimbă comportamentul validatorului pentru documentele care nu le au (JSON Schema: proprietate absentă ≠ eroare, dacă nu e în `required`).

**Regulă de migrare fail-closed (§52-53):** un exercițiu nu poate trece validarea **Gold Standard V2** fără `pedagog_competency_ids` (minim 1), `coach_competency_ids` (minim 1), `do_not_assume`, `coach_intervention`, `verification`, `transfer_check`, `coach_reflection` — dar validarea **V1** (implicită, `gold_standard_version` absent sau `"V1"`) rămâne exact ce e azi. EX-0001–EX-0005 rămân valide V1 până la migrare explicită (§4).

## 4. Planul de migrare Gold Standard V2

Nu se execută în PHASE-29. Secvență propusă pentru o fază viitoare dedicată:

1. Adaugă câmpurile opționale la schemă (zero risc, aditiv).
2. Populează `pedagog_competency_ids`/`coach_competency_ids`/`do_not_assume`/etc. pentru EX-0001–EX-0005 (candidat cel mai apropiat de contract, vezi `EXISTING_PRODUCT_KNOWLEDGE_MAPPING.md` §3).
3. Marchează explicit `gold_standard_version: "V2"` doar pe exercițiile complete.
4. Extinde SES-0001/SES-0002 cu coloana „COACH OBJECTIVES" (Session Contract V2) — cea mai amplă schimbare, dar tot aditivă la nivel de schemă.
5. Abia după ce toate exercițiile/ședințele canonice curente sunt V2, validatorul poate face `gold_standard_version: "V2"` implicit pentru conținut *nou*, fără să retrogradeze conținutul existent.

## 5. Impact runtime (aplicație web)

| Componentă | Impact |
|---|---|
| `app/src/lib/content-bridge.ts` | extensie de tip TypeScript pentru câmpurile noi opționale — pattern deja folosit la fiecare extensie anterioară (media registry, offline packs) |
| Paginile de exercițiu/problemă/ședință existente | ZERO — câmpurile noi nu sunt randate până la o decizie explicită de UI, separată de PHASE-29 |
| `CoachState`/`coach-state.ts` | extensie aditivă v1, al patrulea tipar de acest fel (după `reflections`, `offlinePacks`, acum `coachReflection` opțional în `SessionReflection`) |
| Service Worker / offline pack | ZERO — nu ating rutele sau resursele cache-uite |

## 6. Compatibilitate retroactivă — verdict

**PASS.** Fiecare schimbare propusă e strict aditivă și opțională. Niciun document canonic existent (25 principii, 8 probleme, 5 exerciții, 2 ședințe, 1 evaluare, 15 media, 3 claim-uri, 3 întrebări de cercetare) nu devine invalid. Validatorul `--strict` continuă să treacă fără nicio modificare de date, chiar dacă schemele sunt extinse (verificabil practic: adăugarea unei proprietăți opționale la un JSON Schema Draft 2020-12 cu `additionalProperties` gestionat corect nu respinge documentele existente).

## 7. Ce nu se face în PHASE-29

Nu se editează niciun fișier `schemas/*.json` existent. Nu se editează `scripts/validate_content.py`. Nu se adaugă `pedagog-domain.schema.json`/etc. ca fișiere reale — rămân propuneri documentate aici, gata de implementare într-o fază viitoare de arhitectură de conținut (PHASE-33, `PHASE30_RESEARCH_ROADMAP.md`).
