# ManualFC — Phase-27 Wave-3 browser acceptance

## Verdict

`PASS — MANUALFC_PREMIUM_WAVE3_BASELINE = ae04ed53929ce5a4a06a374a479451c40737e10c`

Preview autoritativ curat: `dpl_ZZvvHG9GTSSycW41RVkmVJUtT9aK`, `https://manualfc-n5mxrlqzi-berescristi-8889s-projects.vercel.app`, target Preview. Deployment-ul a fost construit dintr-un worktree izolat și curat, detached exact la commitul runtime de mai sus (695 fișiere încărcate, 83 pagini generate). Production nu a fost promovat sau modificat.

## Domeniu acceptat

- `TASK-2708 = DONE`: bibliotecă de 8 probleme observabile, dintre care 3 flagship, cu graf canonic fail-closed, ipoteze separate de observație, teste cu o singură variabilă și transfer neconfirmat fără observație de teren.
- `TASK-2709 = DONE`: gateway `/rezolva-pe-teren`, 8 pagini de problemă și handoff-uri canonice către principiu, exercițiu, Group Configurator, ședință, Field Mode și evaluare.
- `TASK-2712 = DONE`: Search & Discovery static, determinist și explicabil peste 6 tipuri de conținut, cu filtre pentru tip, efectiv, timp și dovezi.

## Re-audit browser live

Matricea `/`, `/rezolva-pe-teren`, pagina flagship `primeste-fara-sa-verifice-inainte` și `/cauta` a fost verificată pe Preview la 1440, 1280, 768 și 390 px. Toate cele 16 combinații au `scrollWidth === clientWidth`; nu există overflow orizontal. Pagina flagship are 0 încălcări axe WCAG 2 A/AA confirmate și 0 erori de pagină. Cele 10 noduri `incomplete` sunt exclusiv contraste pe care axe nu le poate determina automat peste logo/SVG și nu sunt încălcări confirmate.

Scenariile A–D sunt reprezentate de primele patru probleme și oferă testul imediat, cue-ul exact și traseul progresiv. Scenariul E, `12 jucători` + `maximum 20 min`, afișează exact 5 rezultate relevante: „Cine ne poate acoperi pe amândoi?”, „Creează opțiunea sub presiune reală”, „Primește gata să continui”, „Sprijin cu doi coechipieri” și „Transferul în joc mic”. Stările fără rezultate și resetarea filtrelor rămân disponibile.

Ținta de 30 de secunde este satisfăcută structural pe primul ecran al problemei: observație, limită, test și cue. Ținta de 2 minute este satisfăcută prin handoff-urile canonice către configurator, ședință, Field Mode și evaluare, fără motoare paralele.

## Constatări și reparații

Cinci constatări Major au fost reparate înaintea re-auditului final: contrastul hero, contrastul corpului cue, overflow mobil de 6 px, semantica filtrului de efectiv (stație vs. cohorta 8–18 a configuratorului) și contrastul etichetei „SPUNE CLAR”. Re-auditul final are `CRITICAL_FINDINGS = 0`, `MAJOR_FINDINGS = 0`, `PAGE_ERRORS = 0`.

Reziduuri non-blocante, nemodificate conform regulii „Critical/Major only”: breadcrumb-ul `/cauta` repetă „Acasă”; rezultatele `CAPITOL` sunt agregate la nivel de volum/suprafață, nu indexate individual pentru toate cele 25 de capitole. Acestea nu blochează joburile Wave-3.

## Validare finală

- `python scripts/validate_content.py --strict`: 0 erori, 0 avertismente;
- `python scripts/validate_project.py`: 222 taskuri, 0 erori, 0 avertismente;
- `python scripts/generate_task_registry.py --check`: reproductibil;
- `python -m unittest discover -s tests -p "test_*.py"`: 435/435 PASS;
- `npm.cmd run check`: 78 fișiere, 0 erori, 0 avertismente, 0 hints;
- `npm.cmd run build`: 83 pagini statice.

## Compatibilitate viitoare

Multimedia, Field Mode, Session Workspace și evaluarea au IDs/hook-uri canonice și rămân compatibile. Conturile, offline, monetizarea și stratul academy/club nu sunt hardcodate în motor și pot consuma ulterior aceleași relații. Extinderea multi-age cere evoluția explicită a schemei U11; nu se presupune automat compatibilitate semantică pentru alte vârste.

## Înghețare

`MANUALFC_PREMIUM_WAVE1_BASELINE = 15694b0`, `MANUALFC_PREMIUM_WAVE2_BASELINE = eccec0b` și `MANUALFC_PREMIUM_WAVE2_FINAL_BASELINE = ba78399` rămân neschimbate. `MANUALFC_PREMIUM_WAVE3_BASELINE = ae04ed53929ce5a4a06a374a479451c40737e10c`. Wave-4 este `NOT_STARTED`. Conform condiției explicite de oprire: `STOP`.
