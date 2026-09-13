# Contractul Teorie → Practică

**Versiune:** 1.0.0 · **Task de referință:** TASK-2905 · **Statut:** Architecture

Cel mai important artefact al PHASE-29. Definește obligația structurală ca orice cunoaștere să ajungă la comportament concret de antrenor, și orice exercițiu/ședință să identifice principiul pedagogic și competența aplicată (regula permanentă din §3 a specificației PHASE-29).

## 1. Lanțul obligatoriu

```
CLAIM DE CERCETARE (CLM-xxxx, deja implementat)
  ↓
CONCEPT (PED-domeniu / COACH-domeniu)
  ↓
MANIFESTARE LA COPIL (ce arată comportamental)
  ↓
OBSERVAȚIE DE ANTRENOR (ce poate vedea, fără presupunere)
  ↓
GRANIȚĂ „NU PRESUPUNE" (ce NU poate concluziona din observație)
  ↓
COMPORTAMENT DE ANTRENOR (ce face)
  ↓
LIMBAJ/ACȚIUNE EXACTĂ (ce spune literal)
  ↓
APLICARE ÎN PRACTICĂ (exercițiu/ședință)
  ↓
RĂSPUNS OBSERVABIL (ce se schimbă la copil)
  ↓
VERIFICARE (cum confirmă antrenorul)
  ↓
TRANSFER (apare în joc liber?)
  ↓
REFLECȚIE (copil/joc + antrenor, separate — §6)
```

**Regulă de acceptare:** o lecție Pedagogul sau Antrenorul nu e completă arhitectural dacă lanțul se oprește înainte de „LIMBAJ/ACȚIUNE EXACTĂ". Un concept fără comportament de antrenor rămâne teorie decorativă — exact ce interzice §3 din specificația PHASE-29.

**Precedent deja implementat:** acest lanț există parțial, funcțional, în `research/dossiers/ch-0103-decision-error.md` (secțiunea „Practical translation") și în structura fiecărei probleme din `problem-library.json` (`observable_behavior → possible_explanations → intervention`). Contractul de mai jos formalizează acest tipar și îl extinde cu pasul explicit de competență, care lipsește azi.

## 2. Relația cu contractul de 18 întrebări existent

`PEDAGOGICAL_PRODUCT_PRINCIPLES.md` cere deja: *ce îi spun copilului; sensul profesional; de ce această formulare; problema; informația observată; decizia; comportamentul observabil; dezvoltarea tactică; perceptivă și decizională; cognitivă; psihologică; socială; adecvarea la vârstă; interpretările greșite; formulările de evitat; verificarea înțelegerii; intervenția dacă nu funcționează; transferul în joc.*

Contractul de lecție Pedagogul (§3) și cel de Antrenorul (§4) de mai jos **sunt aceleași 18 întrebări**, regrupate explicit pe cei doi piloni și cu două adăugiri obligatorii care lipseau: **ID de competență pedagogică** și **ID de competență de coaching**. Nu se creează un contract concurent — se numește explicit ce exista deja implicit.

## 3. Contractul lecției Pedagogul

| # | Întrebare | Corespondent în contractul de 18 întrebări existent |
|---|---|---|
| 1 | CE ESTE? | — (nou, context) |
| 2 | DE CE CONTEAZĂ? | „sensul profesional" |
| 3 | CE ȘTIM DIN CERCETARE? | — (nou — leagă explicit spre `Claim`) |
| 4 | CARE SUNT LIMITELE? | „interpretările greșite" (parțial) |
| 5 | CUM SE POATE MANIFESTA LA COPIL? | „comportamentul observabil" |
| 6 | CE POATE OBSERVA ANTRENORUL? | „informația observată" |
| 7 | CE NU TREBUIE SĂ PRESUPUNĂ? | „interpretările greșite" |
| 8 | CE POATE FACE? | „decizia" |
| 9 | CE POATE SPUNE? | „ce îi spun copilului", „de ce această formulare" |
| 10 | CE AR TREBUI SĂ EVITE? | „formulările de evitat" |
| 11 | EXEMPLU CONCRET | — (nou) |
| 12 | EXEMPLU DE TEREN | — (nou) |
| 13 | COMPETENȚĂ PEDAGOGICĂ | **nou — `PED-C0x`** |
| 14 | COMPETENȚĂ DE COACHING | **nou — `COACH-C0x`** |
| 15 | LEGĂTURA CU PRACTICA | „dezvoltarea tactică; perceptivă și decizională; cognitivă; psihologică; socială" |
| 16 | CUM VERIFICĂ? | „verificarea înțelegerii", „intervenția dacă nu funcționează" |
| 17 | TRANSFER | „transferul în joc" |
| 18 | DOVEZI | — (nou — leagă explicit spre `EVIDENCE_CLASSIFICATION_SYSTEM.md`) |

Câmpurile 1, 3, 11, 12, 13, 14, 18 sunt cele patru completări reale ale PHASE-29; restul erau deja cerute.

## 4. Contractul lecției Antrenorul

| # | Întrebare |
|---|---|
| 1 | CE ESTE COMPETENȚA? |
| 2 | CE PROBLEMĂ PROFESIONALĂ REZOLVĂ? |
| 3 | DE CE FUNCȚIONEAZĂ? |
| 4 | CE SPUNE CERCETAREA? |
| 5 | CÂND ESTE UTILĂ? |
| 6 | CÂND NU ESTE UTILĂ? |
| 7 | CE VEDE ANTRENORUL? |
| 8 | CE DECIZIE IA? |
| 9 | CUM INTERVINE? |
| 10 | LIMBAJ EXACT |
| 11 | ANTI-TIPAR |
| 12 | EXEMPLU |
| 13 | VARIAȚII DE CONTEXT |
| 14 | LEGĂTURA CU PEDAGOGIA — `PED-Dxx`/`PED-C0x` |
| 15 | LEGĂTURA CU EXERCIȚIILE |
| 16 | LEGĂTURA CU ȘEDINȚELE |
| 17 | VERIFICARE |
| 18 | REFLECȚIE |
| 19 | DOVEZI |

Structural identic cu §3, orientat spre competența profesională în loc de concept pedagogic — cele două contracte sunt oglindă una alteia, exact cum cei doi piloni sunt oglindă (§9 din arhitectura master).

## 5. Practice Contract V2 (exercițiu)

Extensie a schemei `exercise.schema.json` deja canonice — nu o înlocuiește. Câmpurile marcate **NOU** nu există azi în schemă; restul există deja (verificat direct în `data/exercises/*.json`).

| Câmp | Stare azi |
|---|---|
| `FOOTBALL_OBJECTIVE` | există (`primary_objective`) |
| `PEDAGOGICAL_PRINCIPLE_IDS` | **NOU** — azi doar `related_principles` fără tipare de „pedagogic" vs. „tactic" |
| `PEDAGOG_COMPETENCY_IDS` | **NOU** |
| `COACH_COMPETENCY_IDS` | **NOU** |
| `CHILD_PERCEPTION` / `CHILD_DECISION` / `CHILD_ACTION` | parțial — `observable_behaviours` există, nu separat explicit pe cele 3 |
| `EXACT_CUE` | există (`exact_cue`, verificat EX-0003) |
| `WHAT_TO_OBSERVE` | există (`observable_behaviours`) |
| `DO_NOT_ASSUME` | **NOU** |
| `COACH_INTERVENTION` | parțial — implicit în `rationales`, nu explicit numit |
| `WHEN_NOT_TO_INTERVENE` | **NOU** |
| `COMMON_COACH_ERROR` | parțial — „formulări de evitat" există la nivel de principiu, nu la exercițiu |
| `PROGRESSION` / `REGRESSION` | există |
| `GROUP_CONFIGURATION` | există (via Group Configurator, derivat) |
| `FIELD_CARD` | există (`FieldCard.astro`) |
| `TACTICAL_MEDIA` | există (`media-registry.json`) |
| `ASSESSMENT` | există parțial (`ASM-0001`) |
| `TRANSFER_CHECK` | există (`SessionReflection.transferState`) |
| `COACH_REFLECTION` | **NOU** (vezi §6) |
| `EVIDENCE_BOUNDARY` | există (`evidence_boundary` din registrul media, TASK-2804) |

**Regulă de migrare:** niciun exercițiu V1 (EX-0001–EX-0005) nu devine invalid prin introducerea acestui contract. Vezi `KNOWLEDGE_SCHEMA_IMPACT_ANALYSIS.md` §Migrare fără destabilizare.

## 6. Session Contract V2

Structură duală obligatorie, nouă:

```
CHILD OBJECTIVES          COACH OBJECTIVES
  ↓                          ↓
problem → principle      pedagog competency → coach competency
  ↓                          ↓
exercises → configuration → Field Mode
  ↓                          ↓
assessment → transfer      coach-focus cues → coach reflection
  ↓                          ↓
child/game reflection ←――――――┘
```

Azi (`WorkspaceSession`, `data/sessions/*.json`) există doar coloana „CHILD OBJECTIVES" (parțial: `problemId`, `items`, fără competențe). Coloana „COACH OBJECTIVES" e complet nouă. Nu se implementează în PHASE-29 (regulă §65).

## 7. Field Mode V2 Contract (specificație, neimplementat)

Ce trebuie să poată afișa Modul Teren viitor, per segment, păstrând viteza actuală (regulă: „minimal și rapid", nu o pagină de citit):

```
CE FAC ACUM           (deja există — Layer 1, Content Depth Standard)
CE SPUN               (deja există — child_message)
CE URMĂRESC LA COPII  (deja există — observable_behaviours)
FOCUS DE ANTRENOR     (NOU — o singură competență de coaching activă per segment)
CÂND NU INTERVIN      (NOU)
CE SCHIMB             (deja există — progression/regression)
CUM VERIFIC           (parțial nou)
```

Singurul câmp cu adevărat nou pentru interfața de teren e „Focus de antrenor" — o competență de coaching, nu un text lung. Restul sunt deja pattern-uri existente în Mod Teren (TASK-2803/2805), doar reetichetate pentru consecvență cu noul model.

## 8. Reflection V2 Contract (specificație, neimplementat)

Extensie a `SessionReflection` (deja implementat, TASK-2803) cu o a doua dimensiune, distinctă:

**A. COPIL / JOC (există deja):** `observedState`, `transferState` — „Ce a apărut? S-a văzut transfer?"

**B. ANTRENOR (nou):**
- Cum am intervenit?
- Am observat înainte de a acționa?
- Am supra-corectat?
- Am întrebat când o instrucție ar fi fost mai potrivită (sau invers)?
- Am permis explorare?
- Cue-ul meu a ajutat?
- Am verificat transferul, nu doar execuția în exercițiu?

**Regulă explicită (reconfirmată din prompt §23 și din regula generală de produs deja aplicată la reflecția copilului, TASK-2803):** fără Coach Score. Reflecție structurată, calitativă, exact ca modelul deja acceptat pentru `observedState`/`transferState` — enumerare de stări, niciodată un număr.

**Compatibilitate cu produsul curent:** `SessionReflection` e deja o extensie aditivă v1 a `CoachState` (al treilea tipar de acest fel după `reflections` și `offlinePacks`, TASK-2803/2805). Dimensiunea B se adaugă după același tipar — un câmp opțional nou, niciodată o schimbare de schemă distructivă. Vezi `KNOWLEDGE_SCHEMA_IMPACT_ANALYSIS.md`.

## 9. Testul central (auto-verificare, cerut de specificație §60-63)

**Test 1 — orice subiect viitor se încadrează?** Exemplu: „autonomia". → PED-D03-S02 (concept) → PED-C07 (competență pedagogică) → COACH-C03/C04 (competențe de coaching: selecție de intervenție, chestionare) → exercițiu cu decizie liberă → verificare prin observație → reflecție. Se încadrează fără structură nouă. **PASS.**

**Test 2 — teorie spre teren, trei exemple:**
- *Subiect pedagogic* („frica de eroare", PED-D04-S03/PED-D05): claim de cercetare (`CLM-0030` etc., deja existent) → concept → PED-C05/PED-C06 → COACH-C01/C03 → intervenție de neintervenție (COACH-D06) → exercițiu existent (orice EX-*, câmpul `child_message`) → observație → reflecție. **Lanț complet, susținut de arhitectură.**
- *Subiect de coaching* („întrebarea ghidată", COACH-D07): cercetare (`content/volume-03/ch-0302`, deja existent) → COACH-C04 → PED-C04 → exercițiu → verificare prin răspunsul copilului → reflecție de antrenor (§8B). **Lanț complet.**
- *Subiect de practică fotbalistică* („sprijinul", deja PRB-0001/EX-0001-0002): principiu de joc existent → COACH-C08/C11 → exercițiu existent → Field Mode → transfer → reflecție. **Lanț complet, deja parțial implementat în produs.**

**Test 3 — teren spre teorie, o problemă flagship reală:** PRB-0003 („Primește mingea fără să verifice înainte", deja implementat) → Decision Engine (existent) → concept explicativ (PED-D02-S01 atenție, COACH-D22 percepție) → COACH-C11 → intervenție (`exact_cue`, existent) → exercițiu (EX-0003, existent) → reflecție. **Navigare inversă confirmată — arhitectura suportă ambele direcții fără structuri paralele.**

**Test 4 — silozuri de cunoaștere?** Niciun document din acest set nu descrie Pedagogul sau Antrenorul ca bibliotecă separată — fiecare domeniu din `PEDAGOG_DOMAIN_MAP.md` are o coloană explicită „competențe de coaching legate", fiecare domeniu din `COACH_DOMAIN_MAP.md` are o coloană „legături pedagogie". **Fără silozuri.**
