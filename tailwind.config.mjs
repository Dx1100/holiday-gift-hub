/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  theme: {
    extend: {
      colors: {
        festive: {
          red: '#C41E3A',
          green: '#165B33',
          gold: '#D4AF37',
          dark: '#0F172A',
        }
      }
    },
  },
  plugins: [],
}
