<?php
require_once __DIR__ . '/includes/functions.php';

$slug = $_GET['slug'] ?? '';
$product = $slug ? fetch_product_by_slug($slug) : null;

if (!$product) {
    http_response_code(404);
    require __DIR__ . '/404.php';
    exit;
}

$currentPage = 'products';
$pageTitle = $product['name'] . ' | Shreya Agro Foods';
$pageDescription = mb_strimwidth($product['short_description'] ?: $product['description'], 0, 155, '...');
$canonicalPath = '/products/' . $product['slug'] . '/';
$ogImage = $product['main_image'] ? 'assets/images/products/' . $product['main_image'] : null;

$related = fetch_related_products((int)$product['category_id'], (int)$product['id'], 4);

$structuredData = json_encode([
    '@context' => 'https://schema.org',
    '@graph' => [
        [
            '@type' => 'Product',
            'name' => $product['name'],
            'description' => $product['short_description'],
            'category' => $product['category_name'],
            'brand' => ['@type' => 'Brand', 'name' => 'Shreya Agro Foods'],
        ],
        [
            '@type' => 'BreadcrumbList',
            'itemListElement' => [
                ['@type' => 'ListItem', 'position' => 1, 'name' => 'Home', 'item' => canonical_url('/')],
                ['@type' => 'ListItem', 'position' => 2, 'name' => 'Products', 'item' => canonical_url('/products/')],
                ['@type' => 'ListItem', 'position' => 3, 'name' => $product['category_name'], 'item' => canonical_url('/products/?category=' . $product['category_slug'])],
                ['@type' => 'ListItem', 'position' => 4, 'name' => $product['name'], 'item' => canonical_url('/products/' . $product['slug'] . '/')],
            ],
        ],
    ],
], JSON_UNESCAPED_SLASHES);

require_once __DIR__ . '/includes/header.php';
?>

<section class="section" style="padding-bottom:0;">
    <div class="container">
        <nav class="breadcrumbs" aria-label="Breadcrumb">
            <a href="/">Home</a> / <a href="/products/">Products</a> /
            <a href="/products/?category=<?= e($product['category_slug']) ?>"><?= e($product['category_name']) ?></a> /
            <?= e($product['name']) ?>
        </nav>
    </div>
</section>

<section class="section">
    <div class="container">
        <div class="product-detail-grid">
            <div>
                <div class="gallery-main">
                    <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center; font-family:var(--font-heading); color:var(--color-primary-dark); text-align:center; padding:20px;">
                        <?= e($product['name']) ?>
                    </div>
                </div>
            </div>
            <div>
                <h1><?= e($product['name']) ?></h1>
                <p><?= e($product['description'] ?: $product['short_description']) ?></p>

                <table class="spec-table">
                    <tr><td>Category</td><td><?= e($product['category_name']) ?></td></tr>
                    <tr><td>Product Type</td><td><?= e($product['product_type'] ?: '—') ?></td></tr>
                    <tr><td>Pack Size</td><td><?= e($product['pack_sizes'] ?: '—') ?></td></tr>
                    <tr><td>Available For</td><td><?= e($product['available_for']) ?></td></tr>
                    <tr><td>MOQ</td><td><?= e($product['moq']) ?></td></tr>
                </table>

                <button type="button" class="btn btn-primary js-open-enquiry"
                        data-product-id="<?= (int)$product['id'] ?>"
                        data-product-name="<?= e($product['name']) ?>"
                        data-enquiry-type="Product Enquiry">Enquire Now</button>
                <p class="form-note">No price displayed publicly — this is a B2B catalogue.</p>
            </div>
        </div>
    </div>
</section>

<section class="section section-alt">
    <div class="container">
        <h2>Why Choose This Product?</h2>
        <div class="card-grid-4">
            <div class="info-card"><h3>Quality Assured</h3><p>Consistent quality standards.</p></div>
            <div class="info-card"><h3>Reliable Supply</h3><p>Designed for regular B2B requirements.</p></div>
            <div class="info-card"><h3>Market Ready</h3><p>Products suitable for diverse markets.</p></div>
            <div class="info-card"><h3>B2B Support</h3><p>Dedicated enquiry and business support.</p></div>
        </div>
    </div>
</section>

<?php if (!empty($related)): ?>
<section class="section">
    <div class="container">
        <h2>You May Also Be Interested In</h2>
        <div class="product-grid">
            <?php foreach ($related as $r): ?>
            <div class="product-card">
                <div class="thumb"><span style="font-family:var(--font-heading); text-align:center; padding:0 10px;"><?= e($r['name']) ?></span></div>
                <h3><?= e($r['name']) ?></h3>
                <a href="/products/<?= e($r['slug']) ?>/" class="btn-link">View Product &rarr;</a>
            </div>
            <?php endforeach; ?>
        </div>
    </div>
</section>
<?php endif; ?>

<?php require_once __DIR__ . '/includes/footer.php'; ?>
