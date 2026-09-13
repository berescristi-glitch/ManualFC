import { chromium } from "playwright";

const base = "http://127.0.0.1:4321";
const browser = await chromium.launch({ headless: true });
const context = await browser.newContext({ viewport: { width: 390, height: 844 }, serviceWorkers: "allow" });
const page = await context.newPage();
const errors = [];
page.on("pageerror", error => errors.push(String(error)));
page.on("console", message => { if (message.type() === "error") errors.push(message.text()); });

await page.goto(base + "/spatiul-meu/sedinta/", { waitUntil: "networkidle" });
await page.locator("[data-session-catalog]").selectOption("SES-0001");
await page.locator("[data-add-session]").click();
await page.locator("form[data-builder]").evaluate(form => form.requestSubmit());
await page.waitForFunction(() => document.querySelector("[data-status]")?.textContent?.includes("salvată"));
const savedUrl = page.url();

await page.goto(base + "/spatiul-meu/", { waitUntil: "networkidle" });
const prepare = page.locator("[data-prepare-offline]").first();
await prepare.click();
let prepareReady = true;
try {
  await page.waitForSelector(".offline-badge-ready", { timeout: 25000 });
} catch { prepareReady = false; }
const prepareNote = prepareReady ? await page.locator(".offline-badge-ready").first().textContent() : await page.locator("[data-offline-note]").first().textContent();
const swState = await page.evaluate(async () => ({
  controller: Boolean(navigator.serviceWorker.controller),
  registration: (await navigator.serviceWorker.getRegistration())?.active?.state ?? null,
  caches: await caches.keys(),
}));
if (!prepareReady) {
  console.log(JSON.stringify({ savedUrl, prepareReady, prepareNote, swState, errors }, null, 2));
  await browser.close();
  process.exit(2);
}
const fieldRoute = "/gold-standard/sedinte/SES-0001/mod-teren/";
await page.goto(base + fieldRoute, { waitUntil: "networkidle" });
await context.setOffline(true);
const response = await page.reload({ waitUntil: "domcontentloaded", timeout: 10000 });
const offlineTitle = await page.title();
const h1 = await page.locator("h1").allTextContents();
const buttons = await page.locator("button").allTextContents();
await page.locator("[data-fm-timer-toggle]").click();
await page.waitForTimeout(1100);
const timer = await page.locator("[data-fm-timer-display]").textContent();
await page.locator("[data-fm-next]").click();
const current = await page.locator("[data-fm-current]").textContent();

console.log(JSON.stringify({ savedUrl, prepareReady, prepareNote, swState, offlineStatus: response?.status() ?? null, offlineTitle, h1, buttons, timer, current, errors }, null, 2));
await browser.close();
