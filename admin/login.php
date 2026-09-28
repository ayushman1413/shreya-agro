<?php
require_once __DIR__ . '/includes/auth.php';

if (!admin_has_any_account()) {
    header('Location: /admin/setup.php');
    exit;
}

if (admin_logged_in()) {
    header('Location: /admin/');
    exit;
}

$error = '';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $username = trim($_POST['username'] ?? '');
    $password = $_POST['password'] ?? '';

    $stmt = db()->prepare('SELECT id, password_hash FROM admin_users WHERE username = ? LIMIT 1');
    $stmt->bind_param('s', $username);
    $stmt->execute();
    $user = $stmt->get_result()->fetch_assoc();

    if ($user && password_verify($password, $user['password_hash'])) {
        session_regenerate_id(true);
        $_SESSION['admin_id'] = $user['id'];
        header('Location: /admin/');
        exit;
    }
    $error = 'Invalid username or password.';
}
?>
<!doctype html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>Admin Login — Shreya Agro Foods</title>
<style>
    body { font-family: -apple-system, Segoe UI, Arial, sans-serif; background: #14392a; display: flex; align-items: center; justify-content: center; height: 100vh; margin: 0; }
    .box { background: #fff; padding: 36px; border-radius: 10px; width: 100%; max-width: 340px; }
    h1 { font-size: 1.2rem; }
    label { display: block; font-weight: 600; font-size: 0.85rem; margin: 14px 0 6px; }
    input { width: 100%; padding: 10px 12px; border: 1px solid #ddd; border-radius: 6px; box-sizing: border-box; }
    button { margin-top: 20px; width: 100%; padding: 11px; background: #1f5d40; color: #fff; border: none; border-radius: 6px; cursor: pointer; font-weight: 600; }
    .error { color: #a13a34; font-size: 0.85rem; margin-top: 10px; }
</style>
</head>
<body>
    <div class="box">
        <h1>Shreya Agro Foods — Admin</h1>
        <?php if ($error): ?><div class="error"><?= htmlspecialchars($error) ?></div><?php endif; ?>
        <form method="post">
            <label>Username</label>
            <input type="text" name="username" required autofocus>
            <label>Password</label>
            <input type="password" name="password" required>
            <button type="submit">Log In</button>
        </form>
    </div>
</body>
</html>
