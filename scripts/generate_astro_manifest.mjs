import { readdirSync, writeFileSync } from 'node:fs';
import { resolve, sep } from 'node:path';

// TASK-2805: the service worker (public/sw.js) is a static file, not processed
// by Vite, so it cannot import the build's hashed /_astro/* filenames directly.
// This manifest lets it precache them deterministically instead of relying on
// a page having been visited online first (see docs/architecture/OFFLINE_ACCOUNT_ENTITLEMENT.md).
const astroDir = resolve('dist', 'web', '_astro');
const expectedSuffix = `${sep}dist${sep}web${sep}_astro`;
if (!astroDir.endsWith(expectedSuffix)) {
  throw new Error(`Refuz generarea manifestului pentru un director neașteptat: ${astroDir}`);
}

const files = readdirSync(astroDir).filter((f) => !f.startsWith('.'));
const routes = files.map((f) => `/_astro/${f}`).sort();

writeFileSync(
  resolve('dist', 'web', 'astro-assets-manifest.json'),
  JSON.stringify({ routes }, null, 2) + '\n'
);
