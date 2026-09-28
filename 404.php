<?php
require_once __DIR__ . '/includes/functions.php';
http_response_code(404);

$currentPage = '';
$pageTitle = 'Page Not Found | Shreya Agro Foods';
$pageDescription = 'The page you are looking for may have moved or no longer exists.';
$canonicalPath = '/404/';

require_once __DIR__ . '/includes/header.php';
?>

<section class="error-page">
    <div class="container">
        <span class="eyebrow">404</span>
        <h1>Page Not Found</h1>
        <p>The page you're looking for may have moved or no longer exists.</p>
        <div class="btn-row">
            <a href="/" class="btn btn-primary">Go Home</a>
            <a href="/products/" class="btn btn-outline">Explore Products</a>
            <a href="/contact-us/" class="btn btn-outline">Contact Us</a>
        </div>
    </div>
</section>

<?php require_once __DIR__ . '/includes/footer.php'; ?>
