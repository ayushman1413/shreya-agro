import os

def fix_product_categories():
    base_dir = "/Users/ayushman/Desktop/shreya-agro"
    index_html_path = os.path.join(base_dir, "index.html")
    products_index_path = os.path.join(base_dir, "products", "index.html")

    with open(index_html_path, "r", encoding="utf-8") as f:
        home_html = f.read()

    # Find the category grid in the homepage
    grid_start_tag = '<div class="category-grid">'
    grid_start_idx = home_html.find(grid_start_tag)
    if grid_start_idx == -1:
        print("Could not find category grid in homepage")
        return

    # Find the end of this div
    # since it's a simple match, let's find the end of the section
    grid_end_idx = home_html.find('</div>\n        </div>\n    </section>', grid_start_idx)
    
    if grid_end_idx == -1:
        print("Could not find end of category grid in homepage")
        return
        
    category_grid_html = home_html[grid_start_idx:grid_end_idx]

    with open(products_index_path, "r", encoding="utf-8") as f:
        prod_html = f.read()

    # Find the category grid in the products page
    prod_grid_start_idx = prod_html.find(grid_start_tag)
    if prod_grid_start_idx == -1:
        print("Could not find category grid in products page")
        return

    # Find where to end the replacement in products page
    prod_grid_end_idx = prod_html.find('</div>\n        </div>\n    </section>', prod_grid_start_idx)
    if prod_grid_end_idx == -1:
        # Check if there's another closing pattern
        prod_grid_end_idx = prod_html.find('</section>', prod_grid_start_idx)
        if prod_grid_end_idx != -1:
            prod_grid_end_idx = prod_html.rfind('</div>', prod_grid_start_idx, prod_grid_end_idx)
            prod_grid_end_idx = prod_html.rfind('</div>', prod_grid_start_idx, prod_grid_end_idx)

    if prod_grid_end_idx == -1:
        print("Could not find end of category grid in products page")
        return

    new_prod_html = prod_html[:prod_grid_start_idx] + category_grid_html + prod_html[prod_grid_end_idx:]

    with open(products_index_path, "w", encoding="utf-8") as f:
        f.write(new_prod_html)
    
    print("Successfully replaced the broken category grid in products/index.html with the fixed one from the homepage.")

if __name__ == "__main__":
    fix_product_categories()
