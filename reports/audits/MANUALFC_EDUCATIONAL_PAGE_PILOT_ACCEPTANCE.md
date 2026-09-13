# MANUALFC — Educational Page Pilot Acceptance

**Data:** 2026-08-26 · **Task de referință:** TASK-3305 · **Statut:** ACCEPTAT

## 1. Selecția pilotului

Trei capitole cu caracteristici diferite (regula §59, nu doar cele mai ușoare):

| Capitol | Caracteristică | ExplanationToggle aplicat? |
|---|---|---|
| CH-0101 | Conceptual (profil de dezvoltare, fără secțiune de elaborare separată) | NU — corect omis, structura mai veche nu are o secțiune "Justificarea completă" distinctă |
| CH-0103 | Practic/procedural (decizie și eroare, protocol observație→intervenție) | DA — "De ce această formulare" comprimat |
| CH-0106 | Relațional/emoțional (frustrare, anxietate, rușine) | DA — "Justificarea completă" comprimat |

## 2. Defect real descoperit și reparat (Gate 5-6, buclă de reparare)

**Defect 1 — hoisting MDX (arhitectural):** componentele Astro (`ExplanationToggle`, `SectionNavigator` etc.) folosite din fișiere `.mdx` din `content/` (în afara `srcDir` — configurat explicit `srcDir: './app/src'` în `astro.config.mjs`) nu beneficiază de bundling automat al blocurilor `<script>`/`<style>` proprii componentei. Markup-ul (clase CSS, atribute `data-*`, structura HTML) se randa corect, dar stilurile și scripturile dispăreau complet din output — verificat direct prin grep pe HTML/CSS/JS compilate, nu presupus. **Reparat** prin centralizarea logicii JS (`app/src/lib/educational-page.ts`) și a stilurilor (`app/src/styles/educational-page.css`) în locații clar interioare `srcDir`, încărcate o singură dată global din `BaseLayout.astro` — funcționează ca Web Components standard, indiferent de unde a fost randat markup-ul `<explanation-toggle>`/`<section-navigator>` în DOM. Reverificat: CSS și JS prezente în bundle-urile compilate, 0 regresie pe `principii/[slug].astro` (consumatorul preexistent al `SectionNavigator`).

**Defect 2 — pierdere de conținut (fidelitate):** prima editare a `content/volume-01/chapter-03.mdx` a eliminat accidental paragraful de deschidere al scenariului („Un copil primește între linii, vede colegul plecat în profunzime și încearcă pasa...") în timpul inserării blocului `ChapterOrganizer`/`SectionNavigator`/`PredictPrompt`. Descoperit prin verificare programatică linie-cu-linie a fiecărui fișier editat contra versiunii `git show HEAD:...` — nu presupus corect doar pentru că `git diff --stat` arăta "1 deletion" fără investigație. **Reparat** prin reintroducerea paragrafului exact în poziția corectă (înaintea `PredictPrompt`, care îl referă explicit: „copilul de mai sus a încercat o pasă riscantă"). Reverificat programatic: 0 linii originale lipsă pe toate cele 3 capitole pilot.

## 3. Verificare structurală (STRUCTURAL_READINESS, nu HUMAN_VALIDATION)

Pe toate cele 3 pagini pilot compilate (`dist/web/volum/01/ch-010{1,3,6}/index.html`):
- Un singur `<main>` per document.
- Toate `href="#..."` din `ChapterOrganizer`/`SectionNavigator`/`QuickRecall` rezolvă la un `id` real prezent în pagină (verificat programatic, nu vizual).
- Ierarhie de titluri fără salturi (h1→h2→h3, niciodată h1→h3).
- `aria-controls` pe butonul `ExplanationToggle` referă exact `id`-ul `ElaborationBlock`-ului existent în pagină (CH-0103, CH-0106).
- `<details>/<summary>` prezente și corect structurate pentru `QuickRecall`/`PredictPrompt`.
- HTTP 200 pe toate cele 3 rute (server de preview local).

**Limitare onestă:** `AXE = NOT_RUN` — Playwright MCP indisponibil pe toată durata sesiunii. Nu s-a fabricat un audit vizual/tastatură prin browser real; verificarea de mai sus e structurală (HTML/HTTP), nu comportamentală.

## 4. Fidelitate de conținut

Verificare automată: fiecare linie non-titlu din versiunile originale (`git show HEAD:content/volume-01/chapter-0{1,3,6}.mdx`) există verbatim în fișierele editate. Rezultat, după repararea Defectului 2: **0 linii lipsă pe toate cele 3 capitole.**

## 5. Verdict pilot

CRITICAL = 0, MAJOR = 0 (ambele defecte găsite au fost reparate în aceeași buclă, înainte de acest raport). **PILOT: PASS.** Autorizat să continue la rollout complet (TASK-3306).
