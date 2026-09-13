import { defineCollection, z } from 'astro:content';

/**
 * Astro Content Collections Configuration (Consumer Layer)
 * Nota Bene: JSON Schemas din schemas/ rămân canonice și sunt validate separat prin scripts/validate_content.py.
 */

const mdxDocsCollection = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    description: z.string(),
    isFixture: z.boolean().optional().default(false),
    date: z.string().optional()
  })
});

export const collections = {
  docs: mdxDocsCollection
};
