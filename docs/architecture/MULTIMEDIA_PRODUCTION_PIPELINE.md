# Multimedia Production Pipeline — TASK-2804

## Relația cu fundația TASK-2711

`docs/architecture/MULTIMEDIA_FOUNDATION.md` a stabilit cele 5 niveluri și un singur prototip real (bucla EX-0001). Acest document nu îl înlocuiește — îl extinde cu: un registru media canonic, generalizarea buclei tactice la alte trei ținte, primul prototip real de Nivel 3 (animație de exercițiu completă) și modelul de producție pentru Nivelul 4 (explicație de antrenor). Nivelurile 4 (înregistrare reală) și 5 (filmare reală de teren/meci) rămân nefabricate.

## De ce fiecare activ nou există

Fiecare activ produs în acest task răspunde la o nevoie spațială sau temporală pe care textul singur nu o poate transmite complet:

- **EX-0002** — comportamentul central e „se repoziționează *continuu*, nu o singură dată”; un text sau o diagramă statică nu poate arăta repetiția.
- **EX-0003** / **PRB-0003** — comportamentul central e o *secvență temporală* (privește → primește orientat → continuă); relația de timp dintre privire și sosirea mingii nu are echivalent static complet.
- **EX-0001 (animație completă)** — regula „rolurile se schimbă după fiecare pasă reușită” e explicit un ciclu, nu o poziție; bucla scurtă deja existentă arată doar jumătate din idee (deschiderea unghiului), nu ciclul complet.
- **EX-0004, EX-0005** — verificate explicit și lăsate **fără** animație nouă: ambele au deja o notă semantică care respinge o formă unică obligatorie, iar o animație ar fabrica exact precizia falsă pe care nota o respinge. Diagrama statică cu săgeți rămâne nivelul corect.

## Registrul media canonic

`data/media/media-registry.json` (validat de `schemas/media-registry.schema.json`, încărcat fail-closed de `app/src/lib/media-registry.ts`) este singura sursă de adevăr pentru ce media există, pentru ce subiect canonic, și cu ce garanții. Fiecare intrare declară explicit:

- `canonical_refs` — trebuie să rezolve la un `EX-*`/`PRB-*` real; `validateMediaRegistry()` aruncă `FAIL_CLOSED` la build dacă nu rezolvă (secțiunea „Verificare la build”);
- `evidence_boundary` — `SYNTHETIC_INSTRUCTIONAL_VISUALIZATION` (animație CSS/SVG instrucțională) sau `CANONICAL_TEXT_DERIVED` (script derivat din date canonice); nicio intrare nu are `REAL_FOOTAGE`, pentru că nu există filmare reală în acest repository;
- `status` — `AVAILABLE`/`SCRIPT_READY`/`NOT_STARTED`/`FIELD_INPUT_REQUIRED`/`NOT_APPLICABLE`, niciodată `AVAILABLE` pentru ceva ce nu există în produs;
- `reduced_motion_fallback` — obligatoriu pentru orice `TACTICAL_LOOP`/`EXERCISE_ANIMATION` cu `status: AVAILABLE` (impus de validator);
- `reason_not_animated` — explicit pentru EX-0004/EX-0005, ca decizia de a NU anima să fie documentată, nu tăcută.

Componentele consumă registrul prin `getMediaForExercise`/`getMediaForProblem`/`getCoachExplainer` — niciun path de asset hardcodat direct în pagini.

## Verificare la build

`validateMediaRegistry()` rulează la import (același tipar ca `validateProblemGraph()` din `problem-library.ts`): verifică `media_id` unice, `canonical_refs` rezolvate la exerciții/probleme reale, fallback de reduced-motion prezent pentru media animată `AVAILABLE`, și `script` prezent pentru `COACH_EXPLAINER` cu `status: SCRIPT_READY`. Un build cu o referință ruptă eșuează, nu randează o interfață stricată tăcut.

## Nivelul 2 — bucla tactică generalizată

`ConceptLoop.astro` generalizează tiparul `TacticalLoop.astro` (EX-0001, TASK-2711) la trei ținte noi: `ex-0002`, `ex-0003`, `prb-0003`. Coordonatele SVG reutilizează exact cele deja validate în `TacticalDiagram.astro`/`ProblemVisual.astro` pentru fiecare țintă — nicio coregrafie nouă inventată. Fiecare buclă: fără sunet, `prefers-reduced-motion` complet respectat (cadrul final așezat rămâne vizibil), buton pauză/redare cu `aria-pressed`, `<title>`/`<desc>` proprii.

## Nivelul 3 — animație de exercițiu

`ExerciseSequenceAnimation.astro` (EX-0001) e primul prototip real de Nivel 3: START → sprijinul deschide unghiul → pasă reușită → schimbul de roluri (regula canonică exactă) → reluare. 24 de secunde, etichetat explicit „reprezentare comprimată a regulii, nu durata reală”. Etapele sunt sincronizate prin CSS pur (aceeași variabilă `--dur` ca animația SVG, fără temporizare JS care s-ar putea desincroniza). Include pauză/redare **și** reluare (cerință de Nivel 3), plus un `<details>` cu transcrierea text a etapelor, disponibil integral indiferent de preferința de mișcare — legenda vizuală animată e `aria-hidden`, pentru că transcrierea text este sursa completă și stabilă pentru tehnologia asistivă.

## Nivelul 4 — model de producție pentru explicația de antrenor

`CoachExplainerScript.astro` randează un script structurat pe 6 părți (Ce vezi / De ce contează / Ce îi spui copilului / Ce urmărești / Greșeala frecventă a antrenorului / Ce faci mai departe) pentru cele 3 probleme flagship, derivat direct din câmpurile canonice deja existente (`observable_behavior`, `child_cues`, `possible_explanations`, `transfer_checks`) — nu conținut nou inventat. `status: SCRIPT_READY`, nu `AVAILABLE` sau `DONE`: nu există nicio înregistrare reală și nu se pretinde una. Nu se randează niciun player video gol — doar scriptul text, accesibil, gata pentru citire sau pentru o viitoare înregistrare.

## Pipeline viitor — filmare reală de teren (Nivel 4 înregistrat / Nivel 5)

Documentat, nefăcut:

```
OBIECT CANONIC (exercițiu/problemă/ședință)
  → CERINȚĂ DE CADRU (ce anume trebuie să se vadă, din step_by_step/rules)
  → CONSIMȚĂMÂNT / SAFEGUARDING (acord scris părinte/tutore, politică club, minori — înaintea oricărei filmări)
  → FILMARE
  → MONTAJ
  → REVIZIE PEDAGOGICĂ (verificare fidelitate cu datele canonice, ca la orice alt conținut)
  → ANONIMIZARE unde e necesară (fețe/nume, conform politicii de safeguarding deja existente)
  → SUBTITRARE
  → TRANSCRIERE
  → POSTER (cadru static de start, pentru fallback fără JS/motion)
  → ÎNREGISTRARE ÎN REGISTRUL MEDIA (media_id nou, evidence_boundary: REAL_FOOTAGE, status: AVAILABLE)
  → LIVRARE WEB (element <video> real, înlocuind CoachExplainerScript fără a schimba forma datelor)
  → LEGĂTURĂ DE VERSIUNE (media.version + referință la versiunea conținutului canonic descris)
```

Niciun pas de mai sus nu a fost executat. Nu s-a filmat nimic, nu s-a fabricat niciun consimțământ, nu există nicio filmare „reprezentativă” prezentată drept reală.

## Pipeline viitor — exemplu de transfer în meci

Un exemplu de transfer trebuie să arate comportamentul țintă în joc mai liber, nu o repetare a coregrafiei exercițiului — altfel ar pretinde fals transferul pornind doar de la o animație tactică (interzis explicit). Cerințe suplimentare față de pipeline-ul de mai sus: contextul trebuie să fie vizibil mai deschis decât exercițiul (mai mulți jucători, mai puține constrângeri), iar comportamentul trebuie să apară fără comandă vizibilă a antrenorului în cadru. Fără date reale de teren, acest nivel rămâne `FIELD_INPUT_REQUIRED`.

## Versionare și compatibilitate cu conținutul canonic

Fiecare intrare din registru are `version`. Dacă un exercițiu sau o problemă canonică se schimbă material mai târziu (coordonate, reguli, comportament țintă), `canonical_refs` tot rezolvă (ID-ul nu s-a schimbat), dar `purpose`/geometria SVG ar putea deveni stale — acesta e un risc cunoscut, documentat, nu ascuns. O revizuire viitoare a conținutului canonic trebuie să verifice manual dacă media asociată media rămâne fidelă; `version` pe fiecare intrare oferă un punct de plecare pentru acea verificare, fără a construi un CMS complet de media.

## Ce nu s-a construit intenționat

Nicio bibliotecă de animație grea (Three.js, motor canvas complex), niciun player video pentru conținut inexistent, niciun filtru nou de căutare „are video” (inflație de filtre nejustificată la acest volum de conținut), nicio galerie media în Mod Teren (rămâne diagrama statică, deja suficientă pentru „ce trebuie să văd acum”), niciun scor de competență a antrenorului legat de media.
