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
  assert.equal(files.length, 101, "the audited route inventory changed");

  for (const file of files) {
    const html = await readFile(file, "utf8");
    assert.equal((html.match(/<main(?:\s|>)/g) ?? []).length, 1, `${file}: main count`);
    assert.equal((html.match(/<h1(?:\s|>)/g) ?? []).length, 1, `${file}: h1 count`);
  }
});
