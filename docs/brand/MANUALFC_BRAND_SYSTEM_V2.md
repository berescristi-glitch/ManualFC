# ManualFC Brand System V2

Status: CANONICAL. Supersedes the shield/crest identity ("V1") in full, per **DEC-0080**.

## 1. Canonical master

- File: [`public/brand/manualfc/logo/manualfc-brand-master.png`](../../public/brand/manualfc/logo/manualfc-brand-master.png)
- 1714 × 918 px, flat RGB PNG (no alpha channel).
- Composition: a navy clipboard holding a football, with a gold-and-white "M" mark above a white "Manual" + gold "FC" wordmark, and the tagline **"ȘTIINȚĂ. PEDAGOGIE. PRACTICĂ."** beneath it.
- This file is the single source of truth. It was supplied as final artwork and must never be redrawn, reinterpreted, or recreated from memory in HTML/CSS/SVG.

## 2. Approved derivatives

All derivatives are produced only by crop / resize / format-convert of the master — never by redrawing, recoloring, or distorting. See [`logo-assets.json`](../../public/brand/manualfc/logo/logo-assets.json) for exact crop boxes and SHA-256 hashes of every file.

| Asset | Dimensions | Use |
|---|---|---|
| `manualfc-logo-full.png` | 1531×549 | Full lockup with tagline — footer, brand/marketing surfaces, source for the social image. |
| `manualfc-logo-horizontal.png` | 1531×400 | Mark + wordmark, no tagline — global header (compact horizontal space). |
| `manualfc-mark.png` | 479×479 | Square brand mark (clipboard + M + football) only — source for all icon/favicon sizes. |
| `manualfc-icon-512.png` / `manualfc-icon-192.png` | 512×512 / 192×192 | PWA manifest icons. |
| `manualfc-apple-touch-icon.png` | 180×180 | `<link rel="apple-touch-icon">`. |
| `manualfc-favicon-48/32/16.png` | 48×48 / 32×32 / 16×16 | `<link rel="icon">` set. |
| `manualfc-social.png` | 1200×630 | `og:image` / `twitter:image` share canvas (full lockup centered on the sampled brand background). |

Used via the `<ManualFCLogo variant="full" | "horizontal" | "mark" />` component ([`app/src/components/ManualFCLogo.astro`](../../app/src/components/ManualFCLogo.astro)), which renders the matching image with explicit width/height (no CLS) and no CSS-level recoloring or filtering.

## 3. What does NOT exist (and must not be invented)

- **No light-surface variant.** The master has a dark navy background baked into every derivative. There is no transparent, white-background, or "for light surfaces" version.
- **No inverted / white-on-transparent variant.** Do not auto-invert the logo in CSS or generate one.
- **No native vector (SVG) source.** All assets are raster PNGs traced back to the master photo/render.
- If a future surface genuinely needs a different treatment, that requires a new piece of *approved* source artwork, added deliberately (with its own decision record) — not an on-the-fly reinterpretation.

## 4. Brand colors

Sampled directly from the master artwork (not guessed):

| Token | Hex | Sampled from artwork | Notes |
|---|---|---|---|
| `--color-bg-brand` | `#010916` | `#010916` (40×40px corner-patch average) | **Corrected in TASK-3704** — see §5. |
| `--color-bg-brand-secondary` | `#1B263B` | — | Unchanged; a lighter navy step already used for secondary surfaces. |
| `--color-brand-gold` | `#F4C430` | ≈ `#F1C94F` (mark/wordmark gold) | Kept — close enough that changing it is not justified; no visible seam risk (gold never forms a background the logo sits on). |

## 5. Design tokens: corrected after visual proof (TASK-3704)

TASK-3701 originally judged the sampled artwork background (`≈#000A16`) close enough to the pre-existing `--color-bg-brand` (`#0D1B2A`) that no token change was made, to avoid unjustified platform-wide recoloring. **That judgment was wrong in practice.** Because every derivative PNG is a flat, opaque rectangle with the artwork's own background baked in, placing it on a header/footer that used the old `#0D1B2A` produced a visible rectangular seam — the logo read as a pasted sticker rather than an integrated mark. Confirmed by pixel sampling: header background `rgb(13,27,42)` vs. the logo image's own background `rgb(1,10,23)` at the boundary — a difference large enough to be clearly visible on screen.

**Fix:** `--color-bg-brand` was corrected to `#010916` (a 40×40px corner-patch average of the master artwork, not a single-pixel guess) in both `config/visual-tokens.json` and `app/src/styles/tokens.css`, plus every hardcoded `#0D1B2A` literal that represented the same "brand navy" background role (`HomepageHero.astro`, `design-system.astro`'s brand-lab swatches, `BaseLayout.astro`'s `theme-color` meta, `public/manifest.webmanifest`'s `theme_color`). `--color-text-primary` (which coincidentally shared the old `#0D1B2A` value for an unrelated role — body text on light backgrounds) was deliberately left untouched, as was the decorative ink color in `HeroBallFlight.astro`'s SVG (an outline on a light ball body, never adjacent to the brand-navy background). This remains a scoped, evidence-based correction of one background token to match the *already-approved* artwork exactly — not a platform re-theme; no other tokens changed, no artwork pixels touched.

## 6. Clear space & minimum sizes

- **Clear space**: keep a margin around any lockup at least half the height of the mark — no text or graphic element inside that margin.
- **Minimum size**: horizontal lockup no smaller than ~120px wide; mark no smaller than ~32px (below that, use the dedicated favicon derivatives instead of downscaling the mark further).

## 7. Do / Don't

**Do**
- Use the `ManualFCLogo` component with the correct `variant` for the available space.
- Preserve aspect ratio on every use (the component already sets explicit width/height).
- Treat the master PNG as read-only; regenerate derivatives from it if a new size is ever needed.

**Don't**
- Stretch, skew, or rotate the logo.
- Add drop shadows, gradients, glows, or recoloring on top of the logo artwork.
- Recreate the "M" / clipboard / football symbol using emoji, icon fonts, or hand-built SVG/CSS.
- Invent a light/inverted/monochrome variant.
- Reintroduce the previous shield/crest identity (fully removed — see §8).

## 8. Superseded identity (V1)

The previous identity — a navy shield/crest containing a gold "M" and a football, no clipboard, no tagline artwork baked in, separate `showTagline` text overlay in code — is fully retired. Its assets (`manualfc-logo-master.png`, `manualfc-mark-master.png`, `manualfc-logo-light-web.png`, `manualfc-logo-dark-web.png`, `manualfc-mark-web.png`, `manualfc-favicon-128.png`, `public/icons/icon-192.png`, `public/icons/icon-512.png`) have been deleted from the repository; zero code references remain. See `logo-assets.json`'s `superseded` block and **DEC-0080** for the record of this change.
