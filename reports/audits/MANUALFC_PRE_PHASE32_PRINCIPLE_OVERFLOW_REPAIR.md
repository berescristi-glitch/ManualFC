# MANUALFC — Pre-PHASE-32 Hygiene Patch: Principle Page Horizontal Overflow Repair

**Data:** 2026-08-26 · **Task de referință:** TASK-3310 · **Statut:** ACCEPTAT — repair izolat, Educational Page System V1 neschimbat

## 1. Guvernanță

`INITIAL_HEAD`: `1d4dc82` (`MANUALFC_EDUCATIONAL_PAGE_SYSTEM_V1 = aff2017`, verificat prin `git rev-parse`, neschimbat/nesuprascris de acest task). Working tree curat la pornire (`git status --short` fără fișiere murdare urmărite). Preflight de integritate a fișierelor: `data/media/media-registry.json` (13183 bytes), `public/icons/icon-192.png` (41651 bytes), `public/icons/icon-512.png` (168436 bytes), `tests/test_task2802_workspace.py` (1293 bytes) — toate confirmate nezero, fără nicio corupere nouă.

## 2. Defect

**REPRODUS ÎNAINTE DE REPARAȚIE** (nu presupus din raportul anterior): browser real conectat prin CDP la sesiunea autentificată Vercel, `/principii/adaptarea-sarcinii-u11/` inspectat la 1440/1280/768/390.

**Geometrie pre-reparație** (identică la toate cele 4 viewport-uri, în pixeli reali măsurați):

| Viewport | `innerWidth` | `clientWidth` | `.principle-hero` right | `.principle-hero` left |
|---|---|---|---|---|
| 1440 | 1440 | 1425 | 1433 | -7 |
| 1280 | 1280 | 1265 | 1273 | -7 |
| 768 | 768 | 753 | 761 | -7 |
| 390 | 390 | 375 | 383 | -7 |

**Root cause confirmat:** `.principle-hero{width:100vw;margin-left:calc(50% - 50vw)}`. `100vw` include lățimea barei de scroll verticale (15px constant, indiferent de viewport — confirmat empiric: discrepanța rămâne fixă la toate cele 4 dimensiuni, nu proporțională), în timp ce `%` (folosit în `calc(50% - ...)`) se rezolvă corect față de content-box-ul containerului părinte, care EXCLUDE bara de scroll. Discrepanța constantă (nu procentuală) e dovada directă că e vorba de bara de scroll, nu de o eroare de calcul procentual.

## 3. Încercare de reparație eșuată, documentată onest

Prima încercare (`overflow:clip` pe `.principle-hero`) NU a funcționat: `overflow` controlează doar randarea conținutului care depășește propria cutie a elementului, nu dimensiunea/poziția cutiei înseși. Cutia `.principle-hero` (100vw lățime, margine negativă) continua să conteze în `scrollWidth`-ul documentului indiferent de `overflow:clip`. Verificat empiric (nu presupus): overflow rămas identic după acest prim fix.

A doua încercare (`--scrollbar-w:calc(100vw - 100%)` definit pe `:root`/`body`, consumat în `.principle-hero`) a eșuat diferit: proprietățile CSS custom nu se „pre-calculează" la locul declarării — `var()` substituie textul brut, iar `calc()` rezultat se evaluează în CONTEXTUL elementului care îl CONSUMĂ. `100%` din interiorul `--scrollbar-w`, folosit în `width` al `.principle-hero`, s-a rezolvat față de containerul de 1200px al lui `.principle-hero` însuși, nu față de viewport — rezultat: efectul de „full-bleed" a dispărut complet (lățime colapsată la 1200px), deși overflow-ul a dispărut incidental. Verificat empiric, nu presupus.

**Fix final, funcțional:** măsurare JS a lățimii reale a barei de scroll (`window.innerWidth - document.documentElement.clientWidth`), scrisă ca proprietate CSS custom `--scrollbar-w` cu o valoare fixă în pixeli (nu procentuală, deci fără capcana de re-rezolvare de mai sus). Scriptul e plasat la finalul conținutului propriu al paginii (nu în `<head>`) — plasat prea devreme, înainte ca documentul să aibă suficient conținut randat pentru a determina dacă are nevoie de bară de scroll verticală, măsurătoarea citea incorect 0. Fallback CSS static `15px` pe `:root` pentru randarea inițială/fără JS. Nu s-a folosit nicio mascare globală (`html,body{overflow-x:hidden}`).

## 4. Fișiere schimbate

Un singur fișier: `app/src/pages/principii/[slug].astro` — 1 regulă CSS `:global(:root){--scrollbar-w:15px}` adăugată, regula `.principle-hero` modificată (width/margin-left/padding recalculate cu `var(--scrollbar-w)`), 1 `<script is:inline>` adăugat la finalul conținutului paginii.

## 5. Verificare POST-fix, browser real

| Rută | 1440 | 1280 | 768 | 390 |
|---|---|---|---|---|
| `/principii/adaptarea-sarcinii-u11/` (primară) | PASS (0 overflow) | PASS | PASS | PASS |
| `/principii/variabilitatea-dezvoltarii-u11/` (a doua rută, generalizare) | PASS | PASS | PASS | PASS |
| `/volum/01/ch-0109/` (regresie Pedagogul, Educational Page System V1) | PASS | PASS | PASS | PASS |
| `/volum/01/ch-0106/` (regresie Pedagogul) | PASS | PASS | PASS | PASS |
| `/gold-standard/exercitii/EX-0001/` (regresie Gold Standard) | PASS | PASS | PASS | PASS |

Toate cele 20 de combinații: `document.documentElement.scrollWidth === document.documentElement.clientWidth` exact (0 overflow), `main` unic, 0 erori de consolă. Verificat pe deployment-ul Preview real (nu doar local) — vezi §8.

Vizual (captură de ecran, 1440 și 390): banda full-bleed rămâne perfect edge-to-edge, fără artefacte, fără decupări vizibile — calitatea vizuală păstrată intact.

**Reduced motion:** `prefers-reduced-motion:reduce` emulat — 0 overflow, nicio dependență de animație în reparație.

**Axe real:** 0 violări pe `/principii/adaptarea-sarcinii-u11/` și pe `/volum/01/ch-0109/` (regresie), al doilea test consecutiv cu 0 violări — singurul item „incomplete" e cel deja cunoscut, preexistent, al logo-ului global (neafectat de acest patch).

## 6. Validare locală

`npm run check`: 0 erori. `npm run build`: 92 pagini. `python -m pytest`: 505/505. `python scripts/validate_project.py`: 0 erori. `git diff --check`: PASS.

## 7. Constatări în afara scopului (nereparate, conform regulii §26)

Niciuna nouă. Constatările deja documentate în DEC-0075 (logo-tagline Axe „incomplete") rămân neschimbate și nu au legătură cu acest patch.

## 8. Preview

Deployment nou creat din candidatul curat (commit `96acb8c`): `dpl_FptDFGDMFS43qWKqzyYurCvNsBGV`, `target: null` (Preview, niciodată Production), `https://manualfc-n5dav8jdz-berescristi-8889s-projects.vercel.app`, `readyState: READY`. Auditat cu browser real (aceeași sesiune Chrome autentificată prin CDP): toate cele 20 combinații rută×viewport din matricea de la §5, PASS identic cu local — 0 overflow, `main` unic, Axe 0 violări (rulat din nou, live). O singură eroare de consolă tranzitorie observată o singură dată, la PRIMA navigare către acest URL de deployment nou (fetch eșuat al `manifest.webmanifest`, redirecționat prin stratul SSO al Vercel) — reprodus explicit de două ori suplimentar pe aceeași pagină (reîncărcare) și confirmat că NU se repetă; artefact de mediu specific primei stabiliri a cookie-ului SSO pentru un URL de deployment nou, nu un defect real, neschimbat de acest patch (linkul de manifest e parte din `BaseLayout.astro`, neatins).

## 9. Verdict final

DEFECT_REPRODUCED_PRE_FIX = DA · ROOT_CAUSE_CONFIRMED = DA (bara de scroll, discrepanță constantă 15px) · GLOBAL_OVERFLOW_MASKING_USED = NU · toate cele 5 rute × 4 viewport-uri = PASS · DOCUMENT_OVERFLOW = 0 · CONSOLE_ERRORS = 0 · VALIDATORS/TESTS/BUILD = PASS · REAL_BROWSER = PASS · CRITICAL = 0 · MAJOR = 0.

`EDUCATIONAL_PAGE_SYSTEM_V1` rămâne `FROZEN`/`aff20175c03fed387fb9afdbaf767d065f7ea1e8`, neschimbat de acest patch. `MANUALFC_PRE_PHASE32_HYGIENE_BASELINE = 96acb8c63e270873de8c562114c0d704743ce545`.

## 10. Autorizare

**PHASE-32 nu este autorizat de acest document.**
