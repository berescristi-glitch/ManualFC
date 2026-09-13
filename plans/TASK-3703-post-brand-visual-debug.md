# TASK-3703 — Post-Brand Visual Debug, Regression Repair & Acceptance

## 1. Titlu și scop

Închide, cu dovadă de browser real, cele două defecte deja cunoscute și declarate ca limitări în TASK-3701 (overflow orizontal ~8px pe homepage, contrast insuficient pe indicatorul „01"), verifică riguros că migrarea de brand (TASK-3701) nu a introdus regresii vizuale/de accesibilitate pe restul suprafețelor, și confirmă integritatea completă a activelor de brand. Rezultatul observabil: homepage fără overflow la toate breakpoint-urile, indicatorul „01" trece WCAG AA, un audit real de browser pe 10 suprafețe × 5 viewport-uri fără regresii, și un raport de acceptare cu verdict explicit.

## 2. Context pentru un cititor nou

- TASK-3701 (`reports/task-reports/TASK-3701.md`, `DECISIONS.md` DEC-0080) a migrat identitatea de brand la artwork-ul clipboard/M/minge și a găsit, dar declarat explicit ca în afara scopului, un overflow homepage de 8px și o violare Axe de contrast pe un indicator „01", ambele confirmate nelegate de logo/header/footer.
- TASK-3702 (investigație inline, neînregistrată formal până acum — reparată în cadrul acestui task, vezi §12) a găsit corupție Git preexistentă (obiecte loose corupte legate de `506cf3b1`, `d7474ded9`, și un ref de checkpoint intern `refs/codex/...`) — verdict `BLOCKED` pentru reparare (fără remote, fără sursă alternativă), zero impact asupra HEAD-ului curent. Acest task NU atinge baza de obiecte Git, multi-pack-index sau `refs/codex/*`.
- Identitatea curentă de brand: `docs/brand/MANUALFC_BRAND_SYSTEM_V2.md`, manifest `public/brand/manualfc/logo/logo-assets.json`.
- Commit-ul curent (`ca62b60`) conține atât TASK-3601 (audit de integritate) cât și TASK-3701 (migrarea de brand).

## 3. Rezultatul verificabil

- Homepage: 0px overflow orizontal documentat la 320/390/768/1280/1440.
- Indicatorul „01": contrast ≥ 3:1 (text mare/bold) sau ≥ 4.5:1 (text normal), verificat cu Axe.
- Audit real de browser pe 10 suprafețe × 5 viewport-uri fără regresii noi.
- Verificare programatică a integrității activelor de brand (hash-uri, dimensiuni, referințe).
- `reports/task-reports/TASK-3703.md`, `reports/audits/MANUALFC_POST_BRAND_VISUAL_ACCEPTANCE.md`, acest plan actualizat.
- Verdict final explicit (`PASS` / `PASS_WITH_DECLARED_NON_BLOCKING_LIMITATIONS` / `FAIL` / `BLOCKED`).

## 4. Domeniu și non-obiective

**Intră:** CSS-ul secțiunii hero a homepage-ului (`app/src/pages/index.astro` și/sau componenta ei), contrastul indicatorului „01", auditul de regresie pe suprafețele listate în prompt, verificarea de integritate a activelor de brand, validarea completă.

**Nu intră:** baza de obiecte Git / multi-pack-index / `refs/codex/*` (TASK-3702 rămâne o limitare declarată, neatinsă), conținut pedagogic, redesenul artwork-ului master, orice funcționalitate nouă, orice pagină/componentă fără legătură demonstrată cu defectele vizate.

## 5. Fișiere și module afectate

De investigat: `app/src/pages/index.astro` (secțiunea `.approved-hero`/`.ball-flight`/`.desktop-art`/`.field-strip`), componenta care randează indicatorul „01" (căutare necesară). Posibil afectate: CSS-ul acelor componente. Fișiere noi: acest plan, cele două rapoarte.

## 6-7. Cercetare / model pedagogic

Nu se aplică — task tehnic (CSS/accesibilitate/QA), fără conținut pedagogic nou.

## 8. Design vizual și interactiv

Nu se introduc elemente vizuale noi; se repară geometria existentă (overflow) și contrastul unui indicator existent, păstrând design-ul intenționat.

## 9. Pași de implementare

1. Citire context obligatoriu (finalizat).
2. Faza 1 — reproducere reală cu browser (Chrome via CDP + Playwright), documentare cauză-rădăcină per defect.
3. Faza 2 — reparație minimă, țintită, verificată vizual.
4. Faza 3 — audit complet post-reparație pe 10 suprafețe × 5 viewport-uri + Axe.
5. Faza 4 — verificare programatică a integrității brandului.
6. Faza 5 — build și validare completă.
7. Faza 6 — Preview Vercel (dacă infrastructura permite).
8. Guvernanță: rapoarte, registry, DECISIONS.md, PROJECT_STATUS.md.

## 10. Validare și acceptare

Vezi criteriile de acceptare din promptul TASK-3703 (overflow=0, contrast AA, integritate brand, 0 regresii, Axe 0, build/teste PASS, Preview verificat sau limitare declarată, corupția Git neatinsă, raport cu dovezi).

## 11. Progres

- [x] 2026-09-01 — Context citit, plan creat.
- [x] 2026-09-01 — Faza 1 — reproducere: 2 defecte cunoscute reproduse + 2 defecte suplimentare găsite (incepe-aici overflow, spatiul-meu contrast), toate 4 confirmate preexistente prin `git show 0466ea9`.
- [x] 2026-09-01 — Faza 2 — reparație: toate 4 reparate cu tiparul `--scrollbar-w` (DEC-0076) sau token existent (`--color-text-muted`, `--color-brand-gold`).
- [x] 2026-09-01 — Faza 3 — audit regresie: 50/50 combinații rută×viewport PASS.
- [x] 2026-09-01 — Faza 4 — integritate brand: toate verificările PASS.
- [x] 2026-09-01 — Faza 5 — build/validare: toate comenzile PASS.
- [x] 2026-09-01 — Faza 6 — Preview: verificat live (`dpl_EsAg7inWWokUqNvnt2ufhbxFWzBC`), blocaj de infrastructură nelegat rezolvat cu `.vercelignore`.
- [x] 2026-09-01 — Guvernanță și raport final.

## 12. Descoperiri și surprize

- TASK-3702 nu fusese niciodată înregistrat formal (fără raport, fără intrare în registru) — doar raportat inline utilizatorului. Reparat în cadrul acestui task: creat `reports/task-reports/TASK-3702.md` retroactiv și înregistrat în generator, pentru ca referința din promptul TASK-3703 să corespundă unui artefact real.

## 13. Jurnal de decizii

- **Decizie:** nu se atinge baza de date Git pentru corupția din TASK-3702, conform instrucțiunii explicite. **Motiv:** risc de pierdere de date fără sursă de recuperare verificată; scop explicit exclus de utilizator. **Alternative:** niciuna evaluată. **Efect:** limitare declarată, neschimbată. **Data:** 2026-09-01.

## 14. Rezultat și retrospectivă

Toate cele 4 defecte vizuale validate (2 declarate în TASK-3701, 2 găsite în timpul auditului obligatoriu al acestui task) au fost reparate la cauza-rădăcină, cu dovadă de precedență (`git show`) și verificare completă de browser real (50/50 combinații PASS). Integritatea brandului confirmată programatic. Preview verificat live. Singura abatere de la scopul strict inițial: extinderea reparației dincolo de cele 2 defecte enumerate explicit în Faza 2 a promptului, la alte 2 defecte de exact același tip descoperite chiar de auditul obligatoriu al acestui task — motivată de obiectivul general („închide toate defectele vizuale cunoscute") și de riscul minim (tipar deja validat de 2 ori anterior în cod). Rămâne nereparat, declarat onest: reflow sub ~200px CSS-pixeli (dincolo de referința WCAG de 320px, ar necesita revizuire mai largă a mai multor componente independente) și corupția Git din TASK-3702 (inclusiv o a 12-a instanță găsită incidental), ambele explicit în afara mandatului acestui task.
