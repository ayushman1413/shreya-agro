<?php
require_once __DIR__ . '/includes/functions.php';

$currentPage = 'contact';
$pageTitle = 'Contact Shreya Agro Foods | B2B & Business Enquiries';
$pageDescription = 'Get in touch with Shreya Agro Foods for product enquiries, B2B partnerships, distribution opportunities and careers.';
$canonicalPath = '/contact-us/';
$presetEnquiry = $_GET['enquiry'] ?? '';

$careers = fetch_active_careers();

require_once __DIR__ . '/includes/header.php';
?>

<section class="page-hero">
    <div class="container">
        <span class="eyebrow">Contact &amp; Careers</span>
        <h1>Let's Connect</h1>
        <p>Whether you're looking for a business partnership, product enquiry, distribution opportunity or career with us, we'd love to hear from you.</p>
        <div class="hero-actions">
            <button type="button" class="btn btn-primary js-open-general-enquiry" data-enquiry-type="Business Partnership">Make a B2B Enquiry</button>
            <a href="#careers" class="btn btn-outline-light">View Careers</a>
        </div>
    </div>
</section>

<section class="section">
    <div class="container">
        <div class="contact-grid">
            <div>
                <h2>Get in Touch</h2>
                <div class="contact-info-item">
                    <div class="label">📍 Our Office</div>
                    <div><?= e(SITE_ADDRESS) ?></div>
                </div>
                <div class="contact-info-item">
                    <div class="label">📞 Phone</div>
                    <div><a href="tel:<?= e(SITE_PHONE) ?>"><?= e(SITE_PHONE) ?></a></div>
                </div>
                <div class="contact-info-item">
                    <div class="label">✉️ Email</div>
                    <div><a href="mailto:<?= e(SITE_EMAIL) ?>"><?= e(SITE_EMAIL) ?></a></div>
                </div>
                <div class="contact-info-item">
                    <div class="label">Business Enquiries</div>
                    <div>For products, distribution and partnerships.</div>
                </div>
            </div>

            <div class="contact-form">
                <h3>Send Us an Enquiry</h3>
                <div id="generalFormWrap">
                    <form id="generalEnquiryForm" action="/actions/submit-enquiry.php" method="post">
                        <input type="text" name="website" class="visually-hidden" tabindex="-1" autocomplete="off">
                        <div class="form-group">
                            <label for="g_name">Name *</label>
                            <input type="text" id="g_name" name="name" placeholder="Enter your name" required>
                        </div>
                        <div class="form-group">
                            <label for="g_company">Company Name</label>
                            <input type="text" id="g_company" name="company_name" placeholder="Enter company name">
                        </div>
                        <div class="form-group">
                            <label for="g_mobile">Mobile Number *</label>
                            <input type="tel" id="g_mobile" name="mobile" placeholder="Enter mobile number" required>
                        </div>
                        <div class="form-group">
                            <label for="g_email">Email</label>
                            <input type="email" id="g_email" name="email" placeholder="Enter email address">
                        </div>
                        <div class="form-group">
                            <label for="g_location">Location *</label>
                            <input type="text" id="g_location" name="location" placeholder="City / State" required>
                        </div>
                        <div class="form-group">
                            <label for="g_type">Enquiry Type</label>
                            <select id="g_type" name="enquiry_type">
                                <option value="Product Enquiry">Product Enquiry</option>
                                <option value="B2B / Wholesale">B2B / Wholesale</option>
                                <option value="Distribution">Distribution</option>
                                <option value="Business Partnership">Business Partnership</option>
                                <option value="General Enquiry" selected>General Enquiry</option>
                                <option value="Career">Career</option>
                            </select>
                        </div>
                        <div class="form-group">
                            <label for="g_message">Message</label>
                            <textarea id="g_message" name="message" placeholder="Tell us how we can help you..."></textarea>
                        </div>
                        <button type="submit" class="btn btn-primary" style="width:100%; justify-content:center;">Submit Enquiry</button>
                    </form>
                </div>
                <div id="generalFormSuccess" class="form-success" style="display:none;">
                    <strong>Thank You! 🎉</strong><br>Your enquiry has been received successfully.
                </div>
            </div>
        </div>
    </div>
</section>

<section class="section section-alt">
    <div class="container">
        <div class="cta-bar">
            <div>
                <h2>Looking for a Long-Term FMCG Partner?</h2>
                <p>Connect with Shreya Agro Foods for B2B, wholesale, distribution and business opportunities.</p>
            </div>
            <button type="button" class="btn js-open-general-enquiry" style="background:#fff; color:var(--color-primary-dark);" data-enquiry-type="Business Partnership">Become a B2B Partner &rarr;</button>
        </div>
    </div>
</section>

<section class="section" id="careers">
    <div class="container">
        <span class="eyebrow">Careers</span>
        <h2>Build Your Career With Shreya Agro Foods</h2>
        <p>We are always looking for passionate, talented and motivated people who want to grow with a growing FMCG organization.</p>
        <p><strong>Explore opportunities. Grow with us. Make an impact.</strong></p>

        <div class="card-grid-4" style="margin-top:28px;">
            <div class="info-card"><h3>🌱 Growth</h3><p>Opportunities to learn, develop and grow.</p></div>
            <div class="info-card"><h3>🤝 Collaboration</h3><p>Work with a team that values ideas and teamwork.</p></div>
            <div class="info-card"><h3>💡 Innovation</h3><p>Be part of a company continuously evolving with the market.</p></div>
            <div class="info-card"><h3>🚀 Opportunity</h3><p>Build your career in a growing FMCG environment.</p></div>
        </div>
    </div>
</section>

<section class="section section-alt">
    <div class="container">
        <h2>Current Openings</h2>
        <?php if (empty($careers)): ?>
        <div class="info-card">
            <h3>No Current Openings</h3>
            <p>We don't have any active positions at the moment, but we're always interested in meeting talented people.</p>
            <button type="button" class="btn btn-outline js-open-application" data-position="General Application">Send Your Resume &rarr;</button>
        </div>
        <?php else: ?>
        <?php foreach ($careers as $job): ?>
        <div class="job-card">
            <div>
                <h3><?= e($job['title']) ?></h3>
                <div class="job-meta">📍 <?= e($job['location']) ?> &nbsp;|&nbsp; 💼 <?= e($job['employment_type']) ?></div>
            </div>
            <button type="button" class="btn-link js-open-application" data-career-id="<?= (int)$job['id'] ?>" data-position="<?= e($job['title']) ?>" style="background:none; border:none; cursor:pointer;">View Details &amp; Apply &rarr;</button>
        </div>
        <?php endforeach; ?>
        <?php endif; ?>
    </div>
</section>

<section class="section">
    <div class="container">
        <h2>Find Us</h2>
        <iframe class="map-embed" loading="lazy" src="https://www.google.com/maps?q=Mumbai,Maharashtra&output=embed" title="Shreya Agro Foods Ltd. location — Mumbai, Maharashtra"></iframe>
    </div>
</section>

<!-- General enquiry modal (reuses the enquiry-modal styling but posts type from dropdown) -->
<div class="modal-overlay" id="generalEnquiryOverlay">
    <div class="modal-box">
        <button class="modal-close" id="generalEnquiryClose" aria-label="Close">&times;</button>
        <h3>Send Us an Enquiry</h3>
        <p>Our team will get back to you shortly.</p>
        <div id="generalModalFormWrap">
            <form id="generalModalForm" action="/actions/submit-enquiry.php" method="post">
                <input type="hidden" name="enquiry_type" id="generalModalType" value="Business Partnership">
                <input type="text" name="website" class="visually-hidden" tabindex="-1" autocomplete="off">
                <div class="form-group"><label>Name *</label><input type="text" name="name" required></div>
                <div class="form-group"><label>Company Name</label><input type="text" name="company_name"></div>
                <div class="form-group"><label>Location *</label><input type="text" name="location" required></div>
                <div class="form-group"><label>Mobile Number *</label><input type="tel" name="mobile" required></div>
                <div class="form-group"><label>Email</label><input type="email" name="email"></div>
                <div class="form-group"><label>Message</label><textarea name="message"></textarea></div>
                <button type="submit" class="btn btn-primary" style="width:100%; justify-content:center;">Submit Enquiry</button>
            </form>
        </div>
        <div id="generalModalSuccess" class="form-success" style="display:none;"><strong>Thank You! 🎉</strong><br>Your enquiry has been received successfully.</div>
    </div>
</div>

<!-- Career application modal -->
<div class="modal-overlay" id="applicationOverlay">
    <div class="modal-box">
        <button class="modal-close" id="applicationClose" aria-label="Close">&times;</button>
        <h3>Apply for this Position</h3>
        <p><strong>Position:</strong> <span id="applicationPosition"></span></p>
        <div id="applicationFormWrap">
            <form id="applicationForm" action="/actions/submit-application.php" method="post" enctype="multipart/form-data">
                <input type="hidden" name="career_id" id="applicationCareerId" value="">
                <input type="hidden" name="position_title" id="applicationPositionTitle" value="">
                <input type="text" name="website" class="visually-hidden" tabindex="-1" autocomplete="off">
                <div class="form-group"><label>Full Name *</label><input type="text" name="full_name" required></div>
                <div class="form-group"><label>Mobile Number *</label><input type="tel" name="mobile" required></div>
                <div class="form-group"><label>Email *</label><input type="email" name="email" required></div>
                <div class="form-group"><label>Current Location *</label><input type="text" name="current_location" required></div>
                <div class="form-group"><label>Experience</label><input type="text" name="experience" placeholder="Years of experience"></div>
                <div class="form-group"><label>Resume *</label><input type="file" name="resume" accept=".pdf,.doc,.docx" required></div>
                <div class="form-group"><label>Message</label><textarea name="message" placeholder="Tell us briefly about yourself..."></textarea></div>
                <button type="submit" class="btn btn-primary" style="width:100%; justify-content:center;">Submit Application</button>
            </form>
        </div>
        <div id="applicationSuccess" class="form-success" style="display:none;">
            <strong>Application Submitted Successfully! 🎉</strong><br>
            Thank you for your interest in joining Shreya Agro Foods. Our team will review your application and contact you if your profile matches an available opportunity.
        </div>
    </div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function () {
    var presetEnquiry = <?= json_encode($presetEnquiry) ?>;
    if (presetEnquiry) {
        var select = document.getElementById('g_type');
        if (select) select.value = presetEnquiry;
    }

    // Business partnership CTA buttons -> general enquiry modal
    var genOverlay = document.getElementById('generalEnquiryOverlay');
    document.querySelectorAll('.js-open-general-enquiry').forEach(function (btn) {
        btn.addEventListener('click', function () {
            document.getElementById('generalModalType').value = btn.getAttribute('data-enquiry-type') || 'Business Partnership';
            genOverlay.classList.add('open');
        });
    });
    document.getElementById('generalEnquiryClose').addEventListener('click', function () { genOverlay.classList.remove('open'); });
    genOverlay.addEventListener('click', function (e) { if (e.target === genOverlay) genOverlay.classList.remove('open'); });

    document.getElementById('generalModalForm').addEventListener('submit', function (e) {
        e.preventDefault();
        var form = e.target, btn = form.querySelector('button[type="submit"]');
        btn.disabled = true;
        fetch(form.action, { method: 'POST', body: new FormData(form) })
            .then(function (r) { return r.json(); })
            .then(function (data) {
                btn.disabled = false;
                if (data.success) {
                    document.getElementById('generalModalFormWrap').style.display = 'none';
                    document.getElementById('generalModalSuccess').style.display = 'block';
                } else { alert(data.message || 'Something went wrong.'); }
            });
    });

    document.getElementById('generalEnquiryForm').addEventListener('submit', function (e) {
        e.preventDefault();
        var form = e.target, btn = form.querySelector('button[type="submit"]');
        btn.disabled = true;
        fetch(form.action, { method: 'POST', body: new FormData(form) })
            .then(function (r) { return r.json(); })
            .then(function (data) {
                btn.disabled = false;
                if (data.success) {
                    document.getElementById('generalFormWrap').style.display = 'none';
                    document.getElementById('generalFormSuccess').style.display = 'block';
                } else { alert(data.message || 'Something went wrong.'); }
            });
    });

    // Career application modal
    var appOverlay = document.getElementById('applicationOverlay');
    document.querySelectorAll('.js-open-application').forEach(function (btn) {
        btn.addEventListener('click', function () {
            document.getElementById('applicationPosition').textContent = btn.getAttribute('data-position') || '';
            document.getElementById('applicationPositionTitle').value = btn.getAttribute('data-position') || '';
            document.getElementById('applicationCareerId').value = btn.getAttribute('data-career-id') || '';
            appOverlay.classList.add('open');
        });
    });
    document.getElementById('applicationClose').addEventListener('click', function () { appOverlay.classList.remove('open'); });
    appOverlay.addEventListener('click', function (e) { if (e.target === appOverlay) appOverlay.classList.remove('open'); });

    document.getElementById('applicationForm').addEventListener('submit', function (e) {
        e.preventDefault();
        var form = e.target, btn = form.querySelector('button[type="submit"]');
        btn.disabled = true;
        fetch(form.action, { method: 'POST', body: new FormData(form) })
            .then(function (r) { return r.json(); })
            .then(function (data) {
                btn.disabled = false;
                if (data.success) {
                    document.getElementById('applicationFormWrap').style.display = 'none';
                    document.getElementById('applicationSuccess').style.display = 'block';
                } else { alert(data.message || 'Something went wrong.'); }
            });
    });
});
</script>

<?php require_once __DIR__ . '/includes/footer.php'; ?>
