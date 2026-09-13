# Gold Standard Readiness Audit — Sprijinul și unghiul de pasă

**Task:** TASK-2201
**Status:** COMPLETE
**Data:** 2026-08-12
**Domeniu:** Primul sistem pedagogic vertical complet al ManualFC — testul dacă arhitectura existentă (principii, cercetare, dovezi) poate produce exerciții, ședințe și evaluare reale, nu doar capitole.

## 0. Recuperarea stării repository-ului

`HEAD` la momentul auditului: `a5251c6` (`POST_GEMINI_TRUST_RESTORED = YES`). `git status --short` confirmă doar fișierele permanent-murdare din design freeze (vezi `plans/MANUALFC-visual-identity-v1.md` pentru listă); niciun alt fișier nesalvat. `git diff`/`git diff --cached` conțin doar diff-ul de design freeze preexistent, neatins.

Toate cele 4 volume publicate: `FIELD_REVIEW_READY`.

## 1. Ce există deja despre „Sprijinul și unghiul de pasă"

O căutare exhaustivă (`Sprijinul și unghiul de pasă`, `unghi de pasă`, `support angle`, `Gold Standard`, `sprijin`) a găsit:

### 1.1 Un lanț de taskuri planificate, nefolosit (`TASK-0410`–`TASK-0418`, `PHASE-04`)

Acest lanț a fost inserat în registru la migrarea inițială a roadmapului (`ROADMAP_MIGRATION_REPORT.md`), cu status `PENDING`, 0 tentative, niciun output pe disc. Depinde de `TASK-0304` (specificația unui „motor de animații") și `TASK-0407` (harness Playwright), ambele **tot `PENDING`** — arhitectură de infrastructură dintr-o fază de planificare timpurie, dinaintea consolidării arhitecturii curente (Astro static + content-bridge + principii JSON). Outputurile declarate (`app/src/pages/prototip/sprijin-unghi-pasa.astro`, `data/prototypes/support-passing-angle.json`) ar crea o pagină izolată, paralelă cu arhitectura reală de conținut (`content/volume-0N/chapter-0M.mdx` + `data/principles/*.json` + `content-bridge.ts`).

**Verdict:** `SUPERSEDE`. Acest lanț nu e șters (politica forward-only), dar Gold Standard-ul de față nu-l folosește ca bază — arhitectura lui e nealiniată cu platforma reală. Documentat în `DEC-0044`.

### 1.2 Fixtures de dezvoltare (`data/fixtures/`)

`exercises.json` (`exercise.2v1-support-angle`), `principles.json` (`principle.scanning-before-receive`), `problems.json` (`problem.no-passing-angle`) — marcate explicit `"development_fixture": true`, folosite doar de `tests/test_ch0101_batch1.py` și `tests/test_taxonomy.py` pentru validarea schemei. Formatul lor nu corespunde schemelor curente (`schemas/exercise.schema.json` cere multe mai multe câmpuri).

**Verdict:** `NOT_REQUIRED` ca material de conținut. Rămân neatinse (nu le șterg — sunt folosite de teste existente, iar ștergerea lor e în afara scopului acestui task).

### 1.3 Conținut canonic real, deja `FIELD_REVIEW_READY`, direct relevant

Aceasta e constatarea centrală a auditului: **conceptul de bază pentru „sprijin și unghi de pasă" există deja, cercetat corect, ca parte a VOLUME-02**, nu ca prototip separat.

- `content/volume-02/chapter-02.mdx` (CH-0202, „Spațiu și unghiuri") + `data/principles/principle-spatiu-si-unghiuri.json` — definește exact problema ([un adversar acoperă doi coechipieri pe aceeași linie]), modelul perceptiv (minge–adversar–coleg–țintă), decizia (direcție + distanță), mesajul copilului („Mută-te până când adversarul nu vă mai poate acoperi pe amândoi"), cele 7 raționamente, formulările de evitat („Stai larg", „Fă triunghi" — ambele explicit respinse ca reguli geometrice fixe).
- `content/volume-02/chapter-03.mdx` (CH-0203, „Progresie și sprijin") + `data/principles/principle-progresie-si-sprijin.json` — completează cu prioritizarea progresie-directă-vs-sprijin, comportamente observabile, verificarea înțelegerii.
- Evidența din spate (`CLM-0036`, `CLM-0038`, `CLM-0040`, `CLM-0041`, `CLM-0042`) e verificată, `VERIFIED`, cu surse reale, nefabricate (Clemente et al. 2021/2023, Pinder/Davids/Renshaw/Araújo 2011 — RLD, Silvino/Sarmento/Teoldo 2024, Machado/Barreira/Teoldo/Serra-Olivares/Góes/Scaglia 2020), niciuna retrasă.

**Decizie:** Gold Standard-ul NU re-derivă modelul conceptual/perceptiv/decizional de la zero. Îl **reutilizează și îl extinde** din `principle-spatiu-si-unghiuri` + `principle-progresie-si-sprijin`, adăugând doar ce lipsește (execuție tehnică, sistem de exerciții, progresie/regresie specifică, ședințe, evaluare, instrumente de teren, integrare web). Documentat în `DEC-0044`.

## 2. Matricea de pregătire

| Dimensiune | Sursă canonică | Status |
|---|---|---|
| Dezvoltarea copilului 10–11 ani | V01 CH-0101 (`principle-variabilitatea-dezvoltarii-u11`) | `READY` |
| Percepție / adaptarea sarcinii | V01 CH-0102 (`principle-adaptarea-sarcinii-u11`) | `READY` |
| Decizie / eroare ca informație | V01 CH-0103 (`principle-eroarea-ca-informatie`) | `READY` — reutilizabil direct pentru modelul de eroare/intervenție |
| Formularea mesajului pedagogic | V01 CH-0104 (`principle-mesaj-pedagogic-observabil`) | `READY` — metodologia de formulare a mesajelor |
| Evaluare / transfer autonom | V01 CH-0105 (`principle-transfer-autonom-cooperare`) | `READY` — comportamentul „creează un unghi fără comandă" e deja listat explicit ca observabil |
| Comunicare (limbaj scurt, întrebări, disciplină, meci) | V03 CH-0301/0302/0304/0305 | `READY` |
| **Concept + percepție + decizie — spațiu/unghi** | V02 CH-0202 (`principle-spatiu-si-unghiuri`) | `READY` — nucleul conceptual al Gold Standard-ului |
| **Concept + decizie — progresie/sprijin** | V02 CH-0203 (`principle-progresie-si-sprijin`) | `READY` — prioritizarea progresie-vs-sprijin |
| Proiectare reprezentativă | V04 CH-0401 | `READY` |
| Constrângeri (fără dogmă CLA) | V04 CH-0402 | `READY` |
| Progresie/regresie (metodologie generală) | V04 CH-0403 | `READY_WITH_ADAPTATION` — principii generale există; pașii specifici 2v1→3v2→4v4 trebuie auditați separat (secțiunea 3) |
| Observare/intervenție (timing) | V04 CH-0404 | `READY` |
| Organizare/timp activ/siguranță | V04 CH-0405 | `READY` |
| Reflecție/transfer post-antrenament | V04 CH-0406 | `READY` |
| **Execuție tehnică** (orientare la recepție, prima atingere, greutatea pasei) | — | `RESEARCH_REQUIRED` — niciun capitol canonic nu acoperă tehnica specifică relevantă pentru sprijin |
| Sistem de exerciții (schemă) | `schemas/exercise.schema.json` (0 instanțe) | `CONTENT_REQUIRED` |
| Sistem de ședințe (schemă) | `schemas/session.schema.json` (0 instanțe) | `CONTENT_REQUIRED` |
| Sistem de evaluare (schemă) | `schemas/assessment.schema.json` (0 instanțe) | `CONTENT_REQUIRED` |
| Semantică vizuală tactică | — | `CONTENT_REQUIRED` — nicio specificație nu există încă |
| Instrumente de teren specifice temei | — | `CONTENT_REQUIRED` |
| Integrare web pentru exercise/session/assessment | `content-bridge.ts` (importă doar principii) | `CONTENT_REQUIRED` |
| Lanțul vechi TASK-0410–0418 | — | `SUPERSEDE` (secțiunea 1.1) |

## 3. Auditul progresiei istorice 2v1 → 3v2 → 4v4 → 7v7

Instrucțiunile cer auditarea explicită a acestei progresii, nu preluarea ei automată. Nu există nicio instanță de exercițiu produsă până acum (doar fixture-uri de dezvoltare nefolosibile), deci nu există o „progresie veche" de auditat ca artefact — doar o convenție vagă menționată istoric. Progresia reală va fi derivată în `TASK-2204` (sistemul de exerciții) direct din `principle-spatiu-si-unghiuri`/`principle-progresie-si-sprijin` și din cercetarea privind jocurile reduse (`CLM-0036`, `CLM-0040`, `CLM-0041`, `CLM-0042` — care deja documentează efecte specifice ale dimensiunii terenului și numărului de jucători), justificând fiecare treaptă prin informația/decizia nouă pe care o introduce, nu prin „mai mulți jucători = mai greu".

## 4. Clasificarea gap-urilor

- `RESEARCH_REQUIRED`: execuția tehnică (orientare la recepție sub presiune, prima atingere orientată spre continuare).
- `CONTENT_REQUIRED`: exerciții, ședințe, evaluare, semantică vizuală, instrumente de teren, integrare web pentru noile entități.
- `PRACTICE_ONLY`: orice prag numeric de exercițiu (dimensiuni exacte de teren per exercițiu) fără sursă directă — va fi etichetat explicit `MANUALFC_HEURISTIC`/`EXERCISE_SPECIFIC_PARAMETER`, niciodată prezentat ca regulă științifică (vezi politica numerelor exacte, secțiunea 6).
- `NOT_REQUIRED`: re-derivarea conceptului de bază (deja acoperit de V02); fixture-urile de dezvoltare.

## 5. Graful minim de taskuri

Nu se creează un task per micro-model (percepție separat de decizie separat de limbaj) — instrucțiunile cer unități verticale coerente. ID-uri noi, `PHASE-22` (fazele 00–21 sunt deja alocate; lanțul vechi `TASK-0410`–`0418` rămâne neatins, `SUPERSEDE`, nu `REPLACE` fizic).

| Task | Titlu | Depinde de | Output principal |
|---|---|---|---|
| `TASK-2201` | Gold Standard Readiness Audit | — | acest document |
| `TASK-2202` | Cercetare execuție tehnică + hartă completă PROPOZIȚIE→DOVADĂ | `TASK-2201` | dosar de cercetare + claims noi |
| `TASK-2203` | Pachetul de concept Gold Standard (model de eroare/intervenție specific temei, taxonomie erori observabile) | `TASK-2202` | `docs/gold-standard/CONCEPT_MODEL.md` |
| `TASK-2204` | Sistemul de exerciții (prima producție reală `data/exercises/*.json`) | `TASK-2203` | familie minimă suficientă de exerciții |
| `TASK-2205` | Sistemul de ședințe (prima producție reală `data/sessions/*.json`) | `TASK-2204` | 1-2 ședințe complete |
| `TASK-2206` | Evaluare + transfer în meci (prima producție `data/assessments/*.json`) | `TASK-2205` | instrument de evaluare + model de transfer |
| `TASK-2207` | Instrumente de teren + specificații vizuale tactice | `TASK-2206` | fișe de teren + specificații semantice |
| `TASK-2208` | Integrare web (Quick Mode + Deep Mode, entități noi în content-bridge) | `TASK-2207` | rute funcționale, fără modificare design freeze |
| `TASK-2209` | Audit independent Gold Standard (task separat, nu combinat cu reparație) | `TASK-2208` | verdict binar |
| `TASK-2210` | Remediere (doar dacă `REPAIR_REQUIRED`) | `TASK-2209` | — |
| `TASK-2211` | Pachetul de field review Gold Standard | `TASK-2209` (PASS) | `docs/field-review/GOLD_STANDARD_SUPPORT_ANGLE_FIELD_REVIEW_PACKAGE.md` |

Acest grafic e minim — 11 taskuri pentru un sistem pedagogic vertical complet, nu zeci de taskuri speculative. `TASK-2210` se creează efectiv doar dacă auditul cere reparație.

## 6. Politica numerelor exacte (reconfirmată pentru acest task)

Orice valoare exactă (grade, metri, secunde, repetiții, dimensiuni de teren, rapoarte de jucători) primește una din etichetele: `SOURCE_DIRECT`, `SOURCE_DERIVED`, `MANUALFC_HEURISTIC`, `EXERCISE_SPECIFIC_PARAMETER`, `UNSUPPORTED`. Niciun unghi exact (ex. 45°) nu va fi prezentat ca regulă tactică validată — cercetarea nu susține un unghi universal; principiul rămâne funcțional („creează o opțiune de pasă utilă"), nu geometric.

## 7. Concluzie

`GOLD_STANDARD_READINESS_AUDIT = PASS`. Fundația conceptuală/perceptivă/decizională există deja și e de încredere (`FIELD_REVIEW_READY`, VOLUME-02). Lucrul nou necesar e clar delimitat: cercetare tehnică punctuală, apoi sistemul de exerciții/ședințe/evaluare — primele din întregul proiect — plus integrarea lor web. `TASK-2202` devine `READY`.
