import assert from "node:assert/strict";
import { readdir, readFile } from "node:fs/promises";
import path from "node:path";
import test from "node:test";

const distRoot = path.resolve("dist");

async function htmlFiles(directory) {
  const entries = await readdir(directory, { withFileTypes: true });
  const nested = await Promise.all(entries.map(async (entry) => {
    const absolute = path.join(directory, entry.name);
    return entry.isDirectory()
      ? htmlFiles(absolute)
      : entry.name.endsWith(".html") ? [absolute] : [];
  }));
  return nested.flat();
}

test("built route inventory is complete and every page has one main and one h1", async () => {
  const files = await htmlFiles(distRoot);
  // TASK-3712: +18 pages from 10 new Gold Standard exercises (EX-0006-EX-0015)
  // and 4 new sessions (SES-0003-SES-0006, each with a normal page + a
  // mod-teren page): 101 + 10 + 4*2 = 119.
  // TASK-3718: +20 pages for the second training theme (apararea-presiune-si-acoperire):
  // 10 new exercises (EX-0016-EX-0025), 4 new sessions (SES-0007-SES-0010, each with a
  // normal page + a mod-teren page), 1 new assessment (ASM-0002), and 1 new theme
  // identity page (/aparare/): 119 + 10 + 4*2 + 1 + 1 = 139.
  // TASK-3719: +27 pages for the communication-scripts content pillar: 26 script
  // detail pages (SCR-0001-SCR-0026) plus 1 browse index (/scripturi/): 139 + 27 = 166.
  assert.equal(files.length, 166, "the audited route inventory changed");

  for (const file of files) {
    const html = await readFile(file, "utf8");
    assert.equal((html.match(/<main(?:\s|>)/g) ?? []).length, 1, `${file}: main count`);
    assert.equal((html.match(/<h1(?:\s|>)/g) ?? []).length, 1, `${file}: h1 count`);
  }
});
