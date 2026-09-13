# Dosar de cercetare CH-0401 — Proiectarea unei situații reprezentative

**Capitol ID:** CH-0401
**Volum:** VOLUME-04
**Domeniu:** Representative Learning Design (RLD), cuplaj percepție-acțiune și fidelitatea sarcinilor
**Status:** VERIFIED (verificare semantică completă, TASK-0809, 2026-08-11)

## Verificare semantică (nu doar bibliografică)

Auditul forensic din 2026-08-11 confirmase deja identitatea bibliografică a `SRC-0058` (DOI rezolvă corect, titlu și autori corespund) — sursa nu era fabricată. Conform aceluiași protocol aplicat la CH-0306, am reverificat separat dacă sursa validă susține exact ce afirmă capitolul.

**Constatare:** Renshaw, Davids, Newcombe și Roberts (2019) este o **carte de metodologie/sinteză** (confirmată via CrossRef: monografie, nu articol empiric), acoperind toate vârstele și sporturile — nu un studiu empiric cu populație măsurată la 10–11 ani în fotbal.

**Probleme găsite și corectate:**
1. `CLM-0059` avea `epistemic_level: HIGH` și `u11_applicability: DIRECT` — corectat la `MODERATE`/`PARTIAL`, reflectând corect natura de sinteză metodologică generală, nu date empirice specifice U11.
2. `context` era `FOOTBALL` — corectat la `CONCEPTUAL_YOUTH_SPORT`, coerent cu `sport: toate` din înregistrarea sursei.
3. Capitolul și principiul conțineau un prag exact „2–3 stimuli simultani” la secțiunea de adecvare la vârstă — **acest număr nu vine din sursă**. Exact tiparul deja identificat și eliminat la CH-0301/CH-0304/CH-0306. Corectat: afirmația rămâne calitativă („număr limitat de stimuli”), cu numărul exact eliminat și eticheta explicită „euristică practică ManualFC” unde relevant.
4. Typo de date („spațiulLiber” fără spațiu) corectat în `principle-proiectarea-situatiilor-reprezentative.json`.

## Lanțuri de evidență

### CLM-0059 -> CIT-0064 -> SRC-0058
- **Claim:** Cartea de metodologie a lui Renshaw, Davids, Newcombe și Roberts (2019) despre abordarea bazată pe constrângeri propune că proiectarea situațiilor de antrenament reprezentative susține cuplajul percepție-acțiune și transferul deciziei în meci, spre deosebire de drilurile izolate; e sinteză metodologică de referință, nu studiu empiric cu populație măsurată la 10–11 ani.
- **Sursă:** Renshaw I., Davids K., Newcombe D. J., Roberts W. M. (2019), *The Constraints-Led Approach: Principles for Sports Coaching and Practice Design*, Routledge. DOI `10.4324/9781315102351`.
- **Nivel epistemic:** MODERATE (carte de sinteză larg citată, nu date empirice proprii pentru U11 fotbal).
- **Aplicabilitate U11:** PARTIAL (sursă generală, extrapolare plauzibilă la 10–11 ani, netestată direct).

## Ghid de aplicare pe teren

- **Fidelitate reprezentativă:** Fiecare exercițiu conține cel puțin o minge, o direcție clară de atac/apărare, porți/zone țintă și un adversar activ.
- **Criteriu de decizie:** Jucătorul în posesie trebuie să aibă cel puțin două opțiuni tactice valide (ex: pasă vs. conducere/dribling).
- **Notă:** Numărul exact de stimuli simultani pe care copiii îi pot procesa nu este specificat de sursă — euristică practică ManualFC, nu prag validat științific.
