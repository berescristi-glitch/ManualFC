# Modelul KPI de cunoaștere și competență

**Versiune:** 1.0.0 · **Task de referință:** TASK-2909 · **Statut:** Architecture

Înlocuiește gândirea centrată exclusiv pe numărul de exerciții (deja recunoscută ca insuficientă în `reports/audits/MANUALFC_AS_BUILT_PRODUCT_PROGRESS_AUDIT.md` §19, „maturitatea sistemului vs. amploarea conținutului") cu patru dimensiuni distincte. **Fără procent global de completare** — regulă explicită, respectată și de auditul as-built precedent.

## K1 — Profunzimea cunoașterii

Măsoară dacă un domeniu/concept e cercetat suficient pentru a fi predat responsabil.

| Dimensiune | Întrebare de verificare |
|---|---|
| Cercetare completă? | există un dosar de cercetare (`research/dossiers/`) pentru domeniu? |
| Acoperire de claim-uri | câte claim-uri (`CLM-*`) susțin conceptul? |
| Tărie a dovezii documentată | `confidence`/`u11_applicability` completate, nu implicite? |
| Limite explicite | secțiunea „ce NU susține dovada" completată? |
| Implicații de vârstă documentate | `age_sensitivity` (§15, `MANUALFC_KNOWLEDGE_ARCHITECTURE.md`) atribuit? |
| Traducere practică completă | secțiunea „practical translation" duce la comportament concret (§`THEORY_TO_PRACTICE_CONTRACT.md`)? |

**Stare azi (verificabilă):** PED-D05 (eroare) și PED-D09 (safeguarding) sunt la K1 matur — dosar complet, claim-uri legate, traducere practică scrisă. Majoritatea celorlalte domenii Pedagog/Coach sunt la K1 minim — domeniu numit, fără dosar de cercetare dedicat încă.

## K2 — Acoperirea de competențe

Măsurată separat pe cele patru sub-întrebări (§41 din prompt), nu combinat:

1. câte competențe pedagogice sunt definite? (azi: 13, `PEDAGOG_COMPETENCY_FRAMEWORK.md`, complet la nivel de arhitectură)
2. câte competențe de coaching sunt definite? (azi: 18, `COACH_COMPETENCY_FRAMEWORK.md`, complet la nivel de arhitectură)
3. câte competențe sunt legate de o lecție reală? (azi: 0 — lecțiile Pedagogul/Antrenorul nu există încă ca conținut canonic)
4. câte competențe sunt legate de un exercițiu? (azi: 0 formal, dar §Matrice de acoperire din fiecare cadru de competență arată legături informale reale prin `child_message`/`exact_cue`/etc.)
5. câte competențe sunt legate de o ședință? (azi: 0)
6. câte competențe primesc reflecție reală în produs? (azi: 0 — Reflection V2 neimplementat)

## K3 — Integritatea teorie-practică

**Cel mai important KPI** (confirmat explicit de prompt §42, „This is a central ManualFC KPI"). Verifică dacă lanțul complet e conectat, nu doar dacă fiecare verigă există izolat:

```
lecție → comportament de antrenor → practică → observație → reflecție → dezvoltare următoare
```

Se măsoară per obiect, nu global: pentru fiecare concept/competență, câte din cele 6 verigi sunt prezente și legate prin ID (nu doar prin text asemănător)? Un concept cu toate 6 verigi e „lanț complet"; un concept cu doar cercetare și fără traducere practică e „lanț rupt la practică" — exact defectul pe care regula permanentă din §3 (arhitectura master) îl interzice.

**Stare azi:** Decision Engine implementează deja lanțul complet pentru cele 3 probleme flagship (PRB-0001, PRB-0002, PRB-0003) — verificabil: observație → ipoteză → cue → exercițiu → reflecție (`transferState`). Lanțul se rupe azi exact la veriga „competență" (nu există legătură explicită spre `PED-C*`/`COACH-C*`), motiv pentru care K3 pentru produsul curent e **„complet minus un pas"**, nu „rupt".

## K4 — Amploarea practică

Numărătoare simple, deja folosite corect în `EXISTING_PRODUCT_KNOWLEDGE_MAPPING.md` și auditul as-built — separate explicit de calitate (K1-K3):

| Obiect | Curent |
|---|---|
| Probleme | 8 (3 flagship) |
| Principii | 25 |
| Exerciții | 5 |
| Ședințe | 2 |
| Evaluări | 1 |
| Media | 15 |
| Bande de vârstă acoperite | 1 (U11) |

Amploarea NU se combină cu K1-K3 într-un scor unic — regulă explicită (§39, „replace exercise-count-centric thinking").

## Cum se folosesc împreună cele patru

Un domeniu poate fi simultan K1 ridicat + K4 scăzut (ex. PED-D05: cercetare matură, dar folosit în doar câteva exerciții) sau K4 ridicat + K3 rupt (ex. un cluster ipotetic viitor cu 20 de exerciții, dar fără nicio legătură de competență). Cele patru dimensiuni previn exact eroarea pe care auditul as-built a semnalat-o deja: confundarea „mult conținut" cu „produs matur".
