# Multimedia Foundation — TASK-2711

## Scop explicit: fundație, nu bibliotecă completă

Acest task NU produce multimedia pentru toate cele 5 exerciții sau pentru principii. Produce: standardul pe niveluri, arhitectura reutilizabilă, un prototip real la Nivelul 1 și pipeline-ul documentat pentru extindere ulterioară. Restul rămâne backlog explicit, nu simulat.

## Cele 5 niveluri

| Nivel | Ce este | Durată | Stare în acest task |
|---|---|---:|---|
| 1 — Buclă tactică | animație scurtă, în buclă, a unei singure decizii | 8–15s | **Prototip real livrat** — EX-0001, CSS/SVG |
| 2 — Animație de exercițiu | desfășurarea completă a exercițiului | 20–40s | Neînceput — necesită producție dedicată per exercițiu |
| 3 — Explicație de antrenor | voce + vizual, predare directă | 45–90s | Neînceput — necesită înregistrare audio/video reală |
| 4 — Exemplu real de teren | filmare reală, validată | — | Neînceput — necesită filmare reală, consimțământ, validare |
| 5 — Exemplu de transfer în meci | filmare de meci oficial | — | Neînceput — necesită filmare reală de meci |

Nivelurile 4–5 nu se fabrică niciodată sintetic — necesită material real, cu acordurile corespunzătoare. Acest task nu pretinde altfel.

## De ce CSS/SVG, nu fișier video

Nu există în acest repository niciun pipeline de producție video, nicio filmare, niciun instrument de randare externă. Un „prototip de buclă tactică" prezentat ca fișier video ar fi fost fie inventat, fie un fake. Nivelul 1 (`TacticalLoop.astro`) este o animație CSS/SVG reală, executabilă, testabilă în browser — nu o simulare a unui viitor video. Extinderea la Nivelurile 2+ necesită decizie separată de resurse (producție reală), nu doar mai mult cod.

## `TacticalLoop.astro` — cerințele Nivelului 1

Implementate, toate verificabile în browser:

- **fără sunet** — nu există element audio, deci „mut din start" e adevărat structural, nu doar setat;
- **buclă** — `animation-iteration-count: infinite`, 10s per ciclu (în intervalul 8–15s cerut);
- **pauză/redare** — buton funcțional, `aria-pressed` sincronizat, JS minimal vanilla (fără framework nou);
- **`prefers-reduced-motion`** — animația se dezactivă complet; elementul rămâne vizibil în starea finală (poziția corectă de sprijin), nu dispare și nu îngheață la jumătatea mișcării;
- **fallback static** — `TacticalDiagram` (Nivelul „static SVG" deja existent din Wave-1) rămâne pe pagină ca referință principală, imediat deasupra buclei;
- **descriere accesibilă** — `<title>`/`<desc>` SVG proprii, separate de diagrama statică.

## Pipeline documentat pentru extindere

```
date canonice (exercise-*.json)
  → specificație vizuală (deja text: step_by_step, rules, rationale)
  → SVG static (TacticalDiagram — Wave-1, 5/5 exerciții)
  → buclă animată CSS/SVG (TacticalLoop — Wave-2, 1/5 exerciții, prototip)
  → [decizie separată] export video / animație Nivel 2+
  → activ web optimizat
  → fallback de accesibilitate (poster static, descriere text, reduced-motion)
```

Fiecare pas reutilizează pasul anterior — nu există date paralele. Extinderea `TacticalLoop` la EX-0002–EX-0005 este mecanică (aceleași keyframes, coordonate diferite din SVG-ul static deja existent), dar rămâne neautorizată explicit în acest task pentru a păstra scopul de „fundație”, nu „bibliotecă completă”.
