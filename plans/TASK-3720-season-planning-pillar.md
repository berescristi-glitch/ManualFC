# TASK-3720 — Pilonul de planificare de sezon

## 1. Titlu și scop

Rezultatul observabil: al patrulea sistem canonic de conținut ManualFC (după cele două teme și pilonul de scripturi) — un set de 4 trasee de planificare de sezon (season plans), fiecare cu propria progresie de blocuri pedagogice și micro-cicluri săptămânale, care leagă explicit probleme din motorul de decizie → principii → exerciții → ședințe → scripturi → reflecție → transfer în meci, cu semnale explicite de continuare/ajustare/încetinire/abandon bazate pe observație reală, nu pe un calendar generic.

## 2. Context pentru un cititor nou

- Repository canonic: `E:\ManualFC-clean`. Repository legacy `E:\ManualFC` — NU se atinge.
- Există deja: două teme complete de antrenament (`sprijin-si-unghi-de-pasa`: EX-0001–EX-0015, SES-0001–SES-0006, ASM-0001; `apararea-presiune-si-acoperire`: EX-0016–EX-0025, SES-0007–SES-0010, ASM-0002), 8 probleme în motorul de decizie (`PRB-0001`–`PRB-0008`), 21 de principii canonice (`principle.<slug>`), 26 de scripturi de comunicare (`SCR-0001`–`SCR-0026`, `TASK-3719`).
- **Există deja două schelete neutilizate direct relevante pentru acest pilon**, descoperite prin inspecție directă, nu presupuse:
  - `schemas/curriculum.schema.json` (tip `CUR-XXXX`) — un document cu `blocks` (array de `{id: BLK-XXXX, order, principle_ids, session_ids}`), 0 fișiere reale, niciun director `data/curriculum/` creat încă.
  - `schemas/season-plan.schema.json` (tip `PLAN-XXXX`) — un document cu `curriculum_ids` (referințe către `CUR-XXXX`) și `microcycles` (array de `{id: MIC-XXXX, order, session_ids}`), 0 fișiere reale în `data/season-plans/` (doar README).
  - Ambele scheme sunt foarte subțiri față de cerințele explicite ale acestui task (~10-20 câmpuri suplimentare cerute la fiecare nivel) — se completează, nu se înlocuiesc.
- `scripts/validate_content.py` are deja mapate directoarele (`data/curriculum/`→`curriculum`, `data/season-plans/`→`season-plan`), prefixele (`CUR`, `PLAN`, `MIC`, `BLK` — acesta din urmă lipsește din `PREFIX_TYPES` și trebuie verificat/adăugat dacă indexarea generică a ID-urilor imbricate o cere), și câmpurile de referință generice (`curriculum_ids`, `session_ids`, `principle_ids`) în `REFERENCE_FIELDS` — referințele `EX-`/`SES-`/`CUR-`/`SCR-` (format `PREFIX-XXXX`) sunt validate GENERIC de `validate_content.py` prin `self.index`; referințele `principle.<slug>` (format cu punct) NU sunt validate generic (regex `ID_RE` nu se potrivește), la fel ca la `TASK-3719` — necesită validator dedicat.
- Evidență reală, deja înregistrată, direct relevantă pentru planificarea de sezon (verificată prin citire completă, nu presupusă): `CLM-0371`/`CLM-0372` — periodizarea pe blocuri (Issurin) și periodizarea tradițională (Matveyev) sunt dezvoltate și testate aproape exclusiv pe sportivi adulți de elită, NU pe dezvoltare juvenilă; modelul Côté (DMSP) plasează 10-11 ani în „anii de eșantionare" — joc deliberat dominant, practică variată, NU specializare orientată spre competiție. **Consecință directă:** acest pilon NU este un instrument de periodizare sportivă în sensul tehnic al termenului și trebuie să declare asta explicit, nu doar implicit. `CLM-0366`–`CLM-0368` documentează că planurile reale de antrenament deviază semnificativ de la intenția inițială din cauza factorilor externi (absențe, cereri concurente) — motivează explicit câmpurile de revizuire/adaptare/semnale de continuare cerute de task, nu doar o listă decorativă. `CLM-0275`/`CLM-0276`/`CLM-0341` susțin structura de reflecție. `CLM-0089`/`CLM-0197` susțin variația constrângerilor față de repetiția rigidă.
- Pattern-ul FAIL_CLOSED deja stabilit (TASK-3712/3718/3719): completarea numelor de câmp deja recunoscute de `validate_content.py` (`rationales` cu 7 chei, etc.) declanșează validare automată; pentru pilonul acesta, structura nu se pretează la formatul „mesaj către copil" (un plan de sezon e document pentru antrenor, nu o replică rostită), deci se scrie un validator dedicat nou (`scripts/validate_season_plans.py`), urmând exact tiparul `validate_gold_standard_v2.py`/`validate_communication_scripts.py`: verifică prezența/nevidul câmpurilor V2-echivalente și rezolvarea reală a fiecărui ID referențiat.
- Pilotarea reală (`TASK-3714`) rămâne `BLOCKED`. Utilizatorul autorizează explicit construcția acestui pilon acum — a treilea caz de această autorizare explicită, după temă (`TASK-3718`) și scripturi (`TASK-3719`).

## 3. Rezultatul verificabil

- Schemele `curriculum.schema.json`/`season-plan.schema.json` extinse (aditiv, 0 documente existente afectate).
- 4 fișiere noi `data/curriculum/curriculum-*.json` (CUR-0001–CUR-0004, 2 blocuri fiecare = 8 blocuri).
- 4 fișiere noi `data/season-plans/season-plan-*.json` (PLAN-0001–PLAN-0004, ~4 micro-cicluri fiecare = 16 micro-cicluri).
- `app/src/lib/content-bridge.ts` extins cu getters pentru curricula/season plans + funcții de surfacing încrucișat.
- Pagini noi: `/planuri-de-sezon/` (index, filtrabil pe scop/nivel — traseu de descoperire 1), `/planuri-de-sezon/[id].astro` (detaliu complet, ierarhie plan→bloc→microciclu într-o singură pagină, cu stil de tipărire).
- Blocuri „Plan de sezon relevant" adăugate pe paginile de problemă, temă, principiu, exercițiu, ședință și script — traseu de descoperire 2.
- `discovery-index.ts` extins să indexeze planurile de sezon.
- Teste noi (`tests/test_task3720_season_plans.py`), teste web actualizate (contor de rute).
- Guvernanță actualizată.

## 4. Domeniu și non-obiective

**În scop:** cele 4 trasee, ierarhia bloc/microciclu, cele două trasee de descoperire, integrarea în căutare/sitemap/rute.

**Non-obiective explicite:**
- NU e periodizare sportivă în sensul tehnic (fiziologie, încărcare GPS) — e planificare pedagogică, declarat explicit, motivat de `CLM-0371`/`CLM-0372`.
- NU se construiește un al treilea pilon (studii de caz rămâne gol, deliberat).
- NU se atinge conținutul existent al celor două teme, al scripturilor sau al motorul de decizie — doar se citește pentru a construi legături reale.
- NU se construiește autentificare, cont, bază de date, analitice sau personalizare.
- NU se creează pagini separate per bloc/microciclu — ierarhia completă apare într-o singură pagină de plan, consecvent cu tiparul existent la ședințe (segmentele apar inline, nu ca rute separate).
- NU se pretinde validare de teren — pilotarea (`TASK-3714`) rămâne `BLOCKED`.

## 5. Fișiere și module afectate

**Noi:** `data/curriculum/curriculum-*.json` (4), `data/season-plans/season-plan-*.json` (4), `scripts/validate_season_plans.py`, `app/src/pages/planuri-de-sezon/index.astro`, `app/src/pages/planuri-de-sezon/[id].astro`, `tests/test_task3720_season_plans.py`.

**Modificate:** `schemas/curriculum.schema.json`, `schemas/season-plan.schema.json`, `app/src/lib/content-bridge.ts`, `app/src/lib/discovery-index.ts`, `app/src/pages/rezolva-pe-teren/[slug].astro`, `app/src/pages/gold-standard/index.astro`, `app/src/pages/aparare/index.astro`, `app/src/pages/principii/[slug].astro`, `app/src/pages/gold-standard/exercitii/[id].astro`, `app/src/pages/gold-standard/sedinte/[id].astro`, `app/src/pages/scripturi/[id].astro`, `tests/web/built-routes.test.js`.

## 6. Cercetare necesară

Niciun claim nou — se reutilizează exclusiv `research/claims.json` existent, verificat deja non-retras, cu accent pe `CLM-0371`/`CLM-0372`/`CLM-0366`–`CLM-0368`/`CLM-0275`/`CLM-0276`/`CLM-0341`/`CLM-0089`/`CLM-0197` (verificate prin citire completă, nu căutare de cuvinte cheie).

## 7. Model pedagogic

Fiecare traseu pornește de la o problemă reală de antrenor (nu o dată de calendar), definește o intenție de învățare, progresează de la simplu la reprezentativ prin blocuri, fiecare bloc conținând micro-cicluri săptămânale cu ședințe reale deja existente. Progresia respectă explicit modelul Côté (10-11 ani = ani de eșantionare, joc variat, nu specializare) — niciun traseu nu prescrie o singură cale rigidă; toate includ reguli de adaptare, criterii de progres/regres și semnale explicite de continuare/ajustare/încetinire/abandon, motivate de dovada că planurile reale deviază constant de la intenție.

## 8. Design vizual și interactiv

Fără diagrame noi (planurile referă ședințe/exerciții existente, care au deja diagramele lor). Pagina de detaliu a planului folosește ierarhie clară de titluri (h1 plan, h2 bloc, h3 microciclu), cu stil de tipărire (`@media print`, salt de pagină între blocuri) — consecvent cu convenția deja folosită la `fise-de-teren.astro`.

## 9. Pași de implementare

1. Inspectare completă — FĂCUT.
2. Extindere scheme `curriculum.schema.json`/`season-plan.schema.json`.
3. Redactare 4 curricula (8 blocuri) + 4 season plans (16 microcicluri).
4. `scripts/validate_season_plans.py` + rulare.
5. Extindere `content-bridge.ts`, `discovery-index.ts`.
6. Pagini noi + blocuri „Plan de sezon relevant" pe 6 tipuri de pagini existente.
7. Teste noi + actualizare `built-routes.test.js`.
8. Validare completă (schemă, validator dedicat, check, build, browser+axe, sitemap).
9. Fresh clone + guvernanță + raport final.

## 10. Validare și acceptare

- `python scripts/validate_content.py --strict` — 0 erori.
- `python scripts/validate_season_plans.py` — 0 erori.
- `npm run check` — 0 erori.
- `npm test` — 9/9 (contor de rute actualizat).
- `python -m pytest tests/ -q` — 0 eșecuri.
- `npm run build` — pagini noi prezente.
- Playwright+axe la 1440px/390px pe paginile noi + cel puțin o pagină din fiecare din cele 6 tipuri cu bloc de legătură nou.
- `git fsck --full` curat, fresh clone reproduce identic.

## 11. Progres

- [x] Inspecție completă + decizie arhitecturală (completarea schemelor CUR/PLAN existente).
- [ ] Scheme extinse
- [ ] 4 curricula + 4 season plans redactate și validate
- [ ] Validator nou scris
- [ ] `content-bridge.ts`/`discovery-index.ts` extinse
- [ ] Pagini noi + blocuri de legătură pe 6 tipuri de pagini
- [ ] Teste noi
- [ ] Validare completă + fresh clone
- [ ] Guvernanță + raport + push

## 12. Descoperiri și surprize

- Ambele scheme necesare (`curriculum.schema.json`, `season-plan.schema.json`) existau deja ca schelete complet neutilizate, cu o relație de compoziție deja gândită corect (`PLAN` referă `CUR` prin `curriculum_ids`, `CUR` conține `blocks`, `PLAN` conține propriile `microcycles`) — arhitectura de bază nu a trebuit reproiectată, doar adâncită cu câmpurile pedagogice cerute explicit de task.
- Evidența despre periodizare (`CLM-0371`/`CLM-0372`) era deja înregistrată în proiect, dintr-un val de cercetare anterior — a oferit motivul direct pentru decizia explicită de a NU numi acest pilon „periodizare" și de a-l încadra corect ca planificare pedagogică pentru anii de eșantionare.

## 13. Jurnal de decizii

1. **Decizie:** păstrarea relației de compoziție `PLAN → curriculum_ids → CUR → blocks`, nu colapsarea într-o singură schemă. **Motiv:** schema există deja așa; schimbarea ei ar fi o modificare nejustificată de arhitectură, nu o completare. **Data:** 2026-09-23.
2. **Decizie:** acest pilon se declară explicit „planificare pedagogică", nu „periodizare sportivă" — motivat de `CLM-0371`/`CLM-0372`. **Efect:** `evidence_boundary` la nivel de plan conține această declarație explicit, în fiecare din cele 4 fișiere. **Data:** 2026-09-23.
3. **Decizie:** fără pagini separate per bloc/microciclu — ierarhia completă apare inline pe pagina de plan. **Motiv:** consecvent cu tiparul existent la ședințe (segmente inline); evită proliferarea de rute pentru conținut care nu are sens navigat independent. **Data:** 2026-09-23.
4. **Decizie:** validator nou dedicat, nu extinderea `validate_gold_standard_v2.py`. **Motiv:** scop diferit, nume specific „Gold Standard V2"; planurile de sezon nu sunt exerciții/ședințe. **Data:** 2026-09-23.

## 14. Rezultat și retrospectivă

_(completat la finalul taskului)_
