# Pipeline-ul de producție a cercetării

**Versiune:** 1.0.0 (formalizare a pipeline-ului deja funcțional) · **Task de referință:** TASK-2907 · **Statut:** Architecture

## 1. Ce există deja, funcțional

Structura `research/` conține deja un pipeline complet, folosit real (nu doar schemă goală): `questions.json` (întrebări canonice), `search-logs.jsonl` (căutări append-only), `sources.json`/`claims.json`/`citations.json` (lanțul probator), `source-notes/`, `source-snapshots/`, `restricted-source-metadata/`, `version-history/`, `evidence-matrices/`, `review-queues/`, `audits/`, `archive-manifests.json`. Dosarele individuale (`research/dossiers/ch-XXXX-*.md`) urmează deja un contract complet și consecvent (verificat direct, `ch-0103-decision-error.md`): research question, ce susține dovada, ce NU susține, populație/context, aplicabilitate U11, limite, traducere practică, întrebări deschise, decizii de claim, hartă de citare.

## 2. Ciclul de viață canonic (deja implementat prin `research-question.schema.json`)

```
PROPOSED → SEARCHING → SCREENING → SYNTHESIZED → AUDITED → CLOSED
                                                        ↘ BLOCKED
```

Acesta E deja lanțul cerut de specificația PHASE-29 §28 (`RESEARCH QUESTION → SOURCE SEARCH → SOURCE SCREENING → RESEARCH DOSSIER → CLAIM REGISTRY → EVIDENCE CLASSIFICATION → SYNTHESIS → ...`), cu o singură adăugire structurală necesară:

```
...→ SYNTHESIZED → [NOU: PEDAGOGICAL_INTERPRETATION] → [NOU: PRACTICAL_TRANSLATION] → AUDITED → CLOSED
```

„Pedagogical interpretation" și „practical translation" nu sunt stări noi de schemă — sunt secțiuni deja prezente în dosarele reale (`## Practical translation`, verificat), doar niciodată numite explicit ca pași distincți de proces. Formalizarea de aici nu cere nicio schimbare de schemă.

## 3. Separarea cercetare/redactare (deja principiu de produs)

`CONTENT_STRATEGY.md`: *„Producția separă cercetarea, redactarea, auditul factual, auditul pedagogic, auditul editorial, repararea și aprobarea."* PHASE-29 adaugă un singur pas explicit, obligatoriu între cercetare și redactare pentru orice conținut Pedagogul/Antrenorul:

```
cercetare → dosar → [NOU: traducere practică — leagă claim de competență]
  → redactare → audit factual → audit pedagogic → audit editorial → reparare → aprobare
```

Fără acest pas, redactarea riscă exact ce interzice principiul de produs: un concept teoretic care nu ajunge la comportament (§3 arhitectură master).

## 4. Contractul dosarului de cercetare (extensie a modelului existent)

Extensie explicită pentru dosare de domeniu Pedagog/Coach (nu doar per-capitol de volum, cum sunt azi):

| Câmp | Deja în dosarele existente? |
|---|---|
| Scope | DA (research question) |
| Key questions | DA |
| Search strategy | implicit (search-logs.jsonl) |
| Source list | DA (citation map) |
| Claims | DA |
| Supporting sources | DA |
| Contradictory evidence | DA („ce NU susține dovada") |
| Limitations | DA |
| Age-specific evidence | DA („aplicabilitate U11") |
| Sport-specific evidence | DA (context, „doar marginea inferioară a unei surse coincide cu 10-11 ani") |
| Inferences | implicit, nu etichetat separat |
| Open questions | DA |
| Practical implications | DA („practical translation") |
| Claims that must not be made | DA („ce NU susține dovada" acoperă parțial; recomandare: secțiune explicită separată pentru dosarele Pedagog/Coach, ca extensie de claritate) |
| **NOU** — Pedagog/Coach domain link | absent — dosarele existente leagă spre `chapter_id`/`volume_id`, nu spre `PED-D*`/`COACH-D*` |

Singura extensie reală de conținut: un dosar de domeniu Pedagog/Coach adaugă câmpul `domain_id` (`PED-Dxx` sau `COACH-Dxx`) alături de (nu în locul) `chapter_id` existent, pentru dosarele care nu corespund unui capitol de volum ci direct unui domeniu din noua taxonomie.

## 5. Registrul de claim-uri — fără schimbare de structură

`claim-registry.schema.json` acoperă deja tot ce cere specificația PHASE-29 §30 (`CLAIM_ID`, `statement`≈`CLAIM_TEXT`, `domain`, `claim_type`+`confidence`≈`EVIDENCE_TYPE`, `source_ids`, `confidence`+`limitations`+`u11_applicability`≈`CONFIDENCE/BOUNDARY`, `participant_age`+`u11_applicability`≈`AGE_SCOPE`, `practical_implication`, `status`). Nu se propune o bază de date nouă — regulă explicită din prompt („cea mai ușoară arhitectură menținebilă"), deja respectată de alegerea JSON validat prin schemă, fără infrastructură suplimentară.

## 6. Ce e genuin nou pentru PHASE-29

1. Dosarele de cercetare pot fi acum ancorate și pe `PED-Dxx`/`COACH-Dxx`, nu doar pe capitole de volum — extinde domeniul de aplicare, nu structura.
2. Pasul „traducere practică" devine obligatoriu explicit înainte de redactarea finală a oricărei lecții Pedagogul/Antrenorul (§3).
3. Fiecare claim folosit într-o competență (`PED-C*`/`COACH-C*`) trebuie să aibă legătura vizibilă în competența respectivă (câmpul „Bază de dovadă" — deja prezent în cadrele de competență, TASK-2904).

Nimic din aceste trei puncte nu cere o schimbare de schemă imediată — sunt reguli de proces și convenții de completare a câmpurilor deja existente.
