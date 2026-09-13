# Matricea de acoperire prin cercetare — Pedagogul

**Versiune:** 1.0.0 · **Fază:** PHASE-30 · **Task de referință:** TASK-3010 · **Statut:** Research

Stări posibile: `NOT_RESEARCHED` (nicio activitate PHASE-30) · `PARTIAL` (atins tangențial de un dosar cu focus în altă parte) · `FOUNDATION_READY` (dosar dedicat, PHASE-30) · `MATURE`/`EXISTING_EVIDENCE_REUSED` (deja acoperit înainte de PHASE-30, verificat, nu re-cercetat) · `RESEARCH_REQUIRED` (recomandat explicit pentru valul următor).

PHASE-30 este primul val de cercetare (regulă §54 din specificație) — nu se pretinde acoperire completă a celor 12 domenii.

| Domeniu | Stare | Sursă acoperire | Notă |
|---|---|---|---|
| PED-D01 — Dezvoltarea copilului | **FOUNDATION_READY** | `CHILD_DEVELOPMENT_10_11_R1.md` (14 claim-uri) | Concluzie centrală: nicio componentă cognitivă majoră nu e „finalizată" la 10-11 ani; variabilitatea individuală ≥ vârsta cronologică ca predictor. |
| PED-D02 — Învățarea (subdomenii) | **FOUNDATION_READY (parțial)** | S01 atenție → `ATTENTION_COGNITIVE_LOAD_R1.md`; S05-S07 achiziția deprinderii → `SKILL_ACQUISITION_FRAMEWORKS_R1.md`; S08 transfer → `TRANSFER_RETENTION_R1.md` | Subdomeniile netratate explicit (memorie declarativă generală, limbaj dincolo de comprehensiune figurată) rămân `PARTIAL`, acoperite doar tangențial în CD. |
| PED-D03 — Motivația | **FOUNDATION_READY** | `MOTIVATION_AUTONOMY_R1.md` (14 claim-uri) | SDT + climat motivațional + alegere/recompensă; evidență fotbal-specifică există dar corelațională, nu experimentală. |
| PED-D04 — Emoțiile | **PARTIAL** | Atins tangențial în CD (reglare emoțională, stil parental „emotion coaching") | `RESEARCH_REQUIRED` pentru frustrare/anxietate specifică U11 fotbal — recomandat Valul 2 (`PHASE30_RESEARCH_ROADMAP.md`). |
| PED-D05 — Eroarea și eșecul | **EXISTING_EVIDENCE_REUSED** | `research/dossiers/ch-0103-decision-error.md` (pre-PHASE-30) | Decizie deliberată de a nu re-cerceta — deja matur, confirmat în `PHASE30_RESEARCH_ROADMAP.md` §2. |
| PED-D06 — Comunicarea | **PARTIAL** | Subdomeniul feedback (S05) → `FEEDBACK_R1.md`; restul netratat | Comunicare generală părinte-copil/antrenor-copil dincolo de feedback = `RESEARCH_REQUIRED`. |
| PED-D07 — Relația pedagogică | **NOT_RESEARCHED** | — | `RESEARCH_REQUIRED`, Val 2 (autoritate/limite, per roadmap). |
| PED-D08 — Dinamica de grup | **NOT_RESEARCHED** | — | `RESEARCH_REQUIRED`, Val 3. |
| PED-D09 — Safeguarding | **EXISTING_EVIDENCE_REUSED** | `data/safeguarding/canonical.json` (pre-PHASE-30) | Matur, tratat ca graniță tare, nu redeschis. |
| PED-D10 — Părinții | **NOT_RESEARCHED** | — | Zero acoperire azi, confirmat de roadmap; `RESEARCH_REQUIRED`, Val 3. |
| PED-D11 — Diferențe individuale | **PARTIAL** | Maturizare biologică/PHV, variabilitate dezvoltare → CD | Diferențe dincolo de maturizarea biologică (temperament, context socio-economic) = `RESEARCH_REQUIRED`, Val 3. |
| PED-D12 — Reflecție și metacogniție (a copilului) | **PARTIAL** | Monitorizare metacognitivă (van Loon et al., 2024) → CD | Aplicare directă pe sarcini motrice/tactice, nu doar memorie verbală = `RESEARCH_REQUIRED`. |

## Rezumat

- `FOUNDATION_READY`: 3 domenii complete (PED-D01, PED-D03) + acoperire parțială majoră pe PED-D02.
- `EXISTING_EVIDENCE_REUSED`: 2 domenii (PED-D05, PED-D09) — corect, nu re-cercetate.
- `PARTIAL`: 4 domenii (PED-D04, PED-D06, PED-D11, PED-D12).
- `NOT_RESEARCHED`: 3 domenii (PED-D07, PED-D08, PED-D10) — toate trei confirmate ca prioritate reală pentru Valurile 2-3 de `PHASE30_RESEARCH_ROADMAP.md`.
