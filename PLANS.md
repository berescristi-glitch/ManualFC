# Planuri de execuție Codex (ExecPlans) — platforma U11

Acest document definește forma planurilor folosite pentru faze și taskuri complexe. Un ExecPlan trebuie să poată fi urmat de un agent care cunoaște doar repository-ul curent și planul respectiv.

## Când este obligatoriu

Folosește un ExecPlan pentru:

- inițializarea arhitecturii;
- fiecare volum;
- un capitol mare cu mai multe artefacte;
- motorul de diagrame și animații;
- sistemul de date și validare;
- generarea PDF;
- integrarea și auditul final;
- orice task care depășește o modificare locală simplă.
- prototipul vertical, pilotarea pe teren și validarea comercială.

## Locație și denumire

Salvează planurile în:

`plans/<task-id>-<slug>.md`

Exemplu:

`plans/TASK-0601-volume-02-perceptie-decizie.md`

## Caracterul planului

Planul este un document viu. Nu îl folosi ca promisiune rigidă. Actualizează-l când apar informații noi, dar păstrează explicația deciziilor și a schimbărilor.

## Structura obligatorie

### 1. Titlu și scop

Descrie rezultatul observabil, nu doar activitatea.

### 2. Context pentru un cititor nou

Explică:

- ce există deja;
- ce documente sunt canonice;
- unde se află datele;
- ce termeni trebuie înțeleși;
- ce taskuri anterioare sunt relevante.

### 3. Rezultatul verificabil

Precizează ce trebuie să poată face utilizatorul sau ce fișiere trebuie să existe la final.

### 4. Domeniu și non-obiective

Definește explicit ce intră și ce nu intră în task. Împiedică extinderea necontrolată.

### 5. Fișiere și module afectate

Listează căile existente și cele ce vor fi create.

### 6. Cercetare necesară

Enumeră întrebările factuale, tipurile de surse și modul de înregistrare a afirmațiilor.

### 7. Model pedagogic

Pentru conținutul de antrenament explică:

- problema de joc;
- percepția și decizia urmărite;
- adecvarea la 10–11 ani;
- transferul în meci;
- riscurile metodologice.

### 8. Design vizual și interactiv

Descrie diagramele, fazele animației, dimensiunile, stările și alternativa pentru PDF.

### 9. Pași de implementare

Pașii trebuie să fie suficient de exacți pentru a fi executați, dar să descrie intenția și efectul, nu doar comenzi arbitrare.

### 10. Validare și acceptare

Include comenzile, verificările manuale și criteriile de acceptare. Un criteriu trebuie să poată fi evaluat ca trecut sau eșuat.

### 11. Progres

Folosește o listă cu marcaje și timestampuri. Actualizeaz-o după fiecare etapă relevantă.

### 12. Descoperiri și surprize

Înregistrează comportamente neașteptate, limite de surse, probleme de build și concluzii care influențează taskurile următoare.

### 13. Jurnal de decizii

Pentru fiecare decizie importantă notează:

- decizia;
- motivul;
- alternativele;
- efectul asupra proiectului;
- data.

### 14. Rezultat și retrospectivă

La încheiere, compară rezultatul cu scopul. Declară ce a rămas incomplet și de ce.

## Reguli de execuție

- Planul trebuie actualizat în timp ce se lucrează, nu rescris retrospectiv.
- Codul, conținutul și planul trebuie să rămână coerente.
- O abatere importantă de la plan trebuie explicată în jurnalul de decizii.
- Planul nu înlocuiește `TASK_REGISTRY.json`; el dezvoltă un task sau un grup strâns de taskuri.
- Un ExecPlan nu poate declara succesul fără rularea validărilor.
