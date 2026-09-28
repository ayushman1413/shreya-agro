<?php
require_once __DIR__ . '/includes/functions.php';
header('Content-Type: application/xml; charset=utf-8');

$urls = [
    ['loc' => '/', 'priority' => '1.0'],
    ['loc' => '/about-us/', 'priority' => '0.8'],
    ['loc' => '/products/', 'priority' => '0.9'],
    ['loc' => '/contact-us/', 'priority' => '0.7'],
];

// Category filter pages use a query parameter (?category=) and are intentionally
// left out of the sitemap per the SEO brief's "no parameter variations" rule.
foreach (fetch_products() as $p) {
    $urls[] = ['loc' => '/products/' . $p['slug'] . '/', 'priority' => '0.7'];
}

echo '<?xml version="1.0" encoding="UTF-8"?>' . "\n";
echo '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' . "\n";
foreach ($urls as $u) {
    echo "  <url>\n";
    echo '    <loc>' . htmlspecialchars(canonical_url($u['loc']), ENT_XML1) . "</loc>\n";
    echo '    <priority>' . $u['priority'] . "</priority>\n";
    echo "  </url>\n";
}
echo '</urlset>';
