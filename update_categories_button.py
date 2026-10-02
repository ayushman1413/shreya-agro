import re

with open('index.html', 'r') as f:
    content = f.read()

def replacer(match):
    before = match.group(1)
    name = match.group(2)
    after = match.group(3)
    
    return f'{before}<button type="button" class="js-open-enquiry" style="background: none; border: none; padding: 0; display: inline-flex; align-items: center; gap: 8px; cursor: pointer; font-family: var(--font-body); font-weight: 600; font-size: 0.85rem; color: var(--color-text);" data-product-name="{name}" data-enquiry-type="Category Enquiry">Enquiry Now <span class="arrow" style="width: 28px; height: 28px; border-radius: 50%; background: var(--color-primary); color: var(--color-white); display: flex; align-items: center; justify-content: center; font-size: 0.85rem; flex-shrink: 0;">&rarr;</span></button>{after}'

pattern = re.compile(
    r'(<a href="[^"]+" style="font-weight:\s*600;\s*font-size:\s*0\.95rem;\s*color:\s*var\(--color-text\);\s*text-decoration:\s*none;">(.*?)</a>\s*)<button type="button" class="enquire-link js-open-enquiry" style="[^"]+" data-product-name="[^"]+" data-enquiry-type="Category Enquiry">Enquiry Now <span style="font-size: 1\.1em;">&rarr;</span></button>(\s*</div>)',
    re.DOTALL
)

new_content = pattern.sub(replacer, content)

with open('index.html', 'w') as f:
    f.write(new_content)
