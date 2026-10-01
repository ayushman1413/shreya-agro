import os

def rebuild_products_page():
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
        
        # We don't know the category, so we'll just use "all" or general
        category = "general"
        desc = f"Authentic {name.title()} from Shreya Agro Foods."
        pack_sizes = "Available in multiple sizes"
        
        grid_html += f'''
        <div class="product-card" data-category="{category}" data-product-name="{name.title()}">
            <div class="thumb"><img src="/assets/images/products/{img}" alt="Shreya Agro Foods {name.title()}" loading="lazy" width="800" height="800"></div>
            <h3>{name.title()}</h3>
            <p class="pack-sizes">{pack_sizes}</p>
            <p class="availability">Available For: B2B | Wholesale</p>
            <a href="/products/{id_name}/" class="btn-link" style="margin-bottom:10px;">View Details &rarr;</a>
            <button type="button" class="enquire-link js-open-enquiry" data-product-name="{name.title()}" data-enquiry-type="Product Enquiry" data-product-image="/assets/images/products/{img}" data-product-desc="{desc}" data-pack-sizes="{pack_sizes}">Product Enquiry &rarr;</button>
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
            print(f"Replaced entire grid with {len(all_images)} products!")
        else:
            print("Could not find grid end")
    else:
        print("Could not find grid start")

if __name__ == "__main__":
    rebuild_products_page()
