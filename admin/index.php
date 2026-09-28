<?php
require_once __DIR__ . '/includes/auth.php';
require_once __DIR__ . '/includes/layout.php';
require_admin_login();

$counts = [
    'products' => db()->query('SELECT COUNT(*) c FROM products')->fetch_assoc()['c'],
    'careers' => db()->query('SELECT COUNT(*) c FROM careers WHERE is_active = 1')->fetch_assoc()['c'],
    'enquiries' => db()->query("SELECT COUNT(*) c FROM enquiries WHERE status = 'new'")->fetch_assoc()['c'],
    'applications' => db()->query("SELECT COUNT(*) c FROM career_applications WHERE status = 'new'")->fetch_assoc()['c'],
];

admin_head('Dashboard');
?>
<h1>Dashboard</h1>
<div class="stat-cards">
    <div class="stat-card"><strong><?= (int)$counts['products'] ?></strong>Products</div>
    <div class="stat-card"><strong><?= (int)$counts['careers'] ?></strong>Active Openings</div>
    <div class="stat-card"><strong><?= (int)$counts['enquiries'] ?></strong>New Enquiries</div>
    <div class="stat-card"><strong><?= (int)$counts['applications'] ?></strong>New Applications</div>
</div>
<div class="card">
    <p>Use the sidebar to manage products, careers, and review incoming B2B enquiries and job applications.</p>
</div>
<?php admin_footer(); ?>
