import re

filepath = 'vendor.html'
with open(filepath, 'r') as f:
    content = f.read()

# Replace <div class="img-wrap"><img src="..." alt="..."></div> to include loading="lazy"
content = re.sub(
    r'(<div class="img-wrap"><img src="/assets/images/products/[^"]+" alt="[^"]+")>',
    r'\1 loading="lazy">',
    content
)

# And remove it from the logo at the bottom if it has it, wait, logo doesn't have it.
# Check if there are other images in vendor.html missing loading="lazy"

with open(filepath, 'w') as f:
    f.write(content)

print("Updated lazy loading in vendor.html")
