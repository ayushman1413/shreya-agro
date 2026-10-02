import re

with open('assets/css/style.css', 'r') as f:
    css = f.read()

# Replace .main-nav in max-width: 900px
old_nav = r'\.main-nav \{ position: fixed; top: 76px; left: 0; right: 0; background: var\(--color-white\); flex-direction: column; align-items: flex-start; padding: 20px 24px; gap: 16px; box-shadow: var\(--shadow-card\); transform: translateY\(-150%\); transition: transform 0\.25s ease; \}'
new_nav = r'.main-nav { position: fixed; top: 0; right: 0; bottom: 0; left: auto; width: 320px; max-width: 85vw; background: var(--color-white); flex-direction: column; align-items: flex-start; padding: 90px 30px 40px; gap: 20px; box-shadow: -15px 0 40px rgba(0,0,0,0.12); transform: translateX(100%); transition: transform 0.4s cubic-bezier(0.25, 1, 0.5, 1); z-index: 1000; }\n    .main-nav a { font-size: 1.25rem; font-weight: 600; width: 100%; border-bottom: 1px solid rgba(0,0,0,0.06); padding-bottom: 12px; }'

css = re.sub(old_nav, new_nav, css)

old_nav_open = r'\.main-nav\.open \{ transform: translateY\(0\); \}'
new_nav_open = r'.main-nav.open { transform: translateX(0); }'
css = re.sub(old_nav_open, new_nav_open, css)

old_nav_toggle = r'\.nav-toggle \{ display: block; order: 3; margin-left: 8px; \}'
new_nav_toggle = r'.nav-toggle { display: block; order: 3; margin-left: 8px; z-index: 1001; position: relative; }'
css = re.sub(old_nav_toggle, new_nav_toggle, css)

old_nav_520 = r'\.main-nav \{ top: 60px; \}'
new_nav_520 = r'.main-nav { top: 0; }'
css = re.sub(old_nav_520, new_nav_520, css)

with open('assets/css/style.css', 'w') as f:
    f.write(css)
