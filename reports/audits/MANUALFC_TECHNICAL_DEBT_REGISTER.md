# ManualFC — Technical Debt Register

| ID | Element | Clasificare | Stare / proprietar / prag |
|---|---|---|---|
| TD-0001 | Suită Node fără teste executate | FIX_NOW | FIXED; test real pe 101 pagini |
| TD-0002 | Artefacte Playwright, cache pytest și copia recuperabilă `node_modules.corrupt-20260831` | FIX_BEFORE_SCALE | DEFERRED; ownership utilizator; nu se șterg automat |
| TD-0003 | Matrice Firefox/WebKit absentă | FIX_BEFORE_COMMERCIAL | OPEN; engineering; înainte de distribuție comercială |
| TD-0004 | Build-ul nu este atomic | FIX_BEFORE_SCALE | DEFERRED_WITH_JUSTIFICATION; necesită staging + swap testat |
| TD-0005 | Audit npm online neexecutat | FIX_BEFORE_COMMERCIAL | POLICY_BLOCKED; necesită autorizare explicită pentru trimiterea metadatelor la npm |
