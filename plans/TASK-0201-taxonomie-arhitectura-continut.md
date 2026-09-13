# ExecPlan — TASK-0201: Taxonomie și Arhitectură Canonică pentru Conținut și Pagini

**Task ID:** TASK-0201  
**Titlu:** Taxonomie și arhitectură pentru conținut și pagini  
**Fază:** PHASE-02 — Taxonomie de conținut și arhitectură de pagini  
**Stare:** IN_PROGRESS  
**Prioritate:** CRITICAL  
**Pondere:** 0.389%  
**Data:** 2026-08-09  

---

## 1. Titlu și scop

Construirea taxonomiei canonice executabile, a contractelor de ID/slug, a modelului relațional (Knowledge Graph Light static-first) și a arhitecturii de rute web pentru platforma **ManualFC**, deservind integrat ambele moduri: **Mode A („Vreau să învăț”)** și **Mode B („Am nevoie acum”)**.

## 2. Context pentru un cititor nou

- Proiectul ManualFC dispune de fundația web Astro + TypeScript strict (`TASK-0401`) și de sistemul de design vizual/editorial/print (`TASK-0302`).
- Sursa de adevăr pentru regulile de validare a datelor este în `schemas/` (Draft 2020-12) și validatorul `scripts/validate_content.py`.
- `INFORMATION_ARCHITECTURE.md` stabilește cele 16 arii de conținut majore și separarea celor două moduri de utilizare.
- Taskul definește registrul mașină-citibil al taxonomiei (`data/taxonomy/registry.json`), extinde Content Collections și Content Bridge, adaugă fixture-uri neutre minimale și livrează rutele dinamice de probă (`/principii/[slug]`, `/exercitii/[slug]`, `/probleme/[slug]`).

## 3. Rezultatul verificabil

- Registrul canonic de taxonomie există în `data/taxonomy/registry.json` și este validat.
- Contractul de ID (`type_prefix.canonical-slug`) și de slug (`kebab-case-romanian`) este definit și aplicat.
- Modulul `app/src/lib/content-bridge.ts` rezolvă relațiile între `Problem`, `Principle`, `Exercise`, `CoachMessage`, `ChildMessage`, `Evidence` și `Source` în mod static și fail-closed.
- Sunt livrate rutele dinamice demonstrative:
  - `/principii/[slug]` -> utilizează `DeepLearningPattern.astro`
  - `/probleme/[slug]` -> utilizează `QuickModePattern.astro`
  - `/exercitii/[slug]` -> utilizează layout-ul de exercițiu
- `npm run check`, `npm run build`, `python -m unittest discover tests` și validatoarele de proiect ies cu starea PASS (0 erori).

## 4. Domeniu și non-obiective

### În domeniu:
- Definitivarea registrului mașină-citibil `data/taxonomy/registry.json`.
- Definirea clasificării entităților (Primary, Supporting, Research, Visual, System).
- Construirea modelului de rezolvare a relațiilor în `app/src/lib/content-bridge.ts`.
- Extinderea `app/src/content.config.ts` cu colecțiile `principii`, `exercitii`, `probleme`.
- Adăugarea fixture-urilor neutre minimale sub `data/fixtures/`.
- Construirea rutelor dinamice demonstrative sub `app/src/pages/`.
- Suita de teste automate `tests/test_taxonomy.py`.

### Non-obiective:
- Crearea de baze de date de tip Graph (Neo4j, Vector DB).
- Redactarea conținutului pedagogic integral (programată în volumele ulterioare).
- Construirea Tactical Visual Engine-ului sau a animațiilor (TASK-0303, TASK-0403, TASK-0404).

## 5. Fișiere și module afectate

- `data/taxonomy/registry.json` (nou)
- `docs/architecture/CONTENT_TAXONOMY.md` (nou)
- `data/fixtures/principles.json` (nou)
- `data/fixtures/exercises.json` (nou)
- `data/fixtures/problems.json` (nou)
- `app/src/content.config.ts` (modificat/extins)
- `app/src/lib/content-bridge.ts` (modificat/extins)
- `app/src/pages/principii/[slug].astro` (nou)
- `app/src/pages/exercitii/[slug].astro` (nou)
- `app/src/pages/probleme/[slug].astro` (nou)
- `plans/TASK-0201-taxonomie-arhitectura-continut.md` (nou)
- `reports/task-reports/TASK-0201.md` (nou)
- `tests/test_taxonomy.py` (nou)
- `scripts/generate_task_registry.py` (modificat)
- `TASK_REGISTRY.json` (modificat)
- `TASK_HISTORY.jsonl` (modificat)
- `PROJECT_STATUS.md` (modificat)

## 6. Cercetare necesară

- Verificarea alinierii registrului de taxonomie cu categoriile stabilite în `INFORMATION_ARCHITECTURE.md` și cu taxonomia din `config/research-taxonomy.json`.

## 7. Model pedagogic

Taxonomia leagă direct problema de joc observată pe teren de simptom, cauze, mesajul transmis copilului, explicația pentru antrenor, exercițiul de corecție și verificarea transferului în meci, susținând contractul pedagogic în 18 puncte.

## 8. Design vizual și interactiv

- **Mode A (Principii/Concepte):** Pagini generate prin `DeepLearningPattern.astro`, cu opțiune de aprofundare pedagogică.
- **Mode B (Probleme Teren):** Pagini generate prin `QuickModePattern.astro`, cu organizare pe pasi de acțiune rapidă pe teren.

## 9. Pași de implementare

1. Crearea ExecPlan-ului `plans/TASK-0201-taxonomie-arhitectura-continut.md`.
2. Definirea specificației `docs/architecture/CONTENT_TAXONOMY.md`.
3. Crearea registrului mașină-citibil `data/taxonomy/registry.json`.
4. Crearea fixture-urilor neutre `data/fixtures/principles.json`, `data/fixtures/exercises.json`, `data/fixtures/problems.json`.
5. Extinderea `app/src/content.config.ts` cu colecțiile de conținut.
6. Extinderea `app/src/lib/content-bridge.ts` cu funcțiile de rezolvare a relațiilor.
7. Construirea paginilor dinamice `/principii/[slug].astro`, `/exercitii/[slug].astro`, `/probleme/[slug].astro`.
8. Implementarea suitei de teste `tests/test_taxonomy.py`.
9. Rularea verificărilor `npm run check`, `npm run build`, `python -m unittest discover tests` și a validatoarelor de proiect.
10. Generarea raportului de task `reports/task-reports/TASK-0201.md`.
11. Actualizarea registrelor de proiect și executarea commit-ului Git `feat(TASK-0201): establish canonical content taxonomy`.

## 10. Validare și acceptare

- `npm run check` -> 0 erori.
- `npm run build` -> 8+ pagini statice HTML generate în `dist/web/` (inclusiv rutele dinamice de probă).
- `python -m unittest discover tests` -> 135+ teste PASS.
- `python scripts/validate_project.py` -> 0 erori.
- `python scripts/validate_content.py` -> 0 erori.
- `python scripts/generate_task_registry.py --check` -> reproductibil.

## 11. Progres

- [x] 2026-08-09 13:05 — Creare ExecPlan `plans/TASK-0201-taxonomie-arhitectura-continut.md`.
- [ ] 2026-08-09 13:15 — Definire `CONTENT_TAXONOMY.md` și `data/taxonomy/registry.json`.
- [ ] 2026-08-09 13:30 — Creare fixture-uri neutre și extindere Content Bridge.
- [ ] 2026-08-09 13:45 — Construire rute dinamice `/principii/[slug]`, `/exercitii/[slug]`, `/probleme/[slug]`.
- [ ] 2026-08-09 14:00 — Validare build, check, teste unitare și commit Git.

## 12. Descoperiri și surprize

- Rezolvarea statică a relațiilor pe bază de ID-uri în `content-bridge.ts` oferă viteză maximă de build și elimină dependențele runtime complexe.
- Separarea clară între `id` (`principle.scanning-before-receive`) și `slug` (`orientare-corporala-scanare`) asigură stabilitatea ID-urilor indiferent de modificările de titlu.

## 13. Jurnal de decizii

- **Decizie:** Utilizarea unui registru JSON simplu pentru Knowledge Graph Light static-first în loc de baze de date cu grafuri sau Neo4j.
- **Motiv:** Păstrarea livrabilului ca aplicație web statică pură, offline-friendly.
- **Data:** 2026-08-09.

## 14. Rezultat și retrospectivă

Taxonomia canonică creată oferă infrastructura de date necesară pentru generarea sistemului tipizat de conținut și relații (`TASK-0402`).
