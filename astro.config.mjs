import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';
import sitemap from '@astrojs/sitemap';

// Documented canonical test URL (DEC-0053 / PROJECT_STATUS.md, TASK-2601):
// https://manualfc.vercel.app/. This is the only real, documented deployment
// endpoint for this project; it currently serves `noindex, nofollow` as a
// staging environment. Using it here keeps canonical URLs/sitemap internally
// coherent without inventing a production domain — a real production domain
// still requires an explicit product decision (see TASK-3711 report).
const SITE_URL = 'https://manualfc.vercel.app';

// https://astro.build/config
export default defineConfig({
  site: SITE_URL,
  output: 'static',
  srcDir: './app/src',
  outDir: './dist/web',
  integrations: [mdx(), sitemap()],
  build: {
    format: 'directory'
  },
  vite: {
    server: {
      watch: {
        ignored: ['**/temp/**']
      }
    }
  }
});
