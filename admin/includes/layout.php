<?php
/** Minimal admin chrome — kept deliberately plain, no framework, matches PHP+MySQL scope. */
function admin_head(string $title): void
{
    ?>
    <!doctype html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="robots" content="noindex, nofollow">
    <title><?= htmlspecialchars($title) ?> — Shreya Agro Foods Admin</title>
    <style>
        body { font-family: -apple-system, Segoe UI, Arial, sans-serif; background: #f4f6f2; margin: 0; color: #262626; }
        .admin-wrap { display: flex; min-height: 100vh; }
        .admin-nav { width: 220px; background: #14392a; color: #fff; padding: 24px 0; flex-shrink: 0; }
        .admin-nav a { display: block; padding: 10px 24px; color: rgba(255,255,255,0.8); text-decoration: none; font-size: 0.92rem; }
        .admin-nav a:hover, .admin-nav a.active { background: rgba(255,255,255,0.08); color: #fff; }
        .admin-nav .brand { padding: 0 24px 20px; font-weight: 700; font-size: 1.05rem; }
        .admin-main { flex: 1; padding: 32px; max-width: 1100px; }
        table { width: 100%; border-collapse: collapse; background: #fff; border-radius: 8px; overflow: hidden; box-shadow: 0 1px 4px rgba(0,0,0,0.06); }
        th, td { text-align: left; padding: 12px 14px; border-bottom: 1px solid #eee; font-size: 0.9rem; }
        th { background: #eef3e6; }
        .btn { display: inline-block; padding: 8px 16px; border-radius: 6px; background: #1f5d40; color: #fff; text-decoration: none; border: none; cursor: pointer; font-size: 0.85rem; }
        .btn-danger { background: #a13a34; }
        .btn-secondary { background: #6b7568; }
        .card { background: #fff; padding: 24px; border-radius: 8px; box-shadow: 0 1px 4px rgba(0,0,0,0.06); margin-bottom: 20px; }
        .form-row { margin-bottom: 14px; }
        .form-row label { display: block; font-weight: 600; font-size: 0.85rem; margin-bottom: 4px; }
        .form-row input, .form-row select, .form-row textarea { width: 100%; padding: 9px 12px; border: 1px solid #d8ddd2; border-radius: 6px; font-size: 0.9rem; box-sizing: border-box; }
        .stat-cards { display: flex; gap: 16px; margin-bottom: 24px; flex-wrap: wrap; }
        .stat-card { background: #fff; padding: 20px 24px; border-radius: 8px; box-shadow: 0 1px 4px rgba(0,0,0,0.06); min-width: 150px; }
        .stat-card strong { display: block; font-size: 1.6rem; color: #1f5d40; }
        .flash { padding: 10px 14px; border-radius: 6px; margin-bottom: 16px; font-size: 0.88rem; }
        .flash-success { background: #e9f6ea; color: #14392a; }
        .flash-error { background: #fdeceb; color: #a13a34; }
        h1 { font-size: 1.4rem; }
        .top-bar { display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; }
    </style>
    </head>
    <body>
    <div class="admin-wrap">
    <nav class="admin-nav">
        <div class="brand">Shreya Agro Admin</div>
        <a href="/admin/">Dashboard</a>
        <a href="/admin/products.php">Products</a>
        <a href="/admin/careers.php">Careers</a>
        <a href="/admin/enquiries.php">Enquiries</a>
        <a href="/admin/applications.php">Job Applications</a>
        <a href="/admin/logout.php">Logout</a>
    </nav>
    <main class="admin-main">
    <?php
}

function admin_footer(): void
{
    ?>
    </main>
    </div>
    </body>
    </html>
    <?php
}
