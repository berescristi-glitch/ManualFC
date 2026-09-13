# TASK-3601–TASK-3604 — Master Integrity & Adversarial Product Audit

## 1. Titlu și scop

Auditarea ostilă a produsului ManualFC, repararea defectelor validate și retestarea până la zero probleme Critical/Major sau până la un blocker real documentat.

## 2. Context

HEAD inițial: `0466ea9b684eff787cd2caea7ee5c76bf01cfbf2`. Baseline runtime verificat: `1404fb980505c9f3d2751dc44827dbe13c5fa1a9`. Auditul pornește după `TASK-3508`. Worktree-ul conține numeroase capturi și artefacte Playwright neversionate, păstrate fără modificare.

## 3. Rezultat verificabil

Cele șase rapoarte cerute, trei registre vii, issue snapshot pre-repair, build și validări reproductibile, journeys reale în browser și verdict final bazat pe dovezi.

## 4. Domeniu și non-obiective

Intră integritatea tehnică, de date, semantică, pedagogică, UX, accesibilitate, offline, stare, privacy și safeguarding. Nu intră funcții noi, validare umană sau de teren inventată, promovare Production ori refaceri arhitecturale fără defect demonstrat.

## 5. Fișiere și module afectate

`reports/audits/MANUALFC_*INTEGRITY*`, registrele de guvernanță și numai fișierele runtime/date strict necesare problemelor validate.

## 6. Cercetare necesară

Se verifică registrele locale și sursele deja arhivate. Orice afirmație actualizabilă care necesită internet se marchează neconfirmată dacă accesul lipsește.

## 7. Model pedagogic

Auditul separă percepția, decizia, execuția și rezultatul; urmărește lanțul Pedagogul → Antrenorul → Practica și protejează autonomia, demnitatea și dreptul copilului de a greși.

## 8. Design vizual și interactiv

Rutele critice se verifică la 1440, 1280, 768 și 390 px; 320 px este stress-test. Se verifică diagramă, legendă, reflow, tastatură, reduced motion și fallback static.

## 9. Pași de implementare

1. Forensics read-only. 2. Journeys/chaos. 3. Semantic/evidence audit. 4. Freeze issue snapshot. 5. Reparații în ordinea severității. 6. Retest și reaudit. 7. Preview structural/browser dacă accesul permite.

## 10. Validare și acceptare

`validate_project.py`, `validate_content.py --strict`, `validate_gold_standard_v2.py`, `pytest`, testele Node, Astro check/build, route crawl, Axe/tastatură/reflow/offline/state și `git diff --check`.

## 11. Progres

- [x] 2026-08-31: guvernanță și baseline recuperate.
- [x] 2026-08-31: integritatea fișierelor versionate și validatoarele canonice verificate.
- [x] Stage 1 complet.
- [x] Stage 2 complet.
- [x] Stage 3 complet și snapshot înghețat.
- [x] Stage 4 și acceptarea finală complete.

## 12. Descoperiri și surprize

- `node_modules` conține directoare ilizibile; Astro check/build eșuează la încărcarea modulelor cu `Unexpected token '|'`.
- `npm test` declară 0 teste, deși comanda iese cu cod 0.
- pytest trece 505 teste, dar nu poate scrie cache-ul din cauza stării anormale a `.pytest_cache`.

## 13. Jurnal de decizii

- 2026-08-31: artefactele neversionate preexistente nu sunt șterse sau adoptate.
- 2026-08-31: build-ul blocat nu este reparat înainte de freeze; auditul semantic continuă pe surse.

## 14. Rezultat și retrospectivă

Finalizat cu verdict `PASS_WITH_NON_BLOCKING_DECLARED_LIMITATIONS`. Zero CRITICAL/MAJOR cunoscute după retest; Firefox/WebKit, npm advisory audit și validarea umană rămân explicit neexecutate.
