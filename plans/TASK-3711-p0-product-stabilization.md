# TASK-3711 — ManualFC P0 Product Stabilization

## 1. Titlu și scop

Elimină defectele P0 identificate în auditul TASK-3710 și în roadmap-ul canonic (Faza 0), astfel încât un fresh clone al `E:/ManualFC-clean` să poată fi instalat, verificat, construit și testat fără cunoaștere locală specială.

## 2. Context pentru un cititor nou

- Repo canonic: `E:/ManualFC-clean`, HEAD inițial `a5ee169e9cd61ef2988e4d95cec26346a32e6db4`.
- Remote `origin` (`git@github.com:berescristi-glitch/ManualFC.git`) conține deja acest HEAD — confirmat prin `git ls-remote origin` chiar la începutul acestui task (SSH auth funcțional).
- Repo legacy `E:/ManualFC` rămâne arhivă forensică, neatins.
- Auditul TASK-3710 și roadmap-ul canonic (`docs/roadmap/MANUALFC_CANONICAL_ROADMAP.md`) au identificat exact aceste defecte P0: ruta CTA „Rezolvă pe teren" greșită, dependențe Playwright/axe nedeclarate, lipsa completă a infrastructurii SEO tehnice, lipsa unui smoke test automat de browser/accesibilitate.

## 3. Rezultatul verificabil

- Link-ul „Rezolvă pe teren" din header/footer/homepage duce la `/rezolva-pe-teren`.
- `package.json` declară `playwright` și `@axe-core/playwright` ca devDependencies reale, cu lockfile actualizat.
- `astro.config.mjs` are `site` setat; sitemap și robots.txt generate corect.
- Un smoke test real (browser + axe) există și rulează, verificând homepage, main/h1 unic, ruta CTA reparată, 0 violări axe pe paginile critice.
- Un fresh clone independent din remote-ul real trece: install, check, teste, smoke test, build, fsck.

## 4. Domeniu și non-obiective

**Intră:** cele 4 lucrări obligatorii de mai sus, plus validarea completă.
**Nu intră:** conținut pedagogic nou, redesign, schema multi-age, documente strategice noi (în afara raportului taskului), infrastructură de autentificare/bază de date/analytics.

## 5. Fișiere și module afectate

De investigat/modificat: `app/src/components/AppHeader.astro`, `AppFooter.astro`, `app/src/pages/index.astro`, `app/src/pages/incepe-aici.astro` (posibil), `tests/web/built-routes.test.js` sau echivalent, `package.json`, `package-lock.json`, `astro.config.mjs`, fișiere noi pentru sitemap/robots dacă nu există integrare automată.

## 9. Pași de implementare

1. Citire context (finalizat — AGENTS.md/CODEX.md/MASTER_EXECUTION_PROMPT.md/PLANS.md/QUALITY_GATES.md deja cunoscute din sesiunea curentă).
2. Verificare stare Git (finalizat — HEAD/remote confirmate).
3. Acest ExecPlan.
4. Investigare cauza exactă a fiecărei probleme (rulat înainte de orice editare).
5. Reparație #1: ruta CTA.
6. Reparație #2: dependențe declarate.
7. Reparație #3: SEO tehnic.
8. Reparație #4: smoke test.
9. Verificare fresh clone completă.
10. Guvernanță și raport final.

## 11. Progres

- [x] Context și stare Git verificate.
- [x] Cauza fiecărei probleme identificată.
- [x] Fix #1 — rută CTA
- [x] Fix #2 — dependențe
- [x] Fix #3 — SEO
- [x] Fix #4 — smoke test
- [ ] Fresh clone verification
- [ ] Guvernanță + raport

## 13. Jurnal de decizii

- **Cauza exactă CTA:** `getPrimaryNavigation()` (`content-bridge.ts`) întorcea deja
  corect `{ label: "Rezolvă pe teren", href: "/rezolva-pe-teren" }` ca rută reală de
  producție. Defectul era în `AppHeader.astro`: harta `preferredLabels` filtra pe
  cheia veche `/gold-standard/rapid`, care nu (mai) există în lista întoarsă de
  `getPrimaryNavigation()` — rezultat: item-ul de nav era eliminat silențios din
  header. `AppFooter.astro`, `HomepageHero.astro` și `incepe-aici.astro` aveau
  `href="/gold-standard/rapid"` scris direct (hardcodat), nu prin sursa de adevăr.
  Reparație: header repointat la cheia reală `/rezolva-pe-teren`; footer/hero/
  incepe-aici repointate direct la `/rezolva-pe-teren`.
- **Ce NU s-a schimbat, intenționat:** `gold-standard/index.astro` ("Pentru
  varianta scurtă, vezi...") și `volum/index.astro` ("Am nevoie acum") rămân
  legate la `/gold-standard/rapid` — pagina chiar există în continuare, se
  autodescrie ca exemplul legacy Quick Mode ("Pattern-ul rapid validat rămâne
  disponibil; noul Decision Engine îl extinde la opt observații") și leagă deja
  înapoi spre `/rezolva-pe-teren`. Acestea sunt referințe interne legitime în
  familia Gold Standard, nu CTA-ul principal "rezolvă o problemă acum" — schimbarea
  lor ar fi fost redesign/copy fără motiv funcțional, interzis explicit de task.
- **Teste actualizate:** `tests/test_task2703_ia_v2.py` (assertions pe mapping-ul
  header/footer, mutate de la `/gold-standard/rapid` la `/rezolva-pe-teren`) și
  `tests/test_web_bootstrap.py` (asertarea pe marcajul "Site URL = unresolved" a
  fost înlocuită cu asertarea reparării reale — vezi Fix #3). `tests/
  test_task2208_web_integration.py` nu a necesitat nicio modificare: verifică
  exclusiv existența/conținutul paginii legacy `gold-standard/rapid.astro`, care
  rămâne neschimbată.
- **Domeniu canonic SEO:** nu există niciun domeniu de producție propriu
  documentat. Singurul URL real, documentat (`PROJECT_STATUS.md`, DEC-0053) este
  `https://manualfc.vercel.app/`, numit explicit acolo "URL canonic de test" —
  servit în prezent cu `X-Robots-Tag: noindex, nofollow` (`vercel.json`), o decizie
  de business deliberată, neatinsă în acest task. S-a folosit acest URL ca `site`
  în `astro.config.mjs` ca să existe canonical/sitemap coerente și verificabile,
  fără a inventa un domeniu de producție nou. **Decizie încă necesară din partea
  proprietarului de produs:** dacă/când se cumpără un domeniu propriu de
  producție, `SITE_URL` din `astro.config.mjs` trebuie actualizat și politica
  `noindex` din `vercel.json` reevaluată explicit.
