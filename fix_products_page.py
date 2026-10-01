import os

base_dir = "/Users/ayushman/Desktop/shreya-agro"
products_img_dir = os.path.join(base_dir, "assets", "images", "products")
prod_idx = os.path.join(base_dir, "products", "index.html")

with open(prod_idx, "r", encoding="utf-8") as f:
    html = f.read()

all_images = [f for f in os.listdir(products_img_dir) if f.endswith(('.png', '.jpg', '.jpeg', '.webp'))]

# Generate grid HTML for ALL images
grid_html = ""
for img in all_images:
    name = img.replace(".png", "").replace(".webp", "").replace(".jpg", "").replace("-", " ").replace("_", " ")
    id_name = img.lower().replace(".png", "").replace(".webp", "").replace(".jpg", "").replace(" ", "-").replace("_", "-")
    id_name = "".join([c for c in id_name if c.isalnum() or c == '-'])
    
    grid_html += f'''
        <div class="product-card">
            <div class="thumb"><img src="/assets/images/products/{img}" alt="{name.title()}" loading="lazy" width="800" height="800"></div>
            <h3>{name.title()}</h3>
            <a href="/products/{id_name}/" class="btn-link">View Details</a>
        </div>
'''

# We need to replace the entire grid. 
grid_start_tag = '<div class="product-grid">'
grid_end_tag = '</div>\n    </div>\n</section>'

grid_start_idx = html.find(grid_start_tag)
if grid_start_idx != -1:
    # also find the section end
    grid_end_idx = html.find(grid_end_tag, grid_start_idx)
    if grid_end_idx == -1:
        grid_end_idx = html.find('</div>\n        </div>\n    </section>', grid_start_idx)
        
    if grid_end_idx != -1:
        new_html = html[:grid_start_idx + len(grid_start_tag)] + grid_html + html[grid_end_idx:]
        with open(prod_idx, "w", encoding="utf-8") as f:
            f.write(new_html)
        print("Replaced entire grid!")
    else:
        print("Could not find grid end")
else:
    print("Could not find grid start")
