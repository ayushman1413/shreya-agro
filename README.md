# Shreya Agro Foods — Website

Fully static site for Shreya Agro Foods Ltd. — plain HTML/CSS/JS, no PHP, no database, no admin panel. Built per the SEO/performance brief and the approved homepage design mockup. B2B catalogue (no cart/pricing) — every product and CTA funnels to an enquiry form.

## Stack

- Plain HTML/CSS/JS — nothing to build, nothing to run server-side
- Plus Jakarta Sans (UI/body) + Playfair Display (headings, matches the approved homepage mockup)
- Clean URLs via folder structure (`/products/mix-fruit-jam/index.html` → `/products/mix-fruit-jam/`) — no rewrite rules needed for routing
- Forms submit to [Web3Forms](https://web3forms.com) (free, no backend needed) instead of a database

## Before you deploy: set up form submissions

There's no server to receive the enquiry/application forms, so they post directly to Web3Forms, which emails submissions to you.

1. Go to [web3forms.com](https://web3forms.com) → enter your email → you'll instantly get a free **Access Key** (no account/signup needed).
2. Find every `<input type="hidden" name="access_key" value="YOUR_WEB3FORMS_ACCESS_KEY">` in the HTML files and replace `YOUR_WEB3FORMS_ACCESS_KEY` with your real key. It appears in:
   - `index.html`, `about-us/index.html`, `products/index.html`, `products/*/index.html` (product enquiry modal)
   - `contact-us/index.html` (three forms: general enquiry, B2B modal, job application modal)
3. Submissions will arrive by email to the address you registered with Web3Forms.

## Deploying on Hostinger (hPanel shared hosting)

1. **Upload the files** — two options:
   - **Git (recommended)**: hPanel → Advanced → Git → repository `https://github.com/saitmplacement/shreya-agro.git`, branch `main`, install path `public_html`.
   - **Manual**: download the repo as a ZIP from GitHub → hPanel → File Manager → upload to `public_html` → extract.
2. **Replace the Web3Forms access key** (see above) directly in File Manager, or do it before uploading.
3. **SSL**: hPanel → SSL — usually auto-issued within minutes once your domain points to Hostinger.
4. Visit `https://yourdomain.com/` — done. No database, no build step, no admin login required.

## Updating content later

Since there's no admin panel or database, content changes are direct file edits:
- **Add/edit/remove a job opening**: edit the "Current Openings" section in `contact-us/index.html`.
- **Add a product**: duplicate one of the `products/<slug>/index.html` files, update its content/meta tags, add a matching card to `products/index.html` and (if it should appear there) `index.html`, and add its URL to `sitemap.xml`.
- **Edit categories, company info, phone/email**: search-and-replace across the HTML files (the phone number `+91 XXXXX XXXXX` and email are repeated in every page's footer/contact section).

## Product & category photography

All product photos, category tiles, the hero banner, the factory/quality photo, and the closing B2B banner are real images (WebP, compressed to 45–130KB each) in `assets/images/categories/`, `assets/images/products/`, and `assets/images/`. Two categories — **Syrups** and **Oils** — still use the icon/gradient placeholder tile since no photo exists for them yet. To finish those:

1. Export/compress a real photo as WebP (100–300KB target).
2. Name it `shreya-agro-foods-syrups.webp` / `shreya-agro-foods-oils.webp` and save to `assets/images/categories/`.
3. In `index.html` and `products/index.html`, replace that category's `<div class="thumb cat-syrups"><span class="icon-tile">🧃</span></div>` (or `cat-oils`) with `<div class="thumb"><img src="/assets/images/categories/shreya-agro-foods-syrups.webp" alt="Shreya Agro Foods Syrups" loading="lazy" width="800" height="600"></div>` (same pattern used for every other category).

If you add more products later, follow the same pattern: a square (800×800) WebP in `assets/images/products/`, referenced from the popular-products card, the product detail page's gallery, and any related-product cards that link to it.

## SEO features already in place

- Unique `<title>` + meta description + canonical URL on every page
- One `<h1>` per page, proper H2/H3 hierarchy
- Organization + WebSite schema (homepage), Product + BreadcrumbList schema (each product page)
- Static `/sitemap.xml` and `/robots.txt`
- Custom 404 page (`404.html`, wired via `.htaccess`)
- Lazy-loading on below-the-fold images, hero loads eagerly
- Clean, lowercase, hyphenated URLs

## What's stubbed / needs your input

- Syrups and Oils category photos (see above)
- Web3Forms access key (see above) — **forms won't work until this is set**
- Phone number placeholder `+91 XXXXX XXXXX` — find-and-replace across all pages
- Social media links in every page's footer currently point to `#`
