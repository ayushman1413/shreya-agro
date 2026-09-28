<?php
require_once __DIR__ . '/includes/functions.php';

$currentPage = 'home';
$pageTitle = 'Shreya Agro Foods | FMCG Products & Food Manufacturer in India';
$pageDescription = 'Shreya Agro Foods is an FMCG company with 26+ years of experience, offering quality food products and B2B business opportunities across India.';
$canonicalPath = '/';

$categories = fetch_categories();
$popularProducts = fetch_popular_products(4);

$structuredData = json_encode([
    '@context' => 'https://schema.org',
    '@graph' => [
        [
            '@type' => 'Organization',
            'name' => 'Shreya Agro Foods Ltd.',
            'url' => SITE_URL,
            'logo' => canonical_url('assets/images/shreya-agro-foods-logo.png'),
            'address' => [
                '@type' => 'PostalAddress',
                'addressLocality' => 'Mumbai',
                'addressRegion' => 'Maharashtra',
                'addressCountry' => 'IN',
            ],
        ],
        [
            '@type' => 'WebSite',
            'name' => SITE_NAME,
            'url' => SITE_URL,
        ],
    ],
], JSON_UNESCAPED_SLASHES);

require_once __DIR__ . '/includes/header.php';
?>

<section class="hero" style="background-image:none;">
    <div class="container">
        <span class="eyebrow">India's Trusted FMCG Brand</span>
        <h1>Authentic Taste.<br>Trusted for Generations.</h1>
        <p class="lead">Bringing the richness of Indian culinary traditions to homes across India and the world.</p>
        <div class="hero-actions">
            <a href="/products/" class="btn btn-primary">Explore Products &rarr;</a>
            <a href="/contact-us/" class="btn btn-outline">Contact Us</a>
        </div>
    </div>
    <div class="hero-badge">
        <span class="years">26+</span>
        <span class="label">Years of<br>Quality</span>
    </div>
</section>

<section class="section" id="products">
    <div class="container">
        <div class="section-head">
            <div>
                <span class="eyebrow">Our Products</span>
                <h2>A Taste for Every Occasion</h2>
                <p>From everyday meals to festive celebrations, our wide range of products brings flavour, nutrition and tradition to your table.</p>
            </div>
            <a href="/products/" class="btn-link">View All Products &rarr;</a>
        </div>

        <div class="category-grid">
            <?php foreach ($categories as $cat): ?>
            <a href="/products/?category=<?= e($cat['slug']) ?>" class="category-card">
                <div class="thumb"><span><?= e($cat['name']) ?></span></div>
                <div class="meta">
                    <span><?= e($cat['name']) ?></span>
                    <span class="arrow">&rarr;</span>
                </div>
            </a>
            <?php endforeach; ?>
        </div>
    </div>
</section>

<section class="section section-alt">
    <div class="container">
        <div class="section-head">
            <div>
                <span class="eyebrow">Our Popular Products</span>
                <h2>Loved for Their Taste, Trusted for Their Quality</h2>
            </div>
            <a href="/products/" class="btn-link">View All Products &rarr;</a>
        </div>

        <div class="product-grid">
            <?php foreach ($popularProducts as $p): ?>
            <div class="product-card">
                <div class="thumb"><span data-product-name="<?= e($p['name']) ?>" style="font-family:var(--font-heading); text-align:center; padding:0 10px;"><?= e($p['name']) ?></span></div>
                <h3><?= e($p['name']) ?></h3>
                <p class="pack-sizes"><?= e($p['pack_sizes']) ?></p>
                <a href="/products/<?= e($p['slug']) ?>/" class="btn-link" style="margin-bottom:10px;">View Details &rarr;</a>
                <button type="button" class="enquire-link js-open-enquiry"
                        data-product-id="<?= (int)$p['id'] ?>"
                        data-product-name="<?= e($p['name']) ?>"
                        data-enquiry-type="Product Enquiry">Product Enquiry &rarr;</button>
            </div>
            <?php endforeach; ?>
        </div>
    </div>
</section>

<section class="section">
    <div class="container">
        <div class="quality-section">
            <div class="quality-image"><img src="/assets/images/shreya-agro-foods-quality-facility.webp" alt="Shreya Agro Foods quality control team packaging products" loading="lazy" width="640" height="480" onerror="this.parentElement.style.display='flex';this.parentElement.style.alignItems='center';this.parentElement.style.justifyContent='center';this.remove();"></div>
            <div>
                <span class="eyebrow">Our Commitment</span>
                <h2>Quality You Can Trust</h2>
                <p>Every product is crafted with care, using 100% natural ingredients, subjected to rigorous lab-tested purity, and released only when it meets our highest standards of taste, nutrition and safety.</p>
                <div class="icon-row">
                    <div class="icon-item"><div class="icon-circle">🌿</div><span>100% Natural Ingredients</span></div>
                    <div class="icon-item"><div class="icon-circle">🔬</div><span>Rigorous Quality Testing</span></div>
                    <div class="icon-item"><div class="icon-circle">🏭</div><span>Modern Production Facilities</span></div>
                    <div class="icon-item"><div class="icon-circle">🍃</div><span>Authentic Taste &amp; Nutrition</span></div>
                    <div class="icon-item"><div class="icon-circle">🛡️</div><span>Food Safety &amp; Purity</span></div>
                </div>
            </div>
        </div>
    </div>
</section>

<section class="section section-dark">
    <div class="container">
        <div class="global-grid">
            <div>
                <span class="eyebrow">Global Presence</span>
                <h2>From India to the World</h2>
                <p>Our products are enjoyed in Nepal, Bangladesh, Bhutan, UAE, South Africa, Canada and beyond, with ambitious expansion plans to reach more homes worldwide.</p>
                <a href="/about-us/" class="btn btn-outline-light">Our Global Reach &rarr;</a>
            </div>
            <div class="flag-grid">
                <div class="flag-item"><div class="flag-circle">🇮🇳</div><span>India</span></div>
                <div class="flag-item"><div class="flag-circle">🇳🇵</div><span>Nepal</span></div>
                <div class="flag-item"><div class="flag-circle">🇧🇩</div><span>Bangladesh</span></div>
                <div class="flag-item"><div class="flag-circle">🇧🇹</div><span>Bhutan</span></div>
                <div class="flag-item"><div class="flag-circle">🇦🇪</div><span>UAE</span></div>
                <div class="flag-item"><div class="flag-circle">🇿🇦</div><span>South Africa</span></div>
                <div class="flag-item"><div class="flag-circle">🇨🇦</div><span>Canada</span></div>
            </div>
        </div>
    </div>
</section>

<section class="section">
    <div class="container">
        <div class="cta-bar">
            <div>
                <h2>Bring Shreya to Your Market</h2>
                <p>Partner with us for distribution and business opportunities.</p>
            </div>
            <a href="/contact-us/?enquiry=Business%20Partnership" class="btn" style="background:#fff; color:var(--color-primary-dark);">Contact Us</a>
        </div>
    </div>
</section>

<?php require_once __DIR__ . '/includes/footer.php'; ?>
