<?php
require_once __DIR__ . '/includes/auth.php';
require_once __DIR__ . '/includes/layout.php';
require_admin_login();

function slugify(string $text): string
{
    $text = strtolower(trim($text));
    $text = preg_replace('/[^a-z0-9]+/', '-', $text);
    return trim($text, '-');
}

$flash = '';

// Delete
if (isset($_GET['delete'])) {
    $stmt = db()->prepare('DELETE FROM careers WHERE id = ?');
    $stmt->bind_param('i', (int)$_GET['delete']);
    $stmt->execute();
    header('Location: /admin/careers.php?flash=deleted');
    exit;
}

// Toggle active
if (isset($_GET['toggle'])) {
    $stmt = db()->prepare('UPDATE careers SET is_active = 1 - is_active WHERE id = ?');
    $stmt->bind_param('i', (int)$_GET['toggle']);
    $stmt->execute();
    header('Location: /admin/careers.php?flash=updated');
    exit;
}

// Create / update
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $id = (int)($_POST['id'] ?? 0);
    $title = trim($_POST['title'] ?? '');
    $location = trim($_POST['location'] ?? 'Mumbai');
    $type = trim($_POST['employment_type'] ?? 'Full Time');
    $description = trim($_POST['description'] ?? '');
    $slug = slugify($title);

    if ($title !== '') {
        if ($id) {
            $stmt = db()->prepare('UPDATE careers SET title=?, slug=?, location=?, employment_type=?, description=? WHERE id=?');
            $stmt->bind_param('sssssi', $title, $slug, $location, $type, $description, $id);
        } else {
            $stmt = db()->prepare('INSERT INTO careers (title, slug, location, employment_type, description) VALUES (?,?,?,?,?)');
            $stmt->bind_param('sssss', $title, $slug, $location, $type, $description);
        }
        $stmt->execute();
    }
    header('Location: /admin/careers.php?flash=saved');
    exit;
}

$editing = null;
if (isset($_GET['edit'])) {
    $stmt = db()->prepare('SELECT * FROM careers WHERE id = ?');
    $stmt->bind_param('i', (int)$_GET['edit']);
    $stmt->execute();
    $editing = $stmt->get_result()->fetch_assoc();
}

$careers = db()->query('SELECT * FROM careers ORDER BY created_at DESC')->fetch_all(MYSQLI_ASSOC);

admin_head('Careers');
?>
<div class="top-bar"><h1>Careers</h1></div>
<?php if (isset($_GET['flash'])): ?><div class="flash flash-success">Saved successfully.</div><?php endif; ?>

<div class="card">
    <h3><?= $editing ? 'Edit Opening' : 'Add New Opening' ?></h3>
    <form method="post">
        <input type="hidden" name="id" value="<?= (int)($editing['id'] ?? 0) ?>">
        <div class="form-row"><label>Job Title *</label><input type="text" name="title" value="<?= htmlspecialchars($editing['title'] ?? '') ?>" required></div>
        <div class="form-row"><label>Location</label><input type="text" name="location" value="<?= htmlspecialchars($editing['location'] ?? 'Mumbai') ?>"></div>
        <div class="form-row"><label>Employment Type</label><input type="text" name="employment_type" value="<?= htmlspecialchars($editing['employment_type'] ?? 'Full Time') ?>"></div>
        <div class="form-row"><label>Description</label><textarea name="description" rows="3"><?= htmlspecialchars($editing['description'] ?? '') ?></textarea></div>
        <button class="btn" type="submit">Save</button>
        <?php if ($editing): ?><a href="/admin/careers.php" class="btn btn-secondary" style="margin-left:8px;">Cancel</a><?php endif; ?>
    </form>
</div>

<table>
    <thead><tr><th>Title</th><th>Location</th><th>Type</th><th>Status</th><th>Actions</th></tr></thead>
    <tbody>
    <?php foreach ($careers as $job): ?>
        <tr>
            <td><?= htmlspecialchars($job['title']) ?></td>
            <td><?= htmlspecialchars($job['location']) ?></td>
            <td><?= htmlspecialchars($job['employment_type']) ?></td>
            <td><?= $job['is_active'] ? 'Active' : 'Hidden' ?></td>
            <td>
                <a href="/admin/careers.php?edit=<?= (int)$job['id'] ?>">Edit</a> ·
                <a href="/admin/careers.php?toggle=<?= (int)$job['id'] ?>"><?= $job['is_active'] ? 'Hide' : 'Show' ?></a> ·
                <a href="/admin/careers.php?delete=<?= (int)$job['id'] ?>" onclick="return confirm('Delete this opening?');">Delete</a>
            </td>
        </tr>
    <?php endforeach; ?>
    </tbody>
</table>
<?php admin_footer(); ?>
