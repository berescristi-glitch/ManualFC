# Assessment & Reflection Loop — contract de domeniu

## Scop

TASK-2803 închide bucla OBSERVĂ → ÎNȚELEGE → TESTEAZĂ → INTERVINE → PREGĂTEȘTE → RULEAZĂ → REFLECTĂ → VERIFICĂ TRANSFERUL → DECIDE URMĂTORUL PAS. Extinde Session Workspace (`TASK-2802`) cu o reflecție scurtă, post-ședință, care face starea locală persistentă pedagogic utilă — nu un tablou de statistici, un scor de copil sau o evaluare a competenței antrenorului.

## Extensie de domeniu, nu model paralel

`SessionReflection` este un câmp nou (`reflections: SessionReflection[]`) pe același `CoachState` versionat (`manualfc.coach-state.v1`) din `TASK-2802` — extensie compatibilă retroactiv (varianta A din opțiunile disponibile), nu o nouă versiune de schemă. `sanitizeState()` completează `reflections: []` pentru orice stare `v1` existentă fără acest câmp; `saved`, `favorites`, `recents`, `sessions` rămân neatinse. Nicio stare TASK-2802 existentă nu se pierde.

O reflecție păstrează exclusiv:

- referințe stabile: `workspaceSessionId?`, `canonicalSessionId?` (ex. `SES-0001`), `problemId?` (ex. `PRB-0001`), `exerciseIds[]`;
- două stări structurate: `observedState` (`not_observed` / `emerging` / `partial` / `consistent_in_task`) și `transferState` (`transfer_unconfirmed` / `transfer_seen`);
- text opțional, scurt: `whatWorked`, `whyItHappened`, `whatToChange`, `coachNote`.

Conținutul pedagogic (mesajul copilului, criteriile de evaluare, verificarea de transfer) rămâne exclusiv în sursele canonice (`data/problems/problem-library.json`, `data/assessments/*.json`). Pagina de reflecție randează contextul din acele surse la citire; nu îl copiază în starea persistată.

## Distincția critică: performanță în sarcină vs. transfer

`observedState` răspunde la „a apărut comportamentul în exercițiu?”. `transferState` răspunde la o întrebare separată — „a apărut și în jocul liber, fără constrângeri?” — și este întrebată explicit numai când `observedState` este `partial` sau `consistent_in_task` (nu are sens să verifici transferul unui comportament care nu a apărut încă în sarcină). Implicit, `transferState = transfer_unconfirmed`; devine `transfer_seen` numai dacă antrenorul raportează explicit observația. Produsul nu declară niciodată transferul confirmat din reușita unui exercițiu.

## Recomandarea „ce urmează” este deterministă, nu generată liber

`computeNextAction(observedState, transferState)` din `coach-state.ts` este o funcție pură, un tabel fix de decizie — nu text liber, nu AI, nu inventat la afișare:

| observedState | transferState | Recomandare |
|---|---|---|
| `not_observed` | — | Reconsideră ipoteza: încearcă o regresie sau un test diferit. |
| `emerging` | — | Repetă sarcina cu același reper; comportamentul abia apare. |
| `partial` | — | Repetă sau ajustează o singură variabilă a sarcinii. |
| `consistent_in_task` | `transfer_unconfirmed` | Păstrează reperul și testează dacă apare și în joc mai liber. |
| `consistent_in_task` | `transfer_seen` | Crește dificultatea sau verifică transferul într-un context diferit. |

Recomandarea nu este stocată — se recalculează la fiecare afișare din cele două stări persistate, deci nu poate ajunge desincronizată de starea reală.

## Context canonic, fără reintroducere manuală

`/spatiul-meu/reflectie` primește context prin query string (`?ws=`, `?sesiune=`, `?problema=`, `?id=` pentru editare) și rezolvă automat, din date canonice deja încărcate în pagină la build: titlul ședinței/exercițiilor, mesajul exact pentru copil (`child_cues[0].say`), criteriile de evaluare canonice legate de exercițiile problemei (extrase din `ASM-0001`, filtrate după exercițiul menționat în text) și verificarea de transfer canonică (`transfer_checks[0].text`). Antrenorul nu retastează nimic cunoscut. Dacă nu există context (`id`/`ws`/`sesiune`/`problema` toate absente), pagina arată explicit „Reflecție liberă, fără context canonic legat” — nu fabrică o problemă sau o ședință.

## Field Mode → Reflecție, fără a întrerupe un segment activ

Bara de navigare din Mod Teren rămâne neschimbată în timpul segmentelor active. Doar la ultimul segment, butonul „Următorul” devine „Termină ședința → Reflecție” și duce la `/spatiul-meu/reflectie?sesiune=...&durata=...`, păstrând `problema`/`sursa` din URL dacă erau prezente (provenite din Decision Engine). Nu există stare intermediară care să ceară reflecție în timp ce antrenorul rulează un segment.

## Continue V2 — prioritate determinist documentată

`/spatiul-meu` calculează cardul „Continuă” în această ordine fixă:

1. ședință Workspace activă (neterminată) — neschimbat față de TASK-2802;
2. o ședință Workspace construită, ne-activă, fără nicio reflecție legată încă (`findUnreflectedSession`) — invită explicit la reflecție;
3. cea mai recentă reflecție salvată, cu recomandarea ei determinist calculată;
4. cel mai recent reper canonic vizitat (comportamentul original TASK-2802).

## Istoric, editare, ștergere

Reflecțiile apar pe `/spatiul-meu`, cele mai noi primele (ordinea de creare — o reflecție editată își păstrează poziția, `updatedAt` se actualizează, `createdAt` nu). O reflecție este complet editabilă la `/spatiul-meu/reflectie?id=...` (aceleași câmpuri, aceeași funcție `saveReflection`, care păstrează `id`/`createdAt` și rescrie `updatedAt`). Atât o ședință Workspace cât și o reflecție pot fi șterse direct din `/spatiul-meu`, cu o confirmare nativă a browserului — nu există istoric local imposibil de șters.

## Corupere și fail-closed

`sanitizeReflection` respinge orice intrare fără `id` valid sau cu `observedState` în afara enumului cunoscut; `transferState` invalid revine implicit la `transfer_unconfirmed`; câmpurile text au fallback la `undefined`, nu la text fabricat. O reflecție coruptă individual este eliminată din listă (fail-closed pe element), nu otrăvește restul `CoachState`.

## Fără precizie falsă, fără PII despre copii

Nu există procente, scoruri sau indici de progres. Stările sunt calitative și etichetate uman (`OBSERVED_STATE_LABELS`, `TRANSFER_STATE_LABELS`), niciodată expuse ca șiruri brute de enum. Nu există câmp pentru nume, dată de naștere, sănătate sau identitate a copilului; textul liber (`coachNote`) poartă un avertisment vizibil, dar produsul nu pretinde — și nu implementează — o interdicție tehnică a introducerii manuale de PII în text liber.

## Compatibilitate viitoare

`SessionReflection` are ID-uri stabile și nu amestecă stare de UI cu domeniul. Portul de persistență (`CoachStatePort`) rămâne singurul punct de contact cu `localStorage`; o migrare ulterioară la un adapter cloud înlocuiește portul, nu paginile sau domeniul. Nu este implementat scor de competență a antrenorului și nu este implementat context de organizație/club — arhitectura lasă loc pentru ambele fără a cere o redesenare distructivă, dar niciuna nu este construită în acest task.
