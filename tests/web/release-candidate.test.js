import assert from "node:assert/strict";
import { createReadStream, existsSync, statSync } from "node:fs";
import http from "node:http";
import path from "node:path";
import { after, before, test } from "node:test";
import { chromium } from "playwright";

// TASK-3722 regression coverage (real Chromium against the built `dist/web`):
//  1. no horizontal page overflow at tablet/laptop widths (10-item header nav);
//  2. tampered localStorage cannot produce a live `javascript:` link;
//  3. a page visited as `/x/` is available offline as `/x` and vice versa.
// Same precondition as the other web tests: run `npm run build` first.

const distRoot = path.resolve("dist", "web");
const MIME = { ".html": "text/html", ".css": "text/css", ".js": "text/javascript", ".json": "application/json", ".xml": "application/xml", ".txt": "text/plain", ".png": "image/png", ".svg": "image/svg+xml", ".webmanifest": "application/manifest+json" };

function resolveFile(urlPath) {
  let rel = decodeURIComponent(urlPath.split("?")[0]);
  if (rel.endsWith("/")) rel += "index.html";
  let filePath = path.join(distRoot, rel);
  if (!existsSync(filePath) || statSync(filePath).isDirectory()) {
    const withIndex = path.join(filePath, "index.html");
    filePath = existsSync(withIndex) ? withIndex : path.join(distRoot, "404.html");
  }
  return filePath;
}

let server;
let baseURL;
let browser;

before(async () => {
  assert.ok(existsSync(distRoot), `dist/web missing — run "npm run build" first (looked in ${distRoot})`);
  server = http.createServer((req, res) => {
    const filePath = resolveFile(req.url ?? "/");
    res.setHeader("Content-Type", MIME[path.extname(filePath)] ?? "application/octet-stream");
    createReadStream(filePath).on("error", () => { res.statusCode = 404; res.end("Not found"); }).pipe(res);
  });
  await new Promise((resolve) => server.listen(0, "127.0.0.1", resolve));
  baseURL = `http://127.0.0.1:${server.address().port}`;
  browser = await chromium.launch();
});

after(async () => {
  await browser?.close();
  await new Promise((resolve) => server.close(resolve));
});

const OVERFLOW_ROUTES = ["/", "/incepe-aici/", "/spatiul-meu/", "/planuri-de-sezon/PLAN-0004/", "/gold-standard/sedinte/SES-0001/", "/offline/"];
for (const width of [1440, 1280, 1100, 1024, 900, 768, 390]) {
  test(`no horizontal overflow at ${width}px on key routes`, async () => {
    const context = await browser.newContext({ viewport: { width, height: 800 } });
    try {
      for (const route of OVERFLOW_ROUTES) {
        const page = await context.newPage();
        await page.goto(new URL(route, baseURL).href, { waitUntil: "networkidle" });
        const overflow = await page.evaluate(() => document.documentElement.scrollWidth - document.documentElement.clientWidth);
        assert.equal(overflow, 0, `${route} overflows by ${overflow}px at ${width}px`);
        await page.close();
      }
    } finally {
      await context.close();
    }
  });
}

test("header navigation keeps every link visible at 1024px", async () => {
  const context = await browser.newContext({ viewport: { width: 1024, height: 800 } });
  const page = await context.newPage();
  await page.goto(baseURL + "/", { waitUntil: "networkidle" });
  const hidden = await page.evaluate(() => {
    const W = document.documentElement.clientWidth;
    return [...document.querySelectorAll(".main-nav a")].filter((a) => { const r = a.getBoundingClientRect(); return r.width === 0 || r.right > W || r.left < 0; }).map((a) => a.textContent);
  });
  assert.deepEqual(hidden, []);
  await context.close();
});

test("tampered localStorage refs never render a javascript: or protocol-relative link", async () => {
  const context = await browser.newContext();
  const page = await context.newPage();
  const dialogs = [];
  page.on("dialog", (d) => { dialogs.push(d.message()); d.dismiss(); });
  await page.goto(baseURL + "/", { waitUntil: "networkidle" });
  await page.evaluate(() => {
    const bad = (id, href) => ({ id, kind: "exercise", title: `T-${id}`, href });
    localStorage.setItem("manualfc.coach-state.v1", JSON.stringify({
      version: 1, profile: { experience: "incepator", defaultPlayers: 12, defaultDuration: 75, onboardingDone: true },
      saved: [bad("EX-0001", "javascript:alert(1)"), bad("EX-0002", "//evil.example/x"), bad("EX-0003", "/gold-standard/exercitii/EX-0003/")],
      favorites: [bad("EX-0004", "data:text/html,<script>alert(1)</script>")],
      recents: [{ ...bad("EX-0005", "JaVaScRiPt:alert(1)"), visitedAt: new Date().toISOString() }],
      sessions: [], reflections: [], offlinePacks: []
    }));
  });
  await page.goto(baseURL + "/spatiul-meu/", { waitUntil: "networkidle" });
  const hrefs = await page.evaluate(() => [...document.querySelectorAll("[data-saved] a, [data-favorites] a, [data-recents] a")].map((a) => a.getAttribute("href")));
  assert.deepEqual(hrefs, ["/gold-standard/exercitii/EX-0003/"], "only the same-origin path survives sanitisation");
  assert.deepEqual(dialogs, []);
  await context.close();
});

test("offline: page visited with a trailing slash is found without it, and vice versa", async () => {
  const context = await browser.newContext();
  const page = await context.newPage();
  await page.goto(baseURL + "/", { waitUntil: "networkidle" });
  await page.evaluate(() => navigator.serviceWorker.ready);
  await page.waitForTimeout(2500);
  await page.reload({ waitUntil: "networkidle" });
  await page.goto(baseURL + "/principii/", { waitUntil: "networkidle" });
  await page.goto(baseURL + "/incepe-aici", { waitUntil: "networkidle" });
  await context.setOffline(true);
  for (const route of ["/principii/", "/principii", "/incepe-aici", "/incepe-aici/"]) {
    await page.goto(baseURL + route, { waitUntil: "domcontentloaded" });
    const title = await page.title();
    assert.ok(!/Fără conexiune/.test(title), `${route} fell back to the offline page although it was visited online`);
  }
  // a never-visited route still gets the honest fallback, not a browser error
  await page.goto(baseURL + "/planuri-de-sezon/PLAN-0004/", { waitUntil: "domcontentloaded" });
  assert.match(await page.title(), /Fără conexiune/);
  await context.close();
});
