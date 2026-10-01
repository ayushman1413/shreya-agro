import os

base_dir = "/Users/ayushman/Desktop/shreya-agro"
about_script = os.path.join(base_dir, "generate_about.py")
contact_script = os.path.join(base_dir, "generate_contact.py")

for script in [about_script, contact_script]:
    with open(script, "r", encoding="utf-8") as f:
        content = f.read()

    # We need to make .hero display: block !important to override style.css's display: flex
    # which causes the items to be laid out horizontally.
    old_hero_style = ".hero { position: relative;"
    new_hero_style = ".hero { display: block !important; position: relative;"
    
    if new_hero_style not in content:
        content = content.replace(old_hero_style, new_hero_style)

    with open(script, "w", encoding="utf-8") as f:
        f.write(content)
        
print("Updated python scripts to fix hero alignment.")
