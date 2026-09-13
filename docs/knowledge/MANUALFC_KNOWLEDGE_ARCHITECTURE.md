# ManualFC — Arhitectura cunoașterii

**Versiune:** 1.0.0
**Data:** 2026-08-18
**Statut:** Canonical / Architecture (PHASE-29)
**Task de referință:** TASK-2901
**Precedent direct:** `PRODUCT_VISION.md`, `PEDAGOGICAL_PRODUCT_PRINCIPLES.md`, `docs/architecture/CONTENT_TAXONOMY.md`, `docs/architecture/PROBLEM_KNOWLEDGE_GRAPH.md`

Acest document e descrierea canonică a modului în care funcționează cunoașterea în ManualFC. Nu înlocuiește niciun document existent — leagă explicit ce există deja (taxonomia din TASK-0201, graful problemă-exercițiu din Wave-3, contractul de 18 întrebări din `PEDAGOGICAL_PRODUCT_PRINCIPLES.md`, registrul de claim-uri, pipeline-ul de cercetare din `research/`) de ce lipsește pentru ca produsul să devină un sistem complet de formare a antrenorului-pedagog, nu doar o bibliotecă de exerciții.

## 0. Ce am găsit deja construit (nu se reinventează)

| Concept cerut de PHASE-29 | Există deja ca | Unde |
|---|---|---|
| Cei doi piloni „copil" / „antrenor" | `cat.copilul-10-11` (order 1), `cat.antrenorul-pedagog` (order 2) | `data/taxonomy/registry.json` |
| Graf de cunoaștere | `problem → observation → hypothesis → test → cue → principle → exercise → session → assessment → transfer → evidence → media` | `docs/architecture/PROBLEM_KNOWLEDGE_GRAPH.md` |
| Contract obligatoriu de conținut (18 întrebări) | listă completă în `PEDAGOGICAL_PRODUCT_PRINCIPLES.md` | rădăcina repo-ului |
| Registru de claim-uri cu încredere/limite/vârstă | `claim-registry.schema.json` (`CLM-XXXX`, `confidence`, `u11_applicability`, `forbidden_overstatements`) | `schemas/`, `research/claims.json` |
| Întrebări de cercetare cu ciclu de viață | `research-question.schema.json` (`PROPOSED→SEARCHING→SCREENING→SYNTHESIZED→AUDITED→CLOSED→BLOCKED`) | `schemas/`, `research/questions.json` |
| Dosar de cercetare per subiect | fișiere reale `research/dossiers/ch-XXXX-*.md` (research question, ce susține dovada, ce NU susține, populație/context, aplicabilitate U11, limite, traducere practică, întrebări deschise, decizii de claim, hartă de citare) | `research/dossiers/` |
| Model de profunzime pe două niveluri | „nivel aprofundat" + „nivel rapid" | `CONTENT_STRATEGY.md` |
| Separare cercetare/redactare/audit | „cercetarea, redactarea, auditul factual, auditul pedagogic, auditul editorial, repararea și aprobarea" | `CONTENT_STRATEGY.md` |
| Pregătire arhitecturală multi-vârstă | câmpuri viitoare documentate, ordine provizorie 8-9/6-7/4-5/12-13/14-15/16-18 | `MULTI_AGE_EXPANSION_ARCHITECTURE.md` |

PHASE-29 **formalizează, numește și extinde** aceste artefacte într-un sistem coerent — nu le înlocuiește. Orice document nou din acest set citează explicit precedentul de mai sus.

## 1. Cei trei piloni

Confirmat de arhitectura deja existentă (`cat.copilul-10-11` + `cat.antrenorul-pedagog`), formalizat acum ca regulă permanentă de produs:

| Pilon | Întrebare | Categorii taxonomie existente acoperite | Ce nu există încă |
|---|---|---|---|
| **PEDAGOGUL** — „Înțelege copilul." | PE CINE ANTRENEZ? | `cat.copilul-10-11`, `cat.psihologie`, `cat.comunicare`, `cat.parinti`, `cat.safeguarding` | domeniu structurat + competențe pedagogice |
| **ANTRENORUL** — „Învață să predai jocul." | CUM ÎL AJUT SĂ ÎNVEȚE? | `cat.antrenorul-pedagog`, `cat.perceptie-decizie`, `cat.tehnica-context`, `cat.evaluare`, `cat.metodologie-surse` | domeniu structurat + competențe de coaching |
| **PRACTICA** — „Aplică pe teren." | CUM TRANSFORM CUNOAȘTEREA ÎN COMPORTAMENT ȘI ANTRENAMENT? | `cat.principii-joc`, `cat.exercitii`, `cat.sedinte`, `cat.probleme-teren`, `cat.motricitate`, `cat.resurse` | legături explicite spre competențele de mai sus |

Pilonii nu sunt trei secțiuni izolate de conținut. Sunt trei **lentile** asupra aceluiași graf de cunoaștere (§7). Aceeași problemă observată pe teren poate fi intrată din oricare pilon (§9, Regula bidirecțională).

## 2. Bucla canonică de învățare

```
TEORIE → ÎNȚELEGERE → COMPORTAMENT DE ANTRENOR → PRACTICĂ → OBSERVAȚIE → REFLECȚIE → DEZVOLTARE
```

Regulă permanentă de produs (nouă, adoptată în PHASE-29):

> Nicio lecție pedagogică nu e completă până nu ajunge la comportamentul concret al antrenorului.
> Niciun exercițiu sau ședință nu e completă până nu identifică principiul pedagogic și competența de coaching aplicată.

Această buclă e implementată deja PARȚIAL în produsul curent: Decision Engine implementează exact `PROBLEMĂ → CONCEPT(ipoteză) → COMPORTAMENT DE ANTRENOR(intervenție/cue) → PRACTICĂ(exercițiu) → OBSERVAȚIE(„Urmărește") → REFLECȚIE(post-ședință)`, dar **fără** pasul explicit „competență" — intervenția e legată de exercițiu, nu de o competență de coaching numită. §17 (Theory-to-Practice Contract) formalizează exact acest gol.

## 3. Straturi de cunoaștere

| Strat | Conține | Obiect canonic existent | Obiect nou |
|---|---|---|---|
| **Cunoaștere de cercetare** | claim-uri, surse, citări | `Claim` (`CLM-`), `Source` (`SRC-`), `Citation` (`CIT-`) | — |
| **Concept pedagogic/de coaching** | idee organizată didactic, nu încă legată de comportament | `Principle` (`principle.*`) parțial | `PEDAGOG_DOMAIN`, `COACH_DOMAIN` (§4-5) |
| **Competență** | ce e capabil să facă antrenorul/pedagogul | — | `PEDAGOG_COMPETENCY`, `COACH_COMPETENCY` (§6) |
| **Practică** | exercițiu, ședință, configurare, Mod Teren | `Exercise`, `Session`, `Problem`, `Assessment` | extensie de relații, nu entități noi |
| **Reflecție/dezvoltare** | ce s-a întâmplat, ce urmează | `SessionReflection` (runtime) | dimensiune de coach, separată de dimensiunea copil/joc |

## 4. Obiecte de cunoaștere (knowledge objects)

Un **obiect de cunoaștere** e orice concept identificabil cu ID stabil care poate purta un claim, o competență sau o traducere practică. Contractul minim (extensie a modelului `entity_contracts` din `data/taxonomy/registry.json`):

```
KNOWLEDGE_CONCEPT
  id: stabil, prefix pe domeniu (ex. ped.eroare-invatare, coach.intrebare-ghidata)
  domain_id: PEDAGOG_DOMAIN | COACH_DOMAIN
  title_ro
  question_answered
  claim_ids: []            # legătură spre Claim Registry existent
  competency_ids: []       # legătură spre competențe (§6)
  depth_layers: {...}      # §12, Content Depth Standard
  age_sensitivity: UNIVERSAL | AGE_SENSITIVE | AGE_SPECIFIC   # §14
  safeguarding_sensitivity: NONE | LOW | HIGH
```

## 5. Obiecte de competență (competency objects)

Definite complet în `PEDAGOG_COMPETENCY_FRAMEWORK.md` și `COACH_COMPETENCY_FRAMEWORK.md`. O competență nu e un subiect — e o capacitate observabilă. Vezi §14-15 din prompt-ul PHASE-29 și documentele dedicate pentru modelul complet.

## 6. Obiecte de practică (practice objects)

Entități deja canonice (`Exercise`, `Session`, `Problem`, `Assessment`) — extinse relațional, nu redefinite. Vezi `THEORY_TO_PRACTICE_CONTRACT.md` §Practice Contract V2.

## 7. Obiecte de dovadă (evidence objects)

Deja canonice: `Claim` (`schemas/claim-registry.schema.json`), `Source` (`schemas/source-registry.schema.json`), `Citation` (`schemas/citation-registry.schema.json`), `ResearchQuestion` (`schemas/research-question.schema.json`). Vezi `EVIDENCE_CLASSIFICATION_SYSTEM.md`.

## 8. Relații — extensie a grafului existent

Graful `PROBLEM_KNOWLEDGE_GRAPH.md` se extinde (nu se înlocuiește) cu noduri de domeniu și competență. Detaliu complet: `KNOWLEDGE_GRAPH_SPECIFICATION.md`.

## 9. Regula bidirecțională

Produsul trebuie să susțină ambele direcții de navigare, deja parțial adevărat:

- **Din teorie**: concept → competență → comportament de antrenor → exercițiu/ședință. (nou, formalizat aici)
- **Din teren**: problemă observată → Decision Engine → concept explicativ → competență → intervenție → exercițiu → reflecție. (deja implementat, lipsește doar legătura explicită spre competență)

Nu se construiește un manual liniar. Fiecare obiect de cunoaștere trebuie accesibil din ambele direcții.

## 10. Straturi de prezentare (Content Depth Standard, rezumat)

Extensie a modelului existent pe două niveluri (`CONTENT_STRATEGY.md`) la patru straturi explicite. Detaliu complet: `CONTENT_DEPTH_STANDARD.md`. Regulă centrală: **un singur obiect canonic, mai multe adâncimi de prezentare** — nu patru articole separate.

## 11. Ciclul de viață al cercetării

Deja implementat prin `research-question.schema.json` + `research/dossiers/`. Formalizat complet în `RESEARCH_PRODUCTION_PIPELINE.md`.

## 12. Ciclul de viață al redactării

Extensie a separării deja documentate în `CONTENT_STRATEGY.md` (cercetare → redactare → audit factual → audit pedagogic → audit editorial → reparare → aprobare), cu adăugarea explicită a pasului „traducere practică" (competență → comportament de antrenor) înaintea redactării finale. Vezi `RESEARCH_PRODUCTION_PIPELINE.md` §Authoring lifecycle.

## 13. Ciclul de viață al validării

Extensie a validatorului canonic Python existent (`scripts/validate_content.py`, `SCHEMA_TYPES`). Detaliu complet: `KNOWLEDGE_SCHEMA_IMPACT_ANALYSIS.md` — inclusiv regula de migrare fără a rupe validarea curentă (§Migrare fără destabilizare).

## 14. Versionare

Fiecare obiect de cunoaștere nou urmează exact tiparul deja folosit de `Claim` (`verified_at`, `next_review_at`, `status: PROPOSED|VERIFIED|CONTESTED|OUTDATED|WITHDRAWN|REPLACED`). Nu se inventează un sistem de versionare paralel.

## 15. Adaptare de vârstă

Trei categorii, explicit distincte (cerere PHASE-29 §33), aplicate peste arhitectura deja pregătită în `MULTI_AGE_EXPANSION_ARCHITECTURE.md`:

- **UNIVERSAL / CROSS-AGE**: safeguarding, principii pedagogice fondatoare (eroarea ca informație, siguranța psihologică) — valabile la orice vârstă, text neschimbat.
- **AGE_SENSITIVE**: durata atenției, lungimea explicației, complexitatea cognitivă — conceptul e universal, aplicarea variază pe bandă de vârstă.
- **AGE_SPECIFIC**: organizarea exercițiului, spațiul, regulile — practică legată direct de o singură bandă de vârstă.

Niciun ID nou de cunoaștere nu conține „U11" sau „10-11" în identificator — vârsta e un câmp (`age_sensitivity`, `age_band_scope`), nu o parte din ID. Asta e regula care păstrează compatibilitatea multi-vârstă fără refactor la introducerea benzilor viitoare.

## 16. Compatibilitate multilingvă viitoare

ID-urile canonice (`ped.*`, `coach.*`, `CLM-*`, etc.) sunt independente de limbă prin construcție (nu conțin text românesc). Eticheta (`title_ro`) e un câmp separat, exact ca la `label_ro` din `data/taxonomy/registry.json`. O etichetă `title_en`/`title_XX` viitoare se adaugă ca proprietate nouă opțională, nu ca schimbare de identitate.

## 17. Cele cinci întrebări fondatoare — răspuns direct

**CE ȘTIE MANUALFC?** — Azi: 25 principii, 8 probleme, 5 exerciții, 2 ședințe, 1 evaluare, 15 obiecte media, un registru de claim-uri cu 3 intrări reale (extensibil). Structurat pe 16 categorii deja existente.

**CUM E ORGANIZATĂ ACEA CUNOAȘTERE?** — Pe trei piloni (Pedagogul/Antrenorul/Practica), fiecare cu domenii și subdomenii (§`PEDAGOG_DOMAIN_MAP.md`, `COACH_DOMAIN_MAP.md`), legate printr-un graf de relații semantice (§`KNOWLEDGE_GRAPH_SPECIFICATION.md`), cu dovezi clasificate explicit (§`EVIDENCE_CLASSIFICATION_SYSTEM.md`).

**CUM DEVINE CUNOAȘTEREA COMPORTAMENT DE ANTRENOR?** — Prin competențe (§`PEDAGOG_COMPETENCY_FRAMEWORK.md`, `COACH_COMPETENCY_FRAMEWORK.md`) și contractul teorie-practică (§`THEORY_TO_PRACTICE_CONTRACT.md`), care obligă fiecare concept să ajungă la limbaj/acțiune exactă.

**CUM DEVINE COMPORTAMENTUL PRACTICĂ?** — Prin Practice Contract V2, Session Contract V2 și Field Mode V2 (toate în `THEORY_TO_PRACTICE_CONTRACT.md`), care leagă competența de exercițiul/ședința/Modul Teren deja existente.

**CUM SE ÎNTOARCE PRACTICA ÎN REFLECȚIE ȘI DEZVOLTARE?** — Prin Reflection V2 (dimensiune copil/joc + dimensiune antrenor, în `THEORY_TO_PRACTICE_CONTRACT.md`) și contractul viitor de Coach Development (`KNOWLEDGE_AND_COMPETENCY_KPI_MODEL.md` §K3).

## 18. Ce NU face acest document

Nu implementează cod. Nu creează conținut canonic nou (exemplele din documentele PHASE-29 sunt etichetate explicit `NON_CANONICAL_ARCHITECTURE_EXAMPLE` unde nu se bazează pe conținut deja canonic). Nu modifică schema JSON existentă fără o propunere separată (`KNOWLEDGE_SCHEMA_IMPACT_ANALYSIS.md`). Nu schimbă runtime-ul Wave-4 acceptat.
