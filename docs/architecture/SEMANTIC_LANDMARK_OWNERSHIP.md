# Semantic landmark ownership

`BaseLayout.astro` owns the single primary `<main id="main-content">` landmark for every generated product document. Page components render semantic descendants (`article` for a self-contained document, `section` for a thematic region, `div` for a layout/index shell) and must never add a second `main` or `role="main"`.

The build gate `python scripts/validate_html_landmarks.py` parses every generated HTML document and fails unless `main_count = 1` and `nested_main = 0`. This built-output check is authoritative because it validates Astro composition rather than isolated source files.
