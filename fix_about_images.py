import os

base_dir = "/Users/ayushman/Desktop/shreya-agro"
about_script = os.path.join(base_dir, "generate_about.py")

with open(about_script, "r", encoding="utf-8") as f:
    content = f.read()

# Replace Hero Image
content = content.replace(
    "https://images.unsplash.com/photo-1595858117769-95fb425ba473?auto=format&fit=crop&q=80",
    "/assets/images/Shreya Farm-to-Table Collection.png"
)

# Replace Factory Image
content = content.replace(
    "https://images.unsplash.com/photo-1621415065099-31ffb91a78ee?auto=format&fit=crop&q=80",
    "/assets/images/shreya-agro-foods-quality-facility.webp"
)

# Replace 4 Quality Images
content = content.replace(
    "https://images.unsplash.com/photo-1563124508-25f05df39f37?auto=format&fit=crop&w=500&q=80",
    "/assets/images/Shreya Sunrise Spice Collection.png"
)
content = content.replace(
    "https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?auto=format&fit=crop&w=500&q=80",
    "/assets/images/products/Shreya Wheat Flour Kitchen Still Life-1.png"
)
content = content.replace(
    "https://images.unsplash.com/photo-1587293852726-70cdb56c2866?auto=format&fit=crop&w=500&q=80",
    "/assets/images/products/Shreya Besan Chakki Ka Atta Package.png"
)
content = content.replace(
    "https://images.unsplash.com/photo-1605338902581-2292f32a76f2?auto=format&fit=crop&w=500&q=80",
    "/assets/images/products/Shreya Spice Powders Poster.png"
)

with open(about_script, "w", encoding="utf-8") as f:
    f.write(content)

print("generate_about.py updated with local images")
