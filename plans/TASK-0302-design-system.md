# ExecPlan — TASK-0302: Design System Web, Editorial, Print și Accesibilitate

**Task ID:** TASK-0302  
**Titlu:** Design system web, editorial, print și accesibilitate  
**Fază:** PHASE-03 — Design system vizual, editorial și tehnic  
**Stare:** IN_PROGRESS  
**Prioritate:** CRITICAL  
**Pondere:** 0.389%  
**Data:** 2026-08-09  

---

## 1. Titlu și scop

Construirea și maturizarea sistemului de design vizual, editorial, de accesibilitate și de printabilitate al platformei **ManualFC**, asigurând suportul pentru cele două moduri de utilizare: **Mode A („Vreau să învăț”)** și **Mode B („Am nevoie acum”)**.

## 2. Context pentru un cititor nou

- Proiectul ManualFC a integrat în `TASK-0401` fundația tehnologică web Astro + TypeScript strict + MDX.
- `AGENTS.md` impune ca antrenorul să fie format întâi ca pedagog și apoi ca antrenor, iar produsele derivate să fie lizibile pe mobil, desktop și la tipar.
- Sursa de adevăr pentru rolurile vizuale este `config/visual-tokens.json`.
- Taskul creează biblioteca de componente reutilizabile și stilurile fără a adăuga framework-uri UI externe (React, Vue, Tailwind).

## 3. Rezultatul verificabil

- Fișierele de tokens și stiluri (`app/src/styles/tokens.css`, `app/src/styles/global.css`, `app/src/styles/print.css`) extind sistemul vizual cu culori semantice, ierarhie tipografică, spațieri, lățimi de prose/wide și reguli de printare alb-negru.
- Biblioteca de componente conține componente pedagogice (`CoachMessage.astro`, `ChildMessage.astro`, `WhyThisMatters.astro`, `ObserveThis.astro`, `DecisionToLearn.astro`, `CommonMistake.astro`, `PhraseToAvoid.astro`, `UnderstandingCheck.astro`, `Adaptation.astro`, `MatchTransfer.astro`), de evidență epistemice (`EvidenceBadge.astro`, `EvidenceNote.astro`, `SourceReference.astro`) și de structură (`ModeCard.astro`, `Callout.astro`, `Card.astro`, `PageHeader.astro`, `SectionHeader.astro`).
- Sunt implementate cele două pattern-uri majore: `QuickModePattern.astro` („Am nevoie acum”) și `DeepLearningPattern.astro` („Vreau să învăț”).
- Ruta tehnică internă `/design-system` marchează și demonstrează toate componentele în mod izolat.
- Paginile `/` și `/incepe-aici` sunt rafinate cu noul design system.
- `npm run check`, `npm run build`, `python -m unittest discover tests` și validatoarele de proiect ies cu starea PASS (0 erori).

## 4. Domeniu și non-obiective

### În domeniu:
- Extinderea jetoanelor vizuale în `app/src/styles/tokens.css`.
- Crearea stilului de print `@media print` în `app/src/styles/print.css`.
- Crearea componentelor fundamentale, pedagogice și epistemice.
- Construirea pattern-urilor de conținut Mode A și Mode B.
- Crearea rutei interne `/design-system`.
- Suita de teste automate `tests/test_design_system.py`.

### Non-obiective:
- Construirea Tactical Visual Engine-ului sau a animațiilor (TASK-0303, TASK-0403, TASK-0404).
- Căutarea integrată Pagefind (TASK-0405).
- Suita Playwright (TASK-0407).
- Instalarea de librării UI terțe.

## 5. Fișiere și module afectate

- `app/src/styles/tokens.css` (modificat/extins)
- `app/src/styles/global.css` (modificat/extins)
- `app/src/styles/print.css` (nou)
- `app/src/components/` (componente noi: `PageHeader.astro`, `SectionHeader.astro`, `ContentContainer.astro`, `ModeCard.astro`, `Callout.astro`, `Card.astro`, `Badge.astro`, `ChildMessage.astro`, `WhyThisMatters.astro`, `ObserveThis.astro`, `DecisionToLearn.astro`, `CommonMistake.astro`, `PhraseToAvoid.astro`, `UnderstandingCheck.astro`, `Adaptation.astro`, `MatchTransfer.astro`, `EvidenceBadge.astro`, `EvidenceNote.astro`, `SourceReference.astro`, `QuickModePattern.astro`, `DeepLearningPattern.astro`; componentă modificată: `CoachMessage.astro`)
- `app/src/pages/design-system.astro` (nou)
- `app/src/pages/index.astro` (modificat)
- `app/src/pages/incepe-aici.astro` (modificat)
- `plans/TASK-0302-design-system.md` (nou)
- `reports/task-reports/TASK-0302.md` (nou)
- `tests/test_design_system.py` (nou)
- `TASK_REGISTRY.json` (modificat)
- `TASK_HISTORY.jsonl` (modificat)
- `PROJECT_STATUS.md` (modificat)

## 6. Cercetare necesară

- Verificarea terminologiei canonice pentru etichetele epistemice în `research/taxonomy.json` / `research/claims.json` (Evidență Puternică, Moderată, Limitată, Practică de Academie, Inferență, Neconfirmat).

## 7. Model pedagogic

Sistemul de design servește direct contractului în 18 puncte din `PEDAGOGICAL_PRODUCT_PRINCIPLES.md`, separând vizual și conceptual formularea transmisă copilului de explicația tehnică adresată antrenorului și de nivelul de dovadă științifică.

## 8. Design vizual și interactiv

- **Mode A („Vreau să învăț”):** Tipografie lejeră, lățime optimă de citire (`68ch`), contrast înalt, casete distincte de dovadă și note de subsol.
- **Mode B („Am nevoie acum”):** Scanare rapidă pe telefon, culori de avertisment/acțiune, carduri compacte, fără elemente ascunse în hover.
- **Print System:** CSS dedicat pentru eliminarea header/footer-ului de navigare, alb-negru curat, spargere controlată a paginilor (`break-inside: avoid`).

## 9. Pași de implementare

1. Crearea ExecPlan-ului `plans/TASK-0302-design-system.md`.
2. Extinderea `app/src/styles/tokens.css` și `app/src/styles/global.css`.
3. Crearea stylesheet-ului de print `app/src/styles/print.css`.
4. Crearea componentelor de bază, pedagogice și epistemice sub `app/src/components/`.
5. Crearea pattern-urilor `QuickModePattern.astro` și `DeepLearningPattern.astro`.
6. Construirea paginii de laborator vizual `/design-system`.
7. Refacerea paginilor `/` și `/incepe-aici` cu noile componente.
8. Crearea suitei de teste `tests/test_design_system.py`.
9. Rularea verificărilor `npm run check`, `npm run build`, `python -m unittest discover tests` și a validatoarelor de proiect.
10. Generarea raportului de task `reports/task-reports/TASK-0302.md`.
11. Actualizarea registrelor de proiect și executarea commit-ului Git `feat(TASK-0302): establish ManualFC design system`.

## 10. Validare și acceptare

- `npm run check` -> 0 erori (14+ fișiere Astro).
- `npm run build` -> 5+ pagini statice HTML generate în `dist/web/`.
- `python -m unittest discover tests` -> 125+ teste PASS.
- `python scripts/validate_project.py` -> 0 erori.
- `python scripts/validate_content.py` -> 0 erori.
- `python scripts/generate_task_registry.py --check` -> reproductibil.

## 11. Progres

- [x] 2026-08-09 12:45 — Creare ExecPlan `plans/TASK-0302-design-system.md`.
- [ ] 2026-08-09 12:55 — Extindere design tokens 2.0 și print CSS.
- [ ] 2026-08-09 13:10 — Creare componente pedagogice și epistemice.
- [ ] 2026-08-09 13:25 — Construire pattern-uri Mode A / Mode B și pagină `/design-system`.
- [ ] 2026-08-09 13:40 — Validare build, check, teste unitare și commit Git.

## 12. Descoperiri și surprize

- Separarea clară între „Mesaj copil” și „Sens antrenor” elimină confuzia metodologică pe teren.
- Design-ul token-driven permite menținerea lizibilității ridicate fără biblioteci externe de UI.

## 13. Jurnal de decizii

- **Decizie:** Neutilizarea niciunui framework CSS terț (Tailwind/Bootstrap).
- **Motiv:** Păstrarea unei suprafețe minime de dependențe și control absolut asupra layout-ului și performanței.
- **Data:** 2026-08-09.

## 14. Rezultat și retrospectivă

Sistemul de design creat pregătește baza vizuală și editorială pentru aplicarea taxonomiei de conținut (`TASK-0201`) și dezvoltarea Tactical Visual Engine (`TASK-0303`).
