import os

NEW_PRODUCTS = [
    {
        "id": "wheat-flour-atta",
        "name": "Wheat Flour (Chakki Atta)",
        "category": "flour",
        "desc": "100% whole wheat stone ground goodness. Rich in fiber and natural nutrition.",
        "image": "Shreya Wheat Flour Atta Still Life-2.png",
        "pack_sizes": "1kg, 5kg, 10kg, 25kg"
    },
    {
        "id": "rusk-toast",
        "name": "Rusk Toast (Elaichi & Milty Flavour)",
        "category": "snacks",
        "desc": "Crunchy and tasty Rusk Toast perfect for your tea-time. Available in Elaichi and Milty flavors.",
        "image": "Shreya Rusk Toast Tea-Time Still Life.png",
        "pack_sizes": "200g, 400g"
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
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/css/style.css">
</head>
<body>
<header class="site-header">
    <div class="container">
        <a href="/" class="brand"><img src="/assets/images/shreya-agro-foods-logo.png" alt="Shreya Agro Foods logo" width="42" height="42"></a>
        <nav class="main-nav">
            <a href="/">Home</a>
            <a href="/products/">Products</a>
            <a href="/contact-us/">Contact Us</a>
        </nav>
    </div>
</header>
<div class="container" style="padding:100px 20px;">
    <h1>{name}</h1>
    <img src="/assets/images/products/{image}" alt="{name}" style="max-width:500px; width:100%;">
    <p>{desc}</p>
    <p><strong>Pack Sizes:</strong> {pack_sizes}</p>
</div>
</body>
</html>
"""

def update():
    base_dir = "/Users/ayushman/Desktop/shreya-agro"
    
    # Generate new product pages
    for p in NEW_PRODUCTS:
        prod_dir = os.path.join(base_dir, "products", p['id'])
        os.makedirs(prod_dir, exist_ok=True)
        content = PRODUCT_TEMPLATE.format(**p)
        with open(os.path.join(prod_dir, "index.html"), "w", encoding="utf-8") as f:
            f.write(content)
            
    # Update products/index.html to append new items
    prod_idx = os.path.join(base_dir, "products", "index.html")
    if os.path.exists(prod_idx):
        with open(prod_idx, "r", encoding="utf-8") as f:
            html = f.read()
            
        grid_html = ""
        for p in NEW_PRODUCTS:
            grid_html += f'''
            <div class="product-card">
                <div class="thumb"><img src="/assets/images/products/{p['image']}" alt="{p['name']}" loading="lazy" width="800" height="800"></div>
                <h3>{p['name']}</h3>
                <a href="/products/{p['id']}/" class="btn-link">View Details</a>
            </div>
            '''
        
        # Insert before closing grid
        insert_idx = html.rfind('</div>\n    </div>\n</section>')
        if insert_idx != -1:
            html = html[:insert_idx] + grid_html + html[insert_idx:]
            with open(prod_idx, "w", encoding="utf-8") as f:
                f.write(html)

    # Update homepage to use the mobile banners
    idx = os.path.join(base_dir, "index.html")
    if os.path.exists(idx):
        with open(idx, "r", encoding="utf-8") as f:
            index_html = f.read()
            
        # Replace hero image if possible
        import re
        index_html = re.sub(r'src="[^"]*hero[^"]*"', r'src="/assets/images/products/Shreya Spice Powders Poster.png"', index_html)
        
        with open(idx, "w", encoding="utf-8") as f:
            f.write(index_html)
            
    print("Website updated with new images!")

if __name__ == "__main__":
    update()
