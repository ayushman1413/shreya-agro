<?php
/**
 * Expects $pageTitle, $pageDescription, $canonicalPath (relative) and optional
 * $ogImage to be set by the including page before this file is required.
 */
require_once __DIR__ . '/functions.php';
$currentPage = $currentPage ?? '';
?>
<!doctype html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<?php seo_head($pageTitle ?? SITE_NAME, $pageDescription ?? SITE_TAGLINE, $canonicalPath ?? '/', $ogImage ?? null); ?>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Playfair+Display:wght@600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/css/style.css">
<link rel="icon" href="/assets/images/shreya-agro-foods-logo.png">
<?php if (!empty($structuredData)): ?>
<script type="application/ld+json"><?= $structuredData ?></script>
<?php endif; ?>
</head>
<body>

<header class="site-header">
    <div class="container">
        <a href="/" class="brand">
            <img src="/assets/images/shreya-agro-foods-logo.png" alt="Shreya Agro Foods logo" width="42" height="42">
            <span class="brand-text">
                <span class="brand-name" style="display:block;">Shreya Agro Foods Ltd.</span>
                <span class="brand-tagline"><?= e(SITE_TAGLINE) ?></span>
            </span>
        </a>

        <button class="nav-toggle" id="navToggle" aria-label="Toggle menu" aria-expanded="false">&#9776;</button>

        <nav class="main-nav" id="mainNav">
            <a href="/" class="<?= $currentPage === 'home' ? 'active' : '' ?>">Home</a>
            <a href="/about-us/" class="<?= $currentPage === 'about' ? 'active' : '' ?>">About</a>
            <a href="/products/" class="<?= $currentPage === 'products' ? 'active' : '' ?>">Products</a>
            <a href="/contact-us/" class="<?= $currentPage === 'contact' ? 'active' : '' ?>">Contact Us</a>
            <a href="/careers/" class="<?= $currentPage === 'careers' ? 'active' : '' ?>">Careers</a>
        </nav>

        <div class="header-actions">
            <button class="search-toggle" id="searchToggle" aria-label="Search products">&#128269;</button>
            <a href="/contact-us/?enquiry=Business%20Partnership" class="btn btn-primary">Enquire Now</a>
        </div>
    </div>
</header>
