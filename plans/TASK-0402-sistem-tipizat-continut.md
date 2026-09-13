# ExecPlan — TASK-0402: Sistemul Tipizat de Conținut și Relații

**Task ID:** TASK-0402  
**Titlu:** Sistemul tipizat de conținut și relații  
**Fază:** PHASE-04 — Arhitectură frontend web și Content Collections  
**Stare:** IN_PROGRESS  
**Prioritate:** CRITICAL  
**Pondere:** 0.389%  
**Data:** 2026-08-09  

---

## 1. Titlu și scop

Construirea sistemului TypeScript complet tipizat și fail-closed pentru reprezentarea entităților de conținut, a relațiilor, a referințelor epistemice și vizuale, precum și maturizarea modulului `app/src/lib/content-bridge.ts` ca API stabil înainte de introducerea conținutului pedagogic real.

## 2. Context pentru un cititor nou

- ManualFC a definit în `TASK-0201` registrul mașină-citibil al taxonomiei (`data/taxonomy/registry.json`), contractele de ID/slug și rutele dinamice de probă.
- Sursa de adevăr pentru validarea canonică rămâne validatorul Python `scripts/validate_content.py` și schemele JSON din `schemas/`.
- Taskul `TASK-0402` adaugă tipizarea strictă în TypeScript (`app/src/types/content-model.ts`), boundary-ul de securitate pentru JSON (`app/src/lib/json-boundary.ts`), separarea fixture-urilor de dezvoltare față de conținutul de producție și suite de teste pozitive/negative.

## 3. Rezultatul verificabil

- Fișierul de definiții TypeScript `app/src/types/content-model.ts` conține tipurile branded (`CanonicalId`, `EntitySlug`, `CategoryId`), tipurile pentru entitățile principale (`PrincipleEntity`, `ExerciseEntity`, `ProblemEntity`, `SessionEntity`), separarea semantică a entității `Problem` (`observation`, `possible_causes`, `intervention`) și structura `TacticalVisualRef`.
- Boundary-ul `app/src/lib/json-boundary.ts` validează datele venite din JSON la runtime în modulul Astro.
- Modulul `app/src/lib/content-bridge.ts` oferă API-ul tipizat complet (`getResolvedPrinciple`, `getResolvedProblem`, `getResolvedExercise`, `getCanonicalContent`, `getDevelopmentFixtures`, `validateNoDuplicateIds`).
- Suita de teste automate Python `tests/test_content_model.py` validează scenarii pozitive și negative (ID-uri duplicate, slug invalid, referințe lipsă fail-closed, separare fixture/producție).
- `npm run check`, `npm run build`, `python -m unittest discover tests` și toate validatoarele iasă PASS.

## 4. Domeniu și non-obiective

### În domeniu:
- Definitivarea `app/src/types/content-model.ts`.
- Construirea `app/src/lib/json-boundary.ts`.
- Refacerea/maturizarea `app/src/lib/content-bridge.ts`.
- Actualizarea paginilor dinamice `/principii/[slug]`, `/probleme/[slug]`, `/exercitii/[slug]`.
- Crearea specificației `docs/architecture/TYPED_CONTENT_MODEL.md`.
- Suita de teste `tests/test_content_model.py`.

### Non-obiective:
- Căutare Pagefind sau integrări search.
- Renderer pentru Tactical Visual Engine sau animații.
- Redactare de volum de conținut pedagogic real.
- Instalare de biblioteci noi de runtime validation.

## 5. Fișiere și module afectate

- `app/src/types/content-model.ts` (nou)
- `app/src/types/index.ts` (modificat)
- `app/src/lib/json-boundary.ts` (nou)
- `app/src/lib/content-bridge.ts` (modificat)
- `app/src/pages/principii/[slug].astro` (modificat)
- `app/src/pages/probleme/[slug].astro` (modificat)
- `app/src/pages/exercitii/[slug].astro` (modificat)
- `docs/architecture/TYPED_CONTENT_MODEL.md` (nou)
- `plans/TASK-0402-sistem-tipizat-continut.md` (nou)
- `reports/task-reports/TASK-0402.md` (nou)
- `tests/test_content_model.py` (nou)
- `scripts/generate_task_registry.py` (modificat)
- `TASK_REGISTRY.json` (modificat)
- `TASK_HISTORY.jsonl` (modificat)
- `PROJECT_STATUS.md` (modificat)

## 6. Pași de implementare

1. Crearea ExecPlan-ului `plans/TASK-0402-sistem-tipizat-continut.md`.
2. Definirea tipurilor în `app/src/types/content-model.ts`.
3. Crearea boundary-ului JSON `app/src/lib/json-boundary.ts`.
4. Maturizarea Content Bridge-ului `app/src/lib/content-bridge.ts`.
5. Actualizarea paginilor dinamice `/principii/[slug]`, `/probleme/[slug]`, `/exercitii/[slug]`.
6. Crearea documentului de arhitectură `docs/architecture/TYPED_CONTENT_MODEL.md`.
7. Crearea suitei de teste `tests/test_content_model.py`.
8. Rularea verificărilor `npm run check`, `npm run build`, `python -m unittest discover tests` și a validatoarelor.
9. Generarea raportului de task `reports/task-reports/TASK-0402.md`.
10. Actualizarea registrelor de proiect și executarea commit-ului Git `feat(TASK-0402): add typed content relation system`.

## 7. Validare și acceptare

- `npm run check` -> 0 erori.
- `npm run build` -> 8 static HTML pages în `dist/web/`.
- `python -m unittest discover tests` -> 140+ teste PASS.
- `python scripts/validate_project.py` -> 0 erori.
- `python scripts/validate_content.py` -> 0 erori.
- `python scripts/generate_task_registry.py --check` -> reproductibil.

## 8. Progres

- [x] 2026-08-09 13:20 — Creare ExecPlan `plans/TASK-0402-sistem-tipizat-continut.md`.
- [ ] 2026-08-09 13:30 — Implementare `app/src/types/content-model.ts` și `json-boundary.ts`.
- [ ] 2026-08-09 13:45 — Actualizare `content-bridge.ts` și rute dinamice.
- [ ] 2026-08-09 14:00 — Validare build, check, teste pozitive/negative și commit Git.

## 9. Decizii și retrospectivă

- Contractul de tipuri branded asigură siguranța referințelor la compilare fără a adăuga overhead runtime.
- Separarea clară a entității `Problem` împiedică confundarea simptomului observat cu diagnoza pe teren.
