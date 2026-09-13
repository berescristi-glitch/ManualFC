import { chromium } from "playwright";
import AxeBuilder from "@axe-core/playwright";

const browser = await chromium.launch({ headless: true });
const context = await browser.newContext({ viewport: { width: 390, height: 844 } });
const page = await context.newPage();
await page.goto("http://127.0.0.1:4321/", { waitUntil: "networkidle" });
const axe = await new AxeBuilder({ page }).analyze();
console.log(JSON.stringify({
  contrast: axe.violations.filter(v => v.id === "color-contrast").flatMap(v => v.nodes.map(n => ({ target: n.target, html: n.html, failureSummary: n.failureSummary }))),
}, null, 2));
await page.goto("http://127.0.0.1:4321/spatiul-meu/", { waitUntil: "networkidle" });
console.log(JSON.stringify({
  workspaceButtons: await page.locator("button").allTextContents(),
  workspaceLinks: await page.locator("a").allTextContents(),
  workspaceInputs: await page.locator("input,select,textarea").evaluateAll(nodes => nodes.map(n => ({ tag: n.tagName, name: n.getAttribute("name"), value: n.value, type: n.getAttribute("type"), aria: n.getAttribute("aria-label") }))),
}, null, 2));
await browser.close();
