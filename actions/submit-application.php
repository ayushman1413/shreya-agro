<?php
require_once __DIR__ . '/../includes/functions.php';

header('Content-Type: application/json');

function respond(bool $success, string $message = ''): void
{
    echo json_encode(['success' => $success, 'message' => $message]);
    exit;
}

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    respond(false, 'Invalid request method.');
}

if (!empty($_POST['website'])) {
    respond(true);
}

$fullName = trim($_POST['full_name'] ?? '');
$mobile = trim($_POST['mobile'] ?? '');
$email = trim($_POST['email'] ?? '');
$currentLocation = trim($_POST['current_location'] ?? '');

if ($fullName === '' || $mobile === '' || $email === '' || $currentLocation === '') {
    respond(false, 'Please fill in all required fields.');
}

if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
    respond(false, 'Please enter a valid email address.');
}

if (empty($_FILES['resume']) || $_FILES['resume']['error'] !== UPLOAD_ERR_OK) {
    respond(false, 'Please attach your resume (PDF or DOC).');
}

$allowedExtensions = ['pdf', 'doc', 'docx'];
$originalName = $_FILES['resume']['name'];
$ext = strtolower(pathinfo($originalName, PATHINFO_EXTENSION));

if (!in_array($ext, $allowedExtensions, true)) {
    respond(false, 'Resume must be a PDF or Word document.');
}

if ($_FILES['resume']['size'] > 5 * 1024 * 1024) {
    respond(false, 'Resume must be smaller than 5MB.');
}

$uploadDir = __DIR__ . '/../storage/resumes/';
if (!is_dir($uploadDir)) {
    mkdir($uploadDir, 0755, true);
}

$safeName = 'resume-' . date('Ymd-His') . '-' . bin2hex(random_bytes(4)) . '.' . $ext;
$destination = $uploadDir . $safeName;

if (!move_uploaded_file($_FILES['resume']['tmp_name'], $destination)) {
    respond(false, 'Could not save resume. Please try again.');
}

$careerId = !empty($_POST['career_id']) ? (int)$_POST['career_id'] : null;
$experience = trim($_POST['experience'] ?? '') ?: null;
$message = trim($_POST['message'] ?? '') ?: null;
$resumePath = 'storage/resumes/' . $safeName;

$stmt = db()->prepare(
    'INSERT INTO career_applications (career_id, full_name, mobile, email, current_location, experience, resume_path, message)
     VALUES (?, ?, ?, ?, ?, ?, ?, ?)'
);
$stmt->bind_param('isssssss', $careerId, $fullName, $mobile, $email, $currentLocation, $experience, $resumePath, $message);

if (!$stmt->execute()) {
    error_log('Application insert failed: ' . $stmt->error);
    respond(false, 'Something went wrong. Please try again shortly.');
}

$positionTitle = trim($_POST['position_title'] ?? 'General Application');

@mail(
    SITE_EMAIL,
    'New Job Application: ' . $positionTitle . ' — Shreya Agro Foods',
    "Position: $positionTitle\nName: $fullName\nMobile: $mobile\nEmail: $email\nLocation: $currentLocation\nExperience: $experience\n\nMessage:\n$message\n\nResume saved at: $resumePath",
    'From: no-reply@' . parse_url(SITE_URL, PHP_URL_HOST)
);

respond(true, 'Application received.');
