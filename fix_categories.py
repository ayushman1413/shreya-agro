import re
import os

def fix_categories():
    index_path = "/Users/ayushman/Desktop/shreya-agro/index.html"
    
    with open(index_path, "r", encoding="utf-8") as f:
        html = f.read()
        
    replacements = {
        'src="/assets/images/categories/shreya-agro-foods-masalas.webp"': 'src="/assets/images/products/Shreya Masalas_ Taste the Difference (1).png" style="object-fit:cover;"',
        'src="/assets/images/categories/shreya-agro-foods-biscuits.webp"': 'src="/assets/images/products/Shreya Rusk Toast Tea-Time Still Life.png" style="object-fit:cover;"',
        'src="/assets/images/categories/shreya-agro-foods-sweets.webp"': 'src="/assets/images/products/Shreya Gulab Jamun and Rasgulla Duo.png" style="object-fit:cover;"',
        'src="/assets/images/categories/shreya-agro-foods-soan-papdi.webp"': 'src="/assets/images/products/Shreya Soan Papdi Flavour Collection.png" style="object-fit:cover;"',
        'src="/assets/images/categories/shreya-agro-foods-jams.webp"': 'src="/assets/images/products/Shreya Mix Fruits Jam Jars.png" style="object-fit:cover;"',
        'src="/assets/images/categories/shreya-agro-foods-chikky.webp"': 'src="/assets/images/products/Shreya Candy Sweetscape.png" style="object-fit:cover;"',
        'src="/assets/images/categories/shreya-agro-foods-jaggery.webp"': 'src="/assets/images/products/Shreya Jaggery Cubes and Powder Duo.png" style="object-fit:cover;"',
        'src="/assets/images/categories/shreya-agro-foods-chutneys.webp"': 'src="/assets/images/products/Shreya Pickles_ Farm-Fresh Flavour.png" style="object-fit:cover;"',
        'src="/assets/images/categories/shreya-agro-foods-flour.webp"': 'src="/assets/images/products/Shreya Wheat Flour Atta Still Life-2.png" style="object-fit:cover;"',
        'src="/assets/images/categories/shreya-agro-foods-rice.webp"': 'src="/assets/images/products/Premium Basmati Rice Still Life.png" style="object-fit:cover;"',
    }
    
    for old, new in replacements.items():
        html = html.replace(old, new)
        
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(html)
        
    print("Fixed category images in index.html!")

if __name__ == "__main__":
    fix_categories()
