# TASK-0601 — Jocul ca sistem de probleme

## 1. Titlu și scop

Producerea primului capitol publicabil din VOLUME-02, astfel încât antrenorul să poată transforma o temă tactică într-o problemă de joc cu informație, opțiuni și consecințe, fără a prescrie o coregrafie.

## 2. Context

VOLUME-01 a stabilit observația prudentă, ciclul percepție–decizie–execuție și limbajul pedagogic. TASK-0601 deschide fundamentele tactice și definește unitatea de proiectare pe care se vor sprijini capitolele CH-0202–CH-0208.

## 3. Rezultat verificabil

- `content/volume-02/chapter-01.mdx` publicabil;
- dosar research și chain-uri noi pentru caracterul reprezentativ al sarcinii;
- o fișă de proiectare „problemă, nu traseu” utilizabilă mâine pe teren;
- audit factual/pedagogic și audit editorial distincte;
- teste și raport TASK-0601.

## 4. Domeniu și non-obiective

Intră: definirea problemei de joc, relația informație–alegere–consecință, exemplu 3v3+portari, limbajul copilului, verificarea și transferul. Nu intră: catalogul tuturor principiilor tactice, exerciții canonice complete, diagrame, animații sau modificări ale designului.

## 5. Fișiere afectate

Registrele research, `research/dossiers/ch-0201-game-problems.md`, capitolul, fișa de teren, auditurile, testele, registrul și rapoartele persistente.

## 6. Cercetare necesară

- Ce susține representative learning design despre păstrarea informației și acțiunii din joc?
- Ce arată comparațiile dintre abordările tactice și tehnice despre decizie și execuție?
- Ce nu poate fi extrapolat direct la fotbal U11?

## 7. Model pedagogic

Problema pilot: purtătorul nu are o cale clară de progresie. Copilul observă apărătorul, spațiul, colegii și ținta; alege să joace prin, pe lângă sau înapoi. Antrenorul verifică procesul, nu doar golul sau pasa reușită.

## 8. Design vizual și interactiv

`VISUAL_DEBT_DEFERRED`: design freeze rămâne activ. Fișa text descrie toate rolurile și dimensiunile necesare unei implementări vizuale ulterioare, dar taskul nu produce active vizuale.

## 9. Pași

- [x] 2026-08-10 — dependențe, task, standarde și worktree inspectate;
- [x] 2026-08-10 — research batch inițiat și surse primare verificate;
- [x] 2026-08-10 — registre, dosar și claim decisions finalizate;
- [x] 2026-08-10 — capitol și instrument de teren finalizate;
- [x] 2026-08-10 — audit factual/pedagogic și editorial separat finalizate;
- [x] 2026-08-10 — 8/8 teste task, 194/194 full Python, validatoare și Astro check/build PASS; registry/history închise.

## 10. Validare și acceptare

Teste TASK-0601, full Python, content strict, registry reproducibil, validator global, Astro check/build și `git diff --check`. Capitolul trebuie să arate explicit ce știm, ce traducem în practică și ce nu putem concluziona.

## 11. Descoperiri

Registrele VOLUME-02 existente acoperă regulamente, nu această bază metodologică. Sunt necesare chain-uri noi; sursele deja folosite în VOLUME-01 pot oferi context, dar nu înlocuiesc claim-ul despre reprezentativitate.

## 12. Jurnal de decizii

- 2026-08-10 — „Sistem de probleme” este tratat ca model metodologic ManualFC, nu ca rezultat experimental ori definiție oficială unică.
- 2026-08-10 — exemplul practic păstrează mingea, adversarul, direcția, ținta, minimum două opțiuni și consecința pierderii.

## 13. Rezultat și retrospectivă

CH-0201 este publicabil și lasă un canvas utilizabil fără a transforma cadrul conceptual în efect U11 garantat. Validatorul a detectat și a blocat două neconformități de enum și un principiu incomplet înainte de închidere. O corupere locală a `node_modules` a fost reparată prin instalare curată; sursele proiectului nu au necesitat modificări pentru incident. TASK-0602 este următorul task READY.
