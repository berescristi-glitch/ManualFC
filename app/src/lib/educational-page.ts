// Componente interactive pentru pagina educațională (ExplanationToggle, SectionNavigator).
// Centralizat aici și încărcat global din BaseLayout.astro: componentele Astro folosite
// din interiorul fișierelor MDX din content/ (în afara srcDir) nu beneficiază de
// script/style hoisting per-componentă, deci logica trebuie înregistrată o singură
// dată, global, ca Web Components — funcționează indiferent de unde a fost randat
// markup-ul <explanation-toggle>/<section-navigator> în DOM.

class ExplanationToggleElement extends HTMLElement {
  connectedCallback() {
    const btn = this.querySelector<HTMLButtonElement>('[data-toggle-btn]');
    const ids = (this.dataset.targets ?? '').split(' ').filter(Boolean);
    const blocks = ids.map(id => document.getElementById(id)).filter((el): el is HTMLElement => !!el);
    const labelCollapse = this.querySelector<HTMLElement>('[data-label-collapse]');
    const labelExpand = this.querySelector<HTMLElement>('[data-label-expand]');
    if (!btn || blocks.length === 0) return;
    btn.addEventListener('click', () => {
      const expanded = btn.getAttribute('aria-expanded') === 'true';
      const next = !expanded;
      btn.setAttribute('aria-expanded', String(next));
      blocks.forEach(block => { if (next) block.removeAttribute('hidden'); else block.setAttribute('hidden', ''); });
      labelCollapse?.toggleAttribute('hidden', !next);
      labelExpand?.toggleAttribute('hidden', next);
    });
  }
}

class SectionNavigatorElement extends HTMLElement {
  connectedCallback() {
    const links = Array.from(this.querySelectorAll<HTMLAnchorElement>('[data-section-link]'));
    const targets = links
      .map(link => { const id = link.getAttribute('href')?.replace('#', ''); return id ? document.getElementById(id) : null; })
      .filter((el): el is HTMLElement => !!el);
    if (targets.length === 0) return;

    const setActive = (id: string) => {
      links.forEach(link => {
        const active = link.getAttribute('href') === `#${id}`;
        link.classList.toggle('active', active);
        if (active) link.setAttribute('aria-current', 'true'); else link.removeAttribute('aria-current');
      });
    };

    const observer = new IntersectionObserver(entries => {
      const visible = entries.filter(e => e.isIntersecting).sort((a, b) => a.boundingClientRect.top - b.boundingClientRect.top);
      if (visible.length > 0) setActive(visible[0].target.id);
    }, { rootMargin: '-15% 0px -70% 0px' });
    targets.forEach(target => observer.observe(target));

    if (this.classList.contains('sticky')) {
      let lastY = window.scrollY;
      window.addEventListener('scroll', () => {
        const y = window.scrollY;
        this.classList.toggle('hide-on-scroll', y > lastY && y > 200);
        lastY = y;
      }, { passive: true });
    }
  }
}

if (!customElements.get('explanation-toggle')) customElements.define('explanation-toggle', ExplanationToggleElement);
if (!customElements.get('section-navigator')) customElements.define('section-navigator', SectionNavigatorElement);
