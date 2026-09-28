# Shreya Agro Foods — Website

PHP + MySQL website for Shreya Agro Foods Ltd., built per the SEO/performance brief and homepage design mockup. B2B catalogue site (no cart/pricing) — every product and CTA funnels to enquiry forms.

## Stack

- Plain PHP (no framework) + MySQL (`mysqli`)
- Vanilla JS (no frontend framework) — matches the "avoid heavy JS" performance rule
- Plus Jakarta Sans (UI/body) + Playfair Display (headings, matches the approved homepage mockup)
- Clean URLs via `.htaccess` rewrite rules

## Deploying on Hostinger (hPanel shared hosting)

1. **Create the database**: hPanel → Databases → MySQL Databases → create a database + user, grant all privileges.
2. **Import the schema**: open phpMyAdmin (linked from the same page) → select the new database → Import → upload `database/schema.sql`. This creates all tables and seeds the 12 product categories, 4 popular products, and 3 sample job openings shown in the design brief.
3. **Set your DB credentials**: edit `config/config.php` and replace the `DB_HOST` / `DB_NAME` / `DB_USER` / `DB_PASS` defaults with the values hPanel gave you. Also update `SITE_URL`, `SITE_PHONE`, `SITE_EMAIL`.
4. **Upload the files**: upload everything in this repo to `public_html` (File Manager or FTP).
5. **Create your admin account**: visit `https://yourdomain.com/admin/setup.php` once — it only works while no admin account exists yet, then redirects to `/admin/login.php` from then on.
6. **Force HTTPS + www/non-www**: already handled in `.htaccess` (redirects to non-www HTTPS — change the rule near the top if you prefer `www`).

## Replacing placeholder images

Per the SEO brief, every image must be WebP, compressed, and descriptively named. This build ships with **layout placeholders** (no stock photography was available from the linked Drive folder at build time — the folder wasn't accessible to this session). To finish:

1. Export/compress real product & category photos as WebP (100–300KB target).
2. Name them exactly like the brief specifies, e.g. `shreya-agro-foods-mix-fruit-jam.webp`.
3. Upload category images to `assets/images/categories/` and product images to `assets/images/products/`.
4. Update each category/product's `image` / `main_image` column via the admin panel (products) or directly in the database (categories), or ask me to wire up an image-upload field in `admin/products.php`.
5. The homepage hero also expects `assets/images/shreya-agro-foods-quality-facility.webp` — until it's uploaded, that section gracefully falls back to blank (see the `onerror` handler in `index.php`).

**Also missing from this push:** `assets/images/shreya-agro-foods-logo.png` (the brand logo) is a binary file that couldn't go through the API-based commit used to push this codebase. Upload it manually via GitHub's web UI (drag-and-drop into `assets/images/`) or add it on your next `git push` once direct git access is available — the code already references this exact filename everywhere.

## Admin panel

`/admin/` (protected, `noindex`) — manage products, careers (add/remove job openings — dynamic per the brief), and review incoming B2B enquiries and job applications (with resume download).

## SEO features already wired up

- Unique `<title>` + meta description + canonical URL per page (`includes/functions.php::seo_head()`)
- One `<h1>` per page, proper H2/H3 hierarchy
- Organization + WebSite schema (homepage), Product + BreadcrumbList schema (product pages)
- `/sitemap.xml` generated dynamically from the database (excludes admin/thin/parameter URLs)
- `/robots.txt` blocks `/admin/`, `/actions/`, `/storage/`, `/config/`, `/database/`
- Custom 404 page with correct HTTP status
- Lazy-loading on below-the-fold images (`loading="lazy"`), hero images load eagerly
- Clean, lowercase, hyphenated URLs (`/products/product-name/`)

## What's stubbed / needs your input

- Real product photography (see above)
- Brand logo file (see above)
- `SITE_PHONE` placeholder — update in `config/config.php`
- Social media links in the footer (`includes/footer.php`) currently point to `#`
- Outbound email via PHP's `mail()` — works once the host's mail is configured; consider SMTP (PHPMailer) if deliverability matters
