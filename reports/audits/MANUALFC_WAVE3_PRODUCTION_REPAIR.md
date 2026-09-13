# ManualFC — Wave-3 Production semantic repair

## Root cause

`BaseLayout.astro` already provided the primary `<main>`, while 15 public page shells independently used another `<main>`. EX-0001 exposed the defect during Phase-28 Gate A, but the pattern also affected other exercises, assessment, configurator, Field Cards, Gold Standard/index, volume indexes and chapter pages.

## Minimum repair

BaseLayout remains the sole landmark owner. Self-contained exercise/assessment/chapter documents now use `article`; index and tool shells use `div`. Classes, CSS selectors, anchors, content and interaction logic are unchanged.

## Regression guard

`scripts/validate_html_landmarks.py` parses built output. `tests/test_html_landmarks.py` proves that one main passes and nested/multiple main fails.

## Local evidence

- source audit: only `BaseLayout.astro` contains `<main>`;
- build: 83 pages;
- semantic validator: 83/83 documents, main=1, nested_main=0;
- tests: 437/437;
- strict content validator: 0 errors/warnings;
- project validator: 0 errors/warnings;
- registry: 228 reproducible tasks;
- Astro check: 78 files, 0/0/0;
- EX-0001 browser 1440/1280/768/390: main=1, nested=0, no overflow, 0 page errors;
- axe WCAG A/AA: 0 confirmed violations; automatic contrast checks remain incomplete for logo/SVG nodes only.

The repaired/final baseline is not frozen until a clean deployed Preview passes live browser audit.
