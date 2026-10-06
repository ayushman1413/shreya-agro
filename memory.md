# Shreya Agro Foods - Complete Project Memory & Documentation

## 1. Project Overview
This project is a fully static B2B catalogue website built for **Shreya Agro Foods Ltd.** It serves as a product showcase to generate business leads. There is no e-commerce cart, checkout, or payment gateway. Instead, every product and call-to-action (CTA) funnels users into an enquiry form.

**Goal:** Create a fast, SEO-optimized, lightweight static site.

## 2. Technology Stack & Architecture
- **Frontend Core**: Plain HTML5, CSS3, and Vanilla JavaScript.
- **Backend/Database**: None. The site is entirely static, meaning no PHP, Node.js, or SQL database is used. No admin panel is provided.
- **Form Handling**: **[Web3Forms](https://web3forms.com)** is used to capture form submissions (enquiries, job applications, contact forms) and forward them directly via email without needing a backend server.
- **Typography**: 
  - *Plus Jakarta Sans* (for UI/body text)
  - *Playfair Display* (for headings) to give it a premium, matching feel to the approved designs.
- **Hosting/Deployment**: Designed to be deployed on shared hosting (like Hostinger hPanel, GitHub Pages, Vercel, Netlify) by simply uploading the files or syncing via Git.

## 3. Directory Structure
```text
/
├── README.md               # Quickstart guide
├── memory.md               # Complete project documentation (this file)
├── index.html              # Homepage
├── 404.html                # Custom 404 Not Found page
├── vendor.html             # Vendor information page
├── sitemap.xml             # XML sitemap for SEO
├── robots.txt              # Search engine crawling rules
├── assets/                 # CSS, JS, Images, Fonts, etc.
├── about-us/               # About Us section (index.html)
├── careers/                # Careers section (index.html)
├── contact-us/             # Contact Us section (index.html)
└── products/               # Product catalogue (index.html and subfolders for each product)
```

## 4. Working Mechanism
- **Clean URLs**: The site uses a folder-based routing structure (e.g., `/products/mix-fruit-jam/index.html`), which naturally resolves to `/products/mix-fruit-jam/` in the browser without requiring `.htaccess` URL rewrite rules.
- **SEO & Performance**: 
  - Each page has unique meta tags, canonical URLs, and structured schema data (Organization/LocalBusiness on the homepage, Product on product pages).
  - Images are compressed in WebP format and lazy-loaded below the fold.
  - A static `sitemap.xml` and `robots.txt` are included.
- **Content Updates**: Since there is no CMS, content is updated by editing the HTML files directly. Adding a new product involves duplicating a product folder, updating the content, and linking it in the products grid.

## 5. Development & Running Locally
To run the project locally and see it working:
1. Open a terminal in the project directory.
2. Run a local HTTP server: `python3 -m http.server 8080` (or use any other static server like Live Server in VS Code).
3. Open your browser and navigate to `http://localhost:8080`.

## 6. Deployment Guide (Hostinger / cPanel)
1. **Upload the files**: You can use Git (Hostinger -> Advanced -> Git -> repository branch `main` to `public_html`) or manually upload a ZIP to the File Manager and extract.
2. **Web3Forms Key**: Ensure all `YOUR_WEB3FORMS_ACCESS_KEY` placeholders are replaced with a real key from Web3Forms.
3. **SSL**: Enable SSL via your hosting provider.
4. Visit your domain!

## 7. Action Items & Pending Work (To-Do)
- **Web3Forms Access Key**: Replace the placeholder `YOUR_WEB3FORMS_ACCESS_KEY` in all HTML files (`index.html`, `about-us/index.html`, `products/index.html`, `products/*/index.html`, `contact-us/index.html`). Forms will not work until this is set.
- **Missing Photos (Syrups & Oils)**: Add real WebP images for the **Syrups** and **Oils** categories to replace the current placeholder tiles in `assets/images/categories/`.
- **Social Media Links**: Update the placeholder YouTube links (`#`) in the footer across all pages once a YouTube channel is available.

## 8. Python Automation Scripts
The project contains several Python scripts used during development to automate repetitive HTML changes:
- `update_hero_css.py`: Updates hero section styles.
- `update_menu.py`: Synchronizes the navigation menu across all pages.
- `update_categories.py`: Updates category grids.
- `fix_headers.py`: Fixes header structures.
- `update_seo.py`: Applies SEO meta tags across files.
*(These scripts are for development utility and are not needed to run the website.)*

## 9. Important Business Details Wired In
- **Address**: Goregaon East, Mumbai
- **Phone**: +91 70586 74452
- **Business Hours**: Included in the Contact page
- **Social Links**: Facebook, Instagram, LinkedIn in footers + Organization/LocalBusiness schema on the homepage.
