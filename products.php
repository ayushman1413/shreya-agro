<?php
require_once __DIR__ . '/includes/functions.php';

$currentPage = 'products';
$categorySlug = $_GET['category'] ?? '';
$searchTerm = trim($_GET['search'] ?? '');

$activeCategory = $categorySlug ? fetch_category_by_slug($categorySlug) : null;

if ($activeCategory) {
    $pageTitle = $activeCategory['name'] . ' | FMCG Products | Shreya Agro Foods';
    $pageDescription = $activeCategory['short_description'] . ' Explore our ' . $activeCategory['name'] . ' range for B2B and wholesale enquiries.';
} else {
    $pageTitle = 'FMCG Products | Shreya Agro Foods';
    $pageDescription = 'Explore Shreya Agro Foods\' full range of FMCG products — masalas, biscuits, sweets, jams, oils, rice and more — available for B2B and wholesale.';
}
$canonicalPath = '/products/' . ($categorySlug ? '?category=' . urlencode($categorySlug) : '');

$categories = fetch_categories();
$products = fetch_products([
    'category_slug' => $categorySlug ?: null,
    'search' => $searchTerm ?: null,
]);

require_once __DIR__ . '/includes/header.php';
?>

<section class="page-hero">
    <div class="container">
        <span class="eyebrow">Products</span>
        <h1>Quality Products for Every Market</h1>
        <p>Explore our range of FMCG products, created with a focus on quality, consistency and customer satisfaction.</p>
        <div class="hero-actions">
            <a href="/products/" class="btn btn-outline-light">View All Products</a>
            <a href="/contact-us/?enquiry=Business%20Partnership" class="btn btn-primary">Become a B2B Partner</a>
        </div>
    </div>
</section>

<section class="section">
    <div class="container">
        <div class="section-head">
            <div>
                <span class="eyebrow">Explore Our Products</span>
                <h2>Product Categories</h2>
            </div>
        </div>
        <div class="category-grid">
            <?php foreach ($categories as $cat): ?>
            <a href="/products/?category=<?= e($cat['slug']) ?>" class="category-card">
                <div class="thumb"><span><?= e($cat['name']) ?></span></div>
                <div class="meta"><span><?= e($cat['name']) ?></span><span class="arrow">&rarr;</span></div>
            </a>
            <?php endforeach; ?>
        </div>
    </div>
</section>

<section class="section section-alt" id="search">
    <div class="container">
        <h2>Our Products</h2>

        <form method="get" class="filter-bar">
            <?php if ($categorySlug): ?><input type="hidden" name="category" value="<?= e($categorySlug) ?>"><?php endif; ?>
            <input type="search" id="productSearchInput" name="search" placeholder="Search by product name..." value="<?= e($searchTerm) ?>">
        </form>

        <div class="filter-chips" style="margin-bottom:24px;">
            <a href="/products/" class="<?= !$categorySlug ? 'active' : '' ?>">All Products</a>
            <?php foreach ($categories as $cat): ?>
            <a href="/products/?category=<?= e($cat['slug']) ?>" class="<?= $categorySlug === $cat['slug'] ? 'active' : '' ?>"><?= e($cat['name']) ?></a>
            <?php endforeach; ?>
        </div>

        <?php if (empty($products)): ?>
            <p>No products found. Please try a different search or category.</p>
        <?php else: ?>
        <div class="product-grid">
            <?php foreach ($products as $p): ?>
            <div class="product-card">
                <div class="thumb"><span data-product-name="<?= e($p['name']) ?>" style="font-family:var(--font-heading); text-align:center; padding:0 10px;"><?= e($p['name']) ?></span></div>
                <h3><?= e($p['name']) ?></h3>
                <p class="pack-sizes"><?= e($p['short_description']) ?></p>
                <p class="availability">Available For: <?= e($p['available_for']) ?></p>
                <a href="/products/<?= e($p['slug']) ?>/" class="btn-link" style="margin-bottom:10px;">View Details &rarr;</a>
                <button type="button" class="enquire-link js-open-enquiry"
                        data-product-id="<?= (int)$p['id'] ?>"
                        data-product-name="<?= e($p['name']) ?>"
                        data-enquiry-type="Product Enquiry">Product Enquiry &rarr;</button>
            </div>
            <?php endforeach; ?>
        </div>
        <?php endif; ?>
    </div>
</section>

<section class="section">
    <div class="container">
        <div class="cta-bar">
            <div>
                <h2>Looking for Bulk FMCG Products?</h2>
                <p>Connect with Shreya Agro Foods for wholesale, distribution and business enquiries.</p>
            </div>
            <div style="display:flex; gap:12px; flex-wrap:wrap;">
                <a href="/contact-us/?enquiry=B2B%20%2F%20Wholesale" class="btn" style="background:#fff; color:var(--color-primary-dark);">Make a B2B Enquiry</a>
                <a href="/contact-us/" class="btn btn-outline-light">Talk to Our Team</a>
            </div>
        </div>
    </div>
</section>

<?php require_once __DIR__ . '/includes/footer.php'; ?>
