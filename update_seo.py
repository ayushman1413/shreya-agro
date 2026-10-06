import os
import re

def update_seo(filepath, title, h1_old, h1_new):
    if not os.path.exists(filepath):
        return
    with open(filepath, 'r') as f:
        content = f.read()

    # Update Title
    content = re.sub(r'<title>.*?</title>', f'<title>{title}</title>', content)

    # Update H1
    if h1_old and h1_new:
        content = content.replace(h1_old, h1_new)

    with open(filepath, 'w') as f:
        f.write(content)
    print(f"Updated SEO for {filepath}")

update_seo('index.html', 'Shreya Agro Foods | FMCG Products & Food Manufacturer in India', None, None) # H1 already correct
update_seo('about-us/index.html', 'About Shreya Agro Foods | 26+ Years of FMCG Experience', None, None) # H1 already correct
update_seo('products/index.html', 'FMCG Products | Shreya Agro Foods', '<h1>Quality Products for Every Market</h1>', '<h1>Our FMCG Products</h1>')
update_seo('contact-us/index.html', 'Contact Shreya Agro Foods | B2B & Business Enquiries', None, None) # H1 already correct
update_seo('careers/index.html', 'Careers at Shreya Agro Foods | Job Opportunities', '<h1>Join Our Team</h1>', '<h1>Build Your Career With Shreya Agro Foods</h1>')
