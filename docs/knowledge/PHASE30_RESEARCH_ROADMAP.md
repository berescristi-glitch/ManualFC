# Roadmap de cercetare — PHASE-30

**Versiune:** 1.0.0 · **Task de referință:** TASK-2909 · **Statut:** Architecture — planificare, nu execuție

Prioritizare pe bază de dependență, importanță fundamentală, impact asupra Gold Standard curent, relevanță pentru Coach Development și risc de afirmații nesusținute — nu ordine alfabetică (regulă explicită §47).

## 1. Metodă de prioritizare

Un domeniu primește prioritate `CRITICAL` de cercetare dacă întrunește cel puțin 2 din 5 criterii: (a) alte domenii depind de el; (b) fundamentează un exercițiu/problemă deja canonic(ă); (c) relevant direct pentru Coach Development; (d) risc mare de afirmație nesusținută dacă rămâne needocumentat; (e) zero acoperire de cercetare azi.

## 2. Clustere inițiale de cercetare — evaluate, nu acceptate necondiționat

Lista candidată din prompt (§48) evaluată împotriva criteriilor de mai sus:

| Cluster candidat | (a) Dependență | (b) Impact Gold Standard | (c) Coach Dev | (d) Risc | (e) Zero azi | Verdict |
|---|---|---|---|---|---|---|
| Dezvoltarea copilului 10-11 | DA (fundamentează tot) | DA (PED-D01) | DA | DA | PARȚIAL | **CRITICAL — Val 1** |
| Eroare și siguranță psihologică | DA | DA (deja PRB/EX legate) | DA | — | NU (deja acoperit) | **redus la LOW — deja matur** |
| Motivație/autonomie | DA | PARȚIAL | DA | DA | DA | **CRITICAL — Val 1** |
| Atenție | DA (percepție/decizie) | DA (PRB-0003) | — | — | PARȚIAL | **HIGH — Val 1** |
| Feedback | DA | DA (`child_message` peste tot) | DA | — | PARȚIAL | **HIGH — Val 1** |
| Chestionare | — | DA | DA | — | PARȚIAL | **HIGH — Val 2** |
| Intervenția antrenorului (când NU intervine) | DA | DA | DA | DA (risc de „joystick coaching" nedocumentat în afara unui capitol) | PARȚIAL | **CRITICAL — Val 1** |
| Achiziția deprinderii (skill acquisition) | DA | DA | — | — | PARȚIAL | **HIGH — Val 2** |
| Percepție-decizie-acțiune | DA | DA (nucleul Decision Engine) | DA | — | PARȚIAL | **CRITICAL — Val 1** |
| Design reprezentativ de învățare | — | DA (deja principiu de exercițiu) | — | — | NU (deja acoperit, `ch-0801`) | **LOW — deja matur** |
| Transfer | DA | DA | DA | DA (`FIELD_INPUT_REQUIRED` structural) | PARȚIAL | **CRITICAL, dar limitat de field input — Val 1 pentru partea teoretică** |
| Reflecție (a antrenorului) | DA (Coach Development) | — | DA | — | DA | **HIGH — Val 2** |

## 3. Secvența propusă

**Valul 1 (fundamente, dependință maximă):** dezvoltarea copilului 10-11 (PED-D01) · motivație/autonomie (PED-D03) · atenție (PED-D02-S01) · feedback (PED-D06-S05/COACH-D08) · intervenția antrenorului — când nu intervine (COACH-D06) · percepție-decizie-acțiune (COACH-D22/D23) · fundamentul teoretic al transferului (PED-D02-S08/COACH-D25, partea care NU cere date de teren).

**Valul 2 (extindere directă din Val 1):** chestionare (COACH-D07) · achiziția deprinderii/variabilitate practică (PED-D02-S05-S07) · reflecția antrenorului (COACH-D32/33, fundamentează Coach Development) · emoții — frustrare/anxietate (PED-D04-S01/S02, dincolo de siguranța psihologică deja acoperită) · relație pedagogică — autoritate/limite (PED-D07).

**Valul 3 (completare, dependință redusă):** dinamică de grup (PED-D08) · părinți (PED-D10, zero cercetare azi, dar fără urgență de Gold Standard) · diferențe individuale — extindere dincolo de variabilitatea de dezvoltare deja parțial acoperită (PED-D11) · planificare de ședință pe termen mediu (COACH-D28, `season-plans` gol).

**Nu se re-cercetează** (deja matur, confirmat prin dosar real): eroare/decizie autonomă (`ch-0103`), siguranță emoțională (`ch-0303`), limbaj concis (`ch-0301`), design reprezentativ (`ch-0801`), constrângeri de sarcină (`ch-0802`).

## 4. De ce nu lista candidată brută, necondiționată

Prompt-ul PHASE-29 §48 cere explicit să nu se accepte lista candidată necondiționat. Doi itemi din lista candidată (siguranță psihologică/eroare, design reprezentativ) au fost retrogradați la prioritate joasă pentru că **deja există** dosare complete și traduceri practice funcționale — cercetarea suplimentară ar fi resursă irosită față de domenii cu zero acoperire (părinți, planificare pe termen mediu, reflecția antrenorului).

## 5. Legătură cu PHASE-30

Acest document e intrarea directă pentru un viitor `TASK-30xx` de cercetare — nu se execută nicio cercetare nouă în PHASE-29 (regulă §8, „PHASE-29 should NOT yet produce ... deep full-domain research dossiers").
