import os

def fix_cta_banner():
    path = "/Users/ayushman/Desktop/shreya-agro/index.html"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    old_cta = """    <section class="cta-split">
        <div class="visual" role="img" aria-label="Fresh spices and ingredients
used in Shreya Agro Foods products">
        </div>
        <div class="content">
            <span class="eyebrow">B2B Opportunities</span>
            <h2>Bring <strong>Shreya</strong> to Your Market</h2>
            <p>Partner with us for distribution and business opportunities.</p>
            <div>
                <a href="/contact-us/?enquiry=Business%20Partnership" class="btn
 btn-primary">Contact Us &rarr;</a>
            </div>
        </div>
    </section>"""
    
    # Try finding with exact newlines first
    if old_cta not in content:
        # Let's do a more robust regex replacement
        import re
        pattern = re.compile(r'<section class="cta-split">.*?</section>', re.DOTALL)
        content, n = pattern.subn(r'''    <div class="container" style="padding: 60px 24px;">
        <section class="cta-split" style="border-top: none; border-radius: 24px; overflow: hidden; box-shadow: 0 15px 35px rgba(20,40,25,0.08); min-height: 340px;">
            <div class="visual" role="img" aria-label="Fresh spices and ingredients used in Shreya Agro Foods products" style="background-image: url('/assets/images/Shreya%20Sunrise%20Spice%20Collection.png'); background-position: center; min-height: 250px;">
            </div>
            <div class="content" style="padding: 60px 4vw;">
                <span class="eyebrow">B2B Opportunities</span>
                <h2>Bring <strong>Shreya</strong> to Your Market</h2>
                <p style="font-size: 1.1rem; max-width: 400px; margin: 0 auto 24px;">Partner with us for distribution and business opportunities across India and beyond.</p>
                <div>
                    <button type="button" class="btn btn-primary js-open-enquiry" data-enquiry-type="Business Partnership">Contact Us &rarr;</button>
                </div>
            </div>
        </section>
    </div>''', content)
        print(f"Replaced {n} occurrences using regex.")
    else:
        content = content.replace(old_cta, '''    <div class="container" style="padding: 60px 24px;">
        <section class="cta-split" style="border-top: none; border-radius: 24px; overflow: hidden; box-shadow: 0 15px 35px rgba(20,40,25,0.08); min-height: 340px;">
            <div class="visual" role="img" aria-label="Fresh spices and ingredients used in Shreya Agro Foods products" style="background-image: url('/assets/images/Shreya%20Sunrise%20Spice%20Collection.png'); background-position: center; min-height: 250px;">
            </div>
            <div class="content" style="padding: 60px 4vw;">
                <span class="eyebrow">B2B Opportunities</span>
                <h2>Bring <strong>Shreya</strong> to Your Market</h2>
                <p style="font-size: 1.1rem; max-width: 400px; margin: 0 auto 24px;">Partner with us for distribution and business opportunities across India and beyond.</p>
                <div>
                    <button type="button" class="btn btn-primary js-open-enquiry" data-enquiry-type="Business Partnership">Contact Us &rarr;</button>
                </div>
            </div>
        </section>
    </div>''')
        print("Replaced exact string.")
        
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

fix_cta_banner()
