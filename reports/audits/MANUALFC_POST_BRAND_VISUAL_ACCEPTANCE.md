# MANUALFC — Post-Brand Visual Debug, Regression Repair & Acceptance (TASK-3703)

## Verdict final

**`PASS_WITH_DECLARED_NON_BLOCKING_LIMITATIONS`**

Toate defectele validate (cele 2 cunoscute de la TASK-3701, plus 2 suplimentare de același tip găsite în timpul auditului obligatoriu) au fost reproduse cu browser real, reparate la cauza-rădăcină și reverificate cu 0 regresii pe o matrice de 50 combinații rută×viewport. Rămâne o singură limitare declarată explicit, nereparată (reflow sub 320px CSS — vezi §6), plus corupția Git deja documentată în TASK-3702 (neatinsă, conform instrucțiunii).

---

## Faza 1 — Reproducere înainte de reparație

### Defect 1 — Overflow orizontal ~8px pe homepage (cunoscut din TASK-3701)

- **Reproducere:** Chrome real (CDP), `document.documentElement.scrollWidth - clientWidth`, la 320/390/768/1280/1440.
- **Element/regulă:** `.approved-hero` (`app/src/components/HomepageHero.astro`) și `.final-cta` (`app/src/pages/index.astro`) — ambele `width:100vw; margin-left:calc(50% - 50vw)`.
- **Geometrie măsurată:** offset simetric ±7.5px pe ambele secțiuni la 1280px (`left:-7.5, right:1272.5` pe un `clientWidth` de 1265px) → 15px total, egal cu lățimea reală a barei de scroll verticale.
- **Cauza-rădăcină:** `100vw` include bara de scroll verticală; `calc(50% - 50vw)` centrează greșit cutia rezultată, extinzând-o simetric peste marginile vizuale ale viewport-ului.
- **Precedență:** confirmat în raportul TASK-3701 (declarat explicit ca limitare, nereparat atunci) — precede acest task.
- **Impact:** scroll orizontal fantomă pe întregul document, pe orice pagină care include homepage-ul; nu afectează logo-ul direct, dar e o regresie de calitate vizuală pe suprafața principală a produsului.

### Defect 2 — Contrast insuficient pe indicatorul „01" (cunoscut din TASK-3701)

- **Element/regulă:** `.proof-index b` (`app/src/pages/index.astro`), `color:var(--color-border)` (#CED2D5) pe fundal `--color-bg-main` (#F7F7F2).
- **Contrast calculat:** 1.42:1 (font 80px bold, prag necesar 3:1) — Axe: `color-contrast`, impact `serious`.
- **Precedență:** declarată în TASK-3701.
- **Impact:** text decorativ mare, dar vizibil ilizibil pentru utilizatori cu vedere redusă.

### Defect 3 — Overflow orizontal ~8px pe /incepe-aici (nou, găsit în auditul obligatoriu)

- **Element/regulă:** `.founding-rule` (`app/src/pages/incepe-aici.astro`), identic tipar `width:100vw; margin-left:calc(50% - 50vw)`.
- **Geometrie măsurată:** 8px overflow constant la toate cele 5 viewport-uri (320/390/768/1280/1440).
- **Cauza-rădăcină:** identică Defectului 1.
- **Dovada de precedență:** `git show 0466ea9:app/src/pages/incepe-aici.astro | grep -c "founding-rule{width:100vw"` → `1` — prezent în commit-ul dinaintea TASK-3601 și TASK-3701. **Precede ambele.**
- **Impact:** identic Defectului 1, pe a doua pagină cea mai vizitată a site-ului (pagina de orientare).

### Defect 4 — Contrast insuficient pe cardul „Continuă" din Spațiul meu (nou, găsit în auditul obligatoriu)

- **Elemente/reguli:** `.continue .eyebrow` (moștenește `color:var(--color-text-accent)` #765800 din regula globală `.eyebrow{}`, care câștigă asupra culorii moștenite de la `.continue{color:#fff}`) și `p[data-continue-copy]` (moștenește `color:var(--color-text-secondary)` #334155 din regula globală `p{}`, din același motiv de specificitate).
- **Contrast calculat:** eyebrow 2.62:1 (font bold 11.5px, prag 4.5:1); copy 1.67:1 (font normal 16px, prag 4.5:1) — ambele Axe `color-contrast`, impact `serious`.
- **Cauza-rădăcină:** `.continue h2{color:#fff}` există deja ca override local, dar lipsește echivalentul pentru `p`/`.eyebrow` — regulile globale de tip-selector (`p{}`) și de clasă (`.eyebrow{}`) au specificitate suficientă pentru a bate moștenirea din `.continue{color:#fff}`.
- **Dovada de precedență:** `git show 0466ea9:app/src/pages/spatiul-meu/index.astro | grep -c 'class="continue"'` → `1` — precede ambele TASK-3601 și TASK-3701.
- **Impact:** cardul „Continuă" (primul element de acțiune pe Spațiul meu) devine ilizibil pentru utilizatori cu vedere redusă.

### Verificări suplimentare Faza 1 (fără defecte găsite)

- Header/footer la 320/390/768/1280/1440: logo randat corect, fără distorsiune, pe toate paginile auditate.
- Meniu mobil (390px): închis inițial, se deschide/închide corect prin click pe `summary`, 0 overflow introdus.
- Zoom 200% (simulat corect prin înjumătățirea viewport-ului, echivalentul CSS-pixel real al zoom-ului browserului — testarea inițială cu proprietatea CSS `zoom` s-a dovedit nereprezentativă, vezi §7): la 640×400 (≈1280×800 la 200%) — 0 overflow.
- Reduced motion: 0 erori de pagină la navigare/reîncărcare cu `prefers-reduced-motion:reduce`.
- Navigare exclusiv din tastatură: 8 din 8 opriri Tab pe homepage au outline vizibil (`outline:solid, 3px`), ordinea logică (skip-link → logo → nav → CTA).
- Online/offline: homepage se încarcă offline din Service Worker cu conținut real și logo funcțional (`complete:true`, `naturalWidth>0`).

---

## Faza 2 — Reparație minimă

| Defect | Fișier | Schimbare |
|---|---|---|
| 1 | `app/src/components/HomepageHero.astro` | `.approved-hero`: `width:calc(100vw - var(--scrollbar-w))`, `margin-left:calc(50% - 50vw + var(--scrollbar-w)/2)` |
| 1 | `app/src/pages/index.astro` | `.final-cta`: identic; script inline la finalul paginii care măsoară `window.innerWidth - clientWidth` și scrie `--scrollbar-w` |
| 2 | `app/src/pages/index.astro` | `.proof-index b`: `color:var(--color-border)` → `color:var(--color-text-muted)` (4.63:1, token existent, nicio culoare nouă) |
| 3 | `app/src/pages/incepe-aici.astro` | `.founding-rule`: identic tipar cu Defectul 1; script inline identic |
| 4 | `app/src/pages/spatiul-meu/index.astro` | adăugat `.continue p{color:#fff}` și `.continue .eyebrow{color:var(--color-brand-gold)}` (10.59:1, token existent, oglindește tiparul deja folosit în `.mode-now .eyebrow` de pe homepage) |

Toate reparațiile respectă restricțiile explicite: niciun `overflow-x:hidden` global, niciun JavaScript nou dincolo de tiparul deja stabilit în `principii/[slug].astro` (DEC-0076), niciun artwork de brand atins, niciun token de brand schimbat, nicio pagină/componentă modificată fără legătură demonstrată cu unul din cele 4 defecte.

---

## Faza 3 — Audit complet post-reparație

Chrome real (CDP) + Playwright + axe-core, 10 suprafețe × 5 viewport-uri (320×568, 390×844, 768×1024, 1280×800, 1440×900) = **50 combinații**:

/, /incepe-aici, /gold-standard, /gold-standard/exercitii/EX-0001, /gold-standard/sedinte/SES-0001, /gold-standard/sedinte/SES-0001/mod-teren, /volum/01/ch-0101, /volum/03/ch-0301, /rezolva-pe-teren/primeste-fara-sa-verifice-inainte, /spatiul-meu.

**Rezultat: 50/50 PASS.** Pentru fiecare combinație: status 200, exact un `<main>`, exact un `<h1>`, 0 overflow orizontal, 0 imagini rupte, 0 violări Axe, 0 erori de consolă/pagină.

Verificare logo: aspect ratio randat vs. natural comparat pe fiecare instanță de logo întâlnită (header „horizontal", footer „full") — nicio distorsiune (diferență <0.05 în raport, în limita rotunjirii la pixel întreg). O singură instanță cu dimensiune randată 0×0 găsită pe Field Mode (`mod-teren`) — investigată și confirmată intenționată: `body:has(.field-mode) .app-footer{display:none}` ascunde deliberat footer-ul (deci și logo-ul din el) în modul de teren pentru o interfață fără distrageri; nu e defect.

---

## Faza 4 — Integritatea brandului

Verificare programatică (Python + PIL) a fiecărui asset din `logo-assets.json`:

- Toate cele 11 fișiere declarate există pe disc.
- Toate hash-urile SHA-256 corespund exact valorilor din manifest (inclusiv masterul — neschimbat față de TASK-3701).
- Toate dimensiunile și modurile de culoare corespund.
- Rapoartele de aspect ale derivatelor (`manualfc-logo-full.png`, `manualfc-logo-horizontal.png`, `manualfc-mark.png`) corespund exact cutiilor de decupare declarate — nicio distorsiune.
- Verificare de bleed pe marginile `manualfc-mark.png` (analiză de luminozitate pe primele/ultimele 10 coloane): luminozitate uniformă ~24 (fundal navy), fără urme ale wordmark-ului adiacent.
- Service worker (`public/sw.js`) referă exclusiv noile iconițe (`manualfc-icon-192/512.png`).
- `og:image`/`twitter:image` din `BaseLayout.astro` folosesc `manualfc-social.png`.
- Căutare repository-wide: 0 referințe runtime către identitatea shield/crest anterioară (singurul hit rămas e documentația proprie `logo-assets.json`, secțiunea `superseded`, care documentează intenționat ce s-a șters).

---

## Faza 5 — Build și validare

| Comandă | Rezultat |
|---|---|
| `python scripts/validate_project.py` | 0 erori, 0 avertismente |
| `python scripts/generate_task_registry.py --check` | reproductibil, 305 taskuri |
| `python scripts/validate_content.py --strict` | VALID: 0 erori |
| `python -m pytest -q` | 518 passed, 25 subtests passed |
| `npm run test` (node --test) | 1/1 PASS |
| `npm run check` (astro check) | 0 erori / 96 fișiere |
| `npm run build` | 101 pagini construite |
| `python scripts/validate_html_landmarks.py` | VALID: 101 documente, main=1, nested_main=0 |
| `python scripts/audit_route_links.py` | 101 HTML, 0 linkuri interne rupte |
| `git diff --check` | 0 erori (doar avertismente CRLF normale Windows) |

Niciun warning sau test neexecutat nu a fost tratat drept PASS.

---

## Faza 6 — Preview

**`PREVIEW_VERIFIED`** — deployment Vercel Preview creat cu succes din starea curentă de lucru (nu Production; `target: null`).

- URL: `https://manualfc-n3yire08m-berescristi-8889s-projects.vercel.app`, `dpl_EsAg7inWWokUqNvnt2ufhbxFWzBC`, `readyState: READY`.
- Blocaj inițial de infrastructură (nu de brand): `vercel deploy` a eșuat prima dată cu `scandir 'node_modules.corrupt-20260831/zod/v4/locales'` — un director corupt, preexistent, nelegat de acest task (artefact vechi de instalare npm eșuată). Reparat prin adăugarea unui `.vercelignore` care exclude explicit `node_modules.corrupt-*` din pachetul de deploy — nicio ștergere a directorului însuși.
- Smoke test prin `vercel curl` (atașează automat credențialele CLI, fără citire de token brut): homepage 200 cu `og:image`/`twitter:image` corecte, favicon 32×32 200 OK, `manifest.webmanifest` cu iconițele noi, imaginea socială 200 OK, `/incepe-aici/` și `/spatiul-meu/` 200 OK.
- Confirmare byte-cu-byte: bundle-ul CSS servit de Preview conține exact regula `--scrollbar-w` a reparației (`scrollbar-w:15px`, `calc(100vw - var(--scrollbar-w))`).
- Nicio credențială sau token afișat.

---

## Criterii de acceptare — verificare finală

| Criteriu | Stare |
|---|---|
| Overflow homepage = 0 la toate viewport-urile | ✅ PASS |
| Contrast „01" trece WCAG AA | ✅ PASS (4.63:1) |
| Toate asseturile brandului trec integritatea | ✅ PASS |
| Zero referințe la identitatea veche | ✅ PASS |
| Browser matrix fără regresii | ✅ PASS (50/50) |
| Axe zero violări pe suprafețele auditate | ✅ PASS |
| Build și validări trec | ✅ PASS |
| Preview verificat sau limitare declarată | ✅ PASS (verificat) |
| Corupția Git din TASK-3702 neatinsă | ✅ PASS (confirmat, plus o a 12-a instanță găsită incidental, doar menționată) |
| Raportul conține dovezi, defecte, reparații, retest, limitări | ✅ acest document |

---

## §6 — Limitare declarată, nereparată (în afara scopului)

**Reflow sub ~200px CSS-pixel lățime** (simulat prin înjumătățirea unui viewport de 390px, reprezentând compunerea unui telefon îngust cu zoom 200%+): la 195×422, homepage-ul are 73px overflow, cauzat de mai multe elemente independente care nu se restrâng sub acest prag (animația decorativă `ball-flight`/`ball-bounce` cu dimensiuni fixe în px, floor-ul `clamp()` al `<h1>`, padding-ul fix al cardurilor din `.mode-split`). **Nu este un singur defect reparabil minimal** — ar necesita o revizuire mai largă a mai multor componente independente, ceea ce depășește mandatul de „reparație minimă, strict pe problemele validate" al acestui task. De asemenea, 195px e sub referința oficială WCAG 1.4.10 (Reflow) de 320px CSS-pixeli, care e deja verificată și trece (0 overflow la 320×568 în Faza 3). Declarat onest, nu ascuns; candidat pentru un task viitor dedicat responsive design-ului la extreme.

Corupția Git documentată integral în TASK-3702 rămâne o limitare separată, neatinsă, conform instrucțiunii explicite a acestui task.

---

## Fișiere modificate

`app/src/components/HomepageHero.astro`, `app/src/pages/index.astro`, `app/src/pages/incepe-aici.astro`, `app/src/pages/spatiul-meu/index.astro`, `.vercelignore` (nou), `plans/TASK-3703-post-brand-visual-debug.md` (nou), `reports/task-reports/TASK-3702.md` (nou, retroactiv), `reports/task-reports/TASK-3703.md` (nou), `reports/audits/MANUALFC_POST_BRAND_VISUAL_ACCEPTANCE.md` (acest document), `scripts/generate_task_registry.py`, `TASK_REGISTRY.json`, `TASK_HISTORY.jsonl`, `PROJECT_STATUS.md`, `DECISIONS.md`.
