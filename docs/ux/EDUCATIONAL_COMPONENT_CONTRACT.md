# ManualFC — Educational Component Contract (Gate 3-4)

Regula de bază (§29): pentru fiecare componentă, „Ce job cognitiv sau informațional face asta?" — dacă răspunsul e doar „arată premium", componenta se elimină.

## 1. Inventar existent — decizie de reutilizare

23 componente au fost auditate (`app/src/components/`). 12 sunt complet nefolosite ("dead code"). Decizie per componentă:

| Componentă | Stare | Decizie pentru Educational Page System V1 |
|---|---|---|
| `CoachMessage` / `ChildMessage` | Folosite (principii) | **REFOLOSIT** pentru „Formularea exactă" — deja face exact acest job |
| `EvidenceBadge` | Folosit | **REFOLOSIT** pentru marcaj de încredere per-citare (P15, #40) |
| `SectionNavigator` | Folosit, DAR fără scroll-spy | **EXTINS** — se adaugă highlight de secțiune curentă (P8); fără asta nu se reutilizează conform regulii §11 din matrice |
| `QuickModePattern` | Folosit (principii) | **NEFOLOSIT aici** — format cu 6 sloturi fixe, specific altui tip de pagină; nu se forțează pe capitole |
| `PedagogicalBlock` + 9 wrapper-e (`WhyThisMatters`, `ObserveThis`, `DecisionToLearn`, `CommonMistake`, `PhraseToAvoid`, `UnderstandingCheck`, `Adaptation`, `MatchTransfer`, `EvidenceNote`) | Dead code, NICIODATĂ folosite | **EVALUAT ȘI RESPINS pentru reutilizare directă** — construite pentru un format necunoscut, niciodată integrat; a le repune acum ar însemna 9+ tipuri de casetă vizuală competitive, exact riscul semnalat de regula §34 („minimizează numărul de semnale vizuale concurente"). Rămân dead code documentat, nu șterse fără autorizare separată de curățenie. |
| `DeepLearningPattern` | Dead code | **RESPINS** — șablon de articol cu 6 sloturi fixe, suprapus parțial cu structura MDX deja existentă; adoptarea lui ar duplica sistemul de conținut (regula §5: nu redesena sisteme fără conflict real) |
| `ModeCard` | Dead code | **RESPINS** — card CTA generic, fără job cognitiv specific acestui task |
| `SourceReference` | Dead code | **REFOLOSIT** pentru chip-uri de citare individuală în secțiunea de dovezi (job clar: autor/an/locator) |
| `TacticalDiagram`, `ConceptLoop`, `ProblemVisual`, `SurfaceMap`, `TacticalMotif` | Folosite (alte tipuri de pagină) | **DISPONIBILE, refolosite selectiv** unde un capitol are nevoie reală de diagramă (P3) — niciun capitol nou nu e obligat să aibă unul dacă nu există relație spațială/temporală de explicat |
| `CoachActions` | Folosit | **NEFOLOSIT pe capitole în V1** — toolbar de salvare/favorite legat de exerciții/ședințe, fără echivalent clar pentru o pagină de lecție; adăugarea lui ar fi „pare premium" fără job cognitiv nou definit acum |
| `Breadcrumb` | Existent, nefolosit pe volum/ | **ADOPTAT** pe capitolele de volum (P § navigare — cost redus, sigur) |

## 2. Componente NOI necesare (buget minim, fiecare cu job cognitiv explicit)

| Componentă nouă | Job cognitiv | Prioritate conținut | Stare implicită | Comportament mobil | Accesibilitate | Când NU se folosește |
|---|---|---|---|---|---|---|
| `ChapterOrganizer` | Orientare la intrare — idee centrală + hartă scurtă a secțiunilor (P12) | P0 | Vizibil | Full-width, sub H1 | Landmark `<aside aria-label="Prezentare generală">`, nu interactiv | Capitole sub ~1500 cuvinte fără elaborare de comprimat |
| `ExplanationToggle` | Comprimă/extinde blocurile de elaborare marcate (P2, P13) | Controlează P2 | Extins (deschis) implicit | Full-width, target ≥44px | Buton real, `aria-expanded`, `aria-controls`, conținutul controlat folosește `hidden`, nu doar CSS | Pagini fără nicio secțiune de „justificare completă" extinsă |
| `ElaborationBlock` | Marchează un bloc de conținut ca elaborare comprimabilă de `ExplanationToggle` (nu independent — un singur toggle de pagină controlează toate instanțele) | P2 | Vizibil când toggle-ul e extins | — | `id` referit de `aria-controls` al toggle-ului părinte | Conținut care aparține nucleului (P1) — niciodată pentru „Ce nu putem concluziona" |
| `QuickRecall` | Secțiune finală de recuperare activă — întrebare/reper întâi, răspuns cu reveal (P10, P11) | Secțiune proprie, P0 ca prezență, conținutul revelat e DEEP_REFERENCE | Întrebările vizibile, răspunsurile ascunse (`<details>`) | Target reveal ≥44px | `<details>/<summary>` nativ — accesibil implicit, fără ARIA custom necesar | Nu se pune pe fiecare secțiune — o singură instanță, la finalul capitolului |
| `PredictPrompt` | Prompt de pre-testare/predicție înaintea unui punct de decizie din scenariu (P10) | P1 (parte din scenariu) | Întrebare vizibilă, răspuns în `<details>` | La fel | La fel ca `QuickRecall` | Maxim 1 per capitol — nu transformă pagina în quiz (regula §39) |
| `SectionNavigator` (extins) | TOC local cu marcaj de secțiune curentă (scroll-spy) (P8) | Navigare, nu conținut | Vizibil, sticky doar dacă pagina >~2500 cuvinte | Colapsabil, hide-on-scroll-down | Landmark `<nav aria-label="Pe această pagină">`, link-urile active marcate `aria-current="true"` | Pagini scurte |

**Total componente noi: 5** (`ChapterOrganizer`, `ExplanationToggle`, `ElaborationBlock`, `QuickRecall`/`PredictPrompt` ca variante ale aceleiași componente de bază `RevealPrompt`, plus extinderea `SectionNavigator`). Acesta e bugetul minim cerut de regula §63 — nu cele ~14 componente candidate listate inițial în specificație, dintre care multe (`LessonHeader`, `KeyIdea`, `ChildObservation`, `DoNotAssume`, `CoachAction`, `ExactLanguage`, `CaseStudy`, `EvidenceSummary`, `EvidenceDetail`, `ReflectionPrompt`, `ApplyNextSession`, `RelatedKnowledge`) sunt deja acoperite de proza structurată existentă (titluri de subsecțiune fixe) și NU au nevoie de o componentă vizuală separată — a le construi ar fi exact „arată premium" fără job cognitiv nou, respins de regula §29.

## 3. Checklist de accesibilitate pentru `ExplanationToggle` (contract minim WCAG 2.1 AA)

Structural/ARIA:
- Trigger e un `<button>` real.
- `aria-expanded="true|false"`, sincronizat la fiecare toggle.
- `aria-controls` referă `id`-urile blocurilor `ElaborationBlock` afectate.
- Fiecare `ElaborationBlock` colapsat folosește atributul `hidden`, nu doar `display:none` prin CSS.

Tastatură:
- Enter/Space comută starea (comportament nativ de `<button>`).
- Focus vizibil pe buton (SC 2.4.7), neobscurat de vreun header sticky (SC 2.4.11).

Vizual/stare:
- Starea e comunicată prin text ("Explicație completă" ⇄ "Doar esențialul") + iconiță, nu doar culoare (SC 1.4.1).
- Target ≥44×44px (practică recomandată, peste minimul AA de 24px).
- Tranziția respectă `prefers-reduced-motion`.

Politică de conținut:
- Niciodată nu comprimă: limbaj exact, comportament urmărit, instrumentul practic, „Ce nu putem concluziona".
- Comprimă doar: justificarea completă pe toate dimensiunile, context teoretic extins.

`QuickRecall`/`PredictPrompt` folosesc `<details>/<summary>` nativ — deja conform WCAG fără ARIA suplimentar, cu condiția ca `<summary>` să conțină text descriptiv (nu „click aici").

## 4. Strategie carduri vs. flux editorial

Regula §28: evită „totul e un card". Pentru capitolele de lecție, formatul rămâne document editorial continuu (Model C, §5 din standard) — cardurile se folosesc DOAR pentru: (a) linkuri de „capitol anterior/următor" la finalul paginii, (b) eventual `ChapterOrganizer` dacă beneficiază de grupare vizuală. Nu se introduc carduri pentru secțiunile de conținut principal (Ce știm, Ce le spun și de ce, etc.) — acestea rămân proză structurată cu titluri, nu cutii separate, pentru a păstra continuitatea conceptuală (regula §72: „a fragmentat cardurile argumentul?").
