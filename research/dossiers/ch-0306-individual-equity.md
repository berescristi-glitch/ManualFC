# Dosar de cercetare CH-0306 — Conversații individuale și echitate

**Capitol ID:** CH-0306
**Volum:** VOLUME-03
**Domeniu:** Dialogul individual 1-la-1, echitatea atenției și prevenirea favoritismului
**Status:** VERIFIED (verificare semantică completă, TASK-0709, 2026-08-11)

## Verificare semantică (nu doar bibliografică)

Auditul forensic din 2026-08-11 confirmase deja identitatea bibliografică a `SRC-0057` (DOI rezolvă corect, titlu și autori corespund) — sursa nu era fabricată. Conform instrucțiunii de a verifica separat dacă sursa validă susține exact ce afirmă capitolul (`CLAIM_SUPPORT`), am reverificat conținutul real al lucrării via CrossRef.

**Constatare:** Mageau & Vallerand (2003) este o **lucrare teoretică/de model conceptual** — propune un model motivațional bazat pe teoria autodeterminării, nu un studiu empiric cu populație măsurată. Articolul nu specifică nicio durată sau frecvență a interacțiunilor individuale.

**Probleme găsite și corectate:**
1. `CLM-0058` avea `claim_type: STUDY_RESULT` și `epistemic_level: HIGH` — corectat la `CONSENSUS`/`MODERATE`, reflectând corect natura teoretică, nu empirică, a sursei.
2. `u11_applicability` era `DIRECT` — corectat la `PARTIAL`, pentru că modelul e general (toate vârstele), nu testat specific la 10–11 ani.
3. Capitolul, fișa de teren și claim-ul conțineau un prag exact „1–2 minute” pentru durata dialogului, plus (doar în fișa de teren) „15 secunde”, „30 secunde”, „1 minut”, „3–4 copii” — **niciunul dintre aceste numere nu vine din sursă**. Exact tiparul deja identificat și eliminat la CH-0301 (regula celor 15 secunde) și CH-0304 (1–2 minute pentru discuția de disciplină). Corectat: numerele rămân ca sugestii practice, dar etichetate explicit „euristică practică ManualFC”, nu prezentate ca prag validat de cercetare.

## Lanțuri de evidență

### CLM-0058 -> CIT-0063 -> SRC-0057
- **Claim:** Modelul motivațional teoretic al lui Mageau și Vallerand (2003) propune că interacțiunile individuale calde și regulate, fără favoritism, susțin conceptual apartenența și motivația intrinsecă a sportivului; nu e un studiu empiric care măsoară durata sau frecvența optimă la copii de 10–11 ani.
- **Sursă:** Mageau G. A., Vallerand R. J. (2003), *The coach-athlete relationship: a motivational model*, Journal of Sports Sciences. DOI `10.1080/0264041031000140374`.
- **Nivel epistemic:** MODERATE (model teoretic larg citat, nu date empirice proprii).
- **Aplicabilitate U11:** PARTIAL (model general, extrapolare plauzibilă la 10–11 ani, netestată direct).

## Ghid de aplicare pe teren

- **Frecvență:** Dialog scurt 1-la-1 cu regularitate cu fiecare copil — durata și frecvența exactă sunt euristică practică ManualFC, nu prag validat de sursă.
- **Conținut:** „Ce simți că ți-a ieșit cel mai bine azi?”, „La ce lucrăm data viitoare?”.
