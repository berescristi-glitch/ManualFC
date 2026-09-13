# Wave-2.1 — TASK-2706 completion patch

## Scop

Închide cele două reziduuri documentate onest în `reports/audits/MANUALFC_PHASE27_WAVE2_FINAL.md`: harta vizuală de suprafață a ședinței și variantele de 60 minute — fără să lărgească scopul Wave-2.

## Decizie de arhitectură — harta terenului

Randator complet dinamic (nu diagrame canonice + variante desenate manual): `app/src/lib/surface-map.ts` transformă direct rezultatul deja calculat de `computeGroupConfiguration` (TASK-2705) — `playingAreas`, `areaDimensions`, `coachPositioning` — într-o specificație de layout (dreptunghiuri așezate unul lângă altul, markere de antrenor, marcaj de echipament). Motivul: 6 efective × 2 variante de antrenor × 5 exerciții ar însemna 60+ diagrame desenate manual, care ar ieși din sincron cu configuratorul la prima schimbare de date. Un randator comun nu poate ieși din sincron, pentru că nu are cifre proprii.

## Progres

- [x] `surface-map.ts` + `SurfaceMap.astro` — SVG accesibil (title/desc), etichete text (nu doar culoare) pentru zonă activă/antrenor/echipament/marjă de siguranță.
- [x] Secțiune „Harta terenului” pe ambele pagini de ședință, cu selector de efectiv (8-18) și antrenori (1/2), randate static la build (12 variante × segmente), comutate cu JS minimal — același tipar ca Mod teren.
- [x] Variante de 60 minute pentru SES-0001 și SES-0002: câmp canonic nou `duration_variant_60min` (doar suprascrieri de timp + motiv per segment; conținutul pedagogic — titlu, mesaj, observare — rămâne aceeași sursă unică, nu duplicat).
- [x] Comutator 75/60 minute pe pagina de ședință, care actualizează și link-ul spre Mod teren (`?durata=60`); Mod teren citește parametrul și arată timpii corespunzători, cu bucla pedagogică completă neschimbată.
- [x] Regresie 75 minute verificată: timpii canonici neschimbați pe ambele sedinte.
- [x] Totaluri 60 minute verificate: însumează exact 60, fără goluri sau suprapuneri, pe ambele sedinte.

## 2 defecte reale găsite și reparate prin testare browser directă

1. **Regula CSS proprie suprascria atributul `[hidden]`** — `.harta-variant { display: grid }` avea aceeași specificitate ca stilul implicit al browserului pentru `[hidden]` și câștiga fiindcă venea mai târziu în cascadă, astfel încât toate cele 12 variante (36 diagrame SVG) erau vizibile simultan, iar pagina ajungea la 18864px. Confirmat prin `getComputedStyle` (`display: grid` pe un element cu `hidden`), nu presupus din capturi de ecran. Reparat cu `.harta-variant[hidden] { display: none }`.
2. **`<main>` dublu imbricat** — moștenit din Wave-1/Wave-2, pagina de ședință folosea propriul `<main class="gs-session">` în interiorul `<main>`-ului deja furnizat de `BaseLayout`. Reparat la `<div>`, limitat la acest fișier (nu o cruciadă pe restul site-ului).

## Limită

Harta terenului nu acoperă exercițiile fără `exercise_ids` (segmentele de încălzire/reflecție/joc liber) — corect, pentru că acelea nu au o zonă de teren distinctă de configurat.
