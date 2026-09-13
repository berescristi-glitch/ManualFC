# ExecPlan — TASK-0111: Definirea Arhitecturii Primului Volum Canonic

**Task ID:** TASK-0111  
**Titlu:** Definirea arhitecturii primului volum canonic  
**Fază:** PHASE-01 — Cadrul normativ, de cercetare și metodologic  
**Stare:** IN_PROGRESS  
**Prioritate:** CRITICAL  
**Pondere:** 0.389%  
**Data:** 2026-08-09  

---

## 1. Titlu și scop

Definirea arhitecturii primului volum canonic al platformei **ManualFC** — **Volumul 1: „Copilul și procesul de învățare” (`VOLUME-01`)**, marcând tranziția oficială de la infrastructură tehnică la producția de conținut pedagogic real.

## 2. Context pentru un cititor nou

- ManualFC are finalizată fundația tehnică web, sistemul de design, taxonomia de conținut și modelul tipizat.
- Conform `MASTER_EXECUTION_PROMPT.md` și `CODEX.md`, Volumul 1 tratează copilul de 10–11 ani (grupele 2015 și 2016) și procesul de învățare, aplicând principiul fondator: *„Antrenorul format mai întâi ca pedagog și apoi ca antrenor”*.
- Taskul creează specificația de arhitectură a volumului (`docs/content/VOLUME_01_ARCHITECTURE.md`), manifestul mașină-citibil (`data/content/volumes/volume-01.json`), șablonul de producție al capitolelor (`docs/content/CHAPTER_PRODUCTION_TEMPLATE.md`), dosarul de reverificare a regulamentelor (`research/dossiers/regulations-u11-recheck.md`) și seed-ul canonic de producție (`data/principles/principle-scanning-before-receive.json`).

## 3. Rezultatul verificabil

- Specificația `docs/content/VOLUME_01_ARCHITECTURE.md` definește cele 5 capitole ale Volumului 1, matricea de dovadă, progresia pedagogică și contractul de redactare.
- Manifestul JSON `data/content/volumes/volume-01.json` este mașină-citibil și conține ID-urile canonice ale capitolelor, ordinea lor deterministă și starea de pregătire a dovezilor.
- Fișierul `docs/content/CHAPTER_PRODUCTION_TEMPLATE.md` oferă șablonul reutilizabil de redactare.
- Fișierul `research/dossiers/regulations-u11-recheck.md` confirmă starea reverificată a regulamentelor FRF/AJF.
- Seed-ul canonic `data/principles/principle-scanning-before-receive.json` este integrat și validat.
- Suita de teste automate `tests/test_volume_01.py` validează structura manifestului și a seed-ului.
- `npm run check`, `npm run build`, `python -m unittest discover tests` și toate validatoarele ies cu PASS (0 erori).

## 4. Domeniu și non-obiective

### În domeniu:
- Structurarea celor 5 capitole ale Volumului 1 (`CH-0101` la `CH-0105`).
- Matricea de pregătire a dovezilor (Evidence Readiness Matrix).
- Manifestul mașină-citibil `data/content/volumes/volume-01.json`.
- Șablonul de redactare `docs/content/CHAPTER_PRODUCTION_TEMPLATE.md`.
- Dosarul de reverificare a regulamentelor `research/dossiers/regulations-u11-recheck.md`.
- Seed-ul canonic de producție `data/principles/principle-scanning-before-receive.json`.
- Suita de teste `tests/test_volume_01.py`.

### Non-obiective:
- Redactarea tuturor celor 10 volume (programată secvențial).
- Generarea de zeci de taskuri noi de infrastructură.
- Construirea Tactical Visual Engine-ului (TASK-0303/0403).

## 5. Fișiere și module afectate

- `docs/content/VOLUME_01_ARCHITECTURE.md` (nou)
- `data/content/volumes/volume-01.json` (nou)
- `docs/content/CHAPTER_PRODUCTION_TEMPLATE.md` (nou)
- `research/dossiers/regulations-u11-recheck.md` (nou)
- `data/principles/principle-scanning-before-receive.json` (nou)
- `plans/TASK-0111-arhitectura-volum-01.md` (nou)
- `reports/task-reports/TASK-0111.md` (nou)
- `tests/test_volume_01.py` (nou)
- `scripts/generate_task_registry.py` (modificat)
- `TASK_REGISTRY.json` (modificat)
- `TASK_HISTORY.jsonl` (modificat)
- `PROJECT_STATUS.md` (modificat)

## 6. Pași de implementare

1. Crearea ExecPlan-ului `plans/TASK-0111-arhitectura-volum-01.md`.
2. Scrierea specificației de arhitectură `docs/content/VOLUME_01_ARCHITECTURE.md`.
3. Crearea manifestului JSON mașină-citibil `data/content/volumes/volume-01.json`.
4. Scrierea șablonului de redactare `docs/content/CHAPTER_PRODUCTION_TEMPLATE.md`.
5. Crearea dosarului de reverificare a regulamentelor `research/dossiers/regulations-u11-recheck.md`.
6. Crearea seed-ului canonic de producție `data/principles/principle-scanning-before-receive.json`.
7. Scrierea suitei de teste `tests/test_volume_01.py`.
8. Rularea verificărilor `npm run check`, `npm run build`, `python -m unittest discover tests` și a validatoarelor.
9. Generarea raportului de task `reports/task-reports/TASK-0111.md`.
10. Actualizarea registrelor de proiect și executarea commit-ului Git `feat(TASK-0111): define first canonical volume architecture`.

## 7. Validare și acceptare

- `npm run check` -> 0 erori.
- `npm run build` -> 8 static HTML pages în `dist/web/`.
- `python -m unittest discover tests` -> 145+ teste PASS.
- `python scripts/validate_project.py` -> 0 erori.
- `python scripts/validate_content.py` -> 0 erori.
- `python scripts/generate_task_registry.py --check` -> reproductibil.

## 8. Progres

- [x] 2026-08-09 13:30 — Creare ExecPlan `plans/TASK-0111-arhitectura-volum-01.md`.
- [ ] 2026-08-09 13:40 — Definitivare `VOLUME_01_ARCHITECTURE.md` și `volume-01.json`.
- [ ] 2026-08-09 13:50 — Scriere șablon capitole, dosar regulamente și seed canonic.
- [ ] 2026-08-09 14:05 — Validare build, check, teste pozitive și commit Git.

## 9. Retrospectivă

Structurarea Volumului 1 oferă blueprint-ul metodologic necesar începerii redactării de conținut pedagogic real.
