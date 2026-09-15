# TASK-3715 — Redeploy ManualFC from origin/main and Verify the Live Production Deployment

## 1. Titlu și scop

Redeployează exact revizia validată `origin/main` pe proiectul Vercel configurat și dovedește că site-ul live corespunde comportamentului repository-ului validat local. **Rezultat posibil, onest:** dacă accesul de deployment nu e disponibil, taskul se oprește `BLOCKED` cu dovezi exacte, fără workaround.

## 2. Context pentru un cititor nou

- Repo canonic: `E:/ManualFC-clean`, HEAD de pornire (= SHA sursă pentru deployment) `b0202f0515b684d6a6984ddbb0420d82d98c78e6` (rezultatul TASK-3713).
- Proiectul Vercel documentat: `manualfc` (`PROJECT_ID: prj_P2o9rzNbCsHraLk5CWVQGozAOZuU`, org `berescristi-8889s-projects`), alias public `https://manualfc.vercel.app/` — confirmat din `reports/deployments/TASK-2601-vercel-staging.md` (`TASK-2601`, DEC-0053). Acest URL e deja folosit ca `site` în `astro.config.mjs` (TASK-3711) — nu se inventează un domeniu nou.
- **Constatare critică:** acel deployment original (`TASK-2601`, `SOURCE_COMMIT: e59f10d`) a fost făcut din **repository-ul legacy** (`E:/ManualFC`), înainte de migrarea clean-genesis (`TASK-3708`). Proiectul Vercel `manualfc` nu are, din câte se poate verifica fără autentificare, nicio garanție de legătură automată (Git integration) cu noul remote GitHub `git@github.com:berescristi-glitch/ManualFC.git` folosit de repo-ul canonic.
- **Verificare live, fără autentificare Vercel** (browser real, Playwright): site-ul de la `https://manualfc.vercel.app/` răspunde 200, dar `/robots.txt` și `/sitemap-index.xml` răspund **404** — ambele au fost adăugate abia în `TASK-3711`. Aceasta e dovadă directă că deployment-ul live curent **precede TASK-3711**, deci precede și `TASK-3712`/`TASK-3713`. Un redeploy e într-adevăr necesar pentru a alinia live-ul cu `origin/main`.
- **Verificare acces de deployment:** `npx vercel whoami` → „Logged out.” Nu există `.vercel/project.json` în `E:/ManualFC-clean`. Nu există variabile de mediu `VERCEL_TOKEN`/`VERCEL_ORG_ID`/`VERCEL_PROJECT_ID`. Nu există `auth.json` pentru Vercel CLI nicăieri pe disc (verificat `%APPDATA%/com.vercel.cli/Data/`). Niciun tool MCP Vercel cu capabilitate de deployment nu e înregistrat în această sesiune. **Concluzie: acces de deployment indisponibil.**

## 3. Rezultatul verificabil

Dat fiind §2, rezultatul verificabil al acestui task e un raport `BLOCKED` complet și onest: validarea locală completă (dovedind ce AR trebui să fie live), dovada exactă a stării live curente (stale, pre-TASK-3711), și acțiunea exactă cerută din partea utilizatorului pentru a debloca deployment-ul.

## 4. Domeniu și non-obiective

**Intră:** validarea locală completă, verificarea accesului de deployment, verificarea directă a stării live curente (fără autentificare, doar prin browser), raport precis.

**Nu intră:** orice încercare de deployment alternativ/de substituție; `vercel login` interactiv (necesită browser OAuth sau confirmare pe e-mail, imposibil într-o sesiune non-interactivă); modificarea repository-ului pentru a ocoli blocajul; reparații de conținut/design/vulnerabilități npm neconectate la deployment.

## 5. Fișiere și module afectate

Niciun fișier de produs sau configurare nu se modifică — blocajul e de autentificare externă, nu de configurare a repository-ului. `vercel.json`/`astro.config.mjs`/`package.json` au fost deja inspectate (TASK-3711) și rămân corecte pentru deployment.

Guvernanță: `TASK_REGISTRY.json`, `TASK_HISTORY.jsonl`, `PROJECT_STATUS.md`, `DECISIONS.md`, raport de task — toate declarând explicit `BLOCKED`, nu `DONE`.

## 9. Pași de implementare

1. Verificare stare Git (HEAD = origin/main, tree curat) — finalizat.
2. Citire documentație relevantă + inspecție configurație de deployment (`vercel.json`, `package.json`, `astro.config.mjs`) — finalizat.
3. Confirmarea proiectului Vercel/URL public documentat, din `reports/deployments/TASK-2601-vercel-staging.md` — finalizat.
4. Verificarea accesului de deployment (`vercel whoami`, `.vercel/project.json`, variabile de mediu, `auth.json`, tool-uri MCP) — finalizat, **indisponibil**.
5. Verificare directă, fără autentificare, a stării live curente (browser real) — finalizat, confirmă stare stale (pre-TASK-3711).
6. Validare locală completă (checklist-ul cerut de task) — în curs.
7. Raport final `BLOCKED`, cu acțiunea exactă cerută din partea utilizatorului.
8. Guvernanță (fără a marca taskul `DONE`).

## 11. Progres

- [x] Stare Git verificată.
- [x] Configurație de deployment inspectată.
- [x] Proiect/URL Vercel confirmat din documentația existentă (fără a inventa un domeniu).
- [x] Acces de deployment verificat — indisponibil (logged out, fără token, fără link de proiect, fără tool MCP).
- [x] Stare live curentă verificată direct (browser, fără autentificare) — stale, precede TASK-3711. CTA header/footer/hero live încă `/gold-standard/rapid`; `EX-0006` (TASK-3712) → 404; niciun `canonical`/`og:url`.
- [x] Validare locală completă: `npm run check` 0 erori, `npm test` 9/9, `pytest` 576/576, `npm run build` 119 pagini, `audit_route_links.py` 0 linkuri rupte, toate EX-0006–EX-0015/SES-0003–SES-0006 prezente local, CTA local = `/rezolva-pe-teren` peste tot (0 apariții `/gold-standard/rapid`), `canonical`/`og:url` prezente și corecte local, offline funcțional local.
- [x] Raport final BLOCKED + guvernanță

## 13. Jurnal de decizii

- **Decizie:** taskul se raportează `BLOCKED`, nu `FAIL` și nu `PASS` cu un deployment simulat. **Motiv:** regula explicită a taskului — „If deployment access is unavailable: stop before making unrelated changes; report BLOCKED... do not create a substitute deployment". Nu există autentificare Vercel utilizabilă în acest mediu, verificat exhaustiv (CLI, fișiere de config, variabile de mediu, tool-uri MCP). **Efect:** nu se încearcă niciun ocol (nu se creează un deployment temporar/alternativ, nu se modifică repo-ul).
- **Decizie:** se execută integral validarea locală cerută de task, chiar dacă deployment-ul e blocat. **Motiv:** taskul cere explicit înregistrarea acestor rezultate în raportul final, indiferent de verdict; demonstrează că blocajul e strict de autentificare externă, nu de calitate a codului sursă. **Efect:** raportul `BLOCKED` conține dovezi complete despre ce anume ar fi fost deployat.
- **Decizie:** se verifică starea live curentă direct prin browser, fără autentificare Vercel. **Motiv:** verificarea unui site public nu necesită credențiale — oferă dovadă independentă, verificabilă, despre cât de „stale" e deployment-ul curent, întărind raportul BLOCKED cu fapte concrete în loc de presupuneri. **Efect:** raportul poate afirma cu precizie (nu presupunere) că live-ul precede TASK-3711 (robots.txt/sitemap-index.xml absente).
