# Sistemul de clasificare a dovezilor

**Versiune:** 1.0.0 (formalizare a vocabularului deja folosit) · **Task de referință:** TASK-2907 · **Statut:** Architecture

Regulă de la care nu se abate acest document (§26 din specificația PHASE-29): **nu se creează un vocabular de dovezi concurent**. ManualFC are deja un vocabular real, folosit consecvent în `schemas/claim-registry.schema.json`, `data/problems/problem-library.json` și `data/media/media-registry.json`. Acest document formalizează acel vocabular existent și îl completează doar acolo unde lipsește ceva genuin.

## 1. Vocabularul deja existent (verificat direct în schemă/date, nu presupus)

| Câmp existent | Unde | Valori |
|---|---|---|
| `claim_type` | `claim-registry.schema.json` | `FACT`, `OFFICIAL_RECOMMENDATION`, `STUDY_RESULT`, `CONSENSUS`, `PRACTICE`, `OPINION`, `METHODOLOGICAL_SYNTHESIS` |
| `confidence` / `epistemic_level` | `claim-registry.schema.json` | `HIGH`, `MODERATE`, `LOW`, `PRACTICE_ONLY`, `UNRESOLVED` |
| `u11_applicability` | `claim-registry.schema.json` | `DIRECT`, `PARTIAL`, `INDIRECT` |
| `status` (claim) | `claim-registry.schema.json` | `PROPOSED`, `VERIFIED`, `CONTESTED`, `OUTDATED`, `WITHDRAWN`, `REPLACED` |
| `status` (research question) | `research-question.schema.json` | `PROPOSED`, `SEARCHING`, `SCREENING`, `SYNTHESIZED`, `AUDITED`, `CLOSED`, `BLOCKED` |
| `research_state` | `problem-library.json`, folosit real | `VERIFIED_WITH_LIMITS`, `NEEDS_FIELD_VALIDATION` |
| `evidence_boundary` | `media-registry.json` (TASK-2804) | `SYNTHETIC_INSTRUCTIONAL_VISUALIZATION`, `CANONICAL_TEXT_DERIVED`, `REAL_FOOTAGE` |
| „Practice Heuristic" | copy real în Group Configurator, contingențe de ședință | etichetă textuală, nu încă enum formal |
| `FIELD_INPUT_REQUIRED` | folosit ca stare de fază întreagă (`PHASE-23`) și ca stare de ledger | text convențional, nu enum de schemă |

## 2. Reconciliere cu candidat-lista din specificația PHASE-29

Specificația PHASE-29 §26 propune: `VERIFIED_FACT`, `SYSTEMATIC_REVIEW_SUPPORTED`, `PRIMARY_RESEARCH_SUPPORTED`, `EXPERT_CONSENSUS`, `PRACTICE_RECOMMENDATION`, `PRACTICE_HEURISTIC`, `INFERENCE`, `HYPOTHESIS`, `FIELD_VALIDATION_REQUIRED`, `FIELD_INPUT_REQUIRED`, `RESEARCH_REQUIRED`. Niciuna nu se adaugă ca enum nou separat — fiecare se mapează pe combinația deja existentă:

| Categorie candidată (prompt) | Se exprimă azi prin | Enum nou necesar? |
|---|---|---|
| `VERIFIED_FACT` | `claim_type=FACT` + `confidence=HIGH` | NU |
| `SYSTEMATIC_REVIEW_SUPPORTED` | `claim_type=METHODOLOGICAL_SYNTHESIS` sau `STUDY_RESULT` + `confidence=HIGH/MODERATE` | NU |
| `PRIMARY_RESEARCH_SUPPORTED` | `claim_type=STUDY_RESULT` + `confidence=MODERATE/LOW` | NU |
| `EXPERT_CONSENSUS` | `claim_type=CONSENSUS` | NU |
| `PRACTICE_RECOMMENDATION` | `claim_type=OFFICIAL_RECOMMENDATION` sau `PRACTICE` + `confidence=PRACTICE_ONLY` | NU |
| `HYPOTHESIS` | `research_state=HYPOTHESIS` (deja folosit ca valoare reală în audituri, nu doar în schemă) | NU |
| `FIELD_VALIDATION_REQUIRED` | `research_state=NEEDS_FIELD_VALIDATION` (deja folosit) | NU |
| `FIELD_INPUT_REQUIRED` | deja stare de produs la nivel de fază (`PHASE-23`) și ledger | NU |
| `RESEARCH_REQUIRED` | `research-question.status=PROPOSED` (nicio sursă găsită încă) | NU |
| `INFERENCE` | `confidence=LOW` + `claim_type=OPINION`/`PRACTICE`, fără sursă directă la populația U11 | NU, dar merită o etichetă text explicită în dossier (§3) |
| `PRACTICE_HEURISTIC` | folosit deja ca text, **nu** ca enum formal | **DA — singura adăugire reală (§4)** |

## 3. Nota despre `INFERENCE`

`INFERENCE` nu primește un enum propriu pentru că nu descrie o proprietate a claim-ului (asta e deja `confidence`) — descrie o **relație de traducere**: un claim cu `u11_applicability=INDIRECT` folosit pentru a justifica o practică U11 e o inferență, indiferent de scorul lui de încredere brut. Se marchează explicit în secțiunea „Practical translation" a dosarului de cercetare (deja pattern existent, `research/dossiers/ch-0103-decision-error.md`), nu într-un câmp de schemă nou.

## 4. Singura adăugire reală: `PRACTICE_HEURISTIC` ca etichetă formală

Azi „Practice Heuristic" apare ca text în interfață (Group Configurator, contingențe operaționale ședință) fără o valoare de schemă corespunzătoare — e o etichetă de UI, nu o proprietate de date verificabilă de validator. Propunere minimă: adăugarea opțională a câmpului `guidance_type: "CANONICAL_DERIVATION" | "PRACTICE_HEURISTIC"` acolo unde apare deja text de tip eroistic (ex. reguli de rotație, poziționare antrenor). Detaliu de implementare și impact: `KNOWLEDGE_SCHEMA_IMPACT_ANALYSIS.md`. Nu se implementează în PHASE-29 (regulă §65).

## 5. Ierarhia surselor (§27)

Deja aplicată informal (research/README.md, dosarele de cercetare citează consecvent surse cu DOI/review-uri sistematice înaintea practicii necitate). Formalizată aici ca regulă explicită de prioritate pentru claim-uri cu miză mare sau fundamentale:

1. organisme oficiale de guvernare/safeguarding (unde se aplică);
2. review-uri sistematice / meta-analize;
3. declarații de consens de înaltă calitate;
4. cercetare primară evaluată de la egal la egal (peer-reviewed);
5. lucrări teoretice fundamentale;
6. cadre recunoscute de formare a antrenorilor;
7. surse de practică expert, etichetate explicit ca atare.

**Interzis ca fundație de dovadă** (regulă explicită, nu presupusă — corespunde direct politicii deja aplicate în `research/dossiers/` de a nu accepta surse necitate): bloguri fără citare, rezumate SEO, afirmații de coaching necitate.

## 6. Compatibilitate cu produsul curent

Zero schimbare de schemă necesară pentru §1-3 — vocabularul existent deja acoperă cerința. Singura extensie reală (§4) e opțională și aditivă, tratată integral în `KNOWLEDGE_SCHEMA_IMPACT_ANALYSIS.md`, nu implementată acum.
