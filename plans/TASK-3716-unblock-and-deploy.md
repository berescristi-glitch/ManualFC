# TASK-3716 — Unblock Vercel Deployment and Publish the Validated ManualFC Baseline

## 1. Titlu și scop

Deblochează accesul de deployment Vercel (blocat în `TASK-3715`) și publică revizia validată `origin/main` pe proiectul Vercel existent `manualfc`, dovedind că site-ul live reflectă acum comportamentul validat local.

## 2. Context pentru un cititor nou

- Repo canonic: `E:/ManualFC-clean`, HEAD de pornire (= SHA sursă pentru deployment) `d2c6c5a399cf245290bb7a1f04f4c7da0763ea22` (rezultatul `TASK-3715`).
- `TASK-3715` a documentat exhaustiv blocajul: `vercel whoami` → „Logged out", fără `.vercel/project.json`, fără `VERCEL_TOKEN`, fără `auth.json`, fără tool MCP de deployment. Verificarea live directă (fără autentificare) a dovedit că site-ul era stale, precedând `TASK-3711`.
- **Deblocare, calea A (CLI autentificat prin fluxul de dispozitiv OAuth):** `npx vercel login` a generat un cod de dispozitiv (`https://vercel.com/oauth/device?user_code=...`), afișat utilizatorului. Primele două coduri au expirat neconfirmate; al treilea a fost confirmat de utilizator în timp util, iar `vercel login` a raportat „Congratulations! You are now signed in." `npx vercel whoami` → `berescristi-8889`, corespunzător organizației documentate `berescristi-8889s-projects`.
- Proiectul a fost legat explicit cu `npx vercel link --yes --project manualfc --scope berescristi-8889s-projects` (scope-ul exact obținut din `npx vercel teams ls`, nu presupus). `.vercel/project.json` rezultat conține `projectId: prj_P2o9rzNbCsHraLk5CWVQGozAOZuU` — **identic** cu ID-ul documentat în `reports/deployments/TASK-2601-vercel-staging.md` — confirmă legarea la proiectul corect existent, nu la unul nou.
- `.vercel/` și `.env.local` (acesta din urmă creat automat de `vercel link`, conține un `VERCEL_OIDC_TOKEN`) sunt deja acoperite de `.gitignore` (`.vercel/`, `.env*`) — confirmat prin `git status --short` neschimbat după `link`.

## 3. Rezultatul verificabil

- Deployment de producție nou, cu `target: production`, aliasat la `https://manualfc.vercel.app`, provenit exact din sursa `d2c6c5a399cf245290bb7a1f04f4c7da0763ea22` (working tree curat, `HEAD == origin/main` la momentul upload-ului).
- Verificare live completă (CTA, rute noi, SEO tehnic, accesibilitate, responsive, offline) — toate PASS, cu dovezi directe din browser real.
- Guvernanță actualizată declarând verdict `PASS`.

## 4. Domeniu și non-obiective

**Intră:** deblocarea autentificării Vercel prin fluxul legitim de dispozitiv OAuth, legarea la proiectul existent, deployment-ul exact al sursei validate, verificarea live completă.

**Nu intră:** orice modificare de cod/produs (niciuna nu a fost necesară — `vercel.json`/`astro.config.mjs`/`package.json` erau deja corecte din `TASK-3711`); crearea unui proiect/organizație/domeniu nou; expunerea vreunui token sau credențial în log-uri sau rapoarte.

## 5. Fișiere și module afectate

Niciun fișier de produs sau configurare de repository nu a fost modificat — deployment-ul folosește exact sursa existentă. `.vercel/project.json` și `.env.local` sunt artefacte locale, negestionate de Git (deja ignorate).

Guvernanță: `TASK_REGISTRY.json`, `TASK_HISTORY.jsonl`, `PROJECT_STATUS.md`, `DECISIONS.md`, `reports/task-reports/TASK-3716.md`.

## 9. Pași de implementare

1. Verificare stare Git (HEAD = origin/main = `d2c6c5a...`, tree curat) — finalizat.
2. Verificare acces de deployment (repetare verificărilor din `TASK-3715`) — inițial tot indisponibil.
3. Deblocare prin flux de dispozitiv OAuth (`npx vercel login`), cu confirmare din partea utilizatorului — finalizat, autentificat ca `berescristi-8889`.
4. Legare explicită la proiectul existent (`vercel link --project manualfc --scope berescristi-8889s-projects`), verificare `projectId` identic cu cel documentat — finalizat.
5. Validare locală completă (`npm run check`, `npm test`, `pytest`, `npm run build`, audit de rute, sitemap/robots, offline) — finalizat, toate PASS, 119 pagini.
6. Deployment de producție (`npx vercel --prod --yes`) — finalizat, `READY`, aliasat la `manualfc.vercel.app`.
7. Verificare live completă cu browser real (CTA, rute, SEO, axe, responsive, offline, identitate deployment) — finalizat, toate PASS.
8. Guvernanță + raport final, verdict `PASS`.

## 11. Progres

- [x] Stare Git verificată.
- [x] Deblocare Vercel prin flux de dispozitiv OAuth, confirmată de utilizator.
- [x] Proiect legat la `manualfc` existent, `projectId` verificat identic.
- [x] Validare locală completă (0 erori check, 9/9 JS, 576/576 Python, 119 pagini, 0 linkuri rupte, offline OK).
- [x] Deployment de producție reușit (`dpl_FEhcEK61vhgJgHh1qoYrzUsih8Cj`, aliasat).
- [x] Verificare live completă (CTA, rute, SEO, axe, responsive, offline, identitate) — toate PASS.
- [x] Guvernanță + raport final.

## 13. Jurnal de decizii

- **Decizie:** deblocarea s-a făcut exclusiv prin fluxul legitim de dispozitiv OAuth al Vercel CLI (`vercel login`), cu utilizatorul confirmând codul în propriul browser. **Motiv:** calea A explicit autorizată de task; nu a necesitat niciodată ca acest proces să vadă o parolă sau un token — doar un cod afișat public, cu durată scurtă de expirare. **Alternativă respinsă:** solicitarea unui `VERCEL_TOKEN` (calea C) — inutilă odată ce calea A a funcționat. **Efect:** nicio expunere de credențial în nicio conversație sau fișier.
- **Decizie:** scope-ul exact (`berescristi-8889s-projects`) a fost obținut din `vercel teams ls`, nu presupus din numele afișat de `whoami` (`berescristi-8889`, diferit de slug-ul echipei). **Motiv:** o primă încercare cu `--scope berescristi-8889` a eșuat explicit („You cannot set your Personal Account as the scope"), dovedind că presupunerea inițială era greșită. **Efect:** legare corectă din prima încercare validă, fără a forța o presupunere greșită mai departe.
- **Decizie:** niciun fișier de produs sau configurare nu a fost modificat pentru acest deployment. **Motiv:** `vercel.json` (build command, output directory, header `X-Robots-Tag`) era deja corect din `TASK-3711`; deployment-ul a folosit exact sursa validată, fără nicio ajustare. **Efect:** deployment-ul dovedește validitatea configurației deja existente, nu o repară.
