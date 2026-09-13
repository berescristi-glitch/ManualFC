# Clasificarea rutelor de producție

## Contract

Astro generează ca suprafață publică numai fișierele din `app/src/pages`. Laboratoarele și fixture-urile vizuale sunt păstrate în `app/src/internal-pages`: pot fi citite, testate și mutate temporar într-un harness dedicat, dar nu intră accidental în buildul public.

| Familie | Clasificare | Motiv |
|---|---|---|
| `/`, `/incepe-aici`, `/volum/**` | public editorial | intrări și curriculum canonic |
| `/principii`, `/principii/{slug canonic}` | public aplicat | cele 25 de principii de producție; fixture-ul este exclus de loader |
| `/gold-standard/**` | public aplicat | sistemul validat pentru pilot de teren |
| `/404` | sistem public | stare necesară pentru rute inexistente |
| `/design-system` | intern | laborator de brand/UI, nu conținut editorial |
| `/fixture-mdx` | intern | probă de compilare MDX |
| `/exercitii/2v1-unghi-de-suport` | intern | entitate fixture neutră, înlocuită public de exercițiile Gold Standard |
| `/probleme/lipsa-unghi-de-pasa` | intern | demonstrație tehnică Mode B, nu Problem Engine public |
| `/principii/orientare-corporala-scanare` | intern | fixture de integrare; filtrat explicit din `getStaticPaths` |

## Reguli de menținere

1. Un fișier din `internal-pages` nu este importat sau legat de navigarea publică.
2. Datele cu `development_fixture: true` pot rămâne în adaptoarele de test, dar nu primesc rută publică.
3. Orice rută nouă declară explicit una dintre clasele `public editorial`, `public aplicat`, `sistem public` sau `intern`.
4. Buildul de acceptanță verifică atât rutele publice critice, cât și absența celor cinci outputuri interne.
5. `npm run build` curăță numai ținta explicită `dist/web` înaintea generării, astfel încât fișierele unor rute retrase nu supraviețuiesc ca output stagnant.

Această separare nu șterge fixture-uri și nu transformă laboratorul într-o capabilitate de produs promisă.
