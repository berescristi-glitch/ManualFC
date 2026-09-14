import assert from "node:assert/strict";
import { createReadStream, existsSync, statSync } from "node:fs";
import http from "node:http";
import path from "node:path";
import { after, before, test } from "node:test";
import { chromium } from "playwright";
import AxeBuilder from "@axe-core/playwright";

// Real-browser + accessibility smoke test (TASK-3711). Serves the already
// built `dist/web` static output (run `npm run build` first, same
// precondition as tests/web/built-routes.test.js) and drives an actual
// Chromium instance via Playwright — no jsdom, no HTML-string assertions.

const distRoot = path.resolve("dist", "web");
const MIME = { ".html": "text/html", ".css": "text/css", ".js": "text/javascript", ".json": "application/json", ".xml": "application/xml", ".txt": "text/plain", ".png": "image/png", ".svg": "image/svg+xml", ".webmanifest": "application/manifest+json" };

function resolveFile(urlPath) {
  let rel = decodeURIComponent(urlPath.split("?")[0]);
  if (rel.endsWith("/")) rel += "index.html";
  let filePath = path.join(distRoot, rel);
  if (!existsSync(filePath) || statSync(filePath).isDirectory()) {
    const withIndex = path.join(filePath, "index.html");
    if (existsSync(withIndex)) filePath = withIndex;
    else {
      const withHtml = `${filePath}.html`;
      filePath = existsSync(withHtml) ? withHtml : path.join(distRoot, "404.html");
    }
  }
  return filePath;
}

let server;
let baseURL;
let browser;
let context;
let page;

before(async () => {
  assert.ok(existsSync(distRoot), `dist/web missing — run "npm run build" before "npm test" (looked in ${distRoot})`);

  server = http.createServer((req, res) => {
    const filePath = resolveFile(req.url ?? "/");
    const ext = path.extname(filePath);
    res.setHeader("Content-Type", MIME[ext] ?? "application/octet-stream");
    createReadStream(filePath)
      .on("error", () => { res.statusCode = 404; res.end("Not found"); })
      .pipe(res);
  });
  await new Promise((resolve) => server.listen(0, "127.0.0.1", resolve));
  const { port } = server.address();
  baseURL = `http://127.0.0.1:${port}`;

  browser = await chromium.launch();
  // @axe-core/playwright opens auxiliary pages within the same context (to
  // inject its script tag); a page created via the browser.newPage() shortcut
  // owns its context exclusively and rejects that with "Please use
  // browser.newContext()", so create the context explicitly instead.
  context = await browser.newContext();
  page = await context.newPage();
});

after(async () => {
  await page?.close();
  await context?.close();
  await browser?.close();
  await new Promise((resolve) => server.close(resolve));
});

test("homepage loads with exactly one main and one h1", async () => {
  const response = await page.goto(`${baseURL}/`, { waitUntil: "load" });
  assert.equal(response.status(), 200);
  assert.equal(await page.locator("main").count(), 1, "expected exactly one <main>");
  assert.equal(await page.locator("h1").count(), 1, "expected exactly one <h1>");
});

test('the "Rezolvă pe teren" CTA in the header routes to /rezolva-pe-teren', async () => {
  await page.goto(`${baseURL}/`, { waitUntil: "load" });
  await page.getByRole("link", { name: "Rezolvă pe teren", exact: true }).first().click();
  await page.waitForLoadState("load");
  const url = new URL(page.url());
  const normalized = url.pathname.endsWith("/") ? url.pathname : `${url.pathname}/`;
  assert.equal(normalized, "/rezolva-pe-teren/", `expected /rezolva-pe-teren/, got ${url.pathname}`);
  assert.equal(await page.locator("h1").count(), 1, "expected exactly one <h1> on the destination page");
});

const criticalPages = ["/", "/incepe-aici/", "/rezolva-pe-teren/", "/volum/", "/principii/", "/gold-standard/"];

for (const route of criticalPages) {
  test(`axe finds no violations on ${route}`, async () => {
    await page.goto(`${baseURL}${route}`, { waitUntil: "load" });
    const results = await new AxeBuilder({ page }).analyze();
    const summary = results.violations.map((v) => `${v.id} (${v.impact}): ${v.nodes.length} node(s) — ${v.help}`);
    assert.deepEqual(summary, [], `axe violations on ${route}:\n${summary.join("\n")}`);
  });
}
