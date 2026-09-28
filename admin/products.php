<?php
require_once __DIR__ . '/includes/auth.php';
require_once __DIR__ . '/includes/layout.php';
require_admin_login();

function slugify_p(string $text): string
{
    $text = strtolower(trim($text));
    $text = preg_replace('/[^a-z0-9]+/', '-', $text);
    return trim($text, '-');
}

if (isset($_GET['delete'])) {
    $stmt = db()->prepare('DELETE FROM products WHERE id = ?');
    $stmt->bind_param('i', (int)$_GET['delete']);
    $stmt->execute();
    header('Location: /admin/products.php?flash=deleted');
    exit;
}

if (isset($_GET['toggle_popular'])) {
    $stmt = db()->prepare('UPDATE products SET is_popular = 1 - is_popular WHERE id = ?');
    $stmt->bind_param('i', (int)$_GET['toggle_popular']);
    $stmt->execute();
    header('Location: /admin/products.php?flash=updated');
    exit;
}

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $id = (int)($_POST['id'] ?? 0);
    $categoryId = (int)($_POST['category_id'] ?? 0);
    $name = trim($_POST['name'] ?? '');
    $shortDescription = trim($_POST['short_description'] ?? '');
    $description = trim($_POST['description'] ?? '');
    $packSizes = trim($_POST['pack_sizes'] ?? '');
    $availableFor = trim($_POST['available_for'] ?? 'B2B / Wholesale');
    $moq = trim($_POST['moq'] ?? 'On Enquiry');
    $slug = slugify_p($name);

    if ($name !== '' && $categoryId) {
        if ($id) {
            $stmt = db()->prepare('UPDATE products SET category_id=?, name=?, slug=?, short_description=?, description=?, pack_sizes=?, available_for=?, moq=? WHERE id=?');
            $stmt->bind_param('isssssssi', $categoryId, $name, $slug, $shortDescription, $description, $packSizes, $availableFor, $moq, $id);
        } else {
            $stmt = db()->prepare('INSERT INTO products (category_id, name, slug, short_description, description, pack_sizes, available_for, moq) VALUES (?,?,?,?,?,?,?,?)');
            $stmt->bind_param('isssssss', $categoryId, $name, $slug, $shortDescription, $description, $packSizes, $availableFor, $moq);
        }
        $stmt->execute();
    }
    header('Location: /admin/products.php?flash=saved');
    exit;
}

$editing = null;
if (isset($_GET['edit'])) {
    $stmt = db()->prepare('SELECT * FROM products WHERE id = ?');
    $stmt->bind_param('i', (int)$_GET['edit']);
    $stmt->execute();
    $editing = $stmt->get_result()->fetch_assoc();
}

$categories = fetch_categories();
$products = db()->query('SELECT p.*, c.name AS category_name FROM products p JOIN categories c ON c.id = p.category_id ORDER BY p.created_at DESC')->fetch_all(MYSQLI_ASSOC);

admin_head('Products');
?>
<div class="top-bar"><h1>Products</h1></div>
<?php if (isset($_GET['flash'])): ?><div class="flash flash-success">Saved successfully.</div><?php endif; ?>

<div class="card">
    <h3><?= $editing ? 'Edit Product' : 'Add New Product' ?></h3>
    <form method="post">
        <input type="hidden" name="id" value="<?= (int)($editing['id'] ?? 0) ?>">
        <div class="form-row">
            <label>Category *</label>
            <select name="category_id" required>
                <option value="">Select category</option>
                <?php foreach ($categories as $cat): ?>
                <option value="<?= (int)$cat['id'] ?>" <?= (($editing['category_id'] ?? 0) == $cat['id']) ? 'selected' : '' ?>><?= htmlspecialchars($cat['name']) ?></option>
                <?php endforeach; ?>
            </select>
        </div>
        <div class="form-row"><label>Product Name *</label><input type="text" name="name" value="<?= htmlspecialchars($editing['name'] ?? '') ?>" required></div>
        <div class="form-row"><label>Short Description</label><input type="text" name="short_description" value="<?= htmlspecialchars($editing['short_description'] ?? '') ?>"></div>
        <div class="form-row"><label>Full Description</label><textarea name="description" rows="3"><?= htmlspecialchars($editing['description'] ?? '') ?></textarea></div>
        <div class="form-row"><label>Pack Sizes</label><input type="text" name="pack_sizes" placeholder="500g | 1kg | 5kg" value="<?= htmlspecialchars($editing['pack_sizes'] ?? '') ?>"></div>
        <div class="form-row"><label>Available For</label><input type="text" name="available_for" value="<?= htmlspecialchars($editing['available_for'] ?? 'B2B | Wholesale | Distribution') ?>"></div>
        <div class="form-row"><label>MOQ</label><input type="text" name="moq" value="<?= htmlspecialchars($editing['moq'] ?? 'On Enquiry') ?>"></div>
        <button class="btn" type="submit">Save</button>
        <?php if ($editing): ?><a href="/admin/products.php" class="btn btn-secondary" style="margin-left:8px;">Cancel</a><?php endif; ?>
    </form>
    <p style="font-size:0.8rem; color:#888; margin-top:10px;">Product images: upload the WebP file to <code>/assets/images/products/</code> via File Manager, named exactly as the product's slug (e.g. <code>mix-fruit-jam.webp</code>).</p>
</div>

<table>
    <thead><tr><th>Name</th><th>Category</th><th>Popular?</th><th>Actions</th></tr></thead>
    <tbody>
    <?php foreach ($products as $p): ?>
        <tr>
            <td><?= htmlspecialchars($p['name']) ?></td>
            <td><?= htmlspecialchars($p['category_name']) ?></td>
            <td><?= $p['is_popular'] ? 'Yes' : 'No' ?></td>
            <td>
                <a href="/admin/products.php?edit=<?= (int)$p['id'] ?>">Edit</a> ·
                <a href="/admin/products.php?toggle_popular=<?= (int)$p['id'] ?>"><?= $p['is_popular'] ? 'Unfeature' : 'Feature' ?></a> ·
                <a href="/products/<?= htmlspecialchars($p['slug']) ?>/" target="_blank">View</a> ·
                <a href="/admin/products.php?delete=<?= (int)$p['id'] ?>" onclick="return confirm('Delete this product?');">Delete</a>
            </td>
        </tr>
    <?php endforeach; ?>
    </tbody>
</table>
<?php admin_footer(); ?>
