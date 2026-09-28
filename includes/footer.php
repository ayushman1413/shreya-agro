<footer class="site-footer">
    <div class="container">
        <div class="footer-grid">
            <div>
                <div class="footer-brand">
                    <img src="/assets/images/shreya-agro-foods-logo.png" alt="Shreya Agro Foods logo" width="34" height="34">
                    <strong style="color:#fff;">Shreya Agro Foods Ltd.</strong>
                </div>
                <p style="color:rgba(255,255,255,0.65); max-width:320px;"><?= e(SITE_TAGLINE) ?></p>
                <div class="social-links">
                    <a href="#" aria-label="Facebook">F</a>
                    <a href="#" aria-label="Instagram">I</a>
                    <a href="#" aria-label="LinkedIn">L</a>
                    <a href="#" aria-label="YouTube">Y</a>
                </div>
            </div>
            <div>
                <h4>Quick Links</h4>
                <ul>
                    <li><a href="/">Home</a></li>
                    <li><a href="/about-us/">About</a></li>
                    <li><a href="/products/">Products</a></li>
                    <li><a href="/contact-us/">Contact Us</a></li>
                    <li><a href="/careers/">Careers</a></li>
                </ul>
            </div>
            <div>
                <h4>Our Products</h4>
                <ul>
                    <?php foreach (array_slice(fetch_categories(), 0, 6) as $cat): ?>
                    <li><a href="/products/?category=<?= e($cat['slug']) ?>"><?= e($cat['name']) ?></a></li>
                    <?php endforeach; ?>
                    <li><a href="/products/">…and more</a></li>
                </ul>
            </div>
            <div>
                <h4>Contact</h4>
                <ul>
                    <li><?= e(SITE_ADDRESS) ?></li>
                    <li><a href="tel:<?= e(SITE_PHONE) ?>"><?= e(SITE_PHONE) ?></a></li>
                    <li><a href="mailto:<?= e(SITE_EMAIL) ?>"><?= e(SITE_EMAIL) ?></a></li>
                </ul>
            </div>
        </div>
        <div class="footer-bottom">
            &copy; <?= date('Y') ?> Shreya Agro Foods Ltd. All rights reserved.
        </div>
    </div>
</footer>

<?php require_once __DIR__ . '/chatbot.php'; ?>
<?php require_once __DIR__ . '/enquiry-modal.php'; ?>

<script src="/assets/js/main.js" defer></script>
</body>
</html>
