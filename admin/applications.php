<?php
require_once __DIR__ . '/includes/auth.php';
require_once __DIR__ . '/includes/layout.php';
require_admin_login();

if (isset($_GET['status'], $_GET['id'])) {
    $allowed = ['new', 'reviewed', 'closed'];
    if (in_array($_GET['status'], $allowed, true)) {
        $stmt = db()->prepare('UPDATE career_applications SET status = ? WHERE id = ?');
        $stmt->bind_param('si', $_GET['status'], (int)$_GET['id']);
        $stmt->execute();
    }
    header('Location: /admin/applications.php');
    exit;
}

$applications = db()->query(
    "SELECT a.*, c.title AS career_title FROM career_applications a
     LEFT JOIN careers c ON c.id = a.career_id
     ORDER BY a.created_at DESC LIMIT 200"
)->fetch_all(MYSQLI_ASSOC);

admin_head('Job Applications');
?>
<h1>Job Applications</h1>
<table>
    <thead><tr><th>Date</th><th>Position</th><th>Name</th><th>Mobile / Email</th><th>Resume</th><th>Status</th><th>Actions</th></tr></thead>
    <tbody>
    <?php foreach ($applications as $app): ?>
        <tr>
            <td><?= htmlspecialchars(date('d M Y', strtotime($app['created_at']))) ?></td>
            <td><?= htmlspecialchars($app['career_title'] ?? 'General Application') ?></td>
            <td><?= htmlspecialchars($app['full_name']) ?></td>
            <td><?= htmlspecialchars($app['mobile']) ?><br><small><?= htmlspecialchars($app['email']) ?></small></td>
            <td><a href="/admin/download-resume.php?id=<?= (int)$app['id'] ?>">Download</a></td>
            <td><?= htmlspecialchars($app['status']) ?></td>
            <td>
                <a href="/admin/applications.php?id=<?= (int)$app['id'] ?>&status=reviewed">Mark Reviewed</a> ·
                <a href="/admin/applications.php?id=<?= (int)$app['id'] ?>&status=closed">Close</a>
            </td>
        </tr>
    <?php endforeach; ?>
    </tbody>
</table>
<?php admin_footer(); ?>
