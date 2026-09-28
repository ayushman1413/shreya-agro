<?php
// One-time first-admin-account creation. Becomes inert automatically once an
// admin account exists, so it's safe to leave deployed.
require_once __DIR__ . '/includes/auth.php';

if (admin_has_any_account()) {
    header('Location: /admin/login.php');
    exit;
}

$error = '';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $username = trim($_POST['username'] ?? '');
    $password = $_POST['password'] ?? '';

    if (strlen($username) < 3 || strlen($password) < 8) {
        $error = 'Username must be at least 3 characters and password at least 8 characters.';
    } else {
        $hash = password_hash($password, PASSWORD_DEFAULT);
        $stmt = db()->prepare('INSERT INTO admin_users (username, password_hash) VALUES (?, ?)');
        $stmt->bind_param('ss', $username, $hash);
        $stmt->execute();
        header('Location: /admin/login.php');
        exit;
    }
}
?>
<!doctype html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>Create Admin Account — Shreya Agro Foods</title>
<style>
    body { font-family: -apple-system, Segoe UI, Arial, sans-serif; background: #14392a; display: flex; align-items: center; justify-content: center; height: 100vh; margin: 0; }
    .box { background: #fff; padding: 36px; border-radius: 10px; width: 100%; max-width: 360px; }
    h1 { font-size: 1.2rem; margin-bottom: 6px; }
    p { color: #666; font-size: 0.85rem; margin-top: 0; }
    label { display: block; font-weight: 600; font-size: 0.85rem; margin: 14px 0 6px; }
    input { width: 100%; padding: 10px 12px; border: 1px solid #ddd; border-radius: 6px; box-sizing: border-box; }
    button { margin-top: 20px; width: 100%; padding: 11px; background: #1f5d40; color: #fff; border: none; border-radius: 6px; cursor: pointer; font-weight: 600; }
    .error { color: #a13a34; font-size: 0.85rem; margin-top: 10px; }
</style>
</head>
<body>
    <div class="box">
        <h1>Create the first admin account</h1>
        <p>This screen only works while no admin account exists yet.</p>
        <?php if ($error): ?><div class="error"><?= htmlspecialchars($error) ?></div><?php endif; ?>
        <form method="post">
            <label>Username</label>
            <input type="text" name="username" required>
            <label>Password</label>
            <input type="password" name="password" required minlength="8">
            <button type="submit">Create Account</button>
        </form>
    </div>
</body>
</html>
