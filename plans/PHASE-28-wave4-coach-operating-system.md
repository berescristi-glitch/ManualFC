# PHASE-28 / Wave-4 — Coach Operating System

## 1. Titlu și scop

Construirea primului flux persistent al antrenorului: de la problemă și intervenție la ședință personală, utilizare pe teren, reflecție reală și continuare la următoarea vizită, cu fundație offline și multimedia extinsă.

## 2. Context

Runtime-ul Wave-3 acceptat este `ae04ed53929ce5a4a06a374a479451c40737e10c`; commitul `0b07f59` documentează acceptarea. Gate A promovează exact deploymentul acceptat, fără rebuild. Conținutul canonic rămâne în `data/`; Workspace păstrează numai referințe și configurări ale antrenorului.

## 3. Rezultat verificabil

Un antrenor anonim poate salva conținut, construi și configura o ședință, pregăti un pachet de teren, rula Field Mode, completa reflecția și regăsi următorul pas după reload. Starea este local-first printr-un adapter înlocuibil; nu se colectează PII despre copii.

## 4. Domeniu și non-obiective

Intră: release Wave-3, ledger permanent, Workspace, persistence, onboarding minim, reflecție, multimedia justificată, PWA/offline, entitlement boundary, audit Preview. Nu intră: billing, conturi cloud reale, Club UI, date nominale despre copii, filmări reale fabricate, Wave-5.

## 5. Task mapping

- `TASK-2801`: release Production Wave-3, ledger final și arhitectura Wave-4.
- `TASK-2802`: persistence adapter, onboarding, salvate/favorite/recente/continuă, Session Workspace și Builder.
- `TASK-2803`: finalizare Field Mode, reflecție și transfer loop.
- `TASK-2804`: multimedia Wave-4 și pipeline coach explainer.
- `TASK-2805`: PWA, offline field pack, connectivity și entitlement/account boundaries.
- `TASK-2806`: validare integrală, Preview curat, audit live și baseline.

ID-urile `TASK-2713`–`TASK-2716` rămân rezervate sensurilor din auditul strategic și nu sunt repurposate.

## 6. Cercetare necesară

Nu sunt introduse afirmații pedagogice noi. Pentru PWA, storage și accesibilitate se folosesc standardele platformei și verificări browser; orice limită de suport este documentată.

## 7. Model pedagogic

Reflecția păstrează distincția observație–interpretare și nu inventează măsurători. Stările calitative separă comportamentul în sarcină de transferul văzut în joc. Conținutul canonic nu este rescris în starea utilizatorului.

## 8. Design vizual și interactiv

Desktopul prioritizează planificarea; 390px prioritizează acțiunea. Field Mode rămâne neaglomerat. Reordonarea are butoane accesibile, nu depinde de drag. Animațiile au control, reduced-motion și fallback static.

## 9. Pași de implementare

1. Închide Gate A și scrie ledgerul/arhitectura.
2. Construiește modelul de domeniu și adapterul local.
3. Construiește Workspace și integrarea Add-to-session.
4. Închide bucla Field Mode → reflecție → continuare.
5. Extinde media din specificații canonice.
6. Adaugă manifest, service worker și pachet offline explicit.
7. Rulează scenariile A–E, validările și auditul responsive local.
8. Creează candidat curat, Preview și audit live independent; repară doar Critical/Major.

## 10. Validare și acceptare

Comenzile canonice complete; teste domeniu pentru referințe/totale/stare/reflecție/offline/entitlement; browser 1440/1280/768/390; reload și offline real; axe; 0 Critical/Major.

## 11. Progres

- [x] 2026-08-16: recovery și documente obligatorii.
- [x] 2026-08-16: deployment acceptat promovat fără rebuild.
- [x] 2026-08-16: Gate A FAIL — EX-0001 are `main main = 1`; STOP obligatoriu.
- [x] 2026-08-16: repair loop autorizat — root cause repository-wide reparat, regression guard și validare locală PASS.
- [x] 2026-08-16: mapping Phase-28 persistat.
- [x] TASK-2801 DONE după repair Preview + Production Gate A PASS.
- [x] 2026-08-16: TASK-2802 DONE — acceptanță browser reală PASS la 1440/1280/768/390; defect Major de scoping CSS pe controale generate dinamic găsit și reparat.
- [x] 2026-08-17: TASK-2803 DONE — reflecție post-ședință și transfer loop; extensie compatibilă v1 a `CoachState`, fără pierdere de date TASK-2802; acceptanță browser reală PASS.
- [x] 2026-08-17: TASK-2804 DONE — bucle tactice noi (EX-0002/EX-0003/PRB-0003), primă animație de exercițiu completă (EX-0001, Nivel 3), scripturi de coach explainer pentru cele 3 probleme flagship; registru media fail-closed; acceptanță browser reală PASS.
- [x] 2026-08-17: TASK-2805 DONE — PWA instalabilă, pachet offline pe ședință Workspace, Mod Teren + reflecție complet funcționale offline (cronometru, navigare segmente, salvare), acceptanță browser reală PASS pentru toate cele 6 scenarii plus cold start plus tranziție online→offline în mijlocul unei ședințe active; 3 defecte reale găsite și reparate prin testare directă (ramură moartă în fluxul de produs, precache incomplet al activelor cu hash, `Vary:Origin` producând falsuri negative în `caches.match()`).
- [x] 2026-08-17: TASK-2806 DONE — **`PHASE-28 / WAVE-4 = PASS`**. Audit local complet de integrare (fluxul semnătură complet, 12/1 și 16/2, 60/75 min, ambele scenarii de reflecție, corupere mixtă de stare pe toate cele 4 felii Wave-4, 0 crash-uri, 505/505 teste) urmat de deployment Preview real (blocajul inițial de acces Vercel rezolvat de utilizator prin autentificare CLI locală) și audit live independent PASS pe infrastructura HTTPS reală — inclusiv un cold start autentic (tab nou, offline, 0 stare JS anterioară) verificat direct pe Preview, nu doar pe localhost. Identitate runtime dovedită prin hash de conținut. 2 defecte reale găsite și reparate în faza locală (pierdere de context Decision Engine→Workspace, regres de țintă de atins din TASK-2805); 0 Critical/Major găsite pe Preview. `MANUALFC_PREMIUM_WAVE4_BASELINE = 560e27c`. Production neschimbat.

## 12. Descoperiri și surprize

- `TASK-2713`–`TASK-2716` apar în auditul strategic, dar nu în generatorul registrului; sensurile lor sunt totuși rezervate și nu trebuie reutilizate.
- Vercel `promote` a creat deploymentul Production `dpl_GwmVnMkeBy7aMnAAQzBNgEFHYRv6` din artifactul acceptat, fără rebuild de HEAD.

## 13. Jurnal de decizii

- 2026-08-16: starea anonimă folosește un port de domeniu și adapter local, astfel încât un provider cloud ulterior să nu rescrie UI-ul.
- 2026-08-16: ședințele personale păstrează IDs canonice plus configurare, niciodată copii ale prozei.
- 2026-08-17: reflecția extinde `CoachState` v1 (`reflections: SessionReflection[]`) în loc de o versiune nouă de schemă; performanța în sarcină și transferul în joc sunt două stări separate, niciodată confundate; recomandarea „ce urmează” este un tabel determinist, nu text generat liber.
- 2026-08-17: EX-0004/EX-0005 rămân deliberat fără animație nouă — o secvență animată ar fabrica o coregrafie fixă pe care nota semantică a fiecărui exercițiu o respinge explicit; decizia e documentată în registrul media (`reason_not_animated`), nu tăcută.
- 2026-08-17: `sw.js` rămâne JS simplu, fără Workbox — nevoia reală (cache-uirea unui set mic, explicit de rute) nu justifică o bibliotecă grea.
- 2026-08-17: nicio actualizare de Service Worker nu forțează `skipWaiting()` — o ședință activă de Mod Teren nu este niciodată întreruptă de un reload forțat; compromisul (actualizarea nu se activează automat dacă fila rămâne deschisă la nesfârșit) e documentat explicit, nu ascuns.
- 2026-08-17: precache-ul complet al activelor `_astro/*` cu hash (`scripts/generate_astro_manifest.mjs`) e mai simplu și mai robust decât urmărirea manuală a dependențelor per pagină — bugetul e mic (116 KB, 13 fișiere) și determinist din build.
- 2026-08-17: TASK-2806 nu declară Wave-4 `PASS` fără auditul live pe Preview, chiar dacă auditul local e complet și curat — condiția explicită de oprire a specificației ("nu declara PASS dacă Preview-ul browser nu a fost testat") e mai importantă decât graba de a închide taskul.
- 2026-08-17: identitatea runtime-ului Preview e dovedită prin hash de conținut al bundle-urilor (`CoachActions.astro...js`), nu presupusă din faptul că s-a publicat "cel mai recent commit" — un deployment poate folosi cache de build vechi, deci verificarea directă contează.
- 2026-08-17: „Protection Bypass for Automation" se activează aditiv pentru testare browser automată, fără a dezactiva protecția SSO globală a Preview-ului — păstrează securitatea implicită în timp ce permite auditul real.

## 14. Rezultat și retrospectivă

Blocaj temporar 2026-08-16 (rezolvat): `agent-browser` nu era instalat în mediul Codex anterior; acceptanța browser a rulat totuși cu succes direct în acest mediu, unde instrumentarea Playwright era deja disponibilă în sesiune, fără nicio instalare nouă. TASK-2802 este `DONE` cu dovezi browser reale la 1440/1280/768/390, inclusiv un defect Major găsit și reparat (scoping CSS Astro nu se aplică elementelor generate dinamic via `innerHTML`).

TASK-2803 închide bucla completă OBSERVĂ→...→DECIDE URMĂTORUL PAS: Field Mode se termină explicit către o reflecție de sub 60 de secunde (nu o pagină de jurnal), care distinge apariția în exercițiu de transferul confirmat în joc liber și oferă o recomandare determinist calculată, niciodată inventată. Testat cu date corupte injectate direct în `localStorage` — recuperare fail-closed completă, 0 erori de consolă.

TASK-2804 transformă multimedia dintr-o fundație cu un singur prototip într-un sistem real de ghidare vizuală: bucla tactică EX-0001 (TASK-2711) rămâne neatinsă, dar se generalizează la EX-0002/EX-0003/PRB-0003, iar EX-0001 primește prima animație completă de Nivel 3 (ciclul de schimb al rolurilor, exact regula canonică). Cele 3 probleme flagship primesc scripturi complete de coach explainer, marcate onest `SCRIPT_READY` — nu `DONE` — pentru că nu există nicio înregistrare reală. Un defect Major a fost găsit prin testare directă: un buton preexistent din TASK-2711 avea doar 32px înălțime; reparat pentru consecvență cu toate controalele noi de pe aceeași pagină.

TASK-2805 face din offline o continuitate reală de teren, nu un badge tehnic: o ședință Workspace legată la o ședință canonică (`SES-0001`) rămâne complet utilizabilă fără conexiune — Mod Teren cu cronometru și navigare pe segmente, Harta terenului randată determinist (nu o captură), reflecția post-ședință salvată fără pierdere. Trei defecte reale au fost găsite exclusiv prin testare browser directă, niciunul vizibil doar din citirea codului: o ramură a modelului de resurse (`kind:'session'`) era moartă în fluxul real de produs, deoarece constructorul de ședință nu oferea nicio cale de a adăuga o ședință canonică întreagă — corectată cu un al doilea selector în `sedinta.astro`; precache-ul unei rute aducea doar documentul HTML, nu și activele `.css`/`.js` cu hash pe care le referea, producând 504 pe pagini niciodată vizitate direct online — corectat cu un manifest de build; și `caches.match()` rata intermitent intrări confirmate ca precache-uite din cauza unui `Vary: Origin` combinat cu modul CORS obligatoriu al fetch-urilor `<script type="module">` — corectat cu `ignoreVary: true`, sigur pentru fișiere hash-uite de conținut. Fără ultima reparație, pagina de reflecție se încărca vizual offline, dar scriptul ei propriu nu se executa niciodată — o rupere reală de funcționalitate mascată drept zgomot de consolă. Acceptanța browser a acoperit toate cele 6 scenarii cerute plus un test de cold start (tab nou, fără stare JS anterioară) și o tranziție online→offline în mijlocul unei ședințe active (cronometrul a continuat neîntrerupt). `SYNC` rămâne explicit `FOUNDATION/NOT_STARTED` — niciun cod de sincronizare cloud nu există.

TASK-2806 închide Wave-4 ca produs integrat, nu ca șase demo-uri de funcții izolate. Auditul de integrare a găsit, prin parcurgerea fluxului semnătură complet (nu prin re-testarea fiecărei funcții separat), două defecte reale invizibile din testele izolate TASK-2802–2805: contextul unei probleme din Decision Engine se pierdea la adăugarea rapidă a unui exercițiu în Workspace (paginile static-prerandate nu expun query string-ul server-side), și butonul nou „Adaugă ședință" din TASK-2805 regresase sub pragul de 44px pentru ținte de atins. Un test de corupere mixtă peste toate cele patru felii de stare Wave-4 simultan (sesiuni/reflecții/pachete offline/salvate) — imposibil de rulat înainte ca `offlinePacks` să existe — a confirmat 0 crash-uri și recuperare fail-closed completă, inclusiv o cascadă corectă de prioritate „Continuă" chiar cu `activeSessionId` nerezolvabil.

Blocajul inițial de deployment Preview (CLI Vercel neinstalat, conectorul MCP autentificat dar fără acces la proiectul `manualfc` — exact tiparul istoric `TASK-2717`) a fost raportat onest, nu ocolit sau ascuns. Utilizatorul l-a rezolvat prin autentificarea CLI Vercel local. Candidatul deja comis a fost publicat neschimbat dintr-un worktree izolat, iar identitatea runtime-ului a fost dovedită prin hash de conținut, nu presupusă. Auditul live independent — inclusiv un cold start autentic pe infrastructura HTTPS reală, cu 0 stare JS anterioară — a confirmat 0 Critical/Major; candidatul local era deja corect. `MANUALFC_PREMIUM_WAVE4_BASELINE = 560e27c`. Production rămâne neschimbat; nicio promovare Wave-4 nu a fost autorizată. Wave-5 așteaptă o nouă decizie explicită a utilizatorului.
