import os

# Four popular products for the homepage
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
        "id": "chicken-masala",
        "name": "Chicken & Meat Masalas",
        "category": "masalas",
        "desc": "Spicy and robust signature blends for classic Indian cooking.",
        "image": "Shreya Masalas_ Taste the Difference (1).png",
        "pack_sizes": "50g, 100g, 250g, 500g, 1kg, 5kg"
    }
]

def update_index():
    index_path = "/Users/ayushman/Desktop/shreya-agro/index.html"
    
    grid_html = ""
    for p in PRODUCTS:
        grid_html += f'''
                <div class="product-card">
                    <div class="thumb"><img src="/assets/images/products/{p['image']}" alt="Shreya Agro Foods {p['name']}" loading="lazy" width="800" height="800"></div>
                    <h3>{p['name']}</h3>
                    <p class="pack-sizes">{p['pack_sizes']}</p>
                    <a href="/products/{p['id']}/" class="btn-link" style="margin-bottom:10px;">View Details &rarr;</a>
                    <button type="button" class="enquire-link js-open-enquiry" data-product-name="{p['name']}" data-enquiry-type="Product Enquiry" data-product-image="/assets/images/products/{p['image']}" data-product-desc="{p['desc']}" data-pack-sizes="{p['pack_sizes']}">Product Enquiry &rarr;</button>
                </div>'''

    with open(index_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    grid_start_tag = '<div class="product-grid">'
    grid_start_idx = content.find(grid_start_tag)
    if grid_start_idx != -1:
        grid_end_idx = content.find('</div>\n        </div>\n    </section>', grid_start_idx)
        new_content = content[:grid_start_idx + len(grid_start_tag)] + grid_html + "\n            " + content[grid_end_idx:]
        with open(index_path, "w", encoding="utf-8") as f:
            f.write(new_content)
            
    print("Homepage updated successfully!")

if __name__ == "__main__":
    update_index()
