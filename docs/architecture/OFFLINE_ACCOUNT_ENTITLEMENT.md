# Offline Field Experience, PWA Foundation & Platform Boundaries — TASK-2805

## Ce înseamnă „offline” aici

Nu „tot site-ul funcționează fără internet”. Un singur lucru concret: **o ședință pregătită explicit de antrenor, din Spațiul meu, rămâne complet utilizabilă pe teren fără conexiune** — Field Mode, cronometru, Field Card-uri, Harta terenului, vizualul tactic relevant și reflecția de după ședință. Restul produsului (evidență, căutare, principii, volume) rămâne o experiență online, cu o pagină de fallback onestă, nu o pagină albă sau o eroare de browser.

Formularea corectă de produs, folosită consecvent în UI:

> „Ședințele pregătite pentru teren rămân disponibile fără conexiune.”

Niciodată:

> „Funcționează complet offline.”

## De ce PWA

Site-ul e deja `output: 'static'` (Astro, fără adapter server), servit de Vercel ca fișiere statice — exact terenul potrivit pentru un service worker clasic, fără schimbări de arhitectură. Nu s-a introdus un shell de aplicație paralel: paginile existente (`/spatiul-meu`, `/gold-standard/sedinte/[id]/mod-teren`, etc.) sunt exact ce se pune în cache, nimic randat separat pentru „modul offline”.

## Decizie: cache simplu, fără bibliotecă

Nevoia reală — cache-uiește un set mic, explicit de rute — nu justifică Workbox sau alt runtime greu (interzis explicit de specificație pentru cazuri simple). `public/sw.js` e JavaScript simplu, ~130 linii, fără build step, fără dependențe.

## Granița offline

**Trebuie să funcționeze offline** (după pregătire explicită):
Spațiul meu · ședința personală salvată · Field Mode al ședinței canonice legate · cronometru · cue/observă · Harta terenului (randată determinist din numerele Group Configurator, nu o captură statică) · Field Card-urile exercițiilor incluse · vizualul tactic static relevant · bucla tactică legată, unde există · reflecția post-ședință, salvare și reîncărcare.

**Poate funcționa offline** (dacă a fost vizitat anterior, fără garanție):
orice altă pagină vizitată deja cât timp browserul avea conexiune — service worker-ul cache-uiește oportunist navigările reușite în `PACK_CACHE`.

**Cere conexiune**:
prima pregătire a unei ședințe pentru teren · pagini niciodată vizitate · căutarea completă (indexul nu e cache-uit deliberat pentru acest task) · orice conținut media viitor greu (filmare reală, explicații video înregistrate) · orice pagină de evidență/cercetare nevizitată.

## Modelul de domeniu: pachet offline

Separare strictă, cerută explicit:

- **Manifestul pachetului** (`OfflinePackManifest` — ce rute, ce referințe canonice, ce versiune de conținut, status) e **stare a antrenorului**, trăiește în `CoachState` prin `coach-state.ts` (extensie aditivă v1, exact tiparul `reflections`/`sessions` din TASK-2802/2803 — niciun date pierdut, nicio versiune nouă de schemă).
- **Octeții efectivi** (HTML/CSS/JS pentru acele rute) trăiesc exclusiv în Cache Storage, gestionați de `public/sw.js`.

Reflecțiile și ședințele personale nu ajung niciodată în Cache Storage; pachetul offline nu conține niciodată proză pedagogică copiată — doar referințe (`canonicalRefs: {kind, id}[]`) și rute.

```
WorkspaceSession
  → computeResourceGraph() [app/src/lib/offline-pack.ts, pur, fara import content-bridge]
    → rute exercitii (din lookup construit server-side in spatiul-meu/index.astro)
    → Field Card-uri + Configurator (rute comune, incluse doar daca exista macar un exercitiu)
    → daca sesiunea contine o referinta canonica de sedinta: pagina sedintei + Mod Teren
    → media_id-uri relevante (din registrul TASK-2804, doar pentru trasabilitate — SW cacheuieste rute, nu asset-uri media individuale in aceasta versiune)
  → prepareOfflinePack() trimite rutele catre Service Worker prin postMessage/MessageChannel
  → Service Worker le aduce explicit (fetch cu cache:'reload', ca sa nu foloseasca un raspuns deja stricat) si le pune in PACK_CACHE
  → raspunde cu cachedRoutes/failedRoutes
  → saveOfflinePack() scrie manifestul in CoachState, status READY doar daca toate rutele au reusit
```

`offline-pack.ts` este deliberat lipsit de orice import din `content-bridge`/`problem-library`, ca să rămână ieftin de inclus în orice script client — tabela de rezolvare (exercițiu/sesiune → rută + media) se construiește o singură dată, server-side, în `spatiul-meu/index.astro`, exact tiparul deja folosit de `sedinta.astro` pentru lista de exerciții.

**Corectat prin testare browser reală**: constructorul de ședință (`sedinta.astro`) inițial permitea adăugarea doar de exerciții individuale — ramura `kind:'session'` din `computeResourceGraph()` exista în cod, dar nu era niciodată atinsă de nicio interacțiune reală, ceea ce ar fi făcut Mod Teren offline de neatins prin fluxul de produs. Adăugat un al doilea selector „Adaugă ședință canonică" (alături de „Adaugă exercițiu"), care leagă o ședință Gold Standard completă (cu Mod Teren-ul ei) ca reper în Workspace. Corectat în același timp un bug real descoperit prin acest test: input-ul „Minute" avea `max="45"` (dimensionat doar pentru exerciții individuale), care bloca tăcut trimiterea formularului (validare HTML5 nativă) de îndată ce o ședință canonică de 75 minute era adăugată — fără nicio eroare vizibilă. Ridicat la `max="90"`.

## Precache-ul activelor cu hash (descoperit prin testare browser reală)

Cache-uirea unei rute prin `MANUALFC_CACHE_URLS` aduce doar documentul HTML. Browserul cere apoi, separat, fiecare `.css`/`.js` cu hash referit din acel HTML — dacă acea pagină nu fusese niciodată vizitată online înainte (exact cazul unei ședințe canonice adăugate în Workspace, dar niciodată deschise direct), acele cereri nu erau niciodată precache-uite și eșuau offline cu 504. Corectat cu `scripts/generate_astro_manifest.mjs`, rulat după `astro build`, care scrie `dist/web/astro-assets-manifest.json` cu toate fișierele din `_astro/` (13 fișiere, 116 KB la acest build) — `sw.js` îl citește la `install` și precache-uiește tot setul, indiferent ce pagini au fost efectiv vizitate.

Un al doilea defect, mai subtil, a fost găsit tot prin testare browser reală (nu prin citirea codului): `caches.match(request)` rata intermitent exact aceleași fișiere deja confirmate ca precache-uite corect — reproductibil, dar nu pe toate fișierele deodată. Cauza: răspunsurile serverului poartă `Vary: Origin`, iar cererile de `<script type="module">` folosesc întotdeauna modul CORS (cerință de spec), care poate atașa un header `Origin` ușor diferit față de cel folosit de fetch-ul propriu al Service Worker-ului la `install`. Cache API compară valorile header-elor din `Vary` la potrivire, deci un `Origin` diferit produce un fals negativ pe o intrare care există cu adevărat. Corectat cu `{ ignoreVary: true }` pe toate apelurile `caches.match()` din `sw.js` — sigur aici pentru că numele fișierelor sunt hash-uite de conținut, deci URL-ul identic garantează deja octeți identici, indiferent de `Origin`.

## Eșec fail-closed

Dacă serviciul worker nu e disponibil, nu controlează pagina încă, sau orice rută nu poate fi adusă: pachetul se salvează cu `status: 'NOT_READY'`, mesajul afișat e explicit („Nu am putut pregăti toate resursele pentru teren. Verifică conexiunea și încearcă din nou.”), nu se pretinde niciodată „Disponibil pe teren” fără ca toate rutele să fi reușit efectiv. Nicio adresă tehnică nu e expusă în mesajul vizibil.

## Versionare cache și siguranța actualizării

`SW_VERSION` în `sw.js` produce nume de cache (`manualfc-shell-v1`, `manualfc-pack-v1`). La `activate`, orice cache `manualfc-*` cu alt nume e șters — curățare fără să atingă `localStorage` (starea antrenorului rămâne intactă la orice actualizare de cache).

Politică deliberat conservatoare: **niciun `self.skipWaiting()` la instalare**. Un service worker nou rămâne „în așteptare” până când antrenorul închide și redeschide natural aplicația — nu forțează niciodată un reload în mijlocul unui Field Mode activ. Compromisul onest: dacă o filă rămâne deschisă la nesfârșit, actualizarea nu se activează automat; e alegerea corectă pentru siguranța ședinței active, documentată aici explicit, nu ascunsă.

`content_version` (din `data/platform/content-version.json`, `"2026-08-17.1"` la acest task) e o valoare simplă, actualizată manual când conținutul canonic Gold Standard/registrul media/structura segmentelor Field Mode se schimbă material. Un pachet salvat compară propriul `contentVersion` cu valoarea curentă (`resolveOfflinePackStatus`); la neconcordanță devine `UPDATE_AVAILABLE`, nu rămâne tăcut `READY`. Nu s-a construit un motor de diff — exact cum cere specificația.

## Instalabilitate

`public/manifest.webmanifest`: `name`/`short_name`, `start_url: /spatiul-meu/` (baza reală de lucru a antrenorului, nu pagina de start generică), `display: standalone`, `background_color`/`theme_color` din tokenii de brand existenți (`#F7F7F2`/`#0D1B2A`, nu culori inventate), icoane 192/512. Instalarea nu e niciodată obligatorie — site-ul rămâne complet funcțional în browser, fără prompturi agresive de „Instalează!”.

**Onestitate despre icoane**: `public/icons/icon-192.png` și `icon-512.png` sunt generate prin upscale (Lanczos) al faviconului existent de 128×128, deja aprobat ca activ de brand — nu s-a fabricat o nouă lucrare grafică. Rezultatul la 512px e vizibil mai puțin clar decât un icon proiectat nativ la acea rezoluție; acceptabil pentru o fundație, semnalat explicit ca limită, nu ascuns.

## Buget de stocare — cifre reale din build, nu estimate

| Resursă | Dimensiune reală |
|---|---|
| Shell partajat (`_astro`, JS/CSS cu hash) | 116 KB |
| `/spatiul-meu` + `/sedinta` + `/reflectie` (shell obligatoriu) | 52 KB |
| `/offline` (pagina de rezervă) | 8 KB |
| O pagină de exercițiu (ex. EX-0001/EX-0002/EX-0003) | ~28–32 KB |
| Pagina unei ședințe canonice (include Harta terenului, 12 variante) | 168 KB |
| Mod Teren pentru o ședință canonică | 28 KB |
| Fișe de teren (toate cele 5) | 40 KB |
| Configurator de grup (toate exercițiile) | 76 KB |
| Iconițe PWA (192+512) | ~212 KB |

**Pachet reprezentativ** pentru o ședință Workspace care include ședința canonică SES-0001 (via „+ Ședință”, 12 jucători / 1 antrenor): shell (52 KB) + pagina SES-0001 (168 KB) + Mod Teren (28 KB) + Fișe de teren (40 KB) + Configurator (76 KB) + shell `_astro` (116 KB, cache-uit o singură dată, partajat între toate paginile) ≈ **480 KB** la prima pregătire; pregătirile ulterioare pentru alte ședințe reutilizează shell-ul deja cache-uit. Nu s-a promis o cotă fixă de stocare pe toate dispozitivele — bugetul variază după browser.

## Contract de sincronizare viitoare (nu implementat acum)

Fiecare `SessionReflection`/`WorkspaceSession`/`OfflinePackManifest` are deja `id` stabil și `createdAt`/`updatedAt`. O sincronizare cloud viitoare trebuie să compare `updatedAt` înainte de a suprascrie — o reflecție locală mai nouă nu poate fi înlocuită tăcut de o versiune la distanță mai veche. Acesta e un contract documentat pentru mai târziu, nu cod scris acum; TASK-2805 nu implementează nicio sincronizare cloud.

## Granițe de platformă (entitlement) — documentat, neconstruit

Arhitectura curentă (`CoachStatePort` înlocuibil, fără identitate necesară) rămâne compatibilă cu, dar nu implementează:

- **Conturi și persistență cloud** — portul de stare rămâne singurul punct de contact cu stocarea; înlocuirea lui cu un adapter cloud nu ar cere rescrierea paginilor.
- **Coach / Coach Pro / Academy / Club** — nicio granularitate de plan nu există în cod; orice granițe comerciale viitoare (limite de ședințe salvate, pachete offline, dispozitive) rămân o decizie de produs separată, neluată aici.
- **Sincronizare cross-device** — imposibilă fără cont; contractul de mai sus (ID-uri stabile, `updatedAt`) pregătește terenul fără să implementeze mecanismul.

Niciun cod de entitlement nu a fost scris în acest task. Documentarea graniței nu e o promisiune de livrare, e o hartă pentru decizia viitoare.

## Ce nu s-a construit intenționat

Fără bibliotecă de service worker (Workbox etc.). Fără cache-uire oarbă a întregului site. Fără cache-uire automată a media viitoare grea (video de antrenor înregistrat, filmare reală de teren — niciuna nu există). Fără căutare offline completă (indexul nu justifică lărgirea cache-ului doar pentru acest task). Fără sincronizare cloud. Fără implementare de entitlement/planuri comerciale.
