# ManualFC — Stage 4 Repair Program

## Ordinea reparațiilor

1. `INT-0007` CRITICAL: PRB-0008 remapat de la claim-uri retrase la `CLM-0073`/`CLM-0079`; validator fail-closed și test de regresie.
2. `INT-0001` MAJOR: instalarea coruptă mutată recuperabil, `npm ci` refăcut, check/build reluate.
3. `INT-0004` MAJOR: contacte instituționale reverificate; contactul IPJ imposibil de reverificat eliminat.
4. `INT-0008`/`INT-0009` MAJOR: ierarhia H1 din Field Mode și contrastul homepage reparate.
5. `INT-0002`/`INT-0005` MODERATE: suită Node reală și output UTF-8 pentru validator.
6. defect târziu: `pytest.ini` restrânge colectarea la testele proiectului și dezactivează numai cache-ul local corupt.

Toate reparațiile au `RETEST_PASS`. `INT-0006` (build atomic) este `DEFERRED_WITH_JUSTIFICATION`; refactorul staging/swap are risc disproporționat pentru această rundă. `INT-0003` rămâne ownership extern și nu a fost șters. Snapshot-ul pre-repair nu a fost modificat.
