import re

path = "/Users/ayushman/Desktop/shreya-agro/assets/css/style.css"
with open(path, "r") as f:
    content = f.read()

# Fix hidden header CTA on mobile
old_header_mobile = ".header-actions .btn-primary { display: none; }"
new_header_mobile = ".header-actions .btn-primary { display: block; padding: 6px 10px; font-size: 0.7rem; }"
if old_header_mobile in content:
    content = content.replace(old_header_mobile, new_header_mobile)

# Make sure brand text is a bit smaller on tiny screens so everything fits
if ".brand-text .brand-name { font-size: 0.95rem; }" in content:
    content = content.replace(".brand-text .brand-name { font-size: 0.95rem; }", ".brand-text .brand-name { font-size: 0.85rem; }")

with open(path, "w") as f:
    f.write(content)
print("Applied final tweaks to style.css")
