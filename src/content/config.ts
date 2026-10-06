import { defineCollection, z } from 'astro:content';

const blogCollection = defineCollection({
  type: 'content',
  schema: () =>
    z.object({
      title: z.string().max(85, 'Title should be under 85 chars for optimal SEO snippets'),
      description: z.string().max(160, 'Description should be under 160 chars for SERPs and Pinterest'),
      pubDate: z.date(),
      updatedDate: z.date().optional(),
      author: z.string().default('Festive Editorial Team'),
      featuredImage: z.string().default('/images/default-cover.jpg'),
      imageAlt: z.string(),
      category: z.enum(['Gift Guides', 'Party Games', 'Printables', 'Festive Food', 'Decor Hacks']),
      tags: z.array(z.string()).default([]),
      isAffiliate: z.boolean().default(true),
      isPrintable: z.boolean().default(false),
      downloadUrl: z.string().optional(),
      pinterestTitle: z.string().optional(),
      pinterestDescription: z.string().optional(),
      canonicalURL: z.string().url().optional(),
    }),
});

export const collections = {
  blog: blogCollection,
};
