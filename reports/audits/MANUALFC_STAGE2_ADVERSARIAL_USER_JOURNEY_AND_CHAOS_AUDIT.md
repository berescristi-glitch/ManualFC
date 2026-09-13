# ManualFC — Stage 2 Adversarial User Journey and Chaos Audit

## Verdict

`PASS_WITH_DECLARED_CROSS_BROWSER_LIMITATION`, 2026-08-31.

Chromium real a trecut 52 combinații (13 rute × 1440/1280/768/390), cu `main=1`, `h1=1`, zero overflow, zero erori de consolă și zero violări Axe pe eșantionul reprezentativ. Reduced-motion a fost activ în matrice.

## Journeys și stări ostile

- stare localStorage coruptă: pagina rămâne vizibilă, fără erori;
- două taburi: modificarea stării este observată în al doilea tab;
- fără pregătire offline: fallback-ul intenționat „Fără conexiune” răspunde 200;
- după „Pregătește pentru teren”: Service Worker activ, cache-urile shell/pack prezente, badge persistent, cold reload offline al Field Mode răspunde 200;
- Field Mode: un singur H1, timerul ajunge la `00:01`, iar „următorul” mută segmentul la 2;
- toate cele 101 pagini construite au fost crawl-uite static: zero referințe interne rupte.

## Defecte reparate

- `INT-0008` (MAJOR): Field Mode avea șase H1; titlu de pagină unic și H2 pe segmente.
- `INT-0009` (MAJOR): două combinații de contrast pe homepage; retest Axe zero.

## Limite

Firefox și WebKit sunt `NOT_RUN`: executabilele Playwright nu sunt instalate. Auditul npm este `NOT_RUN_POLICY_BLOCKED`: exportul metadatelor dependențelor către registrul public nu a fost autorizat explicit.
