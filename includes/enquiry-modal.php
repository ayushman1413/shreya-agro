<div class="modal-overlay" id="enquiryModalOverlay">
    <div class="modal-box">
        <button class="modal-close" id="enquiryModalClose" aria-label="Close">&times;</button>
        <h3>Interested in this product?</h3>
        <p id="enquiryProductLabel" style="display:none;"><strong>Product:</strong> <span id="enquiryProductName"></span></p>
        <p>Share your details and our B2B team will get in touch with you.</p>

        <div id="enquiryFormWrap">
            <form id="enquiryForm" action="/actions/submit-enquiry.php" method="post">
                <input type="hidden" name="enquiry_type" id="enquiryType" value="Product Enquiry">
                <input type="hidden" name="product_id" id="enquiryProductId" value="">
                <input type="text" name="website" class="visually-hidden" tabindex="-1" autocomplete="off">

                <div class="form-group">
                    <label for="enq_name">Name *</label>
                    <input type="text" id="enq_name" name="name" placeholder="Enter your name" required>
                </div>
                <div class="form-group">
                    <label for="enq_company">Company Name</label>
                    <input type="text" id="enq_company" name="company_name" placeholder="Enter company name">
                </div>
                <div class="form-group">
                    <label for="enq_location">Location *</label>
                    <input type="text" id="enq_location" name="location" placeholder="City / State" required>
                </div>
                <div class="form-group">
                    <label for="enq_mobile">Mobile Number *</label>
                    <input type="tel" id="enq_mobile" name="mobile" placeholder="+91 XXXXX XXXXX" required>
                </div>
                <div class="form-group">
                    <label for="enq_email">Email</label>
                    <input type="email" id="enq_email" name="email" placeholder="Enter email">
                </div>
                <div class="form-group">
                    <label for="enq_requirement">Requirement / Quantity</label>
                    <textarea id="enq_requirement" name="requirement" placeholder="Tell us about your requirement"></textarea>
                </div>

                <button type="submit" class="btn btn-primary" style="width:100%; justify-content:center;">Send Enquiry</button>
                <p class="form-note">🔒 Your information is safe with us. We only use it to respond to your enquiry.</p>
            </form>
        </div>

        <div id="enquirySuccess" class="form-success" style="display:none;">
            <strong>Thank You! 🎉</strong><br>
            Your enquiry has been received successfully. Our B2B team will contact you shortly.
        </div>
    </div>
</div>
