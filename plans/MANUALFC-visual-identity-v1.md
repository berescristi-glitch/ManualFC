# ManualFC Visual Identity V1 — implementare structurală

## 1. Titlu și scop

Implementarea primei expresii reale a identității ManualFC pe homepage, pagina de orientare, pagina pedagogică de referință și laboratorul UI intern.

## 2. Context pentru un cititor nou

Aplicația Astro existentă consumă date canonice prin `app/src/lib/content-bridge.ts`. Worktree-ul conține modificări preexistente protejate, inclusiv în acel bridge; sprintul nu îl modifică. Identitatea aprobată este „Hybrid Editorial + Tactical”, cu Midnight Navy, Deep Navy, ManualFC Gold, Warm Off-White și Steel Grey. Browserul integrat nu este disponibil, astfel auditul inițial este bazat exclusiv pe cod, iar verificarea vizuală rămâne manuală.

## 3. Rezultatul verificabil

Rutele `/`, `/incepe-aici`, `/principii/variabilitatea-dezvoltarii-u11` și `/design-system` folosesc noua ierarhie editorială, motive tactice, moduri A/B distincte și componente pedagogice recognoscibile. Build-ul static, Astro check și testele proiectului trebuie să treacă.

## 4. Domeniu și non-obiective

Intră: tokens, CSS global/print, header/footer, componentele ChildMessage, CoachMessage, EvidenceBadge, QuickModePattern, cele patru rute și primitive locale de brand. Nu intră: cercetare, claims, surse, ID-uri, conținut canonic, Tactical Visual Engine, font remote, framework UI sau următorul task din registru.

## 5. Fișiere și module afectate

- `config/visual-tokens.json`
- `app/src/styles/{tokens,global,print}.css`
- `app/src/layouts/BaseLayout.astro`
- componentele de navigare, mesaj, evidence și Mode B din `app/src/components/`
- cele patru rute din `app/src/pages/`
- acest ExecPlan

## 6. Cercetare necesară

Nu este necesară cercetare nouă. UI-ul va reda numai evidence deja rezolvat de stratul canonic.

## 7. Model pedagogic

Compoziția separă observația factuală de interpretare, mesajul simplu pentru copil de raționamentul antrenorului și afirmația de limitele ei. Interfața susține ciclul observare–decizie–adaptare–verificare fără a schimba semantica pedagogică.

## 8. Design vizual și interactiv

Direcție: Hybrid Editorial + Tactical. Momentele de brand și teren sunt navy, lectura lungă este off-white, iar aurul marchează direcție și acțiune, nu status. Primitive: linie de pasă, marcaj de jucător, fragment de teren și coordonate. Responsive explicit la 1024, 768 și 390 px; print-ul elimină fundalurile fără a elimina etichetele.

## 9. Pași de implementare

1. Migrarea tokenilor canonici și a fundației tipografice/CSS.
2. Refacerea headerului, footerului și primitivei tactice.
3. Redesign structural homepage și diferențiere Mode A/B.
4. Refacerea paginii pedagogice și a componentelor Child/Coach/Evidence/Quick Field.
5. Adaptarea `/incepe-aici` și transformarea `/design-system` în Brand/UI Lab.
6. Validări, remediere, audit static responsive/accesibilitate și commit focalizat.

## 10. Validare și acceptare

- `npm run check` în `app/`
- `npm run build` în `app/`
- `python -m unittest discover -s tests -v`
- `python scripts/validate_content.py`
- `python scripts/validate_project.py`
- `git diff --check`
- audit static pentru headings, landmarks, focus, reduced motion, breakpoints și overflow

## 11. Progres

- [x] 2026-08-09 — instrucțiunile, skill-ul, documentele canonice și worktree-ul au fost auditate.
- [x] 2026-08-09 — auditul UI bazat pe cod a fost încheiat; browserul integrat este indisponibil.
- [x] 2026-08-09 — fundația de brand, tokenii și stilurile responsive/print au fost implementate.
- [x] 2026-08-09 — cele patru rute și componentele semnătură au fost redesenate structural.
- [x] 2026-08-09 — Astro check, build-ul static, testele de design system și diff check au trecut.
- [ ] Commitul focalizat este blocat de validatorul general preexistent: draftul protejat TASK-0502 are 9 erori de integritate.
- [x] 2026-08-09 — asset-ul aprobat `manualfc_homepage_hero_v1.png` a fost integrat byte-for-byte ca master public și transformat într-un hero funcțional cu HTML semantic real.
- [x] 2026-08-09 — logo-ul shield/M/football, wordmark-ul și favicon-ul ManualFC au fost implementate în header și footer.
- [x] 2026-08-09 — QA remediation V1.2: ghosting-ul raster a fost eliminat prin erasure opac local, wash-ul mobil a fost eliminat, iar headerul mobil a primit meniu accesibil.
- [x] 2026-08-09 — Composition remediation V1.3: strategia fragilă full-master + masking a fost înlocuită integral cu patru crop-uri deterministe, curate, derivate din master.
- [x] 2026-08-09 — Brand consolidation V1.4: masterele oficiale full logo și mark au fost importate, derivatele web/favion au fost create, iar identitatea aproximativă anterioară a fost eliminată din render.
- [x] 2026-08-09 — Official logo tagline V1.5: lockup-ul full afișează canonic `Cunoaștere. Pedagogie. Practică.` pe suprafețe dark/light; headerul mobil folosește prezentarea compactă, iar Brand Lab documentează full/compact/mark.
- [x] 2026-08-09 — Official lockup refinement V1.6: tagline-ul a fost ridicat la 11 px desktop, 8 px mobile și 12 px footer, rămâne vizibil la 390 px, iar Brand Lab prezintă explicit lockup-ul mobil final.

## 12. Descoperiri și surprize

- Worktree-ul are drafturi TASK-0502 și registre dirty protejate; redesignul poate evita toate suprapunerile, inclusiv `content-bridge.ts`.
- Fără browser integrat nu se pot face afirmații despre aspectul randat; QA vizual rămâne `PENDING_MANUAL_REVIEW`.
- Prima rulare de build a expus lanțul evidence incomplet al draftului TASK-0502. Pagina nu mai încearcă să rezolve acel lanț și redă un state neutru de indisponibilitate; pagina de referință continuă să rezolve integral evidence-ul valid TASK-0501.
- Suita completă rulează 154 teste: 153 trec, iar testul de compatibilitate al validatorului general eșuează exclusiv din cauza celor 9 erori preexistente TASK-0502. Testele specifice design system-ului trec 8/8.
- Masterul hero are SHA-256 `8A58755F8ABA6F214DD3A953CB9F7395F979385F6E14FD94C5575E7364022552`; copia publică și copia din build sunt identice byte-for-byte.
- Captura de QA V1.2 a arătat că gradientul inițial lăsa headline-ul raster să treacă și colora fotografia pe mobil. Remedierea nu mai aplică overlay uniform peste copil sau teren: două zone navy opace șterg UI-ul raster desktop, iar fotografia mobilă rămâne nefiltrată sub o tranziție locală.
- Etichetele de inspector raportate în captură nu există în surse sau build; sursa lor este tooling-ul de captură, nu aplicația.
- QA-ul real V1.2 a demonstrat că masking-ul full-master rămâne fragil. V1.3 nu mai randează deloc masterul complet: scena dreaptă folosește crop-ul `(830,115)–(1672,941)`, nocturna `(0,120)–(140,620)`, terenul `(0,730)–(1672,941)`, iar scena mobilă `(890,115)–(1672,941)`.
- Asset-urile oficiale de logo sunt RGBA 1536×1024. Bounds-urile web, cu padding de 13 px peste geometria alpha, sunt `(189,322)–(1236,635)` pentru lockup și `(527,206)–(1010,771)` pentru mark. Masterele rămân byte-identice cu inputurile.

## 13. Jurnal de decizii

- 2026-08-09 — Se folosește un stack geometric local, fără font remote. Motiv: zero dependențe și funcționare statică; selecția finală a fontului rămâne de revizuit.
- 2026-08-09 — Se păstrează contractul existent al bridge-ului și se redesenează doar stratul de prezentare. Motiv: protecția worktree-ului și a semanticii canonice.
- 2026-08-09 — Imaginea aprobată rămâne master PNG nemodificat; nu se generează WebP/AVIF în acest task. Motiv: masterul are 1,9 MB, iar fidelitatea vizuală este prioritară; orice derivat trebuie comparat vizual înainte de adoptare.
- 2026-08-09 — Textul și navigația raster sunt mascate local, iar UI-ul este reconstruit semantic în HTML. Pe mobil, art-direction folosește partea dreaptă a masterului pentru a păstra copilul, tricoul și mingea fără duplicarea headline-ului raster.
- 2026-08-09 — Pentru V1.2, masking-ul gradual desktop a fost înlocuit cu suprafețe opace dimensionate după coordonatele masterului și cu o decupare separată a nocturnei. Motiv: ghosting zero fără alterarea contrastului cinematic din dreapta.
- 2026-08-09 — La maximum 700 px, navigația desktop este înlocuită de `details/summary` și un panou vertical semantic. Motiv: operare keyboard-native, ARIA clar și touch targets de 52 px fără JavaScript hidratat.
- 2026-08-09 — Strategia V1.2 de erasure/masking al masterului complet este retrasă. Hero-ul desktop compune crop-uri curate pe fundal `#0D1B2A`, iar mobilul folosește o regiune de conținut solidă urmată de crop-ul mobil nefiltrat. Motiv: ghosting imposibil structural și integritate cromatică deterministă.
- 2026-08-09 — `ManualFCLogo.astro` randează exclusiv asset-uri canonice PNG. Pentru dark surfaces, numai pixelii navy ai wordmark-ului „Manual” sunt derivați în Warm Off-White; shield-ul, mingea, proporțiile și `FC` rămân neschimbate. SVG-ul aproximativ și componenta mark temporară au fost eliminate.
- 2026-08-09 — Tagline-ul canonic este text HTML poziționat în spațiul transparent de sub wordmark, aliniat după shield, fără modificarea rasterului oficial. Varianta `full` îl afișează, `compact` și `mark` nu; sub 700 px headerul ascunde tagline-ul pentru a proteja accesul la MENIU și a preveni overflow-ul.
- 2026-08-09 — Decizia V1.5 de a ascunde tagline-ul în headerul mobil este retrasă după QA real. La 390 px, full lockup-ul are 205 px lățime și tagline de 8 px pe un singur rând; MENIU păstrează un touch target de 44 px, iar headerul crește moderat la minimum 78 px.

## 14. Rezultat și retrospectivă

Implementarea structurală este completă în worktree: brand tokens, navigare, footer, homepage, pagina pedagogică de referință, orientarea și laboratorul intern. `npm run check` și `npm run build` trec; build-ul generează 10 pagini. Responsive CSS există pentru tabletă, mobil și pragul critic de 390 px, iar print-ul păstrează etichetele și structura fără dependență de culoare.

Hero-ul aprobat este acum intrarea homepage-ului. Masterul fotografic este livrat nemodificat, iar `HomepageHero.astro` compune crop-urile curate, art-direction, headline-ul, copy-ul și CTA-urile reale. `ManualFCLogo.astro` consumă lockup-ul și mark-ul oficial pentru identitatea reutilizabilă din chrome-ul produsului.

QA vizual rămâne `PENDING_MANUAL_REVIEW`, deoarece browserul integrat nu este disponibil. Sprintul nu poate fi comis în această execuție: gate-ul obligatoriu `python -m unittest discover -s tests -v` rămâne roșu din cauza stării preexistente, protejate, a TASK-0502. Niciun fișier de research sau conținut canonic nu a fost modificat de redesign.
