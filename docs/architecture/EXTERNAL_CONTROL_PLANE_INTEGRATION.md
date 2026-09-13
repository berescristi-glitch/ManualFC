# Specificație de Arhitectură: Integrarea cu Control Plane Extern și Plafonul Strict de Automatizare (Hard Automation Budget)

**Versiune:** 1.0.0  
**Data:** 2026-08-09  
**Statut:** Canonical / Approved  
**Task de referință:** TASK-0004  

---

## 1. Misiune și Principii Fundamentale

Platforma ManualFC este un produs pedagogic web pentru antrenori și copii de vârstă U11 (10–11 ani). Arhitectura proiectului separă clar **produsul final** (aplicația web Astro/TypeScript, manualele, exercițiile, resursele PDF) de **infrastructura de gestiune** (control plane-ul de taskuri, validatoarele, auditul).

### Principiul de Decizie Strategică:
> ManualFC este produsul; control plane-ul este doar o infrastructură auxiliară. Dacă trebuie ales între o îmbunătățire a automatizării și construirea unei componente reale a aplicației ManualFC, se alege întotdeauna construirea componentei de produs.

---

## 2. Politica Hard Automation Budget

Pentru a preveni consumul nejustificat de efort pe infrastructură în detrimentul produsului, se aplică regula strictă **HARD AUTOMATION BUDGET**:

1. **Plafon de intervenții:** Sunt permise maximum **2 intervenții/taskuri suplimentare** dedicated exclusiv integrării, reparării sau extinderii control plane-ului. TASK-0004 reprezintă prima intervenție.
2. **Gate de evaluare a diferențelor (Gap Assessment Gate):**
   După obținerea unei dovezi curate de integrare (*clean integration proof*):
   - **`NONE` (Gap inexistent):** Se folosește infrastructura existentă și se trece imediat la implementarea produsului web (`TASK-0401`).
   - **`SMALL_ADAPTER` (Diferență minoră):** Este permis un singur task suplimentar pentru construirea unui adaptor minim.
   - **`MODERATE_GAP` / `MAJOR_REWORK` (Diferență medie/majoră):** Se abandonează extinderea automatizării și se trece direct la dezvoltarea produsului prin interfața Copilot/Codex.
3. **Definiția eșecului automatizării:**
   Direcția de automatizare este considerată eșuată pentru scopul ManualFC dacă, după maximum 2 intervenții, nu poate executa sigur un task, necesită adaptoare succesive, creează blocaje structurale sau consumă mai mult efort decât economisește.

---

## 3. Rolul Control Plane-ului și Contractul de Integrare

Control plane-ul extern își păstrează rolul de:
- **Auditor:** Verifică conformitatea produsului și a structurii repository-ului.
- **Validator:** Rulează scripturile de validare `validate_project.py` și `validate_content.py`.
- **Task Selector:** Selectează deterministic primul task în stare `READY` pe baza dependențelor închise (`DONE`).
- **Approval Gate:** Asigură aprobarea umană și verificarea dovezilor înainte de închiderea unui task.

Copilot/Codex rămâne executorul efectiv al codului și conținutului pedagogic. Lipsa unui *one-command autonomous loop* complet dezvoltat intern NU constituie un blocker pentru livrarea ManualFC.

---

## 4. Mecanismul Deterministic de Selecție a Taskurilor

Ordinea de execuție a taskurilor este strict determinată de registrul persistent `TASK_REGISTRY.json`:

1. Un task este eligibil pentru stare `READY` numai dacă toate taskurile enumerate în proprietatea `dependencies` au starea `DONE`.
2. Starea `IN_PROGRESS` este atribuită unui singur task principal la un moment dat.
3. Trecerea în starea `DONE` necesită:
   - Existența fizică a tuturor fișierelor declarate în `outputs`.
   - Rularea cu cod de ieșire `0` a tuturor comenzilor din `validation_commands`.
   - Existența raportului oficial de task în `reports/task-reports/<TASK-ID>.md`.

---

## 5. Matrice de Evaluare și Traseul Curent

| Parametru Evaluation | Valoare Curentă | Concluzie & Acțiune |
| :--- | :--- | :--- |
| **Integrabilitate control plane** | Confirmată prin `scripts/control_plane_integration.py` | Clean integration proof validat |
| **Clasificare Gap** | **`NONE`** | Nu sunt necesare adaptoare suplimentare |
| **Consum buget automatizare** | 1 / 2 taskuri (TASK-0004) | Bugetul rămâne conservat |
| **Următoarea acțiune obligatorie** | **Dezvoltare Produs** | Trecere imediată la `TASK-0401` (Bootstrap Astro & TS) |

---

## 6. Rezumatul Contractului de Interfață (`control_plane_integration.py`)

Interfața oferă următoarele funcții Fail-Closed:
- `get_next_ready_task(registry_path)` -> Returnează primul task `READY` valabil sau `None`.
- `validate_task_completion(task_id, registry_path)` -> Validează outputurile și raportul unui task.
- `evaluate_automation_budget_gate(gap_status)` -> Dictă ruta către produs sau adaptor.

Documentul reprezintă norma de arhitectură tehnică pentru integrarea cu control plane-ul extern în proiectul ManualFC.
