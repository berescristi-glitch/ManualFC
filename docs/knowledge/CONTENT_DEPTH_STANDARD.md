# Standardul de profunzime a conținutului

**Versiune:** 2.0.0 (extensie a modelului pe două niveluri deja existent) · **Task de referință:** TASK-2908 · **Statut:** Architecture

`CONTENT_STRATEGY.md` definește deja: *„Conținutul are două niveluri sincronizate. Nivelul aprofundat explică mecanisme, surse, limite și alternative. Nivelul rapid păstrează acțiunea, mesajul, motivul, observația și pragul de adaptare. Ambele derivă din aceleași entități."* Acest document nu înlocuiește modelul pe două niveluri — îl **subdivide** în patru straturi de prezentare, pentru a face profunzimea de cunoaștere cerută de PHASE-29 posibilă fără o interfață mai complexă.

## 1. Cele patru straturi

| Strat | Corespunde nivelului existent | Țintă timp | Întrebare | Exemplu deja implementat |
|---|---|---|---|---|
| **1 — TEREN / ACUM** | „nivel rapid" (parte 1) | 10-30 secunde | CE FAC ACUM? | `exact_cue`, `child_message` afișate în Mod Teren |
| **2 — ÎNȚELEGE** | „nivel rapid" (parte 2) | 3-7 minute | DE CE? | pagina de exercițiu/problemă curentă (obiectiv, raționament pe 7 dimensiuni) |
| **3 — APROFUNDEAZĂ** | „nivel aprofundat" (parte 1) | 15-30+ minute | CARE E MECANISMUL ȘI CONTEXTUL? | capitolele Volumelor 01-04 |
| **4 — DOVEZI** | „nivel aprofundat" (parte 2) | fără limită | PE CE SE BAZEAZĂ ȘI CARE SUNT LIMITELE? | `research/dossiers/*`, secțiunile „Dovezi și limite" deja vizibile pe paginile de problemă |

Straturile 1-2 corespund exact la ce site-ul afișează azi implicit fără separare explicită; straturile 3-4 corespund la ce există deja ca documente separate (`content/volume-*`, `research/dossiers/*`) fără o legătură de prezentare formală unificată.

## 2. Regula obligatorie: un obiect, mai multe adâncimi (§32 din prompt)

```
        UN SINGUR OBIECT CANONIC DE CUNOAȘTERE
                        │
        ┌───────────────┼────────────────┬─────────────────┐
        ▼               ▼                ▼                 ▼
   Strat 1: Teren   Strat 2: Înțelege  Strat 3: Aprofundează  Strat 4: Dovezi
   (extras scurt)   (extras mediu)     (link spre capitol)    (link spre dosar)
```

Fiecare strat e o **proiecție** a aceluiași obiect (concept, competență, exercițiu), nu o copie redactată separat. Tehnic, asta înseamnă: straturile 1-2 sunt câmpuri scurte pe obiectul canonic însuși (exact ca azi — `exact_cue`, `primary_objective`); stratul 3 e o **legătură** spre capitolul de volum relevant, nu text duplicat; stratul 4 e o **legătură** spre dosarul de cercetare, nu text duplicat. Regulă deja aplicată corect azi de paginile de problemă (secțiunea „Dovezi și limite" citează claim-uri prin ID, nu retranscrie sursele).

**Interdicție explicită:** niciun nou câmp de tip „text lung duplicat" pe patru niveluri. Dacă un concept nou are nevoie de conținut la Stratul 3, se scrie o dată, ca și azi, într-un capitol sau document de cunoaștere — nu de patru ori.

## 3. Aplicare la obiectele noi din PHASE-29

| Obiect | Strat 1 | Strat 2 | Strat 3 | Strat 4 |
|---|---|---|---|---|
| `PEDAGOG_CONCEPT` / `COACH_CONCEPT` | — (conceptele nu apar direct în Mod Teren, doar prin competențe) | rezumatul din harta de domeniu (`PEDAGOG_DOMAIN_MAP.md`/`COACH_DOMAIN_MAP.md`, coloana „De ce contează") | capitol de volum viitor sau lecție Pedagogul/Antrenorul | dosar de cercetare (`research/dossiers/`) |
| `PEDAGOG_COMPETENCY` / `COACH_COMPETENCY` | „focus de antrenor" în Field Mode V2 (numele competenței) | secțiunea „Indicatori comportamentali" din cadrul de competență (deja scrisă, TASK-2904) | lecția completă de competență (viitoare) | „Bază de dovadă" din cadrul de competență |
| `EXERCISE`/`SESSION` (existente) | `exact_cue`/`child_message` (deja implementat) | pagina curentă de exercițiu (deja implementat) | capitol de volum legat (`related_principles`) | `evidence_boundary` media + claim-uri legate |

## 4. Adaptare de vârstă pe straturi

Stratul 1 (teren) e cel mai sensibil la vârstă — lungimea și complexitatea variază direct cu banda de vârstă (`AGE_SPECIFIC`, conform `PED-D06`). Straturile 3-4 (aprofundează/dovezi) sunt în mare parte `UNIVERSAL` — mecanismul științific nu variază cu vârsta copiilor antrenați, doar traducerea practică (Strat 1-2) variază. Această distincție e exact ce cere §33 din arhitectura master pentru a evita duplicarea completă a conținutului la extinderea multi-vârstă: straturile 3-4 rămân neschimbate, doar straturile 1-2 primesc variante per bandă de vârstă.

## 5. Compatibilitate cu produsul curent

Zero regres. Fiecare pagină existentă deja afișează, fără să numească explicit, o combinație a acestor straturi (ex. pagina de exercițiu = Strat 1 + Strat 2 + legături spre Strat 3/4). Formalizarea nu cere restructurare de UI în PHASE-29 (regulă §65).
