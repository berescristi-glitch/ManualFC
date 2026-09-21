# TASK-3718 — Build and Validate the Second Complete ManualFC Training Theme

## 1. Titlu și scop

Construiește a doua temă de antrenament completă — principii, probleme ale Deciziei Engine, exerciții, ședințe, reflecție și transfer — care dovedește că modelul de conținut ManualFC se repetă pe o problemă de joc genuin diferită, fără să slăbească standardele pedagogice, editoriale, tehnice, de accesibilitate sau offline deja stabilite.

## 2. Context pentru un cititor nou

- Repo canonic: `E:/ManualFC-clean`, HEAD de pornire `7c68a24a7fc90203c1b66463760be50e89b55408` (rezultatul `TASK-3714`).
- **Abatere explicită de la roadmap, autorizată de utilizator, declarată onest:** `docs/roadmap/MANUALFC_CANONICAL_ROADMAP.md` (Faza 4) spune explicit „Theme selection: decided in Phase 3, from pilot evidence — needs validation, not pre-selected here" și „Do not start a second theme... until pilot behavior — not internal judgment — says so." `TASK-3714` a confirmat că nu există dovezi reale de pilotare (`PILOT STATUS = NOT_STARTED`, `BLOCKED`). Acest task (`TASK-3718`) procedează totuși, la cererea explicită și informată a utilizatorului, care a declarat clar: „the pilot is intentionally being skipped for the next product-building phase" și „do not claim that the product has been validated by real coaches." Această decizie e a utilizatorului, nu a asistentului — respectată aici, documentată transparent, nu ascunsă.
- Selecția temei se face deci pe bază de **dovezi interne** (inventarul de conținut existent, problemele orfane ale Deciziei Engine, principiile deja dezvoltate), exact criteriile alternative oferite explicit de acest task când dovada de pilotare lipsește.

## 3. Selecția temei — 3 candidați evaluați

| Criteriu | A: Presiune și acoperire în apărare | B: 1v1 ofensiv (dribling ca decizie) | C: Finalizarea — decizia în fața porții |
|---|---|---|---|
| Relevanță pentru antrenor | Înaltă — apărarea e la fel de cerută ca posesia | Înaltă | Înaltă |
| Adiacență pedagogică (model percepție-decizie) | Foarte înaltă — principii deja scrise în exact acest model | Medie — necesită cercetare nouă de la zero | Medie — risc de a aluneca spre exercițiu tehnic izolat |
| Distincție față de „Sprijinul și unghiul de pasă" | Înaltă — problemă de joc genuin diferită (a nega spațiu, nu a crea spațiu) | Înaltă | Înaltă |
| Profunzime de conținut deja disponibilă | **Înaltă** — 2 probleme orfane (`PRB-0004`, `PRB-0006`) + 3 principii canonice complete, deja evidențiate (`presiune-si-acoperire`, `protejarea-centrului`, `tranzitia-la-pierderea-mingii`), cu `evidence_claim_ids`/surse reale deja în `research/claims.json`/`research/sources.json` | Nulă — ar necesita cercetare nouă completă în acest task | Nulă — la fel |
| Transferabilitate în joc reprezentativ | Înaltă — testabilă direct în jocuri reduse | Înaltă | Medie — necesită spațiu de finalizare dedicat |
| Efort de schemă/implementare | Scăzut — schema exercițiu/ședință e deja agnostică de temă | Scăzut (schemă) dar risc înalt de cercetare fabricată | Scăzut (schemă) dar risc înalt |
| Risc de duplicare a conținutului existent | Scăzut | Scăzut | Scăzut |
| Capacitate de a construi o temă completă acum, responsabil | **Înaltă** — fundația există deja | Scăzută — ar cere inventarea întregii baze de dovezi în acest task | Scăzută — la fel |

**Decizie: Candidatul A — „Presiune și acoperire în apărare"** (`theme: "apararea-presiune-si-acoperire"`). Motiv decisiv: e singurul candidat cu bază de dovezi deja reală și verificată (principii + probleme deja scrise, evidențiate, validate în taskuri anterioare), eliminând riscul de a inventa cercetare sub presiunea acestui task — exact riscul pe care `AGENTS.md`/`CODEX.md` îl interzic explicit.

## 4. Definiția și scopul temei

**„Presiune și acoperire în apărare"** — cum recunoaște și răspunde un copil de 10-11 ani la pierderea controlului defensiv: încetinirea unui adversar 1v1 (nu atacul imediat al mingii), coordonarea presiune+acoperire între doi apărători, reorganizarea imediată după pierderea mingii, și protejarea drumului central spre poartă — ca decizie percepție-decizie, nu ca tehnică izolată de tackle. Aceeași temelie pedagogică ca „Sprijinul și unghiul de pasă", aplicată unei probleme de joc genuin diferite (a nega opțiunile adversarului, nu a crea opțiuni proprii).

**Principii reutilizate (deja canonice, deja evidențiate — niciunul nou inventat):** `principle.presiune-si-acoperire`, `principle.protejarea-centrului`, `principle.tranzitia-la-pierderea-mingii`, `principle.transfer-autonom-cooperare` (reutilizat, ca și în tema 1, pentru exercițiile de transfer).

**Probleme ale Deciziei Engine întărite (deja existente, orfane până acum):** `PRB-0004` („După pierderea mingii, jucătorii se opresc"), `PRB-0006` („Primul apărător presează fără acoperire").

**Evaluare nouă:** `ASM-0002` — „Evaluarea presiunii și acoperirii în apărare", 5 criterii, aceeași structură calitativă ca `ASM-0001`.

## 5. Decizie de arhitectură — de la o singură evaluare la mai multe

**Constatare, nu presupunere:** `getGoldStandardAssessment()` din `content-bridge.ts` era complet hardcodată la o singură evaluare (`ASM-0001`), consumată fără parametru în 6 locuri (`discovery-index.ts`, `problem-library.ts` [`validateProblemGraph`], `gold-standard/evaluare/[id].astro`, `gold-standard/index.astro`, `gold-standard/sedinte/[id].astro`, `spatiul-meu/reflectie.astro`). Pagina `evaluare/[id].astro` avea proza complet hardcodată la tema 1 (títlu, „EX-0001–EX-0005", „SES-0001"/„SES-0002", maparea C1→EX-0001...C5→EX-0005 scrisă literal în șablon, nu derivată din date).

**Decizie:** generalizare minimă, justificată, fără schimbare de schemă JSON (`assessment.schema.json` era deja suficient de generic): `getGoldStandardAssessment(id?)` primește un parametru opțional (implicit `'ASM-0001'`, păstrând neschimbat comportamentul paginilor specifice temei 1 — `gold-standard/index.astro`); adăugat `getGoldStandardAssessments()` (plural) pentru listare completă; `evaluare/[id].astro` devine complet dinamică (`getStaticPaths` mapează peste toate evaluările, proza derivă exercițiile/ședințele legate din datele evaluării, nu din text scris manual); `sedinte/[id].astro` rezolvă evaluarea corectă prin `assessment_ref`-ul propriilor exerciții legate, nu implicit; `reflectie.astro` verifică criteriile fiecărei probleme față de evaluarea ei reală (`assessment_links`), nu una fixă; `problem-library.ts`/`discovery-index.ts` iterează peste toate evaluările.

**Decizie de rutare — păstrată, nu schimbată:** paginile de detaliu ale exercițiilor/ședințelor rămân la `/gold-standard/exercitii/[id]`/`/gold-standard/sedinte/[id]` pentru **ambele** teme — sunt deja motorul generic de randare, indiferent de temă (identificat prin `id`, nu prin cale). Schimbarea acestor căi ar fi rupt toate URL-urile deja live pentru `EX-0001`–`EX-0015`/`SES-0001`–`SES-0006`, interzis explicit („preserve compatibility with existing routes"). Tema 2 primește propria pagină de identitate/aterizare la o cale nouă, curată: `/aparare/` (mirror structural al `/gold-standard/index.astro`, nu un redesign), cu legături reciproce către `/gold-standard/`, `/rezolva-pe-teren/` și `/principii/` — integrare de navigare minimă, fără a atinge antetul global (ar fi fost un redesign, interzis explicit).

## 6. Inventarul de conținut

**10 exerciții noi** (`EX-0016`–`EX-0025`, continuă numerotarea plată existentă, nu un prefix nou de temă):

| ID | Titlu | Nivel | Relație | Principiu | Problemă |
|---|---|---|---|---|---|
| EX-0016 | Încetinește, nu ataca mingea | introducere | 1v1 | protejarea-centrului | (fundație pentru PRB-0006) |
| EX-0017 | Unul încetinește, celălalt protejează | consolidare | 2v1 | presiune-si-acoperire | PRB-0006 |
| EX-0018 | Schimbă rolul când mingea se mută | consolidare | 2v2 | presiune-si-acoperire | PRB-0006 |
| EX-0019 | Nu vă eliminați amândoi cu aceeași acțiune | avansare | 2v2 | presiune-si-acoperire + protejarea-centrului | PRB-0006 |
| EX-0020 | Al doilea apărător acoperă drumul, nu omul | avansare | 3v2 | protejarea-centrului | PRB-0006 |
| EX-0021 | Primele două secunde după pierdere | avansare | 3v3 | tranzitia-la-pierderea-mingii | PRB-0004 |
| EX-0022 | Cine e aproape, cine protejează centrul | avansare | 4v3 | tranzitia-la-pierderea-mingii + protejarea-centrului | PRB-0004 |
| EX-0023 | Recuperează forma, nu doar mingea | avansare | 4v4 | protejarea-centrului + presiune-si-acoperire | PRB-0004 + PRB-0006 |
| EX-0024 | Joc mic 4v4 cu observare defensivă | transfer | 4v4 | transfer-autonom-cooperare | PRB-0004 + PRB-0006 |
| EX-0025 | Joc mic 6v6 cu zonă de protejat | transfer | 6v6 | transfer-autonom-cooperare | PRB-0004 + PRB-0006 |

**4 ședințe noi** (`SES-0007`–`SES-0010`):

| ID | Titlu | Combină |
|---|---|---|
| SES-0007 | Apărarea individuală: încetinește, nu ataca | EX-0016, EX-0017 |
| SES-0008 | Coordonarea a doi apărători | EX-0018, EX-0019, EX-0020 |
| SES-0009 | Primele secunde după pierderea mingii | EX-0021, EX-0022, EX-0023 |
| SES-0010 | Transfer complet: apărarea în joc real (capstone) | EX-0024, EX-0025 |

**1 evaluare nouă:** `ASM-0002`, 5 criterii (C1→EX-0016/17, C2→EX-0018, C3→EX-0019/20, C4→EX-0021/22, C5→EX-0023/24/25).

**1 pagină nouă de identitate temă:** `app/src/pages/aparare/index.astro`.

## 7. Domeniu și non-obiective

**Intră:** cele de mai sus + generalizarea `content-bridge.ts`/paginile enumerate în §5 + întărirea `problem-library.json` pentru `PRB-0004`/`PRB-0006` + teste noi + validare completă + fresh clone.

**Nu intră:** nicio schemă JSON nouă; nicio temă a treia; nicio arhitectură multi-age; nicio autentificare/bază de date/analytics; nicio pretenție că tema a fost validată de antrenori reali (pilotul rămâne `NOT_STARTED`); nicio modificare a antetului/footer-ului global; niciun asset vizual nou (aceeași convenție `visual_assets: PENDING` ca EX-0006–EX-0015).

## 9. Pași de implementare

1. Context, selecția temei, decizia de arhitectură — finalizat (acest plan).
2. Redactare 10 exerciții noi.
3. Redactare 4 ședințe noi.
4. Redactare `ASM-0002`.
5. Întărire `problem-library.json` (`PRB-0004`, `PRB-0006`).
6. Generalizare `content-bridge.ts` + cele 5 fișiere consumatoare.
7. Pagină nouă `/aparare/index.astro` + legături reciproce.
8. Teste noi (conținut + validare de arhitectură multi-assessment).
9. Validare completă (schemă, V2, pytest, check, build, browser+axe, offline, linkuri, sitemap).
10. Fresh clone + guvernanță + raport final.

## 11. Progres

- [x] Context, inventar, selecția temei (3 candidați evaluați, motiv documentat).
- [x] Decizie de arhitectură (multi-assessment, rutare păstrată, pagină nouă de identitate).
- [ ] 10 exerciții noi
- [ ] 4 ședințe noi
- [ ] ASM-0002
- [ ] problem-library.json întărit
- [ ] content-bridge.ts + 5 fișiere generalizate
- [ ] /aparare/index.astro
- [ ] Teste noi
- [ ] Validare completă
- [ ] Fresh clone + guvernanță + raport

## 13. Jurnal de decizii

- **Decizie:** tema aleasă e „Presiune și acoperire în apărare", nu 1v1 ofensiv sau finalizare. **Motiv:** singurul candidat cu bază de dovezi deja reală (principii + probleme deja evidențiate), eliminând riscul de cercetare fabricată sub presiunea acestui task. **Efect:** zero surse/evidence_claim_ids noi inventate — toate cele reutilizate erau deja reale înainte de acest task.
- **Decizie:** rutele de detaliu exercițiu/ședință rămân la `/gold-standard/exercitii|sedinte/[id]` pentru ambele teme; tema 2 primește doar o pagină de identitate separată la `/aparare/`. **Motiv:** schimbarea căilor existente ar fi rupt URL-uri live, interzis explicit. **Efect:** zero risc de regresie de rutare pentru cele 21 de rute deja publicate.
- **Decizie:** `content-bridge.ts` generalizat la mai multe evaluări, cu compatibilitate completă înapoi (parametru opțional, implicit ASM-0001). **Motiv:** o singură evaluare hardcodată era o limitare arhitecturală reală, descoperită prin citirea codului, nu presupusă — o a doua temă REALĂ cere propria evaluare, corect rutată. **Efect:** `gold-standard/index.astro` (specifică temei 1) rămâne complet neschimbată în comportament; doar paginile generice (`evaluare/[id]`, `sedinte/[id]`, `reflectie.astro`) devin corect sensibile la temă.
- **Decizie:** nu se leagă niciun exercițiu nou de o problemă nouă a Deciziei Engine — se întăresc exclusiv `PRB-0004`/`PRB-0006`, deja existente. **Motiv:** evită orice nevoie de `evidence_claim_ids` noi sau cercetare nouă în acest task. **Efect:** consecvent cu decizia de selecție a temei (§3).
