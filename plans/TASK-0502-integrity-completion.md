# TASK-0502 — închiderea integrității research și a capitolului CH-0102

## 1. Titlu și scop

Închiderea chain-urilor evidence și alinierea draftului cu taskul canonic „Capitol — Percepție, orientare și atenție în joc”.

## 2. Context

Registry-ul definește `TASK-0502`, `VOLUME-01`, output `chapter-02.mdx`. Draftul Batch 2 a introdus patru claims fără citări și cu metadata/scope supra-formulate.

## 3. Rezultat verificabil

Claims au chain complet, metadata și limite; capitolul, dosarul și fișa de teren folosesc formulări susținute; validatorul global trece.

## 4. Domeniu și non-obiective

În scope: `CLM-0026`–`CLM-0029`, `SRC-0025`–`SRC-0028`, citările și outputurile TASK-0502. În afara scope-ului: toate fișierele vizuale înghețate.

## 5. Fișiere afectate

Registrele research, dosarul, principiul, fișa de teren, capitolul, raportul, istoricul și testele TASK-0502.

## 6. Cercetare

Metadata și suport verificate pe paginile editorilor. Accesul numai la metadata/preview este declarat, nu extrapolat.

## 7. Model pedagogic

Observare → ipoteză modestă → o singură ajustare → repetare → reobservare; fără diagnosticarea copilului.

## 8. Design

`DESIGN_FREEZE = YES`; nicio schimbare vizuală.

## 9. Pași

Audit claims/sources; corectare metadata; citări; revizie produse; teste; validări; raport.

## 10. Validare

Teste TASK-0502, validatoare content/research/registry, suita Python, Astro check/build, validator global.

## 11. Progres

- [x] 2026-08-09 — scope și worktree auditate.
- [x] 2026-08-09 — sursele verificate și cele patru claims restrânse/retrogradate.
- [x] 2026-08-09 — chain-urile, dosarul, instrumentul, capitolul și raportul reparate.
- [x] 2026-08-09 — toate validările finale au trecut; închiderea este documentată și pregătită pentru commit focalizat.

## 12. Descoperiri

Draftul a atribuit surselor rezultate U11 inexistente și a folosit metadata bibliografică greșită pentru două surse.

## 13. Decizii

2026-08-09 — Scope-ul registry-ului și outputul `CH-0102` au prioritate; instrumentul de adaptare rămâne suport practic, nu redefinește taskul.

## 14. Rezultat

Integritate închisă: chain-urile research → claim → citation sunt complete, outputul canonic CH-0102 este aliniat, iar toate gate-urile tehnice sunt verzi. Fișierele vizuale au rămas în afara scope-ului.
