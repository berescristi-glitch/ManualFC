# Manual U11 — pachet de pornire pentru Codex

Acest repository este punctul de pornire pentru construirea integrală a unui manual multimedia și interactiv despre predarea tacticii în fotbal copiilor de aproximativ 10–11 ani.

Grupele de copii născuți în 2015 și 2016 sunt tratate ca **o singură categorie de lucru**. Manualul nu separă conținutul după anul nașterii. Adaptările se fac individual, după experiență, maturizare, nivel tehnic, înțelegere, încredere și nevoi de învățare.

## Fișierele esențiale

- `AGENTS.md` — instrucțiunile stabile pe care Codex le citește automat.
- `CODEX.md` — constituția completă a proiectului.
- `PLANS.md` — standardul pentru planurile de execuție pe termen lung.
- `MASTER_EXECUTION_PROMPT.md` — misiunea completă și condiția de finalizare.
- `START_CODEX_PROMPT.md` — primul mesaj care trebuie trimis în Codex.
- `TASK_PROMPTS.md` — mesajele folosite pentru continuare, audit și reparare.
- `TASK_REGISTRY.json` — registrul inițial al fazelor.
- `docs/` — standardele de cercetare, scriere, pedagogie, vizual și calitate.
- `schemas/` — schemele minime pentru taskuri, principii, exerciții și ședințe.
- `scripts/` — validări locale fără dependențe externe.

## Pornire

1. Copiază toate fișierele în rădăcina unui repository Git nou.
2. Deschide repository-ul în Codex din rădăcină.
3. Nu rula `/init` peste acest proiect; `AGENTS.md` este deja pregătit.
4. Trimite integral conținutul din `START_CODEX_PROMPT.md`.
5. După taskul inițial, folosește prompturile din `TASK_PROMPTS.md`.
6. Păstrează taskurile limitate la un livrabil verificabil: un capitol, 3–5 exerciții, 1–2 ședințe sau un audit clar.

## Rezultatul final așteptat

- manual web interactiv, utilizabil local și offline;
- PDF complet, lizibil la tipar;
- minimum 10 volume, 60 de exerciții și 36 de ședințe;
- diagrame SVG și animații tactice;
- resurse editabile;
- arhivă ZIP testată după dezarhivare;
- raport final de audit.

Nu accepta drept „final” un prototip, un cuprins, un volum izolat sau un build cu placeholder-e.
