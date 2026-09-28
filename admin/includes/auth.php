<?php
require_once __DIR__ . '/../../includes/functions.php';

if (session_status() === PHP_SESSION_NONE) {
    session_start();
}

function admin_logged_in(): bool
{
    return !empty($_SESSION['admin_id']);
}

function require_admin_login(): void
{
    if (!admin_logged_in()) {
        header('Location: /admin/login.php');
        exit;
    }
}

function admin_has_any_account(): bool
{
    $result = db()->query('SELECT id FROM admin_users LIMIT 1');
    return $result && $result->num_rows > 0;
}
