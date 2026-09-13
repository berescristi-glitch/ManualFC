# TASK-2717 — Wave-1 browser acceptance și baseline

## Scop și rezultat verificabil

Auditează independent candidatul Wave-1 comis, îl publică numai ca Vercel Preview, verifică fluxurile critice la 1440/1280/768/390 și îngheață baseline-ul doar la verdict `PASS`.

## Progres

- [x] Task formalizat.
- [x] Candidat curat `c18263c` identificat și validat complet.
- [x] Preview exact `dpl_E8523A8CMnkriJ2XRCMwwDBH4XGW` creat fără promovare în Production ManualFC.
- [x] Audit browser independent la 1440/1280/768/390, executat cu `Protection Bypass for Automation` (vezi `reports/audits/MANUALFC_WAVE1_BROWSER_ACCEPTANCE.md`).
- [x] Reparare condițională: 2 constatări Major reparate, commit `15694b0`, validare locală completă PASS.
- [x] Re-audit browser-first pe Preview nou publicat din `15694b0` (`dpl_HrfVSK6s8qYFLoiPby3UQhyurMj9`, deploy din worktree izolat) — PASS la toate cele 4 viewporturi, 0 regresii.
- [x] Baseline, rapoarte și registre finalizate; bucla oprită. `MANUALFC_PREMIUM_WAVE1_BASELINE = 15694b0`.

## Condiție de oprire

După baseline nu începe niciun task TASK-2705–TASK-2716.

## Descoperire operațională

Prima tentativă din snapshot nu a găsit metadatele locale de link și a creat proiectul separat `manualfc-wave1-c18263c`; primul deploy a devenit Production numai în acel proiect nou. Proiectul și Production-ul canonic `manualfc` nu au fost modificate. Snapshotul a fost apoi legat corect la `manualfc`, iar deploymentul autoritativ este Preview-ul de mai sus. Proiectul accidental nu este șters fără autorizare explicită.
