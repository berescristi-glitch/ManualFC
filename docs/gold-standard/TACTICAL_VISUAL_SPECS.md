# Gold Standard — Specificații semantice pentru vizualuri tactice: Sprijinul și unghiul de pasă

**Task:** TASK-2207
**Status:** COMPLETE
**Data:** 2026-08-12

`DESIGN_FREEZE = YES` rămâne activ. Acest document conține exclusiv **specificații semantice** (ce trebuie să comunice fiecare vizual, nu cum arată). Niciun fișier grafic (SVG, animație) nu e produs în acest task — câmpurile `visual_assets` din cele 5 exerciții (`TASK-2204`) rămân marcate `PENDING` până la o aprobare separată de design, în afara acestei bucle.

## Principiu general

Fiecare vizual trebuie să comunice o **relație funcțională** (minge–adversar–coleg–spațiu), nu o poziție geometrică fixă. Niciun vizual nu va desena un unghi exact (ex. 45°) ca fiind „cel corect” — conform `CONCEPT_MODEL.md` secțiunea 2, cercetarea nu susține un unghi universal.

## Specificația per exercițiu

### VIS-EX-0001 — Umbra defensivă
- **Scop:** arată vizual cum un singur adversar poate „umbri” doi coechipieri aflați pe aceeași linie de pasă.
- **Jucători:** 1 purtător de minge, 1 coechipier (poziția „înainte” și poziția „după” deplasare), 1 adversar.
- **Minge:** la piciorul purtătorului, statică pentru cadrul „înainte”.
- **Relația cu adversarul:** conul de umbră defensivă (zona pe care adversarul o poate acoperi) desenat ca zonă, nu ca linie unică.
- **Linia de pasă:** desenată ca linie întreruptă când e acoperită, linie continuă când e deschisă.
- **Punct de decizie:** momentul în care coechipierul recunoaște acoperirea și inițiază deplasarea.
- **Secvența de fază:** stare inițială (acoperit) → informație (adversarul acoperă ambele) → decizie (coechipierul alege direcția) → mișcare → stare nouă (unghi deschis).
- **Legendă:** text scurt „Un adversar, două opțiuni pe aceeași linie → acoperite simultan.”
- **Alternativă textuală:** descrierea de mai sus, fără a necesita percepția culorilor sau formelor.
- **Ce NU trebuie sugerat:** nicio distanță exactă în metri; nicio săgeată care implică un unghi de grade specific.

### VIS-EX-0002 — Repoziționare dinamică
- **Scop:** arată că decizia de sprijin se actualizează continuu, nu o singură dată.
- **Jucători:** aceiași 3 ca la EX-0001, dar în minimum 3 cadre succesive (nu 2).
- **Secvența de fază:** stare 1 (unghi deschis) → adversarul se mută → stare 2 (unghi reacoperit) → coechipierul se repoziționează → stare 3 (unghi nou deschis).
- **Punct de decizie:** repetat, la fiecare schimbare de stare a adversarului.
- **Legendă:** „Unghiul bun de acum poate deveni unghi acoperit — verifică din nou.”
- **Ce NU trebuie sugerat:** o poziție finală „corectă” unică; animația trebuie să arate mișcare repetată, nu un singur salt.

### VIS-EX-0003 — Orientarea la recepție
- **Scop:** arată diferența dintre a primi cu corpul închis (nu poate continua) și a primi orientat (poate continua).
- **Jucători:** purtător, coechipier care primește, adversar, plus indicarea spațiului util (conul colorat din exercițiu, reprezentat ca zonă marcată).
- **Punct de decizie:** momentul scanării, chiar înainte ca mingea să ajungă la coechipier.
- **Secvența de fază:** scanare (privirea către zona utilă) → recepție orientată → continuare posibilă (săgeată spre acțiunea următoare), comparat side-by-side cu recepție neorientată → blocaj.
- **Legendă:** „Ce vezi înainte să primești schimbă ce poți face după.”
- **Ce NU trebuie sugerat:** o poziție exactă a piciorului sau un unghi al corpului ca fiind „tehnica corectă” (`CLM-0103` — nicio tehnică unică validată).

### VIS-EX-0004 — Coordonarea a doi jucători de sprijin
- **Scop:** arată diferența dintre doi coechipieri grupați în aceeași zonă (eroare) și doi coechipieri diferențiați spațial (corect).
- **Jucători:** purtător, doi coechipieri de sprijin, doi adversari.
- **Comparație:** două cadre alăturate — „grupați” (ambele opțiuni acoperibile de un singur adversar) vs. „diferențiați” (necesită doi adversari pentru acoperire).
- **Legendă:** „Dacă amândoi stați în aceeași zonă, un singur adversar vă acoperă pe amândoi.”
- **Ce NU trebuie sugerat:** o distanță minimă exactă între cei doi coechipieri.

### VIS-EX-0005 — Transfer în joc mic
- **Scop:** arată aceleași principii (unghi, orientare, coordonare) apărând natural într-un context de joc 4v4, fără marcaje artificiale.
- **Jucători:** 8 (4v4), fără conuri colorate sau zone marcate — vizual „curat”, reprezentativ.
- **Secvența de fază:** un moment de joc real în care principiul apare vizibil, adnotat retroactiv (nu ghidat în timp real).
- **Legendă:** „Același principiu, fără indicii artificiale.”
- **Ce NU trebuie sugerat:** că acest moment specific de joc e singura formă corectă de aplicare — instrucțiunea #49 („variabilitate a jucătorului”) cere explicit ca vizualul să nu implice o soluție unică.

## Specificația animației (dacă produsă, în afara acestei bucle)

Pentru orice vizual animat viitor, secvența de fază standard:
`STARE` → `SCHIMBARE DE INFORMAȚIE` (adversarul/mingea se mută) → `DECIZIA JUCĂTORULUI` (moment de pauză vizuală scurtă) → `MIȘCARE` → `PASĂ/ACȚIUNE` → `STARE NOUĂ`.

Animația se justifică doar pentru VIS-EX-0002 (natura dinamică, greu de arătat static) și VIS-EX-0003 (secvența scanare→recepție→continuare). Pentru VIS-EX-0001, VIS-EX-0004 și VIS-EX-0005, o diagramă statică sau o comparație de cadre alăturate comunică la fel de eficient — nu se animează doar pentru că platforma permite.

## Confirmare design freeze

Niciun fișier din lista de design freeze (`AppFooter.astro`, `AppHeader.astro`, `ChildMessage.astro`, `CoachMessage.astro`, `EvidenceBadge.astro`, `QuickModePattern.astro`, `BaseLayout.astro`, `design-system.astro`, `incepe-aici.astro`, `index.astro`, `principii/[slug].astro`, `global.css`, `print.css`, `tokens.css`, `astro.config.mjs`, `config/visual-tokens.json`, `_incoming/`, `HeroBallFlight.astro`, `HomepageHero.astro`, `ManualFCLogo.astro`, `TacticalMotif.astro`, `plans/MANUALFC-visual-identity-v1.md`, `public/`) nu a fost atins de acest task.

`TACTICAL_VISUAL_SPECS = COMPLETE`.
