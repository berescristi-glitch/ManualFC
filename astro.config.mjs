import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';

// https://astro.build/config
export default defineConfig({
  output: 'static',
  srcDir: './app/src',
  outDir: './dist/web',
  integrations: [mdx()],
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
