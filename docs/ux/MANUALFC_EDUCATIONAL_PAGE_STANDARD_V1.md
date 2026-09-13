# ManualFC — Educational Page Standard V1 (Gate 3-4: Competing Architectures, Decision, Canonical Standard)

Baza factuală: `MANUALFC_EDUCATIONAL_PAGE_RESEARCH.md`, `LEARNING_UX_EVIDENCE_MATRIX.md`, `MANUALFC_EDUCATIONAL_DESIGN_PRINCIPLES.md`. Baza arhitecturală reală: componentele existente în `app/src/components/` (23 componente, dintre care 12 nefolosite deloc — vezi inventarul de mai jos) și pagina `principii/[slug].astro`, singurul șablon deja bogat în componente din tot codul.

---

## 1. Trei arhitecturi concurente

### Model A — LINEAR EDITORIAL (versiune puternică)

Un flux unic, de sus în jos, fără mecanisme de disclosure. Ordinea actuală a capitolelor (scenariu → Ce știm → secțiune structurală → Ce le spun și de ce → Instrumentul practic → Ce nu putem concluziona → Transfer) rămâne neschimbată în structură, dar primește: casetă de orientare la început (advance organizer, P12), semnalizare vizuală distinctă pentru categoriile de conținut (idee centrală / acțiune de antrenor / observație / nu presupune / exemplu / dovadă), diagrame inline lângă text (P3), breadcrumb, măsură tipografică 60-75ch (P7). Nimic se ascunde niciodată. Pagina poate fi lungă (3000-6000 cuvinte) dar navigabilă doar prin scroll + breadcrumb.

**Puncte forte:** cel mai aproape de structura deja acceptată/validată editorial (PHASE-31); zero risc de omisiune de conținut (P1); implementare cea mai simplă și mai ieftină de întreținut; cel mai aliniat cu benchmarking-ul platformelor de coaching fotbalistic reale (Coaching Manual, PDP — ambele flux liniar unic, fără TOC).
**Sacrificiu:** niciun mecanism de comprimare pentru antrenorul experimentat (P2 neaplicat); niciun TOC pentru orientare rapidă pe pagini de 6000 de cuvinte; nicio suprafață de recall rapid separată (P11 neaplicat).

### Model B — LAYERED PROGRESSIVE DISCLOSURE (versiune puternică)

Fiecare secțiune non-esențială e într-un accordion cu stare implicită închisă; conținutul e împărțit pe cele patru straturi TEREN/ÎNȚELEGE/APROFUNDEAZĂ/DOVEZI ca tab-uri sau acordeoane separate; scopul explicit e reducerea lungimii vizibile a paginii.

**Puncte forte:** pagina pare mult mai scurtă la prima vizualizare; utilizatorul poate alege exact ce strat vrea.
**Sacrificiu (dovedit, nu presupus):** exact pattern-ul pe care cercetarea îl respinge cel mai ferm — risc de omisiune a conținutului esențial (#1, #26), cost cognitiv suplimentar de navigare mai mare pentru novici (#28), conflație engagement↔învățare (pagina *pare* mai ușoară, nu e dovedit că e mai bine învățată). Această variantă e construită "puternic" ca exercițiu de comparație corectă, dar cercetarea îi limitează sever aplicabilitatea la conținut esențial.

### Model C — HYBRID LEARNING + REFERENCE (versiune puternică)

Un singur document canonic (nu straturi duplicate), cu:
- Nucleu procedural mereu vizibil (P1) — niciodată în spatele unui click.
- Un toggle persistent de pagină, nu accordion-per-secțiune: **"Explicație completă" ⇄ "Doar esențialul"** (P2, P13) care comprimă/extinde DOAR blocurile de elaborare marcate ca atare (rațiunea completă pe mai multe dimensiuni, context extins) — nucleul (limbaj exact, comportament urmărit, riscuri, verificare, instrumentul practic, limitele) rămâne vizibil în ambele stări.
- TOC local cu marcaj de secțiune curentă (P8), vizibil doar de la o lungime minimă de pagină în sus, hide-on-scroll pe mobil.
- Diagrame inline lângă text (P3).
- O secțiune finală distinctă **"Recall rapid"** (P11): 3-5 întrebări/repere cu reveal `<details>`, formulate ca angajament, nu ca rezumat pasiv.
- Un prompt opțional de pre-testare (P10) plasat înaintea unui punct de decizie din scenariu, maxim unul per capitol.
- "Ce nu putem concluziona" exclus explicit din toggle-ul de comprimare — rămâne mereu vizibil (P4).

**Puncte forte:** singurul model care implementează simultan toate cele 17 principii din Gate 2 fără compromisuri forțate; oferă atât modul LEARN (citire completă) cât și modul RECALL (secțiunea de recall rapid) și APPLY (nucleul procedural mereu vizibil) fără a construi produse separate.
**Sacrificiu:** cea mai mare complexitate de implementare dintre cele trei (componente noi, JS minim pentru toggle — vezi §5).

---

## 2. Matricea de decizie

Scală: PUTERNIC / MODERAT / SLAB (nu scoruri numerice inventate — regula §48).

| Criteriu | Model A Linear | Model B Layered | Model C Hybrid |
|---|---|---|---|
| Findability (P0 imediat) | PUTERNIC | MODERAT (depinde de titluri) | PUTERNIC |
| Comprehensiune | PUTERNIC | SLAB (risc omisiune) | PUTERNIC |
| Suport pentru retenție | MODERAT | SLAB | PUTERNIC (recall rapid) |
| Aplicare | PUTERNIC | MODERAT | PUTERNIC |
| Orientare | MODERAT (fără TOC) | MODERAT | PUTERNIC |
| Încărcare cognitivă | MODERAT (pagină lungă fără scaping) | SLAB (cost decizie navigare) | MODERAT-PUTERNIC (toggle reduce elaborare fără a ascunde nucleul) |
| Mobil | PUTERNIC | SLAB (atingeri suplimentare) | MODERAT-PUTERNIC |
| Accesibilitate | PUTERNIC (nimic de construit greșit) | MODERAT (risc de implementare incorectă a acordeonului) | MODERAT (necesită implementare corectă a toggle-ului + TOC) |
| Reference use (revenire) | SLAB | MODERAT | PUTERNIC (recall rapid dedicat) |
| Deep linking | MODERAT (doar anchors) | MODERAT | PUTERNIC (anchors + TOC + recall) |
| Complexitate implementare | SLAB (cea mai simplă) | MODERAT | MODERAT-RIDICATĂ |
| Mentenanță de conținut | PUTERNIC (un singur flux) | MODERAT (straturi duplicate de întreținut) | PUTERNIC (un singur document canonic, doar marcaje) |
| Calitate premium | MODERAT | MODERAT | PUTERNIC |

---

## 3. Decizie — câștigător

**MODEL C — HYBRID LEARNING + REFERENCE câștigă.**

**De ce a câștigat:** este singurul model care respectă simultan P1 (nucleul mereu vizibil — cerința cea mai riguros fundamentată din cercetare) ȘI oferă un răspuns real, dovedit-adiacent, la problema reală semnalată de expertise reversal (P2) — fără a ceda la Modelul B, care rezolvă aceeași grijă prin exact mecanismul (acordeon implicit închis) pe care cercetarea îl respinge cel mai ferm pentru conținut esențial. Modelul A e complet sigur dar nu răspunde deloc nevoii reale a antrenorului experimentat sau nevoii de recall rapid (P11, cea mai bine fundamentată idee nouă din cercetare) — l-ar lăsa needited.

**Ce sacrifică:** complexitate de implementare mai mare (un toggle de pagină cu JS minim, o componentă nouă de recall, extinderea `SectionNavigator` cu scroll-spy). Acesta e un cost acceptat explicit, nu ignorat.

**Când se folosește o alternativă:** Modelul A rămâne varianta corectă pentru conținut foarte scurt (sub ~1500 cuvinte, fără secțiuni de elaborare extinsă) unde toggle-ul de comprimare nu ar avea ce comprima — de exemplu pagini scurte de tip index/introducere. Modelul B nu se recomandă în nicio circumstanță pentru conținut de lecție ManualFC; rămâne document de comparație, nu opțiune vie.

---

## 4. Flux Pedagogul vs. Antrenorul

### Flux Pedagogul (înțelegerea copilului) — CONFIRMAT, nu schimbat structural

```
SCENARIU DE TEREN
→ CE ȘTIM (sinteză hedged)
→ [advance organizer scurt, dacă pagina > ~2500 cuvinte]
→ SECȚIUNE STRUCTURALĂ PROPRIE CAPITOLULUI (variază: protocol, 3 reacții, etc.)
→ CE ÎI SPUI COPILULUI ȘI DE CE (8 subsecțiuni fixe — NUCLEU, mereu vizibil)
→ INSTRUMENTUL PRACTIC (NUCLEU, mereu vizibil)
→ CE NU PUTEM CONCLUZIONA (NUCLEU, mereu vizibil, exclus din toggle)
→ TRANSFER ÎN MECI
→ [RECALL RAPID — nou, secțiune finală]
```

Motiv pentru NEschimbarea ordinii: dovada de instrucție ghidată + ancorare (P17) susține exact acest tipar; inversarea la "concept întâi" nu are suport.

### Flux Antrenorul (viitor, PHASE-32, doar proiectat aici ca extensie a aceluiași sistem de design — NU autorat acum)

```
PROBLEMĂ PROFESIONALĂ
→ COMPETENȚA VIZATĂ
→ OBSERVĂ
→ ÎNȚELEGE (mecanism)
→ DECIDE
→ INTERVINE (NUCLEU)
→ EXEMPLU
→ ANTI-PATTERN (exemplu contrastant — P14)
→ PRACTICĂ
→ VERIFICĂ (NUCLEU)
→ REFLECTĂ
→ DOVEZI (NUCLEU, mereu vizibil)
→ [RECALL RAPID]
```

**Diferență explicită față de Pedagogul:** Antrenorul include un slot dedicat de "anti-pattern" (P14) chiar în flux, nu doar ca subsecțiune de riscuri — pentru că literatura de contrastare (Durkin & Rittle-Johnson, Schwartz & Bransford) e mai direct aplicabilă unei decizii profesionale de coaching (o alegere corectă vs. o greșeală comună de antrenor) decât unei interpretări a comportamentului unui copil. Ambele fluxuri împart același sistem de design (componente, tipografie, toggle, recall) dar NU aceeași secvență cognitivă — conform regulii §51 din specificație.

---

## 5. Standardul canonic de pagină

### 5.1 Scopul paginii
O lecție ManualFC transformă o constatare de cercetare parțială într-un comportament de antrenor observabil, verificabil, cu limitele lui explicite — pentru un antrenor care o citește prima dată (LEARN) și pentru unul care revine să găsească un răspuns în câteva secunde (RECALL) sau se pregătește pentru o ședință (APPLY).

### 5.2 Tipuri de pagină
Un singur tip de șablon („Lecție") pentru volumele Pedagogul/Antrenorul — regula §55 (evită proliferarea de șabloane). `principii/`, `gold-standard/exercitii/`, `rezolva-pe-teren/` rămân tipuri distincte existente (probleme/exerciții/ședințe), neatinse de acest task.

### 5.3 Priorități de informație (P0-P3)

| Prioritate | Conținut | Stare implicită |
|---|---|---|
| P0 — Imediat | Titlu, idee centrală, breadcrumb | VISIBLE_BY_DEFAULT |
| P1 — Înțelegere de bază | Scenariu, Ce știm, secțiune structurală, limbaj exact, comportament urmărit, riscuri de evitat, instrumentul practic | VISIBLE_BY_DEFAULT |
| P2 — Aprofundare | Justificarea completă pe toate dimensiunile, context teoretic extins | AVAILABLE_ONE_ACTION_AWAY (toggle „Explicație completă") |
| P3 — Dovadă/referință | Ce nu putem concluziona, citări individuale cu sursă completă | P3a „Ce nu putem concluziona" = VISIBLE_BY_DEFAULT (P4); P3b citări individuale = DEEP_REFERENCE (`<details>` per citare, ca la `principii/[slug].astro` deja) |

### 5.4 Clasificarea tipurilor de conținut (regula §24)

| Tip conținut | Vizibilitate |
|---|---|
| Idee centrală | VISIBLE_BY_DEFAULT |
| Scenariu | VISIBLE_BY_DEFAULT |
| Ce știm (sinteză) | VISIBLE_BY_DEFAULT |
| Comportament observabil al copilului | VISIBLE_BY_DEFAULT |
| Nu presupune | VISIBLE_BY_DEFAULT |
| Acțiune de antrenor | VISIBLE_BY_DEFAULT |
| Limbaj exact | VISIBLE_BY_DEFAULT |
| Justificare completă (toate dimensiunile) | AVAILABLE_ONE_ACTION_AWAY (toggle) |
| Exemplu/caz | VISIBLE_BY_DEFAULT |
| Anti-pattern (Antrenorul) | VISIBLE_BY_DEFAULT |
| Verificare | VISIBLE_BY_DEFAULT |
| Reflecție (recall rapid) | secțiune finală proprie, VISIBLE_BY_DEFAULT ca secțiune, reveal-uri individuale DEEP_REFERENCE |
| Rezumat de dovezi | VISIBLE_BY_DEFAULT |
| Citări individuale complete | DEEP_REFERENCE |
| Limitări ale cercetării | VISIBLE_BY_DEFAULT (parte din „Ce nu putem concluziona") |
| Related content/practică | VISIBLE_BY_DEFAULT, la finalul paginii |
| Next action | VISIBLE_BY_DEFAULT, ultima secțiune |

### 5.5 Navigare
- Breadcrumb: DA (cost redus, sigur — #10).
- TOC: DA pentru pagini >~2500 cuvinte, cu scroll-spy obligatoriu (P8) — altfel NU se adaugă.
- Sticky: doar TOC-ul, hide-on-scroll-down pe mobil.
- Anchors: DA, ID stabil per secțiune fixă (deep linking).
- Progress bar: NU în V1 (P9, prioritate scăzută, fără dovadă).
- Previous/Next capitol: DA, la finalul paginii.

### 5.6 Tipografie
- Body: 16-18px, line-height ≥1.5.
- Măsură: 60-75ch (păstrează `72ch` existent, nu extinde).
- Titluri: ierarhie clară h1→h2→h3 fără salturi, front-loaded.

### 5.7 Semnalizare/culoare
Categorii cu tratament vizual distinct (regula §34, minimizat): IDEE CENTRALĂ, ACȚIUNE DE ANTRENOR, NU PRESUPUNE, EXEMPLU/CAZ, DOVADĂ/LIMITE. Culoarea nu e niciodată singurul semnal (P15) — fiecare are și o etichetă textuală/simbol.

### 5.8 Multimedia
Regula permanentă §37: text singur insuficient dacă relația spațială contează → diagramă; timp/mișcare esențial → animație (`ConceptLoop`); comportament uman de coaching → video (viitor, neautorat acum). Toate media inline, lângă text (P3).

### 5.9 Componentă de comprimare (toggle „Explicație completă")
Un singur toggle per pagină (nu per secțiune), persistent vizual (nu ascuns în meniu), stare implicită **deschisă** (extinsă) — regula P2: implicit sigur pentru novice. Marchează explicit blocurile de „justificare completă" ca fiind cele afectate; restul paginii nu se mișcă.

### 5.10 Recall rapid
Secțiune finală, titlu propriu, 3-5 perechi întrebare/reper → răspuns cu `<details>/<summary>`, formulare de angajament explicit ("Gândește-te înainte să extinzi").

### 5.11 Accesibilitate — vezi `EDUCATIONAL_COMPONENT_CONTRACT.md` pentru contractul complet.

### 5.12 Performanță
Toggle-ul și scroll-spy-ul TOC se implementează cu JS minim (vanilla, fără framework client), consistent cu arhitectura Astro static-first existentă (regula §62-63). Nicio hidratare de componentă grea.

### 5.13 Deep linking
ID-uri stabile pe fiecare `<h2>`/`<h3>` de secțiune fixă (ex. `#ce-le-spun-si-de-ce`, `#instrumentul-practic`) — permite trimiterea unei secțiuni specifice, nu doar a paginii întregi.

---

## 6. Wireframe-uri textuale

### 6.1 Pedagogul Desktop (1440/1280)

```
┌─────────────────────────────────────────────────────────┐
│ AppHeader                                                │
├─────────────────────────────────────────────────────────┤
│ ← Cuprins Volumul 01                    [breadcrumb]     │
│                                                           │
│  H1: Emoțiile copilului: frustrare, anxietate...         │
│  [Idee centrală, 1-2 propoziții, tratament vizual distinct]│
│                                                           │
│  ┌── Advance organizer (dacă >2500 cuvinte) ──┐          │
│  │ În acest capitol: 3 reacții distincte,      │          │
│  │ o formulă de răspuns, un instrument de citire│         │
│  └──────────────────────────────────────────────┘        │
│                                                           │
│  [TOC sticky, colț dreapta sus la scroll, cu highlight]  │
│                                                           │
│  Scenariu de teren (proză)                                │
│                                                           │
│  ## Ce știm                                               │
│  proză + [diagramă inline dacă relevantă]                │
│                                                           │
│  ## Secțiune structurală proprie                          │
│                                                           │
│  ## Ce le spun și de ce  ⟵ NUCLEU, mereu vizibil          │
│    ### Formularea exactă        [tratament: CoachMessage] │
│    ### Sensul profesional                                 │
│    ### Problema rezolvată                                 │
│    ### Ce observă/decide antrenorul                       │
│    ### Comportamentul urmărit                             │
│    [toggle: "▸ Explicație completă"] ⟵ comprimă doar asta:│
│    ### Justificarea completă (comprimabil)                │
│    ### Riscuri și formulări de evitat                     │
│    ### Verificarea înțelegerii                             │
│                                                           │
│  ## Instrumentul practic  ⟵ NUCLEU                        │
│                                                           │
│  ## Ce nu putem concluziona  ⟵ NUCLEU, exclus din toggle  │
│                                                           │
│  ## Transfer în meci                                       │
│                                                           │
│  ## Recall rapid  (nou)                                   │
│    Î: Ce faci dacă un copil aruncă mingea după o greșeală? │
│    [▸ vezi răspunsul]                                      │
│    (3-5 perechi)                                           │
│                                                           │
│  [← Capitol anterior]        [Capitol următor →]          │
├─────────────────────────────────────────────────────────┤
│ AppFooter                                                │
└─────────────────────────────────────────────────────────┘
```

### 6.2 Pedagogul Mobile (390px)

```
┌───────────────────────┐
│ AppHeader (compact)   │
├───────────────────────┤
│ ← Cuprins             │
│                       │
│ H1 (2-3 rânduri)      │
│ [Idee centrală]       │
│                       │
│ [TOC: buton "Pe       │
│  această pagină ▾",   │
│  NU sticky permanent, │
│  se ascunde la scroll │
│  jos, apare la scroll │
│  sus]                 │
│                       │
│ Scenariu              │
│                       │
│ ## Ce știm            │
│ [diagramă: lățime     │
│  completă, sub text]  │
│                       │
│ ## Ce le spun...      │
│  NUCLEU vizibil       │
│  [toggle full-width,  │
│   touch target 44px]  │
│                       │
│ ## Instrumentul       │
│   practic — NUCLEU    │
│                       │
│ ## Ce nu putem        │
│   concluziona— NUCLEU │
│                       │
│ ## Recall rapid       │
│  [detalii tap-to-     │
│   reveal, 44px target]│
│                       │
│ [◄ Anterior|Următor►] │
├───────────────────────┤
│ AppFooter             │
└───────────────────────┘
```
Fără scroll orizontal la niciun element (P16); nucleul procedural accesibil fără a deschide vreo secțiune comprimată.

### 6.3 Antrenorul Desktop (proiectat, neautorat)

```
[Aceeași shell/tipografie/toggle/TOC ca Pedagogul]
PROBLEMĂ PROFESIONALĂ → COMPETENȚA → OBSERVĂ → ÎNȚELEGE
→ DECIDE → INTERVINE (NUCLEU) → EXEMPLU
→ ANTI-PATTERN (NOU, tratament vizual contrastant, roșu/gri lângă verde)
→ PRACTICĂ → VERIFICĂ (NUCLEU) → REFLECTĂ → DOVEZI (NUCLEU)
→ RECALL RAPID
```

### 6.4 Antrenorul Mobile (proiectat, neautorat)
Aceeași adaptare ca 6.2, cu blocul ANTI-PATTERN afișat ca o casetă alăturată (stacked pe mobil) exemplului corect, nu ca tab separat.

### 6.5 Stare „Recall rapid" (Quick/Recall state)

```
┌── Recall rapid: Emoțiile copilului ──────────┐
│ Î1: Ce faci dacă un copil aruncă mingea?      │
│    [▸ vezi răspunsul]                          │
│ Î2: Cum deosebești rușinea de vinovăție?       │
│    [▸ vezi răspunsul]                          │
│ Î3: Ce NU spui unui copil frustrat?            │
│    [▸ vezi răspunsul]                          │
│                                                 │
│ [Vezi capitolul complet →]                     │
└─────────────────────────────────────────────────┘
```
Accesibil direct via ancoră (`#recall-rapid`) pentru revenire rapidă — link-abil separat de restul paginii, dar NU rută separată (P11, decizie §7 mai jos).

### 6.6 Stare „Deep Evidence" (Toggle extins + citări)

```
[... nucleu vizibil ca mai sus ...]
### Justificarea completă  [▾ Explicație completă — activ]
  Emoțional: ...
  Cognitiv: ...
  Social: ...
  Pedagogic: ...

## Ce nu putem concluziona
  proză + [EvidenceBadge HIGH/MODERATE/LOW/...]
  <details><summary>Sursă: Aune et al. 2025 →</summary>
    Locator complet, tip studiu, populație, limitări
  </details>
  (per citare, DEEP_REFERENCE, pattern deja existent la principii/[slug].astro)
```

---

## 7. Decizie explicită: recall rapid = secțiune pe aceeași pagină, NU rută separată

Conform benchmarking-ului (#39, UpToDate: zona de rezumat repetată la început ȘI sfârșit, pe ACEEAȘI pagină lungă) și evidenței de scrolling (#12: o singură pagină preferată pentru un fir narativ unic), secțiunea „Recall rapid" e o secțiune ancorabilă (`#recall-rapid`) la finalul aceleiași pagini de capitol — NU o rută nouă (`/volum/01/ch-0106/recall`). Aceasta evită proliferarea de rute (regula §55) și păstrează un singur document canonic de întreținut (regula §76 — nu construi conținut duplicat).
