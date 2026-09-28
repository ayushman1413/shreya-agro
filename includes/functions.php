<?php
require_once __DIR__ . '/../config/db.php';

function e(?string $value): string
{
    return htmlspecialchars($value ?? '', ENT_QUOTES, 'UTF-8');
}

function current_url(): string
{
    $scheme = (!empty($_SERVER['HTTPS']) && $_SERVER['HTTPS'] !== 'off') ? 'https' : 'http';
    return $scheme . '://' . ($_SERVER['HTTP_HOST'] ?? '') . ($_SERVER['REQUEST_URI'] ?? '/');
}

function canonical_url(string $path): string
{
    return rtrim(SITE_URL, '/') . '/' . ltrim($path, '/');
}

/**
 * Renders the shared <head> SEO block: unique title, meta description,
 * canonical URL, and Open Graph tags — required per-page by the SEO brief.
 */
function seo_head(string $title, string $description, string $canonicalPath, ?string $ogImage = null): void
{
    $canonical = canonical_url($canonicalPath);
    $ogImage = $ogImage ? canonical_url($ogImage) : canonical_url('assets/images/shreya-agro-foods-logo.png');
    ?>
    <title><?= e($title) ?></title>
    <meta name="description" content="<?= e($description) ?>">
    <link rel="canonical" href="<?= e($canonical) ?>">
    <meta property="og:type" content="website">
    <meta property="og:site_name" content="<?= e(SITE_NAME) ?>">
    <meta property="og:title" content="<?= e($title) ?>">
    <meta property="og:description" content="<?= e($description) ?>">
    <meta property="og:image" content="<?= e($ogImage) ?>">
    <meta property="og:url" content="<?= e($canonical) ?>">
    <meta name="twitter:card" content="summary_large_image">
    <?php
}

function fetch_categories(): array
{
    $result = db()->query('SELECT * FROM categories ORDER BY sort_order ASC');
    return $result ? $result->fetch_all(MYSQLI_ASSOC) : [];
}

function fetch_category_by_slug(string $slug): ?array
{
    $stmt = db()->prepare('SELECT * FROM categories WHERE slug = ? LIMIT 1');
    $stmt->bind_param('s', $slug);
    $stmt->execute();
    $row = $stmt->get_result()->fetch_assoc();
    return $row ?: null;
}

function fetch_popular_products(int $limit = 4): array
{
    $stmt = db()->prepare('SELECT * FROM products WHERE is_popular = 1 AND is_active = 1 ORDER BY created_at DESC LIMIT ?');
    $stmt->bind_param('i', $limit);
    $stmt->execute();
    return $stmt->get_result()->fetch_all(MYSQLI_ASSOC);
}

function fetch_products(array $filters = []): array
{
    $sql = 'SELECT p.*, c.name AS category_name, c.slug AS category_slug FROM products p
            JOIN categories c ON c.id = p.category_id WHERE p.is_active = 1';
    $params = [];
    $types = '';

    if (!empty($filters['category_slug'])) {
        $sql .= ' AND c.slug = ?';
        $params[] = $filters['category_slug'];
        $types .= 's';
    }

    if (!empty($filters['search'])) {
        $sql .= ' AND p.name LIKE ?';
        $params[] = '%' . $filters['search'] . '%';
        $types .= 's';
    }

    $sql .= ' ORDER BY p.name ASC';

    $stmt = db()->prepare($sql);
    if ($params) {
        $stmt->bind_param($types, ...$params);
    }
    $stmt->execute();
    return $stmt->get_result()->fetch_all(MYSQLI_ASSOC);
}

function fetch_product_by_slug(string $slug): ?array
{
    $stmt = db()->prepare('SELECT p.*, c.name AS category_name, c.slug AS category_slug
                            FROM products p JOIN categories c ON c.id = p.category_id
                            WHERE p.slug = ? AND p.is_active = 1 LIMIT 1');
    $stmt->bind_param('s', $slug);
    $stmt->execute();
    $row = $stmt->get_result()->fetch_assoc();
    return $row ?: null;
}

function fetch_related_products(int $categoryId, int $excludeId, int $limit = 4): array
{
    $stmt = db()->prepare('SELECT * FROM products WHERE category_id = ? AND id != ? AND is_active = 1 LIMIT ?');
    $stmt->bind_param('iii', $categoryId, $excludeId, $limit);
    $stmt->execute();
    return $stmt->get_result()->fetch_all(MYSQLI_ASSOC);
}

function fetch_active_careers(): array
{
    $result = db()->query('SELECT * FROM careers WHERE is_active = 1 ORDER BY created_at DESC');
    return $result ? $result->fetch_all(MYSQLI_ASSOC) : [];
}

function fetch_career_by_slug(string $slug): ?array
{
    $stmt = db()->prepare('SELECT * FROM careers WHERE slug = ? AND is_active = 1 LIMIT 1');
    $stmt->bind_param('s', $slug);
    $stmt->execute();
    $row = $stmt->get_result()->fetch_assoc();
    return $row ?: null;
}

function all_products_for_search(): array
{
    $result = db()->query('SELECT id, name, slug FROM products WHERE is_active = 1 ORDER BY name ASC');
    return $result ? $result->fetch_all(MYSQLI_ASSOC) : [];
}
