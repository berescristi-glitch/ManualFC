# Cadrul de competențe al Antrenorului

**Versiune:** 1.0.0 · **Task de referință:** TASK-2904 · **Statut:** Architecture, complet la nivel de arhitectură

Prefix ID: `COACH-C`. Fără scor numeric, fără niveluri de rang (regulă permanentă). Fiecare competență se poate lega de exercițiu, ședință, Field Mode, Reflecție sau curriculum Academy prin ID stabil.

**Notă de reconciliere:** `docs/knowledge/COACH_DOMAIN_MAP.md` (scris înaintea acestui document) folosește referințe punctuale de competență (`COACH-C09`, `COACH-C25` etc.) aliniate informal la numerele de domeniu. Numerotarea oficială și definitivă e cea de mai jos (C01-C18, ordinea cerută de specificația PHASE-29 §15). Corespondența exactă domeniu→competență e în tabelul final al acestui document, nu în numerele menționate în harta de domeniu.

---

### COACH-C01 — Observație
**Definiție:** Descrie ce se întâmplă pe teren înainte de a interpreta.
**Cunoaștere necesară:** COACH-D02, COACH-D03. **Legătură pedagogie:** PED-C01.
**Indicatori:** notează comportamentul exact, nu concluzia. **Anti-tipar:** diagnostichează instant fără verificare.
**Exemplu:** „Doi jucători se apropie la 1m de purtător" (deja exemplu canonic, `CONTENT_TAXONOMY.md`).
**Practică legată:** `Problem.observable_behavior`. **Dovadă:** CRITICAL. **Reflecție:** Ce am văzut, fără cauza pe care o presupun?

### COACH-C02 — Formularea problemei
**Definiție:** Transformă o observație într-o problemă lucrabilă, testabilă.
**Cunoaștere necesară:** COACH-D04. **Legătură pedagogie:** PED-C01, PED-C02.
**Indicatori:** formulează comportamental („nu se repoziționează după pasă"), nu ca etichetă.
**Anti-tipar:** problemă formulată ca trăsătură de caracter.
**Practică legată:** `problem-library.json` (deja implementat). **Dovadă:** HIGH.

### COACH-C03 — Selecția intervenției
**Definiție:** Alege intervenția potrivită dintre mai multe ipoteze posibile, nu prima idee.
**Cunoaștere necesară:** COACH-D05. **Legătură pedagogie:** PED-C02.
**Indicatori:** ia în calcul cel puțin 2 explicații posibile înainte de a acționa.
**Anti-tipar:** o singură ipoteză, aplicată automat de fiecare dată.
**Practică legată:** `possible_explanations` (deja în schema `problem`). **Dovadă:** HIGH.

### COACH-C04 — Chestionare
**Definiție:** Folosește întrebarea ghidată ca instrument de predare, nu doar retoric.
**Cunoaștere necesară:** COACH-D07. **Legătură pedagogie:** PED-C04.
**Indicatori:** întrebare deschisă înaintea corecției directe. **Anti-tipar:** întreabă și răspunde singur imediat.
**Practică legată:** `content/volume-03/ch-0302`. **Dovadă:** HIGH.

### COACH-C05 — Feedback
**Definiție:** Oferă informație specifică legată de acțiune, nu evaluare generală.
**Cunoaștere necesară:** COACH-D08. **Legătură pedagogie:** PED-C03, PED-C06.
**Indicatori:** descrie acțiunea + o schimbare posibilă. **Anti-tipar:** „bravo"/„nu așa" fără informație.
**Practică legată:** `child_message`. **Dovadă:** HIGH.

### COACH-C06 — Cueing
**Definiție:** Folosește reper extern de atenție, nu instrucție tehnică internă.
**Cunoaștere necesară:** COACH-D09. **Legătură pedagogie:** PED-C03.
**Indicatori:** „uită-te la con" nu „pune piciorul la 45°". **Anti-tipar:** prescrie un unghi exact al corpului.
**Practică legată:** `exact_cue` (deja implementat, EX-0003). **Dovadă:** HIGH.

### COACH-C07 — Demonstrație
**Definiție:** Arată o variantă posibilă fără să o impună ca unică formă corectă.
**Cunoaștere necesară:** COACH-D10.
**Indicatori:** prezintă demonstrația ca exemplu, nu ca șablon. **Anti-tipar:** „așa se face", ca unică soluție validă.
**Dovadă:** MEDIUM.

### COACH-C08 — Proiectare de exercițiu
**Definiție:** Construiește un exercițiu care amplifică problema reală, păstrând cuplajul percepție-acțiune.
**Cunoaștere necesară:** COACH-D12, COACH-D14. **Legătură pedagogie:** PED-D02-S08 (transfer).
**Indicatori:** opoziție activă reală, nu coregrafie fără adversar. **Anti-tipar:** exercițiu analitic decuplat de joc.
**Practică legată:** `content/volume-04/chapter-01.mdx (CH-0401)` + EX-0001-0005 (deja implementat). **Dovadă:** MEDIUM.

### COACH-C09 — Manipularea constrângerilor
**Definiție:** Ajustează spațiu/număr/reguli pentru a produce comportamentul țintă.
**Cunoaștere necesară:** COACH-D13.
**Indicatori:** schimbă o singură constrângere, observă efectul. **Anti-tipar:** schimbă totul simultan, nu poate atribui efectul.
**Practică legată:** `content/volume-04/chapter-02.mdx (CH-0402)`. **Dovadă:** MEDIUM.

### COACH-C10 — Organizare de grup
**Definiție:** Organizează grupul pentru siguranță și învățare, folosind logică de rotație.
**Cunoaștere necesară:** COACH-D17, COACH-D18. **Legătură pedagogie:** PED-D08.
**Indicatori:** folosește Group Configurator, nu improvizație. **Anti-tipar:** grupe arbitrare, fără rotație.
**Practică legată:** `docs/architecture/GROUP_CONFIGURATOR.md` (deja implementat). **Dovadă:** HIGH.

### COACH-C11 — Predarea percepției și deciziei
**Definiție:** Antrenează ce vede și decide copilul, nu doar execuția.
**Cunoaștere necesară:** COACH-D22, COACH-D23.
**Indicatori:** verifică ce a văzut copilul înainte de a corecta decizia. **Anti-tipar:** corectează orice decizie diferită de a antrenorului.
**Practică legată:** PRB-0003, Decision Engine (deja implementat, flagship). **Dovadă:** CRITICAL.

### COACH-C12 — Progresie/regresie
**Definiție:** Are pregătit un pas mai ușor și unul mai greu pentru fiecare exercițiu.
**Cunoaștere necesară:** COACH-D16. **Legătură pedagogie:** PED-C10.
**Indicatori:** folosește regresia la primul semn de blocaj repetat. **Anti-tipar:** insistă pe aceeași formă când nu funcționează.
**Practică legată:** câmpurile `progression`/`regression` (deja implementat). **Dovadă:** MEDIUM.

### COACH-C13 — Diferențiere
**Definiție:** Adaptează sarcina la copilul din fața lui fără separare vizibilă.
**Cunoaștere necesară:** COACH-D29. **Legătură pedagogie:** PED-C10.
**Indicatori:** variantă individuală discretă. **Anti-tipar:** grupare vizibilă pe „nivel".
**Dovadă:** HIGH.

### COACH-C14 — Verificarea transferului
**Definiție:** Confirmă apariția comportamentului în joc liber, nu doar în exercițiul structurat.
**Cunoaștere necesară:** COACH-D25. **Legătură pedagogie:** PED-D02-S08.
**Indicatori:** observă în segmentul de joc liber, nu doar în exercițiu. **Anti-tipar:** declară succes după o repetiție reușită izolată.
**Practică legată:** `SessionReflection.transferState` (deja implementat, TASK-2803). **Dovadă:** CRITICAL — transferul real rămâne `FIELD_INPUT_REQUIRED`.

### COACH-C15 — Evaluare
**Definiție:** Evaluează comportament observabil folosind criterii explicite, nu impresie globală.
**Cunoaștere necesară:** COACH-D26.
**Indicatori:** folosește criterii scrise (`ASM-0001`). **Anti-tipar:** „a fost bine azi", fără criteriu.
**Practică legată:** Assessment (deja implementat). **Dovadă:** MEDIUM.

### COACH-C16 — Planificarea ședinței
**Definiție:** Leagă exercițiile într-o progresie coerentă spre un obiectiv de ședință.
**Cunoaștere necesară:** COACH-D27, COACH-D28.
**Indicatori:** tranziții logice între exerciții, obiectiv unic de ședință. **Anti-tipar:** exerciții disparate, fără temă.
**Practică legată:** SES-0001/0002 + Session Workspace (deja implementat). **Dovadă:** HIGH — `season-plans` fără conținut azi.

### COACH-C17 — Reflecție (a antrenorului)
**Definiție:** Reflectează asupra propriei intervenții — a observat înainte de a acționa? a supra-corectat?
**Cunoaștere necesară:** COACH-D32, COACH-D33. **Legătură pedagogie:** PED-C13.
**Indicatori:** identifică un moment concret de supra-intervenție sau non-intervenție utilă.
**Anti-tipar:** reflectă doar asupra rezultatului copiilor, niciodată asupra propriei acțiuni.
**Practică legată:** Reflection V2 (specificat, neimplementat). **Dovadă:** MEDIUM.

### COACH-C18 — Dezvoltare profesională
**Definiție:** Alege activ o competență de dezvoltat, urmărește progresul propriu.
**Cunoaștere necesară:** COACH-D34.
**Indicatori:** declară o competență-țintă pentru perioada următoare. **Anti-tipar:** repetă același stil fără intenție de schimbare.
**Practică legată:** Coach Development (fundație, neimplementat — vezi `KNOWLEDGE_AND_COMPETENCY_KPI_MODEL.md` K3). **Dovadă:** MEDIUM.

---

## Corespondență domeniu → competență (corectează referințele din `COACH_DOMAIN_MAP.md`)

| Domeniu (COACH-D) | Competență primară (COACH-C) |
|---|---|
| D02, D03 | C01 |
| D04 | C02 |
| D05 | C03 |
| D06 (nu intervine) | C03 (parte din selecția intervenției — a nu interveni e o alegere de intervenție) |
| D07 | C04 |
| D08 | C05 |
| D09 | C06 |
| D10 | C07 |
| D12, D13 | C09 |
| D14 | C08 |
| D16 | C12 |
| D17, D18 | C10 |
| D19 | C01 (aplicat la poziționare) |
| D22, D23 | C11 |
| D25 | C14 |
| D26 | C15 |
| D27, D28 | C16 |
| D29 | C13 |
| D31 | — (climat motivațional e ieșire comună a mai multor competențe, nu are competență dedicată; legat de PED-C05/C08) |
| D32, D33 | C17 |
| D34 | C18 |

## Matrice de acoperire (competență × practică curentă)

| Competență | Conectată la practică azi? |
|---|---|
| C01, C02, C11, C14 | DA — nucleul Decision Engine |
| C05, C06 | DA — `child_message`, `exact_cue` |
| C08, C09, C12 | DA — schema exercițiu |
| C10 | DA — Group Configurator |
| C15 | DA — Assessment |
| C16 | PARȚIAL — SES-0001/0002 există, `season-plans` gol |
| C03, C04, C07, C13 | CONCEPTUAL — prezent în copy, fără ID de competență în date |
| C17, C18 | NU — necesită Reflection V2 și Coach Development |
