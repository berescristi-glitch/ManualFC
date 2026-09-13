# TASK-0501 — remedierea integrității dovezilor

## 1. Titlu și scop

Restabilirea forward-only a lanțului `claim → citation → source → conținut canonic → pagină web` pentru primul batch CH-0101, fără modificarea istoriei TASK-0501 și fără includerea draftului TASK-0502.

## 2. Context

Commitul `69b62d0` conține conținutul Batch 1, dar `CLM-0022`–`CLM-0025` nu au citări normalizate, metadata de aplicabilitate este incompletă, iar pagina web afișează dovezi hard-coded. Remedierea este executată într-un worktree curat; draftul TASK-0502 din worktree-ul principal rămâne protejat.

## 3. Rezultat verificabil

Cele patru claims au formulări proporționale cu sursele, metadata completă și cel puțin o citare validă. Entitatea canonică rezolvă aceste relații în Content Bridge, iar ruta principiului afișează registrul real, fără ID-uri sau niveluri hard-coded.

## 4. Domeniu și non-obiective

Intră numai TASK-0501, schemele strict necesare, validatorul, testele, pagina și documentele Batch 1. Nu intră TASK-0502, taxonomia generală sau un motor generic de cercetare.

## 5. Fișiere afectate

Registrele și schemele research, `scripts/validate_content.py`, Content Bridge, tipurile și pagina principiului, testele TASK-0501, dosarul și fișa practică, raportul corectiv și evidențele de governance.

## 6. Cercetare necesară

Se reverifică titlul, autorii, tipul, DOI-ul, populația și limitele pentru `SRC-0021`–`SRC-0024`; fiecare claim primește decizia KEEP/NARROW/DOWNGRADE/SPLIT/REMOVE.

## 7. Model pedagogic

Observarea de teren rămâne descriptivă. Antrenorul separă comportamentul văzut de interpretarea despre maturizare, motivație sau potențial și tratează adaptarea sarcinii ca ipoteză practică verificată prin reobservare.

## 8. Design vizual și interactiv

Nu se adaugă vizual nou. Secțiunea evidence separă „Ce știm”, „Ce înseamnă pentru antrenor” și „Ce nu putem concluziona”, folosind badge-ul nivelului real.

## 9. Pași de implementare

- [x] 2026-08-09: snapshot al worktree-ului protejat și worktree curat creat.
- [x] 2026-08-09: sursele și claims-urile reverificate; supra-afirmațiile identificate.
- [x] 2026-08-09: Restrângerea claims-urilor, corectarea sursei și crearea citărilor.
- [x] 2026-08-09: Resolver minim și randare web canonică.
- [x] 2026-08-09: Gate-uri de validator și teste de drift.
- [x] 2026-08-09: Validări automate complete și raport corectiv; browserul nu a fost disponibil pentru audit vizual.

## 10. Validare și acceptare

Se rulează comenzile cerute în solicitare, inclusiv Astro check/build, întreaga suită Python, validatoarele tematice și `git diff --check`. Testele negative trebuie să demonstreze lipsa citării și metadata incompletă.

## 11. Progres

Implementarea și validarea automată sunt încheiate. Auditul vizual rămâne neexecutat deoarece sesiunea nu a expus niciun browser.

## 12. Descoperiri și surprize

`SRC-0024` avea un DOI inexistent și metadata amestecată. Sursele asociate nu susțin efectul experimental al modificării spațiului, timpului și opțiunilor formulat în `CLM-0024`.

Worktree-ul curat a expus un test istoric care încă așteaptă `TASK-0501` în starea READY; în worktree-ul principal, corecția preexistentă protejată pentru progresia TASK-0502 rezolvă această așteptare. Hunk-ul respectiv nu intră în commitul remedierii.

## 13. Jurnal de decizii

- 2026-08-09: claims-urile sunt restrânse/downgrade-ate în loc să primească citări decorative.
- 2026-08-09: gate-ul de metadata se aplică numai claims-urilor folosite de conținutul canonic de producție, evitând o migrare retroactivă nejustificată.

## 14. Rezultat și retrospectivă

Chain-ul research–product este restaurat și testat fail-closed. Toate validările tematice și build-ul trec. Singura verificare neexecutată este inspecția vizuală în browser, indisponibilă în sesiune.
