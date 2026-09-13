# TASK-2601 — Vercel Preview staging

## Scop

Publică baseline-ul ManualFC acceptat într-un deployment Vercel Preview reproductibil și folosește URL-ul live pentru verificarea rutelor, activelor și experienței responsive. Nu configurează domeniu custom, producție comercială, analytics, autentificare în aplicație sau funcții server.

## Context și rezultat verificabil

Baseline-ul Phase-25 este `4bf2064`. Configurația minimă Vercel și starea persistentă de staging sunt în commitul `e59f10d`. Repository-ul nu are remote Git și aplicația nu necesită variabile de mediu. Deploymentul este realizat direct dintr-un snapshot Git curat.

## Progres

- [x] Recuperare Git și audit root/configurație.
- [x] Audit secrete și date personale: zero expuneri găsite.
- [x] Gate local: validatoare PASS, registry reproductibil, 417/417 teste, Astro check PASS, build 74 pagini.
- [x] Strategie: direct Vercel Preview; niciun remote Git disponibil.
- [x] Autentificare Vercel validă și proiect `manualfc` creat.
- [x] Primul deploy a identificat configurația greșită de output (`dist` în loc de `dist/web`).
- [x] Reparație minimă `vercel.json`, commit `e59f10d` și redeploy Preview.
- [x] Smoke test autentificat: 18/18 rute critice PASS; header `noindex, nofollow` prezent.
- [x] Promovare fără rebuild a artefactului `e59f10d`; aliasul Production indică deploymentul echivalent corect.
- [x] Protecție îngustată la Preview-only; Production este public, Preview rămâne protejat.
- [x] Browser QA la 1440/1280/768/390: PASS.
- [x] URL, deployment ID, commit și starea intermediară persistate.
- [x] Verdict final și închiderea taskului.

## Descoperiri și decizii

Primul deployment a construit 74 pagini, dar auto-detectarea Vercel a publicat `dist` în loc de `dist/web`, producând `404_NOT_FOUND`. `vercel.json` declară acum explicit outputul canonic și adaugă protecția anti-indexare.

Deploymentul reparat `dpl_DM6ueZVLZwQpVL942NUnSDDYxQic` a fost promovat fără rebuild în `dpl_9UpgnY7xuhpcR2FZyMjZ4JrWzsnE`. Aliasul `manualfc.vercel.app` indică noul Production, iar `ssoProtection.deploymentType=preview` păstrează Preview-urile protejate și permite acces anonim pe Production. Smoke testul 18/18, activele, siguranța publică și auditul browser responsive sunt PASS.

## Reluare exactă

Taskul este închis. Următorul pas nu este dezvoltare sau analiză simulată, ci Runda 1 reală din `PHASE-23`, urmată de returnarea datelor de teren.
