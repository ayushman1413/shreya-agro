import os
import re

PRODUCTS = [
    {
        "id": "basmati-rice",
        "name": "Premium Basmati Rice",
        "category": "rice",
        "desc": "Extra-long grain basmati rice, naturally aged for 12 months to enhance its aroma, texture, and flavour.",
        "image": "Premium Basmati Rice Still Life.png",
        "pack_sizes": "1kg, 5kg, 25kg"
    },
    {
        "id": "mango-pickle",
        "name": "Rustic Mango Pickle",
        "category": "chutneys",
        "desc": "Authentic taste bringing the true essence of Indian kitchens to your plate with time-honored recipes.",
        "image": "Rustic Shreya Pickle Product Display.png",
        "pack_sizes": "100g, 200g, 250g, 500g, 1kg, 5kg"
    },
    {
        "id": "red-chilli-powder",
        "name": "Red Chilli Powder",
        "category": "masalas",
        "desc": "Fiery flavor and natural red color crafted from high-quality sun-dried red chillies.",
        "image": "Screenshot 2026-10-01 at 6.54.33 PM.png",
        "pack_sizes": "50g, 100g, 250g, 500g, 1kg, 5kg"
    },
    {
        "id": "turmeric-powder",
        "name": "Turmeric Powder",
        "category": "masalas",
        "desc": "Bright color and pure aroma made from carefully selected turmeric rhizomes.",
        "image": "Screenshot 2026-10-01 at 6.54.44 PM.png",
        "pack_sizes": "50g, 100g, 250g, 500g, 1kg, 5kg"
    },
    {
        "id": "besan-flour",
        "name": "Premium Besan Flour",
        "category": "flour",
        "desc": "Made from 100% pure Bengal gram (chana dal) finely milled for a smooth, lump-free texture.",
        "image": "Shreya Besan Flour with Chana Dal.png",
        "pack_sizes": "500g, 1kg, 30kg"
    },
    {
        "id": "hardball-candy",
        "name": "Hardball Candy",
        "category": "sweets",
        "desc": "A burst of vibrant, fruity flavors in delightful long-lasting hard candies.",
        "image": "Shreya Candy Sweetscape.png",
        "pack_sizes": "Available in Jars"
    },
    {
        "id": "ginger-garlic-paste",
        "name": "Ginger & Garlic Paste",
        "category": "masalas",
        "desc": "Balanced blend of fresh ginger and garlic processed to a fine, smooth texture.",
        "image": "Shreya Ginger Garlic Paste Still Life.png",
        "pack_sizes": "500g, 1kg, 5kg"
    },
    {
        "id": "gulab-jamun-rasgulla",
        "name": "Gulab Jamun & Rasgulla",
        "category": "sweets",
        "desc": "Timeless taste of traditional Indian desserts, soft and syrup-soaked.",
        "image": "Shreya Gulab Jamun and Rasgulla Duo.png",
        "pack_sizes": "500g, 1kg"
    },
    {
        "id": "jaggery",
        "name": "Jaggery Cubes & Powder",
        "category": "jaggery",
        "desc": "Natural sweetener made from pure sun-ripened sugarcane juice.",
        "image": "Shreya Jaggery Cubes and Powder Duo.png",
        "pack_sizes": "500g"
    },
    {
        "id": "chicken-masala",
        "name": "Chicken & Meat Masalas",
        "category": "masalas",
        "desc": "Spicy and robust signature blends for classic Indian cooking.",
        "image": "Shreya Masalas_ Taste the Difference (1).png",
        "pack_sizes": "50g, 100g, 250g, 500g, 1kg, 5kg"
    },
    {
        "id": "mix-fruit-jam",
        "name": "Mix Fruit Jam",
        "category": "jams",
        "desc": "Made with the finest fruits, our Mix Fruit Jam brings the perfect blend of taste, richness and natural goodness.",
        "image": "Shreya Mix Fruits Jam Jars.png",
        "pack_sizes": "250g, 500g, 1kg"
    },
    {
        "id": "farm-fresh-pickles",
        "name": "Farm-Fresh Pickles",
        "category": "chutneys",
        "desc": "Authentic pickles packed with flavor and traditional spices.",
        "image": "Shreya Pickles_ Farm-Fresh Flavour.png",
        "pack_sizes": "100g, 200g, 250g, 500g, 1kg, 5kg"
    },
    {
        "id": "soan-papdi-assorted",
        "name": "Assorted Soan Papdi",
        "category": "soan-papdi",
        "desc": "Crisp and flaky traditional sweet in assorted flavors.",
        "image": "Shreya Soan Papdi Flavour Collection.png",
        "pack_sizes": "180g, 200g"
    },
    {
        "id": "garam-masala",
        "name": "Garam Masala",
        "category": "masalas",
        "desc": "A rich, aromatic blend of traditional Indian spices.",
        "image": "garam-masala.webp",
        "pack_sizes": "100g, 200g, 500g"
    },
    {
        "id": "tomato-ketchup",
        "name": "Tomato Ketchup",
        "category": "chutneys",
        "desc": "Rich, tangy tomato ketchup made from quality tomatoes.",
        "image": "tomato-ketchup.webp",
        "pack_sizes": "500g, 1kg"
    }
]

PRODUCT_TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{name} | Shreya Agro Foods</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="https://www.shreyaagrofoods.com/products/{id}/">
<meta property="og:type" content="product">
<meta property="og:site_name" content="Shreya Agro Foods">
<meta property="og:title" content="{name} | Shreya Agro Foods">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="https://www.shreyaagrofoods.com/assets/images/products/{image}">
<meta property="og:url" content="https://www.shreyaagrofoods.com/products/{id}/">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Playfair+Display:wght@600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/css/style.css">
<link rel="icon" href="/assets/images/shreya-agro-foods-logo.png">
<script type="application/ld+json">
{{
  "@context": "https://schema.org/",
  "@type": "Product",
  "name": "{name}",
  "image": "https://www.shreyaagrofoods.com/assets/images/products/{image}",
  "description": "{desc}",
  "brand": {{
    "@type": "Brand",
    "name": "Shreya Agro Foods"
  }}
}}
</script>
</head>
<body>
<header class="site-header">
        <div class="container">
            <a href="/" class="brand">
                <img src="/assets/images/shreya-agro-foods-logo.png" alt="Shreya Agro Foods logo" width="42"
                    height="42">
                <span class="brand-text">
                    <span class="brand-name" style="display:block;">Shreya Agro Foods Ltd.</span>
                    <span class="brand-tagline">Authentic Taste. Trusted Quality.</span>
                </span>
            </a>
            <button class="nav-toggle" id="navToggle" aria-label="Toggle menu" aria-expanded="false">&#9776;</button>
            <nav class="main-nav" id="mainNav">
                <a href="/" class="active">Home</a>
                <a href="/about-us/">About</a>
                <a href="/products/">Products</a>
                <a href="/contact-us/">Contact Us</a>
            </nav>
            <div class="header-actions">
                <button class="search-toggle" id="searchToggle" aria-label="Search products">&#128269;</button>
                <button type="button" class="btn btn-primary js-open-enquiry" data-enquiry-type="Business Partnership">Enquire Now</button>
            </div>
        </div>
    </header>

<div class="container" style="padding-top:100px; padding-bottom: 40px;">
    <div class="breadcrumb" style="margin-bottom:20px; font-size:14px; color:#666;">
        <a href="/" style="color:#000;">Home</a> / <a href="/products/" style="color:#000;">Products</a> / <a href="/products/?category={category}" style="color:#000; text-transform:capitalize;">{category}</a> / <span style="color:#666;">{name}</span>
    </div>
    
    <div style="display:flex; flex-wrap:wrap; gap:40px;">
        <div style="flex:1; min-width:300px;">
            <img src="/assets/images/products/{image}" alt="Shreya Agro Foods {name}" style="width:100%; border-radius:12px; border:1px solid #eee;">
        </div>
        <div style="flex:1.5; min-width:300px;">
            <h1 style="font-size:32px; margin-bottom:16px;">{name}</h1>
            <p style="font-size:18px; line-height:1.6; color:#444; margin-bottom:24px;">{desc}</p>
            
            <div style="background:#f9f9f9; padding:20px; border-radius:8px; margin-bottom:30px;">
                <h3 style="margin-bottom:16px; font-size:18px;">Product Information</h3>
                <table style="width:100%; border-collapse:collapse;">
                    <tr style="border-bottom:1px solid #ddd;">
                        <td style="padding:10px 0; font-weight:600; color:#555;">Category</td>
                        <td style="padding:10px 0; text-transform:capitalize;">{category}</td>
                    </tr>
                    <tr style="border-bottom:1px solid #ddd;">
                        <td style="padding:10px 0; font-weight:600; color:#555;">Pack Sizes</td>
                        <td style="padding:10px 0;">{pack_sizes}</td>
                    </tr>
                    <tr style="border-bottom:1px solid #ddd;">
                        <td style="padding:10px 0; font-weight:600; color:#555;">Available For</td>
                        <td style="padding:10px 0;">B2B / Wholesale / Distribution</td>
                    </tr>
                </table>
            </div>
            
            <button type="button" class="btn btn-primary js-open-enquiry" data-product-name="{name}" data-enquiry-type="Product Enquiry" data-product-image="/assets/images/products/{image}" data-product-desc="{desc}" data-pack-sizes="{pack_sizes}" style="font-size:18px; padding:15px 30px;">Make a B2B Enquiry</button>
        </div>
    </div>
</div>

<footer class="site-footer">
    <div class="container">
        <div class="footer-bottom">
            &copy; 2026 Shreya Agro Foods Ltd. All rights reserved.
        </div>
    </div>
</footer>


<div class="modal-overlay" id="enquiryModalOverlay">
    <div class="modal-box modal-box-product" id="enquiryModalBox">
        <button class="modal-close" id="enquiryModalClose" aria-label="Close">&times;</button>
        <div class="modal-grid">
            <div class="modal-product-panel" id="enquiryProductPanel" style="display:none;">
                <div class="modal-product-image"><img id="enquiryProductImage" src="" alt=""></div>
                <span class="modal-product-badge">Food Product</span>
                <h3 id="enquiryProductTitle"></h3>
                <p id="enquiryProductDesc"></p>
                <div class="modal-trust-icons">
                    <div class="trust-icon"><span>🌿</span>100% Natural Ingredients</div>
                    <div class="trust-icon"><span>✅</span>No Artificial Colours</div>
                    <div class="trust-icon"><span>📦</span>Hygienically Packed</div>
                </div>
                <div class="modal-pack-sizes" id="enquiryPackSizesWrap">
                    <span class="pack-label">Available Pack Sizes</span>
                    <div class="pack-pills" id="enquiryPackSizes"></div>
                </div>
            </div>
            <div class="modal-form-panel">
                <span class="modal-form-eyebrow">B2B Enquiry Only</span>
                <h3>Product Enquiry</h3>
                <p>Interested in our products? Fill in your details and our team will get back to you shortly.</p>
                <div id="enquiryFormWrap">
                    <form id="enquiryForm">
                        <input type="hidden" name="access_key" value="YOUR_WEB3FORMS_ACCESS_KEY">
                        <input type="hidden" name="subject" value="New Product Enquiry — Shreya Agro Foods">
                        <input type="hidden" name="enquiry_type" id="enquiryType" value="Product Enquiry">
                        <input type="hidden" name="product" id="enquiryProductId" value="">
                        <input type="checkbox" name="botcheck" class="visually-hidden" tabindex="-1" autocomplete="off">
                        <div class="form-group"><label for="enq_name">Name *</label><input type="text" id="enq_name" name="name" placeholder="Enter your name" required></div>
                        <div class="form-group"><label for="enq_location">Location / City *</label><input type="text" id="enq_location" name="location" placeholder="City / State" required></div>
                        <div class="form-group"><label for="enq_mobile">Phone Number *</label><input type="tel" id="enq_mobile" name="mobile" placeholder="+91 XXXXX XXXXX" required></div>
                        <div class="form-group"><label for="enq_requirement">Message (Optional)</label><textarea id="enq_requirement" name="requirement" placeholder="Tell us about your requirement"></textarea></div>
                        <button type="submit" class="btn btn-primary" style="width:100%; justify-content:center;">Send Enquiry</button>
                        <p class="form-note">🔒 Your information is safe with us. We only use it to respond to your enquiry.</p>
                    </form>
                </div>
                <div id="enquirySuccess" class="form-success" style="display:none;"><strong>Thank You! 🎉</strong><br>Your enquiry has been received successfully. Our B2B team will contact you shortly.</div>
            </div>
        </div>
    </div>
</div>

<script src="/assets/js/main.js" defer></script>
</body>
</html>
"""

def generate_products():
    base_dir = "/Users/ayushman/Desktop/shreya-agro/products"
    
    # Generate HTML string for grid
    grid_html = ""
    for p in PRODUCTS:
        # create product directory
        prod_dir = os.path.join(base_dir, p['id'])
        os.makedirs(prod_dir, exist_ok=True)
        
        # write index.html for product
        content = PRODUCT_TEMPLATE.format(**p)
        with open(os.path.join(prod_dir, "index.html"), "w", encoding="utf-8") as f:
            f.write(content)
            
        # build grid item
        grid_html += f'''
        <div class="product-card" data-category="{p['category']}" data-product-name="{p['name']}">
            <div class="thumb"><img src="/assets/images/products/{p['image']}" alt="Shreya Agro Foods {p['name']}" loading="lazy" width="800" height="800"></div>
            <h3>{p['name']}</h3>
            <p class="pack-sizes">{p['pack_sizes']}</p>
            <p class="availability">Available For: B2B | Wholesale</p>
            <a href="/products/{p['id']}/" class="btn-link" style="margin-bottom:10px;">View Details &rarr;</a>
            <button type="button" class="enquire-link js-open-enquiry" data-product-name="{p['name']}" data-enquiry-type="Product Enquiry" data-product-image="/assets/images/products/{p['image']}" data-product-desc="{p['desc']}" data-pack-sizes="{p['pack_sizes']}">Product Enquiry &rarr;</button>
        </div>
        '''

    # Update products/index.html
    prod_idx_path = os.path.join(base_dir, "index.html")
    with open(prod_idx_path, "r", encoding="utf-8") as f:
        prod_idx_content = f.read()
        
    grid_start_tag = '<div class="product-grid">'
    grid_start_idx = prod_idx_content.find(grid_start_tag)
    if grid_start_idx != -1:
        grid_end_idx = prod_idx_content.find('</div>\n    </div>\n</section>', grid_start_idx)
        new_content = prod_idx_content[:grid_start_idx + len(grid_start_tag)] + grid_html + "\n        " + prod_idx_content[grid_end_idx:]
        with open(prod_idx_path, "w", encoding="utf-8") as f:
            f.write(new_content)
            
    print("Products updated successfully!")

if __name__ == "__main__":
    generate_products()
