import re
import os
from pathlib import Path

html_file = "/Users/ayushman/Desktop/shreya-agro/products/index.html"
with open(html_file, 'r') as f:
    content = f.read()

# Find all img src attributes
img_srcs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', content)

missing_images = []
for src in img_srcs:
    # If absolute path in HTML, make relative to project root
    if src.startswith('/'):
        file_path = "/Users/ayushman/Desktop/shreya-agro" + src
    else:
        file_path = "/Users/ayushman/Desktop/shreya-agro/products/" + src
    
    if not os.path.exists(file_path):
        missing_images.append(src)

print(f"Total images referenced in products/index.html: {len(img_srcs)}")
print(f"Missing images: {len(missing_images)}")
for missing in missing_images:
    print(f"Missing: {missing}")
