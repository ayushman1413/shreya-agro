<?php
require_once __DIR__ . '/includes/auth.php';
require_once __DIR__ . '/includes/layout.php';
require_admin_login();

if (isset($_GET['status'], $_GET['id'])) {
    $allowed = ['new', 'contacted', 'closed'];
    if (in_array($_GET['status'], $allowed, true)) {
        $stmt = db()->prepare('UPDATE enquiries SET status = ? WHERE id = ?');
        $stmt->bind_param('si', $_GET['status'], (int)$_GET['id']);
        $stmt->execute();
    }
    header('Location: /admin/enquiries.php');
    exit;
}

$enquiries = db()->query(
    "SELECT e.*, p.name AS product_name FROM enquiries e
     LEFT JOIN products p ON p.id = e.product_id
     ORDER BY e.created_at DESC LIMIT 200"
)->fetch_all(MYSQLI_ASSOC);

admin_head('Enquiries');
?>
<h1>Enquiries</h1>
<table>
    <thead><tr><th>Date</th><th>Type</th><th>Name</th><th>Company</th><th>Mobile</th><th>Product</th><th>Status</th><th>Actions</th></tr></thead>
    <tbody>
    <?php foreach ($enquiries as $en): ?>
        <tr>
            <td><?= htmlspecialchars(date('d M Y', strtotime($en['created_at']))) ?></td>
            <td><?= htmlspecialchars($en['enquiry_type']) ?></td>
            <td><?= htmlspecialchars($en['name']) ?><br><small><?= htmlspecialchars($en['email'] ?? '') ?></small></td>
            <td><?= htmlspecialchars($en['company_name'] ?? '—') ?></td>
            <td><?= htmlspecialchars($en['mobile']) ?></td>
            <td><?= htmlspecialchars($en['product_name'] ?? '—') ?></td>
            <td><?= htmlspecialchars($en['status']) ?></td>
            <td>
                <a href="/admin/enquiries.php?id=<?= (int)$en['id'] ?>&status=contacted">Mark Contacted</a> ·
                <a href="/admin/enquiries.php?id=<?= (int)$en['id'] ?>&status=closed">Close</a>
            </td>
        </tr>
    <?php endforeach; ?>
    </tbody>
</table>
<?php admin_footer(); ?>
