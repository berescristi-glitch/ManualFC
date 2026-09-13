import { chromium, firefox, webkit } from "playwright";
import AxeBuilder from "@axe-core/playwright";

const base = process.env.MANUALFC_AUDIT_BASE || "http://127.0.0.1:4321";
const routes = [
  "/", "/incepe-aici/", "/volum/01/ch-0101/", "/volum/04/ch-0408/",
  "/principii/spatiu-si-unghiuri/", "/rezolva-pe-teren/primeste-fara-sa-verifice-inainte/",
  "/rezolva-pe-teren/evita-repetat-sa-primeasca-sub-presiune/",
  "/gold-standard/exercitii/EX-0001/", "/gold-standard/exercitii/EX-0005/",
  "/gold-standard/sedinte/SES-0001/", "/gold-standard/sedinte/SES-0001/mod-teren/",
  "/spatiul-meu/", "/spatiul-meu/reflectie/",
];
const viewports = [
  { width: 1440, height: 900 }, { width: 1280, height: 800 },
  { width: 768, height: 1024 }, { width: 390, height: 844 },
];
const axeRoutes = ["/", "/volum/01/ch-0101/", "/volum/04/ch-0408/", "/rezolva-pe-teren/evita-repetat-sa-primeasca-sub-presiune/", "/gold-standard/exercitii/EX-0001/", "/gold-standard/sedinte/SES-0001/mod-teren/", "/spatiul-meu/reflectie/"];

async function auditEngine(name, engine, full) {
  let browser;
  try { browser = await engine.launch({ headless: true }); }
  catch (error) { return { engine: name, status: "NOT_RUN", error: String(error) }; }
  const findings = [];
  const matrix = full ? viewports : [{ width: 390, height: 844 }];
  const checkedRoutes = full ? routes : ["/", "/gold-standard/sedinte/SES-0001/mod-teren/", "/spatiul-meu/reflectie/"];
  for (const viewport of matrix) {
    const context = await browser.newContext({ viewport, reducedMotion: "reduce" });
    for (const route of checkedRoutes) {
      const page = await context.newPage();
      const consoleErrors = [];
      page.on("console", msg => { if (msg.type() === "error") consoleErrors.push(msg.text()); });
      page.on("pageerror", error => consoleErrors.push(String(error)));
      const response = await page.goto(base + route, { waitUntil: "networkidle" });
      const metrics = await page.evaluate(() => ({
        main: document.querySelectorAll("main").length,
        h1: document.querySelectorAll("h1").length,
        overflow: document.documentElement.scrollWidth - document.documentElement.clientWidth,
        title: document.title,
      }));
      if (!response || response.status() >= 400 || metrics.main !== 1 || metrics.h1 !== 1 || metrics.overflow > 1 || consoleErrors.length) {
        findings.push({ route, viewport, status: response?.status(), ...metrics, consoleErrors });
      }
      await page.close();
    }
    await context.close();
  }
  const axe = [];
  if (full) {
    const context = await browser.newContext({ viewport: { width: 390, height: 844 }, reducedMotion: "reduce" });
    for (const route of axeRoutes) {
      const page = await context.newPage();
      await page.goto(base + route, { waitUntil: "networkidle" });
      const result = await new AxeBuilder({ page }).analyze();
      if (result.violations.length) axe.push({ route, violations: result.violations.map(v => ({ id: v.id, impact: v.impact, nodes: v.nodes.length })) });
      await page.close();
    }
    await context.close();
  }
  await browser.close();
  return { engine: name, status: findings.length || axe.length ? "FAIL" : "PASS", combinations: matrix.length * checkedRoutes.length, findings, axe };
}

async function chaos() {
  const browser = await chromium.launch({ headless: true });
  const results = {};
  const corrupt = await browser.newContext({ viewport: { width: 390, height: 844 } });
  await corrupt.addInitScript(() => {
    localStorage.setItem("manualfc:coach-state", "{broken-json");
    localStorage.setItem("manualfc:coach-state:v1", JSON.stringify({ version: 0, savedSessions: [{ id: "MISSING" }] }));
  });
  const page = await corrupt.newPage();
  const errors = [];
  page.on("pageerror", e => errors.push(String(e)));
  await page.goto(base + "/spatiul-meu/", { waitUntil: "networkidle" });
  await page.reload({ waitUntil: "networkidle" });
  results.corruptState = { errors, bodyVisible: await page.locator("body").isVisible() };
  await corrupt.close();

  const multi = await browser.newContext({ viewport: { width: 390, height: 844 } });
  const a = await multi.newPage(); const b = await multi.newPage();
  await a.goto(base + "/spatiul-meu/", { waitUntil: "networkidle" });
  await b.goto(base + "/spatiul-meu/reflectie/", { waitUntil: "networkidle" });
  await a.evaluate(() => localStorage.setItem("manualfc:audit-multitab", "changed"));
  await b.waitForTimeout(250);
  results.multiTab = await b.evaluate(() => localStorage.getItem("manualfc:audit-multitab"));
  await multi.close();

  const offline = await browser.newContext({ serviceWorkers: "allow", viewport: { width: 390, height: 844 } });
  const off = await offline.newPage();
  await off.goto(base + "/gold-standard/sedinte/SES-0001/mod-teren/", { waitUntil: "networkidle" });
  await off.waitForTimeout(1000);
  await offline.setOffline(true);
  let offlineResult;
  try {
    const response = await off.reload({ waitUntil: "domcontentloaded", timeout: 10000 });
    offlineResult = { loaded: true, status: response?.status() ?? null, title: await off.title() };
  } catch (error) { offlineResult = { loaded: false, error: String(error) }; }
  results.offline = offlineResult;
  await offline.close();
  await browser.close();
  return results;
}

const output = {
  chromium: await auditEngine("chromium", chromium, true),
  firefox: await auditEngine("firefox", firefox, false),
  webkit: await auditEngine("webkit", webkit, false),
};
try { output.chaos = await chaos(); } catch (error) { output.chaos = { status: "FAIL", error: String(error) }; }
console.log(JSON.stringify(output, null, 2));
