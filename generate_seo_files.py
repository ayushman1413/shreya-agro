import os
import datetime

def create_seo_files():
    base_dir = "/Users/ayushman/Desktop/shreya-agro"
    
    # 1. Create robots.txt (Rule 15)
    robots_content = """User-agent: *
Allow: /
Disallow: /admin/
Disallow: /private/

Sitemap: https://www.shreyaagrofoods.com/sitemap.xml
"""
    with open(os.path.join(base_dir, "robots.txt"), "w") as f:
        f.write(robots_content)
        
    # 2. Create 404.html (Rule 19)
    error_page = """<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Page Not Found | Shreya Agro Foods</title>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="/assets/css/style.css">
    <style>
        .error-container { text-align: center; padding: 100px 20px; font-family: 'Plus Jakarta Sans', sans-serif; }
        .error-container h1 { font-size: 48px; color: #333; margin-bottom: 20px; }
        .error-container p { font-size: 18px; color: #666; margin-bottom: 30px; }
        .error-actions a { margin: 0 10px; display: inline-block; padding: 12px 24px; background: #e63946; color: white; text-decoration: none; border-radius: 4px; font-weight: 600; }
        .error-actions a.secondary { background: #1d3557; }
    </style>
</head>
<body>
    <div class="error-container">
        <h1>404 - Page Not Found</h1>
        <p>The page you're looking for may have moved or no longer exists.</p>
        <div class="error-actions">
            <a href="/">Go Home</a>
            <a href="/products/" class="secondary">Explore Products</a>
            <a href="/contact-us/" class="secondary">Contact Us</a>
        </div>
    </div>
</body>
</html>"""
    with open(os.path.join(base_dir, "404.html"), "w") as f:
        f.write(error_page)

    # 3. Create sitemap.xml (Rule 16)
    pages = [
        "",
        "about-us/",
        "products/",
        "contact-us/"
    ]
    
    # Read product dirs to add them to sitemap
    products_dir = os.path.join(base_dir, "products")
    if os.path.exists(products_dir):
        for item in os.listdir(products_dir):
            item_path = os.path.join(products_dir, item)
            if os.path.isdir(item_path) and os.path.exists(os.path.join(item_path, "index.html")):
                pages.append(f"products/{item}/")

    date_str = datetime.datetime.now().strftime("%Y-%m-%d")
    
    sitemap_xml = ['<?xml version="1.0" encoding="UTF-8"?>']
    sitemap_xml.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')
    
    for page in pages:
        sitemap_xml.append('  <url>')
        sitemap_xml.append(f'    <loc>https://www.shreyaagrofoods.com/{page}</loc>')
        sitemap_xml.append(f'    <lastmod>{date_str}</lastmod>')
        sitemap_xml.append('    <changefreq>weekly</changefreq>')
        sitemap_xml.append('  </url>')
        
    sitemap_xml.append('</urlset>')
    
    with open(os.path.join(base_dir, "sitemap.xml"), "w") as f:
        f.write("\\n".join(sitemap_xml))
        
    print("SEO files (robots.txt, 404.html, sitemap.xml) generated successfully.")

if __name__ == "__main__":
    create_seo_files()
