# Raport de migrare a roadmapului

## Baseline și reconcilierea TASK-0104

Baseline: 177 taskuri, 6 `DONE`, progres 2,462%. Commitul TASK-0104 are exact
31 de fișiere, 1.484 inserții și 18 ștergeri. Raportul TASK-0104 numără 19
outputuri declarate, iar sumarul numără toate cele 31 de fișiere atinse. Este o
diferență de metodă, nu o abatere.

## Rezultat

Registrul migrat are 188 taskuri. Cele șase taskuri închise înaintea pivotului
rămân `DONE` și își păstrează exact ponderile însumate de 2,462%. TASK-0003
adaugă progres numai după validare. Fiecare task are câmpul
`migration_disposition`, validat prin schemă.

Au fost adăugate TASK-0003, TASK-0004 și TASK-0410–TASK-0418: pivot,
orchestrator, specificația/producția/auditul/pilotul/repararea prototipului,
blocarea șablonului, versiunea pilot, validarea comercială și decizia multi-age.

Taskurile tehnice 0401, 0302, 0201, 0402, 0303, 0403, 0304, 0404, 0405 și 0407
au fost mutate într-un lanț explicit după TASK-0004. Cercetarea încă neexecutată
0105–0109 este mutată după blocarea șablonului canonic. Capitolele sunt marcate
`SPLIT`, deoarece producția și auditurile pedagogic/editorial trebuie urmărite
separat. Vechile capitole despre „manualul digital” sunt `REPLACE`, fiind
absorbite de arhitectura platformei. Buildul PDF este `MOVE_LATER`, ca livrabil
secundar.

În plus, TASK-0111 este deja `READY` după închiderea dependenței TASK-0103, iar
TASK-0004 a fost recalibrat pentru a reutiliza un control plane extern în loc să
construiască un orchestrator autonom intern.

TASK-0418 este `DEFER_TO_MULTI_AGE`; nu produce conținut 4–18 ani. Nu au fost
șterse taskuri și nici istoricul. Toate dispozițiile individuale sunt păstrate
direct în `TASK_REGISTRY.json`, care constituie anexa completă auditabilă.

Distribuția finală este: 113 `KEEP_WITH_WEB_OUTPUT`, 1 `KEEP_UNCHANGED`, 17
`MOVE_EARLIER`, 10 `MOVE_LATER`, 42 `SPLIT`, 4 `REPLACE` și 1
`DEFER_TO_MULTI_AGE`. Nu există `MERGE` sau `REMOVE_WITH_JUSTIFICATION`, deoarece
nicio responsabilitate existentă nu a trebuit eliminată ori absorbită complet.

## Ordinea rezultată

TASK-0004 → fundație site → design system → sistem conținut/pagini → motor
diagrame → motor animații → prototip „Sprijinul și unghiul de pasă” → audit →
pilot pe teren → reparare → șablon canonic → producție U11 → versiune pilot →
validare comercială → decizie viitoare multi-age.
