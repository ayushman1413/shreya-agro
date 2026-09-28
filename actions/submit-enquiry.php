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

// Honeypot: bots fill hidden fields, real users never see them.
if (!empty($_POST['website'])) {
    respond(true); // silently pretend success so bots move on
}

$name = trim($_POST['name'] ?? '');
$mobile = trim($_POST['mobile'] ?? '');
$location = trim($_POST['location'] ?? '');

if ($name === '' || $mobile === '' || $location === '') {
    respond(false, 'Please fill in all required fields.');
}

if (!preg_match('/^[0-9+\-\s()]{7,20}$/', $mobile)) {
    respond(false, 'Please enter a valid mobile number.');
}

$companyName = trim($_POST['company_name'] ?? '') ?: null;
$email = trim($_POST['email'] ?? '') ?: null;
if ($email && !filter_var($email, FILTER_VALIDATE_EMAIL)) {
    respond(false, 'Please enter a valid email address.');
}

$enquiryType = trim($_POST['enquiry_type'] ?? 'General Enquiry');
$requirement = trim($_POST['requirement'] ?? '') ?: null;
$message = trim($_POST['message'] ?? '') ?: null;
$productId = !empty($_POST['product_id']) ? (int)$_POST['product_id'] : null;

$stmt = db()->prepare(
    'INSERT INTO enquiries (enquiry_type, product_id, name, company_name, location, mobile, email, requirement, message)
     VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)'
);
$stmt->bind_param('sisssssss', $enquiryType, $productId, $name, $companyName, $location, $mobile, $email, $requirement, $message);

if (!$stmt->execute()) {
    error_log('Enquiry insert failed: ' . $stmt->error);
    respond(false, 'Something went wrong. Please try again shortly.');
}

// Optional: notify the sales team by email (works once the server's mail() is configured).
@mail(
    SITE_EMAIL,
    'New ' . $enquiryType . ' — Shreya Agro Foods website',
    "Name: $name\nCompany: $companyName\nLocation: $location\nMobile: $mobile\nEmail: $email\n\nRequirement:\n$requirement\n\nMessage:\n$message",
    'From: no-reply@' . parse_url(SITE_URL, PHP_URL_HOST)
);

respond(true, 'Enquiry received.');
