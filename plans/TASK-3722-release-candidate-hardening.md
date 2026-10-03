# TASK-3722 — Hardening candidat de lansare și poartă de pregătire (Readiness Gate)

## 1. Titlu și scop

Rezultatul observabil: un verdict de pregătire justificat prin dovezi pentru ManualFC, plus remedierea exclusiv a defectelor P0/P1 reproductibile. Nu este un task de extindere de conținut.

## 2. Context pentru un cititor nou

- Repository canonic: `E:\ManualFC-clean`. Repository legacy `E:\ManualFC` — NU se atinge.
- Stare de pornire verificată: `main == origin/main == 21da05d3b47ce30ea5905610f19e889e972df265` (TASK-3721, DEC-0093), arbore curat.
- Produs: Astro static, patru sisteme de conținut (teme/metodologie, exerciții/ședințe, scripturi, planuri de sezon), local-first (`localStorage`), service worker, producție `https://manualfc.vercel.app/`.
- Nu există dovezi de teren (`TASK-3714 = BLOCKED`). Nicio verificare automată din acest task nu este tratată ca validare de teren.

## 3. Rezultatul verificabil

Raport `reports/task-reports/TASK-3722.md` cu matrice de pregătire completă, constatări, remedieri, rezultate local + fresh clone + producție și clasificarea de pregătire.

## 4. Domeniu și non-obiective

În scop: audit pe cele 9 arii din cerință; remedieri P0/P1 cu regresie.
În afara scopului: piloni noi de conținut, multi-vârstă, analytics, autentificare, baze de date, redesign, rescrierea guvernanței istorice, upgrade major forțat pentru vulnerabilități npm preexistente, alegerea unui domeniu de producție nou.

## 5. Matricea de pregătire (definită înainte de modificări)

Stări: V = verificat, PV = parțial verificat, NV = neverificat, B = blocat, OS = în afara scopului.

| Aria | Ce se verifică | Metodă | Stare inițială |
|---|---|---|---|
| 1 Flux antrenor | acasă→onboarding→principiu/DE→exercițiu/ședință→script→plan→reflecție→salvare→Spațiul meu; fundături, linkuri, back, etichete, stări goale, fără cont | Playwright pe build + inventar linkuri | NV |
| 2 Integritate conținut | ID unice, referințe, orfani, duplicate, câmpuri pedagogice, limite de dovezi, fără pretenții de validare reală, rute/etichete învechite | validatoare + script de integritate | NV |
| 3 Accesibilitate | axe + landmark/main/headings/tastatură/focus/etichete/dialog/touch/contrast/reduced-motion pe 12 pagini | Playwright+axe | NV |
| 4 Responsive | 1440/1024/390: overflow, clipping, diagrame, sticky, controale | Playwright | NV |
| 5 Performanță/build | install curat, build, nr. pagini, dimensiuni, JS critic, imagini, consolă, rețea, cache | build + măsurători | NV |
| 6 SEO | canonical, title/desc, OG, robots, sitemap, noindex, 404, trailing slash, domeniu | analiza dist + live | NV |
| 7 Offline/local-first | SW, acasă offline, rute vizitate, salvate, recente, reflecție, fără transmitere | Playwright offline | NV |
| 8 Securitate/confidențialitate | secrete, URL, third-party, date copii, scripturi externe, injecție HTML, rute dev, stocare | scan țintit | NV |
| 9 Producție | rute, sitemap/robots live, canonical/OG, axe live, responsive, offline, paritate sursă | fetch + Playwright pe URL live | NV |
| Teren real (pilot) | validare cu antrenori reali | — | B (TASK-3714), OS pentru acest task |

## 6. Politica de remediere

Doar P0/P1 reproductibile, în scop, sigure, cu test de regresie, re-validare și documentarea riscului. Commit-uri focalizate cu `TASK-3722`.

## 7. Jurnal de progres și descoperiri

- 4 defecte P1 remediate cu regresie (overflow nav, miss offline la slash, href javascript: din localStorage, obiecte git corupte). Productia e la d2c6c5a (TASK-3715): drift de deployment, fara deploy.

## 8. Decizii

(se completează în timpul execuției)

## 9. Rezultate

Vezi reports/task-reports/TASK-3722.md. Verdict PASS; clasificare READY FOR PRIVATE PILOT.
