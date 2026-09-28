<?php
require_once __DIR__ . '/includes/auth.php';
require_admin_login();

$id = (int)($_GET['id'] ?? 0);
$stmt = db()->prepare('SELECT resume_path, full_name FROM career_applications WHERE id = ?');
$stmt->bind_param('i', $id);
$stmt->execute();
$row = $stmt->get_result()->fetch_assoc();

if (!$row || !$row['resume_path']) {
    http_response_code(404);
    exit('Resume not found.');
}

$path = realpath(__DIR__ . '/../' . $row['resume_path']);
$storageRoot = realpath(__DIR__ . '/../storage/resumes');

if (!$path || strpos($path, $storageRoot) !== 0 || !is_file($path)) {
    http_response_code(404);
    exit('Resume not found.');
}

$ext = pathinfo($path, PATHINFO_EXTENSION);
header('Content-Type: application/octet-stream');
header('Content-Disposition: attachment; filename="' . preg_replace('/[^a-zA-Z0-9-_]/', '_', $row['full_name']) . '.' . $ext . '"');
header('Content-Length: ' . filesize($path));
readfile($path);
