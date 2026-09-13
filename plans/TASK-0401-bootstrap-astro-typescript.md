# ExecPlan — TASK-0401: Fundația arhitecturii site-ului Astro și TypeScript strict

**Task ID:** TASK-0401  
**Titlu:** Fundația arhitecturii site-ului Astro și TypeScript strict  
**Fază:** PHASE-04 — Implementare platformă web  
**Stare:** IN_PROGRESS  
**Prioritate:** CRITICAL  
**Pondere:** 0.389%  
**Data:** 2026-08-09  

---

## 1. Titlu și scop

Construirea fundației tehnice executabile, strict tipate și reproductibile pentru platforma web pedagogică ManualFC, utilizând Astro, TypeScript strict, MDX, CSS bazat pe jetoane vizuale (visual tokens) și un model de conectare cu datele canonice existente.

## 2. Context pentru un cititor nou

- Proiectul ManualFC s-a reorientat în `TASK-0003` și `TASK-0004` de la o redactare pur documentară către o aplicație web pedagogică statică.
- Sursa de adevăr pentru date și reguli rămâne în `schemas/`, `config/`, `data/` și `research/`.
- `AGENTS.md` impune ca antrenorul să fie format întâi ca pedagog și apoi ca antrenor.
- Stack-ul stabilit prin deciziile tehnice (`DEC-0004`, `DEC-0019`) este Astro static cu insule TypeScript, MDX pentru conținut pedagogic, CSS vanilla token-driven și suport offline/accessibility.

## 3. Rezultatul verificabil

- Aplicația web Astro este inițializată în repository sub `app/` cu fișierele de configurare la rădăcină (`package.json`, `astro.config.mjs`, `tsconfig.json`).
- Comanda `npm run check` (Astro check) și `npm run build` rulează cu succes (Exit Code 0), generând buildul static sub `dist/`.
- TypeScript este configurat în modul strict (`strict: true`, `noImplicitAny: true`, `strictNullChecks: true`).
- Paginile `/`, `/incepe-aici`, `/404` și o pagină de fixture MDX funcționează și folosesc un layout comun accesibil (`BaseLayout.astro`) și un shell de navigare responsive.
- Jetoanele vizuale din `config/visual-tokens.json` sunt cartografiate în variabile CSS (`styles/tokens.css`).
- Toate cele 114+ teste Python existente continuă să treacă (`OK`), iar registrul de taskuri rămâne reproductibil.

## 4. Domeniu și non-obiective

### În domeniu:
- Integrarea package managerului `npm` și generarea `package-lock.json`.
- Instalarea și configurarea `@astrojs/mdx` și TypeScript strict.
- Structurarea directorului `app/src/` (components, layouts, pages, styles, content, lib, types).
- Crearea shell-ului de aplicație, a paginilor inițiale și a fallback-ului 404.
- Crearea unui bridge minimal între JSON schemas/data și Astro Content Collections.
- Adăugarea suitei de teste unitare web în Python/Node.

### Non-obiective:
- Construirea Tactical Visual Engine-ului (programat pentru TASK-0303/TASK-0403).
- Implementarea motorului de animații sau a Playwright harness-ului complet (TASK-0404, TASK-0407).
- Redactarea conținutului pedagogic extins (prevăzută în volumele ulterioare).
- Adăugarea de framework-uri UI grele (React, Vue, Tailwind).

## 5. Fișiere și module afectate

- `package.json` (nou)
- `package-lock.json` (nou)
- `astro.config.mjs` (nou)
- `tsconfig.json` (nou)
- `app/src/` (directoare noi: `components/`, `layouts/`, `pages/`, `styles/`, `content/`, `lib/`, `types/`)
- `plans/TASK-0401-bootstrap-astro-typescript.md` (nou)
- `reports/task-reports/TASK-0401.md` (nou)
- `tests/test_web_bootstrap.py` (nou)
- `scripts/generate_task_registry.py` (modificat)
- `TASK_REGISTRY.json` (modificat)
- `TASK_HISTORY.jsonl` (modificat)
- `PROJECT_STATUS.md` (modificat)

## 6. Cercetare necesară

- Verificarea compatibilității oricărui pachet instalat cu Node v24.17.0 și npm 11.13.0.
- Asigurarea că exportul static din `astro.config.mjs` nu interferează cu validatorul Python sau cu directoarele `schemas/` și `data/`.

## 7. Model pedagogic

Fundația web susține cele două intrări pedagogice majore definite în `PRODUCT_REQUIREMENTS.md`:
1. **„Vreau să învăț”** — parcursul editorial de la copil și pedagogie la tactică, planificare și safeguarding.
2. **„Am nevoie de o soluție acum”** — rezolvarea rapidă pe teren (simptom → cauze → obiectiv → mesaj → exerciții).

## 8. Design vizual și interactiv

- `styles/tokens.css`: Variabile CSS pentru culorile rolurilor (possession: `#1769AA`, opponent: `#C62828`, neutral: `#F9A825`, goalkeeper: `#2E7D32`, coach: `#FFFFFF`), tipografie, spațieri, raze de colț și contrast înalt.
- Accesibilitate: `skip-to-content`, `focus-visible`, `lang="ro"`, semantic landmark elements (`<header>`, `<nav>`, `<main>`, `<footer>`), `prefers-reduced-motion`.

## 9. Pași de implementare

1. Crearea fișierelor de configurare `package.json`, `astro.config.mjs`, `tsconfig.json`.
2. Rularea `npm install` pentru instalarea Astro și `@astrojs/mdx`.
3. Structurarea `app/src/` și adăugarea token-urilor CSS în `styles/tokens.css` și `styles/global.css`.
4. Crearea `BaseLayout.astro`, `AppHeader.astro`, `AppFooter.astro`, `CoachMessage.astro`, `Breadcrumb.astro`.
5. Implementarea paginilor `pages/index.astro`, `pages/incepe-aici.astro`, `pages/404.astro` și fixture-ului MDX `pages/fixture-mdx.mdx`.
6. Implementarea modului strict TypeScript și a lib-ului `app/src/lib/content-bridge.ts`.
7. Adăugarea scripturilor `dev`, `build`, `preview`, `check` și executarea build-ului.
8. Crearea suitei de teste `tests/test_web_bootstrap.py` și verificarea prin `python -m unittest discover tests`.
9. Rularea tuturor validatoarelor proiectului (`validate_project.py`, `validate_content.py`, `generate_task_registry.py --check`).
10. Generarea raportului de task `reports/task-reports/TASK-0401.md`.
11. Actualizarea registrelor de proiect și executarea commit-ului Git `feat(TASK-0401): bootstrap Astro static site architecture with strict TypeScript and MDX`.

## 10. Validare și acceptare

- `npm run check` -> 0 erori TypeScript/Astro.
- `npm run build` -> build static generat cu succes în `dist/`.
- `python -m unittest discover tests` -> 114+ teste PASS (inclusiv testele web noi).
- `python scripts/validate_project.py` -> 0 erori.
- `python scripts/validate_content.py` -> 0 erori.
- `python scripts/generate_task_registry.py --check` -> reproductibil.

## 11. Progres

- [x] 2026-08-09 12:30 — Creare ExecPlan `plans/TASK-0401-bootstrap-astro-typescript.md`.
- [ ] 2026-08-09 12:35 — Inițializare `package.json`, Astro și `@astrojs/mdx`.
- [ ] 2026-08-09 12:45 — Creare structură `app/src/`, layouts, pagini și componente CSS token-driven.
- [ ] 2026-08-09 12:55 — Validare build static, verificări TypeScript strict și teste unitare web.
- [ ] 2026-08-09 13:05 — Actualizare registre de proiect și commit Git.

## 12. Descoperiri și surprize

- Integrările statice Astro permit generarea curată de cod HTML fără hidratare client JS pentru pagini pur editoriale.
- Structurarea sub `app/src` izolează logic codul aplicației web în timp ce păstrează schemele și datele canonice la nivel de rădăcină.

## 13. Jurnal de decizii

- **Decizie:** Utilizarea `npm` ca package manager unic cu `package-lock.json`.
- **Motiv:** Este instrumentul disponibil nativ în mediul local de executare (Node v24.17.0, npm 11.13.0).
- **Data:** 2026-08-09.

## 14. Rezultat și retrospectivă

Fundația Astro oferă sprijinul tehnic necesar pentru construirea design system-ului web (`TASK-0302`) și a taxonomiei de conținut (`TASK-0201`).
