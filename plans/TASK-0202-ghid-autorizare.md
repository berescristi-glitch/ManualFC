# ExecPlan — TASK-0202: Ghidul Metodologic și Protocolul Operațional de Autorizare

**Task ID:** TASK-0202  
**Titlu:** Ghidul metodologic pentru redactarea capitolelor  
**Fază:** PHASE-02 — Taxonomie, ontologie și arhitectură de conținut  
**Stare:** IN_PROGRESS  
**Prioritate:** CRITICAL  
**Pondere:** 0.389%  
**Data:** 2026-08-09  

---

## 1. Titlu și scop

Executarea versiunii minimale operaționale a **TASK-0202** prin crearea protocolului de autorizare și QA în 10 pași (`docs/guidelines/CHAPTER_AUTHORING_GUIDE.md`). Redundanța a fost auditată ca fiind `PARTIAL` (peste 80% din conceptele pedagogice și tehnice fiind deja acoperite de `CHAPTER_PRODUCTION_TEMPLATE.md` și `VOLUME_01_ARCHITECTURE.md`).

## 2. Context pentru un cititor nou

- Auditul Phase Gate a arătat că filosofia, taxonomia și modelul de tipizare există deja.
- TASK-0202 este redus la un singur artefact operațional concis: `docs/guidelines/CHAPTER_AUTHORING_GUIDE.md` (`CANONICAL_AUTHORING_AND_QA_PROTOCOL`).
- După finalizarea TASK-0202, proiectul intră în faza **CANONICAL CONTENT PRODUCTION**, iar task-ul `TASK-0501` (`Capitol — Profilul variabil al copilului de 10–11 ani`) devine `READY`.

## 3. Rezultatul verificabil

- `docs/guidelines/CHAPTER_AUTHORING_GUIDE.md` creat.
- `reports/task-reports/TASK-0202.md` creat.
- `npm run check`, `npm run build`, `python -m unittest discover tests` și toate validatoarele ies cu PASS (0 erori).
- Registrul de taskuri actualizat (`TASK-0202` -> `DONE`, `TASK-0501` -> `READY`).

## 4. Pași de implementare

1. Crearea ExecPlan-ului `plans/TASK-0202-ghid-autorizare.md`.
2. Crearea ghidului operațional `docs/guidelines/CHAPTER_AUTHORING_GUIDE.md`.
3. Rularea verificărilor `npm run check`, `npm run build`, `python -m unittest discover tests` și a validatoarelor.
4. Generarea raportului de task `reports/task-reports/TASK-0202.md`.
5. Actualizarea registrelor de proiect și executarea commit-ului Git `feat(TASK-0202): define canonical authoring and QA protocol`.
