// TASK-3722 — coach journey audit (real Chromium, real clicks, no account).
// HOME -> problem -> principle -> exercise/session -> script -> season plan ->
// reflection -> save -> "Spațiul meu". Usage:
//   node scripts/audit_rc_journey.mjs [https://live-url]
// Automated QA only; NOT evidence of real-coach usability.
import { createReadStream, existsSync, statSync } from "node:fs";
import http from "node:http";
import path from "node:path";
import { chromium } from "playwright";

const distRoot = path.resolve("dist", "web");
const MIME = { ".html": "text/html", ".css": "text/css", ".js": "text/javascript", ".json": "application/json", ".webmanifest": "application/manifest+json", ".png": "image/png", ".svg": "image/svg+xml" };
let server, base = process.argv[2];
if (!base) {
  server = http.createServer((req, res) => {
    let rel = decodeURIComponent((req.url ?? "/").split("?")[0]);
    if (rel.endsWith("/")) rel += "index.html";
    let f = path.join(distRoot, rel);
    if (!existsSync(f) || statSync(f).isDirectory()) f = existsSync(path.join(f, "index.html")) ? path.join(f, "index.html") : path.join(distRoot, "404.html");
    res.setHeader("Content-Type", MIME[path.extname(f)] ?? "application/octet-stream");
    createReadStream(f).pipe(res);
  });
  await new Promise((r) => server.listen(0, "127.0.0.1", r));
  base = `http://127.0.0.1:${server.address().port}`;
}

const problems = [];
const log = (ok, msg) => { console.log(`${ok ? "PASS" : "FAIL"} ${msg}`); if (!ok) problems.push(msg); };
const browser = await chromium.launch();
const ctx = await browser.newContext({ viewport: { width: 390, height: 844 }, hasTouch: true });
const page = await ctx.newPage();
const errors = [];
page.on("pageerror", (e) => errors.push(e.message));
page.on("console", (m) => { if (m.type() === "error") errors.push(m.text()); });
const h1 = async () => (await page.locator("h1").first().innerText()).replace(/\s+/g, " ").trim();
const onward = async () => page.evaluate(() => [...document.querySelectorAll("main a[href]")].map((a) => a.getAttribute("href")).filter((h) => h && h.startsWith("/")));
const go = async (href) => { const r = await page.goto(new URL(href, base).href, { waitUntil: "networkidle" }); return r?.status(); };
const clickFirst = async (selector, label) => {
  const loc = page.locator(selector).first();
  if (!(await loc.count())) { log(false, `${label}: no link matching ${selector} on ${page.url()}`); return false; }
  await Promise.all([page.waitForURL((u) => u.href !== page.url(), { timeout: 8000 }).catch(() => {}), loc.click()]);
  await page.waitForLoadState("networkidle");
  return true;
};

// 1. HOME -> primary CTA
await go("/");
const homeLinks = await onward();
log(homeLinks.some((h) => h.startsWith("/rezolva-pe-teren")), "home offers 'Rezolvă pe teren' entry");
log(homeLinks.some((h) => h.startsWith("/incepe-aici")), "home offers onboarding entry");
log(homeLinks.some((h) => h.startsWith("/planuri-de-sezon")), "home offers season-plan entry");
// 2. onboarding has onward routes
await go("/incepe-aici/");
log((await onward()).filter((h) => /^\/(rezolva|principii|planuri|scripturi|volum|gold)/.test(h)).length >= 3, "onboarding offers >=3 onward paths");
// 3. problem hub -> problem
await go("/rezolva-pe-teren/");
const probHref = await page.locator('main a[href^="/rezolva-pe-teren/"]').first().getAttribute("href");
await go(probHref);
const probTitle = await h1();
const probLinks = await onward();
const need = { principle: /^\/principii\/[^/]+\/?$/, exercise: /^\/gold-standard\/exercitii\//, session: /^\/gold-standard\/sedinte\//, script: /^\/scripturi\/[^/]+/, plan: /^\/planuri-de-sezon\/[^/]+/ };
for (const [k, re] of Object.entries(need)) log(probLinks.some((h) => re.test(h)), `problem "${probTitle}" links onward to ${k}`);
// 4. follow each onward type; each must be 200, have a way back to a problem or hub, and further onward links
const visited = {};
for (const [k, re] of Object.entries(need)) {
  const href = probLinks.find((h) => re.test(h));
  if (!href) continue;
  const status = await go(href);
  const links = await onward();
  visited[k] = { href, links };
  log(status === 200 && links.length >= 2, `${k} ${href} -> ${status}, ${links.length} onward links`);
  log(links.some((h) => h.startsWith("/rezolva-pe-teren/")), `${k} page links back to a problem`);
}
// 5. session -> reflection with context
const sesHref = visited.session?.href;
if (sesHref) {
  await go(sesHref);
  const refl = (await onward()).find((h) => h.startsWith("/spatiul-meu/reflectie"));
  log(!!refl, "session page links to reflection");
  if (refl) {
    await go(refl);
    const ctx1 = await page.locator("[data-reflection-context], .refl-ctx-session, .refl-ctx-problem, #context, [data-context]").first().innerText().catch(() => "");
    log(/./.test(await h1()), `reflection opens (${refl}); context text length ${ctx1.length}`);
    // fill the form with the first radio/checkbox per group and submit
    const radios = page.locator('input[type="radio"]');
    const n = await radios.count();
    const groups = new Set();
    for (let i = 0; i < n; i++) {
      const name = await radios.nth(i).getAttribute("name");
      if (groups.has(name)) continue;
      groups.add(name);
      await radios.nth(i).evaluate((el) => (el.closest("label") ?? el).click()); // inputs may be visually hidden behind a styled label
    }
    const labelled = await page.evaluate(() => [...document.querySelectorAll("input,select,textarea")].filter((e) => e.type !== "hidden" && !(e.labels && e.labels.length) && !e.getAttribute("aria-label")).length);
    log(labelled === 0, "reflection form controls are all labelled");
    await page.locator('button[type="submit"], button.save').first().click();
    await page.waitForTimeout(600);
  }
}
// 6. save an exercise and return via Spatiul meu
if (visited.exercise) {
  await go(visited.exercise.href);
  await page.locator("[data-save]").first().click();
  await page.waitForTimeout(300);
  log((await page.locator("[data-save]").first().getAttribute("aria-pressed")) === "true", "save button reflects saved state (aria-pressed)");
}
if (visited.script) await go(visited.script.href);
if (visited.plan) await go(visited.plan.href);
await go("/spatiul-meu/");
await page.waitForTimeout(400);
const saved = await page.locator("[data-saved]").innerText();
const recents = await page.locator("[data-recents]").innerText();
const reflections = await page.locator("[data-reflections]").innerText();
log(/EXERCIȚIU/i.test(saved), `Spațiul meu 'Salvate' shows typed entry: ${saved.replace(/\s+/g, " ").slice(0, 80)}`);
log(/SCRIPT/i.test(recents) && /PLAN/i.test(recents), `Spațiul meu 'Recente' shows typed script + plan entries: ${recents.replace(/\s+/g, " ").slice(0, 120)}`);
log(!/Nicio reflecție încă/.test(reflections), `reflection appears in Spațiul meu: ${reflections.replace(/\s+/g, " ").slice(0, 80)}`);
// 7. empty state is actionable (fresh context)
const ctx2 = await browser.newContext();
const p2 = await ctx2.newPage();
await p2.goto(new URL("/spatiul-meu/", base).href, { waitUntil: "networkidle" });
const empties = await p2.locator(".empty").allInnerTexts();
log(empties.length >= 3 && empties.every((t) => /„|folosește|deschide|marchează|adaugă|construiește|automat/i.test(t)), `empty states name a concrete action (${empties.length})`);
const emptyActionLinks = await p2.evaluate(() => [...document.querySelectorAll("main a[href]")].map((a) => a.getAttribute("href")).filter((h) => h.startsWith("/")).length);
log(emptyActionLinks >= 2, `empty Spațiul meu still has onward links (${emptyActionLinks})`);
// 8. browser Back keeps context
await page.goto(new URL("/rezolva-pe-teren/", base).href, { waitUntil: "networkidle" });
await go(probHref);
await go(visited.principle?.href ?? "/principii/");
await page.goBack({ waitUntil: "networkidle" });
log(new URL(page.url()).pathname.replace(/\/$/, "") === probHref.replace(/\/$/, ""), "browser Back from principle returns to the originating problem");
log(errors.length === 0, `no console/page errors during journey (${errors.length}) ${errors[0] ?? ""}`);
await browser.close();
server?.close();
console.log(problems.length ? `JOURNEY FAIL (${problems.length})` : "JOURNEY PASS");
process.exit(problems.length ? 1 : 0);
