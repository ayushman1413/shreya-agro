import os

def ensure_all_products():
    base_dir = "/Users/ayushman/Desktop/shreya-agro"
    products_img_dir = os.path.join(base_dir, "assets", "images", "products")
    prod_idx = os.path.join(base_dir, "products", "index.html")
    
    with open(prod_idx, "r", encoding="utf-8") as f:
        html = f.read()
        
    all_images = [f for f in os.listdir(products_img_dir) if f.endswith(('.png', '.jpg', '.jpeg', '.webp'))]
    
    missing_images = []
    for img in all_images:
        # Check if the image filename is in the products HTML
        if img not in html:
            missing_images.append(img)
            
    print(f"Found {len(missing_images)} missing images to add to the products grid.")
    
    if not missing_images:
        return

    PRODUCT_TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{name} | Shreya Agro Foods</title>
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
            <a href="/about-us/">About Us</a>
            <a href="/contact-us/">Contact Us</a>
        </nav>
    </div>
</header>
<div class="container" style="padding:100px 20px;">
    <h1>{name}</h1>
    <img src="/assets/images/products/{image}" alt="{name}" style="max-width:500px; width:100%;">
    <p>Authentic and high-quality product from Shreya Agro Foods. Delivering the best taste and nutrition directly to your home.</p>
</div>
</body>
</html>
"""

    grid_html = ""
    for img in missing_images:
        # Generate a name from the filename
        name = img.replace(".png", "").replace(".webp", "").replace(".jpg", "").replace("-", " ").replace("_", " ")
        id_name = img.lower().replace(".png", "").replace(".webp", "").replace(".jpg", "").replace(" ", "-").replace("_", "-")
        
        # Remove weird characters for folder name
        id_name = "".join([c for c in id_name if c.isalnum() or c == '-'])
        
        prod_dir = os.path.join(base_dir, "products", id_name)
        os.makedirs(prod_dir, exist_ok=True)
        content = PRODUCT_TEMPLATE.format(name=name.title(), image=img)
        with open(os.path.join(prod_dir, "index.html"), "w", encoding="utf-8") as f:
            f.write(content)
            
        grid_html += f'''
            <div class="product-card">
                <div class="thumb"><img src="/assets/images/products/{img}" alt="{name.title()}" loading="lazy" width="800" height="800"></div>
                <h3>{name.title()}</h3>
                <a href="/products/{id_name}/" class="btn-link">View Details</a>
            </div>
            '''
            
    # Insert before closing grid
    insert_idx = html.rfind('</div>\\n    </div>\\n</section>')
    if insert_idx == -1: # fallback
        insert_idx = html.rfind('</div>\\n        </div>\\n    </section>')
        
    if insert_idx != -1:
        html = html[:insert_idx] + grid_html + html[insert_idx:]
        with open(prod_idx, "w", encoding="utf-8") as f:
            f.write(html)
            
    print("All missing products added!")

if __name__ == "__main__":
    ensure_all_products()
