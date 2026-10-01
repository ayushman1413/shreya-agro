import re

def update_hero_banners():
    index_path = "/Users/ayushman/Desktop/shreya-agro/index.html"
    
    with open(index_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    # We will look for the hero section background or the hero image tag.
    # If the hero section is using a background image in inline style or CSS, we'll replace it with a picture tag.
    
    # Since I don't know the exact structure of index.html hero section, I'll search for the hero section
    # and replace its inner HTML with the new picture tag.
    
    hero_pattern = re.compile(r'(<section class="hero".*?>)(.*?)(</section>)', re.DOTALL)
    
    # New hero content using the requested images
    new_hero_content = """
        <picture>
            <source media="(max-width: 768px)" srcset="/assets/images/Shreya Farm-to-Table Collection.png">
            <img src="/assets/images/Shreya Sunrise Spice Collection.png" alt="Shreya Agro Foods Hero Banner" style="width: 100%; height: auto; display: block;">
        </picture>
        <div class="hero-overlay" style="position: absolute; top: 0; left: 0; right: 0; bottom: 0; display: flex; align-items: center; justify-content: center; flex-direction: column; text-align: center; color: white; background: rgba(0,0,0,0.4);">
            <h1>Quality FMCG Products Built on Trust</h1>
            <p style="font-size: 20px; margin-bottom: 20px;">Delivering authentic taste and trusted quality for over 26 years.</p>
            <a href="/products/" class="btn btn-primary" style="padding: 15px 30px; font-size: 18px;">Explore Our Products</a>
        </div>
    """
    
    match = hero_pattern.search(content)
    if match:
        # We need to make sure the hero section is relatively positioned so the overlay works
        hero_start = match.group(1).replace('class="hero"', 'class="hero" style="position: relative; overflow: hidden; padding: 0;"')
        new_content = content[:match.start()] + hero_start + new_hero_content + match.group(3) + content[match.end():]
        
        with open(index_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print("Hero section updated successfully with both mobile and desktop banners.")
    else:
        print("Could not find the hero section in index.html")

if __name__ == "__main__":
    update_hero_banners()
