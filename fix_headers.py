import os

target = '<span class="brand-name" style="display:block;">Shreya Agro Foods Ltd.</span>'
replacement = '<span class="brand-name" style="display:block;"><span class="hide-on-mobile">Shreya </span>Agro Foods Ltd.</span>'

for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r') as f:
                content = f.read()
            if target in content:
                content = content.replace(target, replacement)
                with open(filepath, 'w') as f:
                    f.write(content)
                print(f"Updated {filepath}")
