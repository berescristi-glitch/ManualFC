# ManualFC Wave-1 — browser acceptance

## Stare curentă

`PASS — MANUALFC_PREMIUM_WAVE1_BASELINE = 15694b0`

## Candidat autoritativ

- commit implementare: `c18263c`;
- deployment: `dpl_E8523A8CMnkriJ2XRCMwwDBH4XGW`;
- Preview: `https://manualfc-cm9aa2y25-berescristi-8889s-projects.vercel.app`;
- Vercel: `target=preview`, `status=READY`, proiect `manualfc`;
- Production canonic `https://manualfc.vercel.app/` nu a fost promovat sau realiasat.

## Dovezi finalizate

- gate local complet: 428/428 teste, validatoare 0 erori, registry reproductibil, Astro check 0/0/0, build 69 pagini;
- buildul Vercel al snapshotului curat a produs 69 pagini;
- smoke autentificat prin Vercel: root 200, principiu 200, EX-0001 200, `/design-system` 404;
- browser local pe același commit: IA și patru eșantioane V2 verificate la 1440/1280/768/390.

## Gate rămas

Preview-ul este protejat prin Vercel Authentication. Browserul automat separat ajunge corect la pagina `Login – Vercel`; sesiunea Chrome conectabilă nu este disponibilă. Nu s-a extras niciun secret și nu s-a dezactivat protecția. Pentru verdictul final trebuie deschis Preview-ul într-o sesiune Vercel autentificată accesibilă, apoi reluate cele patru viewporturi și fluxurile critice.

Baseline-ul nu este încă înghețat și verdictul nu este `PASS`.

## Încercare 2026-08-14 — Vercel Shareable Link, tot blocat

Utilizatorul a regenerat un Shareable Link nou (`_vercel_share=xkLMYHq0MTuk0yRjNoEQoOvKRLE2XIf8`) pe același deployment `dpl_E8523A8CMnkriJ2XRCMwwDBH4XGW` / Preview `https://manualfc-cm9aa2y25-berescristi-8889s-projects.vercel.app`, pe premisa că Shareable Links permit acces extern fără cont Vercel.

Rezultat browser-first, verificat direct: navigarea la URL-ul cu `_vercel_share` a redirecționat automat browserul Playwright la `vercel.com/login?next=%2Fsso-api%3Furl%3D...%26nonce%3D...` — o pagină completă de autentificare Vercel (Email, Google, GitHub, ChatGPT, SAML SSO, Passkey), fără nicio opțiune de acces anonim/"continue as guest". Sesiunea de browser automat nu are cont Vercel autentificat, deci accesul rămâne blocat identic cu încercarea anterioară.

Verificare API suplimentară: conexiunea Vercel MCP disponibilă în această sesiune listează un singur proiect vizibil (`insuliniq`) pentru echipa `berescristi-8889s-projects`; proiectul `manualfc` nu apare, deci nu există acces API din această sesiune pentru a inspecta sau ajusta setările de Deployment Protection ale proiectului `manualfc` (nici pentru a confirma tipul exact de protecție, nici pentru a genera un `Protection Bypass for Automation` secret).

**Constatare:** Shareable Link, așa cum e configurat/generat, nu produce acces anonim pentru un browser automat fără sesiune Vercel — cere autentificare completă. Nu s-a introdus nicio credențială și nu s-a încercat ocolirea autentificării. Auditul browser-first la 1440/1280/768/390 rămâne neexecutat pentru această rundă.

Stare neschimbată: `PREVIEW_BROWSER_AUTH_REQUIRED`. Opțiuni reale pentru deblocare (necesită acțiune din contul Vercel al utilizatorului, nu poate fi făcută autonom):
1. comută temporar protecția acestui Preview pe `Password Protection` (nu Vercel Authentication) și transmite parola — un vizitator anonim poate trece de un prompt de parolă fără cont Vercel;
2. generează din Project Settings → Deployment Protection un secret `Protection Bypass for Automation` și transmite-l, ca să poată fi atașat ca query param/header la cererile automate;
3. deschide chiar tu Preview-ul într-o sesiune de browser autentificată și confirmă acceptanța manual, sau oferă acces la o sesiune de browser deja autentificată în contul Vercel corect.

Baseline-ul rămâne neînghețat; verdictul rămâne diferit de `PASS`.

## Încercare 2026-08-14 — Protection Bypass for Automation, acces reușit, audit browser-first executat

Utilizatorul a generat un secret `Protection Bypass for Automation` din setările proiectului Vercel. Atașat ca query param (`?x-vercel-protection-bypass=...&x-vercel-set-bypass-cookie=true`) pe Preview-ul `dpl_E8523A8CMnkriJ2XRCMwwDBH4XGW` (`https://manualfc-cm9aa2y25-berescristi-8889s-projects.vercel.app`), acesta a debloca imediat accesul: browserul automat a primit conținutul real (titlu „Metodologie U11 | ManualFC U11”), nu pagina de login. Cookie-ul de bypass a persistat pentru restul sesiunii de navigare.

### Audit browser-first executat la 1440/1280/768/390

Rute verificate la toate cele 4 lățimi (console 0 erori/avertismente pe fiecare): `/`, `/incepe-aici`, `/volum`, `/principii`, `/principii/tranzitia-la-pierderea-mingii`, `/gold-standard`, `/gold-standard/rapid`, `/gold-standard/exercitii/EX-0001`, `/gold-standard/exercitii/EX-0004`, `/gold-standard/sedinte/SES-0001`, `/gold-standard/evaluare/ASM-0001`. Verificate și cele 4 rute fixture/interne (`/design-system`, `/principii/orientare-corporala-scanare`, `/probleme/lipsa-unghi-de-pasa`, `/exercitii/2v1-unghi-de-suport`) — toate 404, confirmă `TASK-2702`. Cele 5 rute IA V2 din navigarea principală funcționează identic la toate lățimile. Ierarhia Presentation Layer V2 (`Aplică acum → Înțelege mecanismul → Verifică dovezile`) confirmată vizual pe pagina de principiu și de exercițiu. EX-0004 confirmă declarația onestă „Organizare fără diagramă în această versiune” — nicio diagramă inventată.

### Constatări Major (2), reparate

1. **Clipping pe titlul hero al homepage-ului, toate viewporturile.** `HomepageHero.astro` seta `line-height:.9` (bază) și `line-height:.92` (`@media max-width:680px`) pe `<h1>`, mai strâns decât `line-height:.98` folosit implicit pe restul site-ului (`global.css`). Rezultat: accentul circumflex al literei „Î” din „Înțelege copilul.” — titlul principal, primul element vizibil pe homepage — apărea vizibil tăiat, confirmat identic la 1440 și 768 prin capturi țintite pe elementul `<h1>`. Confirmat izolat: `/incepe-aici`, care folosește `line-height:.98` implicit pentru un titlu care începe tot cu „Î”, randează complet curat, fără nicio tăiere. Reparat: ambele reguli `line-height` aliniate la `.98`.
2. **Coliziune vizuală în navigarea „Pe această pagină” la 768px.** `SectionNavigator.astro` trecea la layout coloană abia sub 600px; la 768px rămânea pe rând (`display:flex` fără `flex-wrap` pe container), dar `<ul>`-ul din interior se înfășură intern pe 2 linii quando conținutul nu încape. Eticheta `<span>` rămânea centrată vertical față de întreaga înălțime a listei de 2 linii, aterizând vizual între primul și al doilea rând de link-uri (confirmat prin captură țintită pe `EX-0001`). Reparat: pragul media query ridicat de la `600px` la `900px`, ca 768px să primească layout-ul coloană curat (etichetă deasupra, link-uri dedesubt).

Nicio altă constatare Critical/Major găsită la cele 4 lățimi. Validare locală completă după reparare: `validate_content.py --strict` (0 erori), `validate_project.py` (0 erori), `generate_task_registry.py --check` (reproductibil, 214 taskuri), `python -m unittest discover` (428/428 teste PASS), `npm run check` (0 erori/avertismente/hints), `npm run build` (69 pagini). Commit reparație: `15694b0`, pe lucrul curent al ramurii `main`.

### Gate rămas: acces de deployment lipsă pentru re-audit pe Preview nou

Repararea trebuie re-auditată browser-first pe un Preview nou publicat din `15694b0`, nu doar validată local, înainte de a îngheța baseline-ul. Nu există niciun mecanism disponibil în această sesiune pentru a publica acel Preview:

- nu există Vercel CLI instalat local și niciun `.vercel/project.json` care leagă acest checkout de un proiect;
- conexiunea Vercel MCP disponibilă vede un singur proiect (`insuliniq`) pentru echipa `berescristi-8889s-projects`; o cerere directă `get_project` pentru `manualfc` pe același team ID întoarce `404 Not Found` — acces API real absent pentru acest proiect, nu doar filtrare de listă.

Acesta este un blocaj extern real, de același fel ca cele documentate anterior în `PROJECT_STATUS.md` (`TASK-2501`, `TASK-2601`). Nu s-a încercat nicio ocolire.

## Deblocare 2026-08-14 — `vercel login` interactiv, deploy curat din worktree izolat, re-audit PASS

Utilizatorul a rulat `npx vercel@latest login` (flux OAuth pe dispozitiv) direct în această sesiune, autentificând CLI-ul ca `berescristi-8889`. `npx vercel@latest link --yes --project manualfc --scope berescristi-8889s-projects` a legat checkout-ul de proiectul corect.

Pentru a garanta un candidat exact și curat (fără fișierele de audit/documentație necomise din working tree-ul principal), deploy-ul s-a făcut dintr-un git worktree izolat: `git worktree add E:\ManualFC-wave1-preview 15694b0` (detached la exact commit-ul de reparație), apoi `npx vercel@latest deploy --yes --scope berescristi-8889s-projects --project prj_P2o9rzNbCsHraLk5CWVQGozAOZuU` din acel worktree. Rezultat: `target: null` (Preview, fără promovare Production), `readyState: READY`.

### Candidat autoritativ final

- commit implementare: `15694b0` (reparație Wave-1, pe `main`);
- deployment: `dpl_HrfVSK6s8qYFLoiPby3UQhyurMj9`;
- Preview: `https://manualfc-pr08yqh1a-berescristi-8889s-projects.vercel.app`;
- build Vercel: 69 pagini, cache de build restaurat din deploymentul anterior `E8523A8CMnkriJ2XRCMwwDBH4XGW`;
- Production canonic `https://manualfc.vercel.app/` nu a fost promovat sau realiasat.

### Re-audit browser-first pe candidatul reparat, la 1440/1280/768/390

Cu același `Protection Bypass for Automation`, browserul automat a primit conținutul real imediat (fără login). Verificări țintite pe exact cele 2 constatări reparate, plus verificare generală de regresie:

1. **Titlul hero.** Captură țintită pe `<h1>` la 1440, 1280, 768 și 390 — accentul „Î” complet vizibil, fără nicio tăiere, la toate cele 4 lățimi (comparativ direct cu tăierea plată confirmată anterior pe candidatul `c18263c`).
2. **Navigarea „Pe această pagină”.** Verificat pe `/gold-standard/exercitii/EX-0001` la 768px — toate cele 4 link-uri (`Organizează`, `Observă și adaptează`, `Înțelege de ce`, `Verifică transferul`) încap acum pe un singur rând sub eticheta „PE ACEASTĂ PAGINĂ”, fără nicio coliziune vizuală.
3. **Regresie generală.** 0 erori/avertismente în consolă pe `/` (1440/1280/768/390), `/gold-standard/exercitii/EX-0004` (onestitatea despre diagrama lipsă intactă) și `/design-system` (tot 404, `TASK-2702` neatins).

Nicio constatare nouă. Baseline-ul se îngheață.

## Verdict final

**`PASS`.** `MANUALFC_PREMIUM_WAVE1_BASELINE = 15694b0` (Preview autoritativ: `dpl_HrfVSK6s8qYFLoiPby3UQhyurMj9`, `https://manualfc-pr08yqh1a-berescristi-8889s-projects.vercel.app`). Production canonic `https://manualfc.vercel.app/` rămâne neschimbat — acest baseline nu a fost promovat automat în Production; promovarea rămâne o decizie separată, explicită a utilizatorului. Conform condiției de oprire din `plans/TASK-2717-wave1-acceptance.md`, niciun task `TASK-2705`–`TASK-2716` nu pornește după acest verdict.
