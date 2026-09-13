# ExecPlan — TASK-0004: Integrarea ManualFC cu control plane-ul autonom existent

**Task ID:** TASK-0004  
**Titlu:** Integrarea ManualFC cu control plane-ul autonom existent și aplicarea plafonului strict de automatizare  
**Fază:** PHASE-00  
**Stare:** IN_PROGRESS  
**Prioritate:** CRITICAL  
**Pondere:** 0.519%  
**Data:** 2026-08-09  

---

## 1. Titlu și scop

Integrarea proiectului ManualFC cu infrastructura de control plane externă, validarea mecanicilor de selecție a taskurilor `READY` din `TASK_REGISTRY.json` și aplicarea regulii strategice **HARD AUTOMATION BUDGET** (maximum 2 intervenții/taskuri de automatizare permise, cu trecere directă la produsul `TASK-0401` la un gap `NONE` sau `SMALL_ADAPTER`).

## 2. Context pentru un cititor nou

- Proiectul ManualFC a efectuat pivotul strategic în `TASK-0003` către o platformă web pedagogică bazată pe Astro și TypeScript.
- Sursa de adevăr pentru starea și ordinea taskurilor este `TASK_REGISTRY.json`.
- `AGENTS.md` stabilește că antrenorul-pedagog este format mai întâi ca pedagog, iar produsul principal este platforma web.
- Control plane-ul este infrastructură auxiliară; extinderea sa nelimitată este oprită prin decizia strategică Hard Automation Budget.
- TASK-0004 este prima din cele maximum două intervenții de automatizare permise.

## 3. Rezultatul verificabil

- Fișiere produse:
  - `docs/architecture/EXTERNAL_CONTROL_PLANE_INTEGRATION.md`
  - `scripts/control_plane_integration.py`
  - `tests/test_control_plane_integration.py`
  - `reports/task-reports/TASK-0004.md`
- Toate testele automate din `tests/test_control_plane_integration.py` și `python -m unittest discover tests` trec cu `OK`.
- Scriptul `python scripts/validate_project.py` indică 0 erori.
- Taskul `TASK-0004` devine `DONE`, iar `TASK-0401` devine `READY`.

## 4. Domeniu și non-obiective

### În domeniu:
- Definirea contractului tehnic de integrare cu control plane-ul extern.
- Implementarea scriptului Python de integrare, audit și gating (`scripts/control_plane_integration.py`).
- Implementarea suitei de teste dedicate (`tests/test_control_plane_integration.py`).
- Aplicarea politicii Hard Automation Budget (evaluare Gate: `NONE` -> trecere la produs).
- Actualizarea registrelor de proiect (`TASK_REGISTRY.json`, `TASK_HISTORY.jsonl`, `PROJECT_STATUS.md`, `DECISIONS.md`).

### Non-obiective:
- Construirea unui orchestrator autonom intern complex în interiorul ManualFC.
- Modificarea mecanicilor de rulare a LLM/Codex sau extinderea permisiunilor de executare.
- Amânarea taskului de produs `TASK-0401`.

## 5. Fișiere și module afectate

- `plans/TASK-0004-integrare-control-plane.md` (nou)
- `docs/architecture/EXTERNAL_CONTROL_PLANE_INTEGRATION.md` (nou)
- `scripts/control_plane_integration.py` (nou)
- `tests/test_control_plane_integration.py` (nou)
- `reports/task-reports/TASK-0004.md` (nou)
- `TASK_REGISTRY.json` (modificat)
- `TASK_HISTORY.jsonl` (modificat)
- `PROJECT_STATUS.md` (modificat)
- `DECISIONS.md` (modificat)

## 6. Cercetare necesară

- Verificarea structurii `TASK_REGISTRY.json` și a mecanicilor de selecție a taskurilor în starea `READY`.
- Confirmarea că dependențele pentru `TASK-0004` sunt îndeplinite (`TASK-0003` are starea `DONE`).
- Verificarea politicii `HARD AUTOMATION BUDGET` din instrucțiunile primite.

## 7. Model pedagogic

Nu se aplică direct pentru acest task de infrastructură, însă taskul respectă principiul fundamental: infrastructura este auxiliară, iar valoarea pedagogică rezidă în dezvoltarea rapidă și sigură a aplicației de produs (`TASK-0401`).

## 8. Design vizual și interactiv

Nu se aplică direct UI pentru TASK-0004; interfața va fi realizată începând cu TASK-0401 (Bootstrap Astro).

## 9. Pași de implementare

1. Crearea ExecPlan-ului `plans/TASK-0004-integrare-control-plane.md`.
2. Scrierea specificației tehnice `docs/architecture/EXTERNAL_CONTROL_PLANE_INTEGRATION.md`.
3. Implementarea modulelor Python în `scripts/control_plane_integration.py`.
4. Crearea suitei de testare în `tests/test_control_plane_integration.py`.
5. Rularea verificărilor automate (`unittest` și `validate_project.py`).
6. Generarea raportului oficial `reports/task-reports/TASK-0004.md`.
7. Actualizarea registrelor `TASK_REGISTRY.json`, `TASK_HISTORY.jsonl`, `PROJECT_STATUS.md` și `DECISIONS.md`.

## 10. Validare și acceptare

- `python scripts/control_plane_integration.py --check` -> exit code 0.
- `python -m unittest tests/test_control_plane_integration.py` -> 15+ teste PASS.
- `python scripts/validate_project.py` -> 0 erori.
- `python scripts/validate_content.py` -> 0 erori.

## 11. Progres

- [x] 2026-08-09 12:15 — Creare ExecPlan `plans/TASK-0004-integrare-control-plane.md`.
- [ ] 2026-08-09 12:18 — Implementare `EXTERNAL_CONTROL_PLANE_INTEGRATION.md`.
- [ ] 2026-08-09 12:20 — Implementare `scripts/control_plane_integration.py`.
- [ ] 2026-08-09 12:22 — Implementare `tests/test_control_plane_integration.py`.
- [ ] 2026-08-09 12:25 — Validare și generare raport `TASK-0004.md`.
- [ ] 2026-08-09 12:30 — Actualizare registre de proiect și marcare `DONE`.

## 12. Descoperiri și surprize

- Integrarea cu un control plane extern poate fi complet realizată printr-un contract clar bazat pe `TASK_REGISTRY.json` și pe validatoare de stare.
- Gap-ul de automatizare identificat este `NONE`: control plane-ul extern / agentic funcționează deja ca task selector, auditor, validator și approval gate.

## 13. Jurnal de decizii

- **Decizie:** Implementarea integrării ca adaptor pasiv fail-closed fără loop autonom intern.
- **Motiv:** Se previne duplicarea infrastructurii și se respectă directiva Hard Automation Budget.
- **Data:** 2026-08-09.

## 14. Rezultat și retrospectivă

Taskul securizează arhitectura de integrare a proiectului ManualFC și deschide calea directă pentru începerea lucrului la platforma web prin `TASK-0401`.
