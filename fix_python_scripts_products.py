import os
import re

base_dir = "/Users/ayushman/Desktop/shreya-agro"
index_html_path = os.path.join(base_dir, "index.html")

# 1. Get the correct header HTML
with open(index_html_path, "r", encoding="utf-8") as f:
    home_html = f.read()
    
header_start = home_html.find('<header class="site-header">')
header_end = home_html.find('</header>') + len('</header>')
correct_header = home_html[header_start:header_end]

# Update generate_website.py
gen_website_path = os.path.join(base_dir, "generate_website.py")
with open(gen_website_path, "r", encoding="utf-8") as f:
    script_content = f.read()
    
h_start = script_content.find('<header class="site-header">')
h_end = script_content.find('</header>') + len('</header>')

if h_start != -1 and h_end != -1:
    script_content = script_content[:h_start] + correct_header + script_content[h_end:]
    with open(gen_website_path, "w", encoding="utf-8") as f:
        f.write(script_content)
    print("generate_website.py updated")

# Wait! The products/index.html header needs to be updated directly, because 
# earlier we ran rebuild_products_grid.py which only touched the grid.
# The overall products page header might be broken too.
prod_idx = os.path.join(base_dir, "products", "index.html")
with open(prod_idx, "r", encoding="utf-8") as f:
    prod_html = f.read()

p_start = prod_html.find('<header class="site-header">')
p_end = prod_html.find('</header>') + len('</header>')

if p_start != -1 and p_end != -1:
    prod_html = prod_html[:p_start] + correct_header + prod_html[p_end:]
    
    # Also let's ensure .hero text is white if it has an embedded style
    prod_html = prod_html.replace(
        ".hero h1 { font-size: 48px; font-weight: 800; margin-bottom: 24px; }",
        ".hero h1 { font-size: 48px; font-weight: 800; margin-bottom: 24px; color: white !important; }"
    )
    prod_html = prod_html.replace(
        ".hero p { font-size: 20px; max-width: 800px; margin: 0 auto 40px; line-height: 1.6; }",
        ".hero p { font-size: 20px; max-width: 800px; margin: 0 auto 40px; line-height: 1.6; color: white !important; }"
    )
    with open(prod_idx, "w", encoding="utf-8") as f:
        f.write(prod_html)
    print("products/index.html updated")

