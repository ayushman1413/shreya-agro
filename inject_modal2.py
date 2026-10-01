import os

MODAL_HTML = """
<div class="modal-overlay" id="enquiryModalOverlay">
    <div class="modal-box modal-box-product" id="enquiryModalBox">
        <button class="modal-close" id="enquiryModalClose" aria-label="Close">&times;</button>
        <div class="modal-grid">
            <div class="modal-product-panel" id="enquiryProductPanel" style="display:none;">
                <div class="modal-product-image"><img id="enquiryProductImage" src="" alt=""></div>
                <span class="modal-product-badge">Food Product</span>
                <h3 id="enquiryProductTitle"></h3>
                <p id="enquiryProductDesc"></p>
                <div class="modal-trust-icons">
                    <div class="trust-icon"><span>🌿</span>100% Natural Ingredients</div>
                    <div class="trust-icon"><span>✅</span>No Artificial Colours</div>
                    <div class="trust-icon"><span>📦</span>Hygienically Packed</div>
                </div>
                <div class="modal-pack-sizes" id="enquiryPackSizesWrap">
                    <span class="pack-label">Available Pack Sizes</span>
                    <div class="pack-pills" id="enquiryPackSizes"></div>
                </div>
            </div>
            <div class="modal-form-panel">
                <span class="modal-form-eyebrow">B2B Enquiry Only</span>
                <h3>Product Enquiry</h3>
                <p>Interested in our products? Fill in your details and our team will get back to you shortly.</p>
                <div id="enquiryFormWrap">
                    <form id="enquiryForm">
                        <input type="hidden" name="access_key" value="YOUR_WEB3FORMS_ACCESS_KEY">
                        <input type="hidden" name="subject" value="New Product Enquiry — Shreya Agro Foods">
                        <input type="hidden" name="enquiry_type" id="enquiryType" value="Product Enquiry">
                        <input type="hidden" name="product" id="enquiryProductId" value="">
                        <input type="checkbox" name="botcheck" class="visually-hidden" tabindex="-1" autocomplete="off">
                        <div class="form-group"><label for="enq_name">Name *</label><input type="text" id="enq_name" name="name" placeholder="Enter your name" required></div>
                        <div class="form-group"><label for="enq_location">Location / City *</label><input type="text" id="enq_location" name="location" placeholder="City / State" required></div>
                        <div class="form-group"><label for="enq_mobile">Phone Number *</label><input type="tel" id="enq_mobile" name="mobile" placeholder="+91 XXXXX XXXXX" required></div>
                        <div class="form-group"><label for="enq_requirement">Message (Optional)</label><textarea id="enq_requirement" name="requirement" placeholder="Tell us about your requirement"></textarea></div>
                        <button type="submit" class="btn btn-primary" style="width:100%; justify-content:center;">Send Enquiry</button>
                        <p class="form-note">🔒 Your information is safe with us. We only use it to respond to your enquiry.</p>
                    </form>
                </div>
                <div id="enquirySuccess" class="form-success" style="display:none;"><strong>Thank You! 🎉</strong><br>Your enquiry has been received successfully. Our B2B team will contact you shortly.</div>
            </div>
        </div>
    </div>
</div>
"""

def update_header_button(content):
    # Replace old link with new modal button
    old_btn = '<a href="/contact-us/?enquiry=Business%20Partnership" class="btn btn-primary">Enquire Now</a>'
    new_btn = '<button type="button" class="btn btn-primary js-open-enquiry" data-enquiry-type="Business Partnership">Enquire Now</button>'
    return content.replace(old_btn, new_btn)

def ensure_modal(content):
    if 'id="enquiryModalOverlay"' not in content:
        # inject before <script src="/assets/js/main.js" defer></script>
        script_tag = '<script src="/assets/js/main.js" defer></script>'
        if script_tag in content:
            content = content.replace(script_tag, MODAL_HTML + "\n" + script_tag)
        else:
            # maybe just before </body>
            content = content.replace('</body>', MODAL_HTML + "\n</body>")
    return content

files_to_update = [
    'index.html'
]

for f in files_to_update:
    path = os.path.join('/Users/ayushman/Desktop/shreya-agro', f)
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        new_content = update_header_button(content)
        new_content = ensure_modal(new_content)
        
        if new_content != content:
            with open(path, 'w', encoding='utf-8') as file:
                file.write(new_content)
            print(f"Updated {f}")

print("Done.")
