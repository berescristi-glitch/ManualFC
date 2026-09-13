# Cadrul de competențe al Pedagogului

**Versiune:** 1.0.0 · **Task de referință:** TASK-2904 · **Statut:** Architecture, complet la nivel de arhitectură (nu autorat final)

O competență **nu e un subiect** — descrie ce e capabil să facă antrenorul, observabil. Fiecare competență de mai jos poate fi legată stabil de o lecție Pedagogul, un exercițiu, o ședință, Field Mode, Reflecție sau un curriculum Academy — ID-urile sunt independente de UI (regulă §16 din prompt-ul PHASE-29).

Prefix ID: `PED-C`. Nu există scor numeric, nu există niveluri de rang — regulă permanentă (secțiunea 15 din prompt).

---

### PED-C01 — Observă înainte de a judeca
**Definiție:** Descrie comportamentul copilului așa cum apare, înainte de a-l interpreta sau eticheta.
**De ce contează:** Fundamentul întregului Decision Engine — deja separat semantic în produs (`OBSERVATION` vs. `POSSIBLE_CAUSE`, `CONTENT_TAXONOMY.md` §4).

| Câmp | Conținut |
|---|---|
| Cunoaștere necesară | PED-D01 (dezvoltare), PED-D02 (învățare) |
| Indicatori comportamentali | descrie acțiunea observată în propoziții factuale; separă explicit „văd" de „cred" |
| Exemplu de bună practică | „Copilul rămâne pe loc după pasă" (nu „copilul e leneș") |
| Anti-tipar | sare direct la etichetă de caracter sau capacitate |
| Exemplu situațional | doi copii nu cer mingea sub presiune — antrenorul notează comportamentul, nu conchide „le e frică" fără verificare |
| Cunoaștere legată | PED-D01, PED-D02 |
| Practică legată | `problem-library.json` → câmpul `observable_behavior` (deja implementat) |
| Întrebări de reflecție | Ce am văzut concret, fără cuvinte care presupun o cauză? |
| Bază de dovadă | HIGH — separarea observație/interpretare e fundament în formarea profesorilor și antrenorilor |
| Considerații de vârstă | universal — nu variază cu vârsta copilului, variază complexitatea comportamentului observat |

---

### PED-C02 — Înțelege comportamentul în context de dezvoltare
**Definiție:** Interpretează un comportament ținând cont de variabilitatea normală de dezvoltare, nu de un standard fix pe vârstă cronologică.

| Câmp | Conținut |
|---|---|
| Cunoaștere necesară | PED-D01 (toate subdomeniile) |
| Indicatori comportamentali | nu compară doi copii de aceeași vârstă cronologică ca și cum ar trebui să fie identici |
| Exemplu de bună practică | recunoaște că doi copii de 10 ani pot fi la maturizări diferite fără să tragă o concluzie despre potențial |
| Anti-tipar | „la vârsta asta ar trebui să știe deja" |
| Exemplu situațional | un copil matur fizic domină un exercițiu — antrenorul nu confundă asta cu superioritate tehnică/tactică reală |
| Cunoaștere legată | PED-D01-S05, PED-D01-S06, PED-D01-S07 |
| Practică legată | regresie/progresie individuală (schema exercițiu) |
| Întrebări de reflecție | Am presupus o normă de vârstă care nu ține cont de variabilitate? |
| Bază de dovadă | CRITICAL |
| Considerații de vârstă | AGE_SPECIFIC — conținut direct despre variabilitatea 10-11 ani |

---

### PED-C03 — Comunică adecvat vârstei
**Definiție:** Formulează mesajul cu lungime, complexitate și limbaj potrivite pentru 10-11 ani.

| Câmp | Conținut |
|---|---|
| Cunoaștere necesară | PED-D06-S01, PED-D02-S03 (încărcare cognitivă) |
| Indicatori comportamentali | propoziții scurte, un singur concept per mesaj |
| Exemplu | „Uită-te la con înainte să primești" (o singură instrucțiune) |
| Anti-tipar | instrucțiune cu 3 clauze condiționale simultan |
| Cunoaștere legată | PED-D06 |
| Practică legată | `child_message` din schema exercițiu (deja implementat) |
| Întrebări de reflecție | Ar înțelege un copil de 10 ani asta din prima? |
| Bază de dovadă | HIGH |
| Considerații de vârstă | AGE_SPECIFIC |

---

### PED-C04 — Ascultă activ
**Definiție:** Primește ce comunică verbal și non-verbal copilul înainte de a răspunde.

| Câmp | Conținut |
|---|---|
| Indicatori comportamentali | lasă copilul să termine, reformulează ce a înțeles |
| Anti-tipar | întrerupe, presupune răspunsul |
| Cunoaștere legată | PED-D06-S02 |
| Practică legată | chestionare ghidată (COACH-C04) |
| Bază de dovadă | MEDIUM |
| Considerații de vârstă | universal |

---

### PED-C05 — Creează siguranță psihologică
**Definiție:** Construiește un climat în care greșeala nu produce teamă de expunere.

| Câmp | Conținut |
|---|---|
| Cunoaștere necesară | PED-D04-S06, PED-D05-S02 |
| Indicatori comportamentali | răspunde la greșeală cu informație, nu cu critică publică |
| Exemplu | „Ce ai văzut înainte de pasă?" în loc de „Nu așa!" |
| Anti-tipar | corectează public în fața grupului repetat |
| Cunoaștere legată | PED-D04, PED-D05 |
| Practică legată | `child_message` + `PED-C06` |
| Bază de dovadă | CRITICAL |
| Considerații de vârstă | universal, dar sensibilitate mai mare la 10-11 ani (conștiință socială crescută) |

---

### PED-C06 — Răspunde constructiv la eroare
**Definiție:** Tratează greșeala ca informație despre sarcină, nu ca verdict despre copil.

| Câmp | Conținut |
|---|---|
| Cunoaștere necesară | PED-D05 (complet) |
| Indicatori comportamentali | reconstruiește episodul (ce informație era disponibilă, ce a ales copilul) înainte de a corecta |
| Exemplu de bună practică | vezi `research/dossiers/ch-0103-decision-error.md` — traducerea practică deja documentată |
| Anti-tipar | „joystick coaching" — comandă continuă la fiecare greșeală |
| Cunoaștere legată | PED-D05, dosar de cercetare deja existent |
| Practică legată | `docs/architecture/ASSESSMENT_REFLECTION_LOOP.md` |
| Bază de dovadă | HIGH — cel mai bine documentat domeniu din tot Pedagogul |
| Considerații de vârstă | universal |

---

### PED-C07 — Susține autonomia
**Definiție:** Oferă copilului spațiu real de alegere, fără a abandona structura.

| Câmp | Conținut |
|---|---|
| Cunoaștere necesară | PED-D03-S02, PED-D02-S04 (explorare) |
| Indicatori comportamentali | oferă opțiuni reale, nu o singură soluție „corectă" |
| Anti-tipar | oferă o „alegere" cu un singur răspuns acceptat |
| Cunoaștere legată | PED-D03, PED-D02 |
| Practică legată | regresie/progresie, decizie liberă în exercițiu |
| Bază de dovadă | HIGH |
| Considerații de vârstă | AGE_SENSITIVE |

---

### PED-C08 — Protejează demnitatea
**Definiție:** Evită orice acțiune care expune copilul la rușine publică.

| Câmp | Conținut |
|---|---|
| Cunoaștere necesară | PED-D04-S04, PED-D07 |
| Indicatori comportamentali | corectează individual, nu evidențiază public eșecul |
| Anti-tipar | folosește un copil ca exemplu negativ în fața grupului |
| Cunoaștere legată | PED-D04, PED-D07, PED-D09 (safeguarding) |
| Bază de dovadă | HIGH |
| Considerații de vârstă | universal, cu sensibilitate crescută la 10-11 (conștiință socială) |

---

### PED-C09 — Stabilește limite sănătoase
**Definiție:** Menține autoritate fără autoritarism, cu limite clare și respectuoase.

| Câmp | Conținut |
|---|---|
| Cunoaștere necesară | PED-D07 (complet) |
| Indicatori comportamentali | explică limita, nu doar o impune |
| Anti-tipar | disciplină prin frică sau umilire |
| Cunoaștere legată | PED-D07, PED-D09 |
| Practică legată | `content/volume-03/ch-0304` (disciplină respectuoasă) — deja acoperit |
| Bază de dovadă | HIGH |
| Considerații de vârstă | universal |

---

### PED-C10 — Adaptează la diferențe individuale
**Definiție:** Ajustează sarcina la copilul din fața lui, fără etichetare sau diagnostic.

| Câmp | Conținut |
|---|---|
| Cunoaștere necesară | PED-D01-S06, PED-D11 (complet) |
| Indicatori comportamentali | oferă variantă individuală discret, nu vizibil separat |
| Anti-tipar | grupare vizibilă „nivel slab" / „nivel bun" |
| Cunoaștere legată | PED-D11 |
| Practică legată | regresie/progresie per exercițiu |
| Bază de dovadă | CRITICAL |
| Considerații de vârstă | AGE_SPECIFIC |

---

### PED-C11 — Creează apartenență
**Definiție:** Construiește un climat de grup în care fiecare copil se simte inclus.

| Câmp | Conținut |
|---|---|
| Cunoaștere necesară | PED-D08 (complet) |
| Indicatori comportamentali | rotește activ copiii marginali în roluri centrale |
| Anti-tipar | lasă aceiași copii mereu la marginea exercițiului |
| Cunoaștere legată | PED-D08 |
| Practică legată | Group Configurator (rotație, deja implementat) |
| Bază de dovadă | HIGH |
| Considerații de vârstă | universal |

---

### PED-C12 — Lucrează constructiv cu părinții
**Definiție:** Comunică cu adulții din jurul copilului fără a compromite prioritatea dezvoltării.

| Câmp | Conținut |
|---|---|
| Cunoaștere necesară | PED-D10 (complet) |
| Indicatori comportamentali | explică prioritatea dezvoltării înainte de rezultat, cu exemple concrete |
| Anti-tipar | evită orice conversație cu părinții sau cedează presiunii de rezultat |
| Cunoaștere legată | PED-D10 |
| Practică legată | — (neimplementat azi) |
| Bază de dovadă | MEDIUM — zero cercetare directă în produs azi |
| Considerații de vârstă | universal |

---

### PED-C13 — Reflectează asupra propriului impact
**Definiție:** Evaluează onest efectul propriilor cuvinte/acțiuni asupra copilului, nu doar rezultatul.

| Câmp | Conținut |
|---|---|
| Cunoaștere necesară | PED-D12, COACH-D32/33 |
| Indicatori comportamentali | identifică un moment concret unde reacția proprie a ajutat/încurcat |
| Anti-tipar | reflectă doar asupra performanței copiilor, niciodată asupra propriei intervenții |
| Cunoaștere legată | PED-D12 |
| Practică legată | Reflection V2 (specificat, neimplementat — vezi `THEORY_TO_PRACTICE_CONTRACT.md`) |
| Bază de dovadă | MEDIUM |
| Considerații de vârstă | n/a (despre antrenor, nu despre copil) |

---

## Matrice de acoperire (competență × practică curentă)

| Competență | Deja conectată la practică? | Cum |
|---|---|---|
| PED-C01, PED-C06 | DA | Decision Engine, `observable_behavior` |
| PED-C03 | DA | `child_message` |
| PED-C10, PED-C07 | PARȚIAL | regresie/progresie există, dar fără legătură explicită de ID |
| PED-C11 | PARȚIAL | Group Configurator (rotație), fără legătură explicită |
| PED-C02, PED-C04, PED-C05, PED-C08, PED-C09, PED-C13 | NU | conceptual prezente în copy, fără ID de competență în date |
| PED-C12 | NU | zero prezență azi |

Această matrice devine baza pentru K2 (`KNOWLEDGE_AND_COMPETENCY_KPI_MODEL.md`).
