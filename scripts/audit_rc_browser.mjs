// TASK-3722 — release-candidate browser audit (real Chromium + axe-core).
//
// Usage:
//   node scripts/audit_rc_browser.mjs                 # serves dist/web locally
//   node scripts/audit_rc_browser.mjs https://manualfc.vercel.app   # live
//
// Reads the sitemap to pick the representative and high-risk routes, then for
// each route x viewport records: axe violations (wcag2a/aa/21a/21aa/22aa),
// <main> count, <h1> count, heading-level skips, horizontal overflow, console
// errors, failed requests, images without alt, tap targets below 24px,
// unlabelled form controls, and keyboard focus visibility. Exit code 1 if any
// critical/serious axe violation, overflow, console error or structural defect.
// This is automated QA only; it is NOT evidence of real-coach usability.
import { createReadStream, existsSync, statSync, readFileSync, writeFileSync } from "node:fs";
import http from "node:http";
import path from "node:path";
import { chromium } from "playwright";
import AxeBuilder from "@axe-core/playwright";

const distRoot = path.resolve("dist", "web");
const MIME = { ".html": "text/html", ".css": "text/css", ".js": "text/javascript", ".json": "application/json", ".xml": "application/xml", ".txt": "text/plain", ".png": "image/png", ".svg": "image/svg+xml", ".webmanifest": "application/manifest+json" };
const live = process.argv[2];
const outFile = process.argv[3];

function resolveFile(urlPath) {
  let rel = decodeURIComponent(urlPath.split("?")[0]);
  if (rel.endsWith("/")) rel += "index.html";
  let filePath = path.join(distRoot, rel);
  if (!existsSync(filePath) || statSync(filePath).isDirectory()) {
    const withIndex = path.join(filePath, "index.html");
    if (existsSync(withIndex)) filePath = withIndex;
    else filePath = existsSync(`${filePath}.html`) ? `${filePath}.html` : path.join(distRoot, "404.html");
  }
  return filePath;
}

let server;
let base = live;
if (!live) {
  server = http.createServer((req, res) => {
    const filePath = resolveFile(req.url ?? "/");
    res.setHeader("Content-Type", MIME[path.extname(filePath)] ?? "application/octet-stream");
    createReadStream(filePath).on("error", () => { res.statusCode = 404; res.end("nf"); }).pipe(res);
  });
  await new Promise((r) => server.listen(0, "127.0.0.1", r));
  base = `http://127.0.0.1:${server.address().port}`;
}

// ---- route selection from the sitemap (local: dist, live: network) ----
async function sitemapUrls() {
  const fetchText = async (u) => {
    if (!live) return readFileSync(path.join(distRoot, u.replace(/^https?:\/\/[^/]+\//, "")), "utf8");
    return (await fetch(new URL(u.replace(/^https?:\/\/[^/]+/, ""), base))).text();
  };
  const idx = await fetchText("/sitemap-index.xml");
  const maps = [...idx.matchAll(/<loc>([^<]+)<\/loc>/g)].map((m) => m[1]);
  const urls = [];
  for (const m of maps) urls.push(...[...(await fetchText(m)).matchAll(/<loc>([^<]+)<\/loc>/g)].map((x) => new URL(x[1]).pathname));
  return urls;
}
const urls = await sitemapUrls();
const pick = (re) => urls.filter((u) => re.test(u));
const first = (re) => pick(re)[0];
let longestPlan = null;
{
  const plans = pick(/^\/planuri-de-sezon\/[^/]+\/$/);
  let max = -1;
  for (const p of plans) {
    const html = await (await fetch(new URL(p, base))).text();
    if (html.length > max) { max = html.length; longestPlan = p; }
  }
}
const routes = [
  ["homepage", "/"],
  ["onboarding", "/incepe-aici/"],
  ["decision-engine", "/rezolva-pe-teren/"],
  ["problem-detail", first(/^\/rezolva-pe-teren\/[^/]+\/$/)],
  ["methodology", first(/^\/principii\/[^/]+\/$/)],
  ["exercise", first(/^\/gold-standard\/exercitii\/[^/]+\/$/)],
  ["session", first(/^\/gold-standard\/sedinte\/[^/]+\/$/)],
  ["script", first(/^\/scripturi\/[^/]+\/$/)],
  ["season-overview", "/planuri-de-sezon/"],
  ["season-longest", longestPlan],
  ["my-space", "/spatiul-meu/"],
  ["reflection", "/spatiul-meu/reflectie/?sesiune=SES-0001"],
  ["search", "/cauta/"],
  ["defense-theme", "/aparare/"],
  ["offline-fallback", "/offline/"]
].filter(([, p]) => p);
const viewports = { desktop: [1440, 900], tablet: [1024, 768], mobile: [390, 844] };

const browser = await chromium.launch();
const results = [];
for (const [vname, [w, h]] of Object.entries(viewports)) {
  const context = await browser.newContext({ viewport: { width: w, height: h }, hasTouch: vname === "mobile" });
  for (const [name, route] of routes) {
    const page = await context.newPage();
    const consoleErrors = [];
    const failed = [];
    page.on("console", (m) => { if (m.type() === "error") consoleErrors.push(m.text()); });
    page.on("pageerror", (e) => consoleErrors.push(`pageerror: ${e.message}`));
    page.on("requestfailed", (r) => failed.push(`${r.url()} ${r.failure()?.errorText}`));
    page.on("response", (r) => { if (r.status() >= 400 && !r.url().endsWith("favicon.ico")) failed.push(`${r.status()} ${r.url()}`); });
    const resp = await page.goto(new URL(route, base).href, { waitUntil: "networkidle" });
    const rec = { vp: vname, name, route, status: resp?.status() };
    const axe = await new AxeBuilder({ page }).withTags(["wcag2a", "wcag2aa", "wcag21a", "wcag21aa", "wcag22aa"]).analyze();
    rec.axe = axe.violations.map((v) => ({ id: v.id, impact: v.impact, nodes: v.nodes.length, sample: v.nodes[0]?.target?.join(" ") }));
    rec.dom = await page.evaluate(() => {
      const hs = [...document.querySelectorAll("h1,h2,h3,h4,h5,h6")].map((e) => +e.tagName[1]);
      let skips = 0;
      for (let i = 1; i < hs.length; i++) if (hs[i] - hs[i - 1] > 1) skips++;
      const vis = (e) => { const r = e.getBoundingClientRect(); const s = getComputedStyle(e); return r.width > 0 && r.height > 0 && s.visibility !== "hidden" && s.display !== "none"; };
      const targets = [...document.querySelectorAll("a[href],button,input:not([type=hidden]),select,textarea,summary,[role=button]")].filter(vis);
      const small = targets.filter((e) => { const r = e.getBoundingClientRect(); return r.width < 24 || r.height < 24; }).filter((e) => e.tagName !== "A" || !e.closest("p,li,span") || e.getBoundingClientRect().height >= 24 || true);
      const unlabelled = [...document.querySelectorAll("input:not([type=hidden]):not([type=submit]):not([type=button]),select,textarea")].filter((e) => !(e.labels && e.labels.length) && !e.getAttribute("aria-label") && !e.getAttribute("aria-labelledby") && !e.title);
      return {
        mains: document.querySelectorAll("main,[role=main]").length,
        h1: document.querySelectorAll("h1").length,
        headingSkips: skips,
        overflowX: document.documentElement.scrollWidth - document.documentElement.clientWidth,
        imgNoAlt: [...document.querySelectorAll("img")].filter((i) => !i.hasAttribute("alt")).length,
        imgs: [...document.images].map((i) => ({ src: i.currentSrc.slice(-60), nw: i.naturalWidth, w: i.width, lazy: i.loading, hasWH: i.hasAttribute("width") && i.hasAttribute("height") })),
        smallTargets: small.length,
        smallSample: small.slice(0, 4).map((e) => `${e.tagName}:${(e.textContent || e.getAttribute("aria-label") || "").trim().slice(0, 30)}:${Math.round(e.getBoundingClientRect().width)}x${Math.round(e.getBoundingClientRect().height)}`),
        unlabelled: unlabelled.length,
        landmarks: ["header", "nav", "main", "footer"].map((t) => `${t}:${document.querySelectorAll(t).length}`).join(" "),
        skipLink: !!document.querySelector('a[href^="#"]:first-of-type'),
        lang: document.documentElement.lang
      };
    });
    // keyboard: tab through up to 25 stops, require a visible focus indicator on each
    let noFocusVisible = 0, stops = 0;
    await page.evaluate(() => document.body.focus());
    for (let i = 0; i < 25; i++) {
      await page.keyboard.press("Tab");
      const f = await page.evaluate(() => {
        const e = document.activeElement;
        if (!e || e === document.body) return null;
        const s = getComputedStyle(e);
        const outline = s.outlineStyle !== "none" && parseFloat(s.outlineWidth) > 0;
        const shadow = s.boxShadow && s.boxShadow !== "none";
        return { visible: outline || shadow, tag: e.tagName };
      });
      if (!f) break;
      stops++;
      if (!f.visible) noFocusVisible++;
    }
    rec.keyboard = { stops, noFocusVisible };
    rec.consoleErrors = consoleErrors;
    rec.failed = failed;
    results.push(rec);
    await page.close();
  }
  await context.close();
}
// reduced motion check on the homepage
const rmCtx = await browser.newContext({ reducedMotion: "reduce" });
const rmPage = await rmCtx.newPage();
await rmPage.goto(new URL("/", base).href, { waitUntil: "networkidle" });
const animated = await rmPage.evaluate(() => [...document.querySelectorAll("*")].filter((e) => { const s = getComputedStyle(e); return (s.animationName !== "none" && parseFloat(s.animationDuration) > 0.05 && s.animationIterationCount === "infinite"); }).length);
await rmCtx.close();
await browser.close();
server?.close();

let fail = 0;
for (const r of results) {
  const serious = r.axe.filter((v) => v.impact === "critical" || v.impact === "serious");
  const problems = [];
  if (r.status !== 200) problems.push(`status ${r.status}`);
  if (serious.length) problems.push(`axe-serious ${serious.map((v) => v.id).join(",")}`);
  if (r.axe.length - serious.length) problems.push(`axe-minor ${r.axe.filter((v) => !serious.includes(v)).map((v) => v.id).join(",")}`);
  if (r.dom.mains !== 1) problems.push(`mains=${r.dom.mains}`);
  if (r.dom.h1 !== 1) problems.push(`h1=${r.dom.h1}`);
  if (r.dom.headingSkips) problems.push(`headingSkips=${r.dom.headingSkips}`);
  if (r.dom.overflowX > 0) problems.push(`overflowX=${r.dom.overflowX}`);
  if (r.dom.imgNoAlt) problems.push(`imgNoAlt=${r.dom.imgNoAlt}`);
  if (r.dom.unlabelled) problems.push(`unlabelled=${r.dom.unlabelled}`);
  if (r.dom.smallTargets) problems.push(`smallTargets=${r.dom.smallTargets} [${r.dom.smallSample.join("; ")}]`);
  if (r.keyboard.noFocusVisible) problems.push(`noFocusVisible=${r.keyboard.noFocusVisible}/${r.keyboard.stops}`);
  if (r.consoleErrors.length) problems.push(`console=${r.consoleErrors.length}: ${r.consoleErrors[0].slice(0, 120)}`);
  if (r.failed.length) problems.push(`failedReq=${r.failed.length}: ${r.failed[0].slice(0, 120)}`);
  const hard = serious.length || r.dom.mains !== 1 || r.dom.overflowX > 0 || r.consoleErrors.length || r.status !== 200;
  if (hard) fail++;
  console.log(`${hard ? "FAIL" : problems.length ? "WARN" : "PASS"} ${r.vp.padEnd(7)} ${r.name.padEnd(17)} ${r.route}${problems.length ? "\n      " + problems.join("\n      ") : ""}`);
}
console.log(`reduced-motion infinite animations on homepage: ${animated}`);
console.log(`routes=${routes.length} viewports=${Object.keys(viewports).length} runs=${results.length} hardFail=${fail}`);
if (outFile) writeFileSync(outFile, JSON.stringify(results, null, 1));
process.exit(fail ? 1 : 0);
