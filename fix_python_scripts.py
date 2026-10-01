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

# 2. Function to update python scripts that generate pages
def update_script(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        script_content = f.read()
        
    # Replace the inline header with the correct one
    # In the python scripts, the header starts with <header class="site-header">
    # and ends with </header>
    h_start = script_content.find('<header class="site-header">')
    h_end = script_content.find('</header>') + len('</header>')
    
    if h_start != -1 and h_end != -1:
        # We need to indent correct_header so it looks okay in the python string, 
        # but since it's just HTML, we can just replace it directly.
        script_content = script_content[:h_start] + correct_header + script_content[h_end:]
        
    # Fix CSS for the hero text
    script_content = script_content.replace(
        ".hero h1 { font-size: 48px; font-weight: 800; margin-bottom: 24px; }",
        ".hero h1 { font-size: 48px; font-weight: 800; margin-bottom: 24px; color: white !important; }"
    )
    script_content = script_content.replace(
        ".hero p { font-size: 20px; max-width: 800px; margin: 0 auto 40px; line-height: 1.6; }",
        ".hero p { font-size: 20px; max-width: 800px; margin: 0 auto 40px; line-height: 1.6; color: white !important; }"
    )
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(script_content)

# Update the python generators
update_script(os.path.join(base_dir, "generate_about.py"))
update_script(os.path.join(base_dir, "generate_contact.py"))

print("Scripts updated successfully.")
