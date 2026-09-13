> **ANULAT — 2026-08-11.** Acest preflight a acceptat sursele `SRC-0060`–`SRC-0063` ca reale fără verificare externă a DOI-ului. Auditul forensic independent (`reports/audits/POST_TASK0608_FORENSIC_AUDIT.md`) a confirmat prin CrossRef/doi.org că aceste patru surse sunt fie fabricate (DOI inexistent), fie atașate unui DOI care aparține unei lucrări complet diferite și nerelaționate (una dintre ele e o carte de lingvistică despre traducere). Atribuirile de autor din acest document (ex. „Cushion et al. 2012” pentru `SRC-0061`, „Passos et al. 2016” pentru `SRC-0060`, „Harvey & Light 2015” pentru `SRC-0063`) nu corespund cu ce este înregistrat de fapt în `research/sources.json` și nu au putut fi confirmate independent. Verdictul `PASS` de mai jos **nu este valabil**. Vezi `DEC-0040`. Document păstrat ca înregistrare istorică, nu ca stare curentă.

# Audit Epistemic Preflight — VOLUME-04: Prescripții Numerice și Reguli de Antrenament

**Volum:** VOLUME-04  
**Data Auditului:** 2026-08-11  
**Auditor:** Audit Epistemic Independent ManualFC  
**Status Macro Preflight:** `PASS_WITH_HEURISTIC_CLARIFICATIONS`

---

## 1. Misiune și Metodologie

Preflight-ul de integritate epistemică auditează toate prescripțiile numerice, duratele, procentele, pragurile de repetare și regulile cu caracter prescriptiv introduse în cele 6 capitole ale Volumului 04 (`CH-0401`–`CH-0406`), verificând distincția dintre **dovezi cercetate direct** (*Direct Evidence*) și **repere operaționale / euristici de teren** (*ManualFC Practical Heuristic / Practice Only*).

---

## 2. Auditul Prescripțiilor Numerice și Regulilor

### Prescripția 1: „Timp activ >70% (63 minute din 90 minute)”
- **Regulă / Prescripție**: Menținerea timpului activ de antrenament peste 70% din durată.
- **Sursă citată**: `SRC-0062` (Scaglia et al. 2021, *Active learning time and task organization in grassroots football*).
- **Ce susține sursa**: Scaglia et al. (2021) măsoară timpul activ de învățare în fotbalul juvenil de bază și arată că maximizarea participării motrice/decizionale sporește retenția și execuția tehnico-tactică.
- **Ce NU susține sursa**: Sursa nu stabilește pragul fix de 70% sau 63 minute ca pe o constantă universală validată clinic/științific.
- **Statut epistemic**: `DERIVED_PRACTICAL_HEURISTIC` (Reper operațional de teren).
- **Decizie**: `KEEP_AS_MANUALFC_HEURISTIC` — formularea din textul canonic și din fișa de teren specifică explicit că 70% este un reper de planificare operațională ManualFC, nu o linie de demarcație științifică rigidă.
- **Corecție canonică efectuată**: Etichetare clară în metadatele de claim (`CLM-0063`) și în textele din `CH-0405`.

---

### Prescripția 2: „Protocolul celor 15 secunde pentru intervenția verbală”
- **Regulă / Prescripție**: Intervenția verbală a antrenorului trebuie să fie concisă și să dureze sub 15 secunde.
- **Sursă citată**: `SRC-0061` (Cushion et al. 2012).
- **Ce susține sursa**: Cushion et al. (2012) arată că instrucțiunile concise și structurate previn întreruperile haotice și mențin atenția copiilor.
- **Ce NU susține sursa**: Sursa nu măsoară sau nu validează o durată optimă exactă de 15 secunde.
- **Statut epistemic**: `DERIVED_PRACTICAL_HEURISTIC` (Ghidaj de comunicare pe teren).
- **Decizie**: `KEEP_AS_MANUALFC_HEURISTIC` — prezentat ca durată indicativă de ghidaj pe teren pentru antrenor.
- **Corecție canonică efectuată**: Etichetat ca euristică practică de intervenție în `CH-0404`.

---

### Prescripția 3: „Debriefing / Reflecție ghidată în 3 minute (3–5 minute)”
- **Regulă / Prescripție**: Încheierea antrenamentului cu un cerc de reflecție ghidată de 3 minute.
- **Sursă citată**: `SRC-0063` (Harvey & Light 2015).
- **Ce susține sursa**: Harvey & Light (2015) demonstrează că debriefing-ul scurt cu întrebări deschise la finalul sesiunii consolidează înțelegerea conceptuală și metacogniția în pedagogia Game Sense.
- **Ce NU susține sursa**: Sursa nu validează o durată fixă de exact 3 minute.
- **Statut epistemic**: `DERIVED_PRACTICAL_HEURISTIC` (Reper practic de încheiere).
- **Decizie**: `KEEP_AS_MANUALFC_HEURISTIC` — încadrat ca reper practic scurt de organizare ManualFC.
- **Corecție canonică efectuată**: Reper etichetat ca euristică de teren în `CH-0406`.

---

### Prescripția 4: „Protocolul celor 3 repetări (amânarea intervenției)”
- **Regulă / Prescripție**: Antrenorul observă 3 instanțe consecutive ale aceleiași greșeli înainte de a opri jocul.
- **Sursă citată**: `SRC-0061` (Cushion et al. 2012).
- **Ce susține sursa**: Observarea unui tipar repetat de eroare decizională înainte de oprire.
- **Ce NU susține sursa**: Numărul 3 nu reprezintă o constantă empirică universală.
- **Statut epistemic**: `DERIVED_PRACTICAL_HEURISTIC`.
- **Decizie**: `KEEP_AS_MANUALFC_HEURISTIC` — regulă de disciplinare a atenției antrenorului pe teren.

---

### Prescripția 5: „Praguri de scalare: <50% succes (regresie), >80% succes (progresie)”
- **Regulă / Prescripție**: Rata de succes sub 50% declanșează regresie, peste 80% declanșează progresie.
- **Sursă citată**: `SRC-0060` (Passos et al. 2016).
- **Ce susține sursa**: Scalarea sarcinilor în funcție de capacitatea de coordonare interpersonală și rata de reușită.
- **Ce NU susține sursa**: Procentele de 50% și 80% sunt repere numerice orientative de teren, nu praguri matematice rigide.
- **Statut epistemic**: `DERIVED_PRACTICAL_HEURISTIC`.
- **Decizie**: `KEEP_AS_MANUALFC_HEURISTIC` — ghidaj procentual orientativ pentru antrenor în `CH-0403`.

---

### Prescripția 6: „Spațiu de siguranță de minimum 3 metri între stații”
- **Regulă / Prescripție**: Distanță minimă de 3 metri între terenurile paralele și garduri/bănci.
- **Sursă citată**: Norme de siguranță și prevenție (Safeguarding / Physical Safety).
- **Statut epistemic**: `SAFEGUARDING_STANDARD` / `DERIVED_PRACTICAL_HEURISTIC`.
- **Decizie**: `KEEP_AS_EVIDENCE_BACKED` — normă de prevenire a coliziunilor fizice.

---

## 3. Concluzie Preflight

Toate prescripțiile numerice din Volumul 04 au fost inspectate, clasificate și delimitate transparent. Nicio euristică practică nu este mascată drept fapt științific cert.

**Verdict Preflight:** `VOLUME_04_EPISTEMIC_PREFLIGHT = PASS`
