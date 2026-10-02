import re

with open('index.html', 'r') as f:
    content = f.read()

def replacer(match):
    href = match.group(1)
    img_block = match.group(2)
    name = match.group(3)
    
    return f"""<div class="category-card">
                    <a href="{href}" class="thumb">{img_block}</a>
                    <div class="meta" style="flex-wrap: wrap; gap: 8px;">
                        <a href="{href}" style="font-weight: 600; font-size: 0.95rem; color: var(--color-text); text-decoration: none;">{name}</a>
                        <button type="button" class="enquire-link js-open-enquiry" style="font-weight: 600; color: var(--color-primary); font-size: 0.85rem; background: none; border: none; cursor: pointer; padding: 0; display: inline-flex; align-items: center; gap: 4px;" data-product-name="{name}" data-enquiry-type="Category Enquiry">Enquiry Now <span style="font-size: 1.1em;">&rarr;</span></button>
                    </div>
                </div>"""

pattern = re.compile(
    r'<a href="([^"]+)" class="category-card">\s*<div class="thumb">(.*?)</div>\s*<div class="meta"><span>(.*?)</span><span class="arrow">&rarr;</span></div>\s*</a>',
    re.DOTALL
)

new_content = pattern.sub(replacer, content)

with open('index.html', 'w') as f:
    f.write(new_content)
