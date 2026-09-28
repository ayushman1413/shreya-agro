<?php
require_once __DIR__ . '/config.php';

function db(): mysqli
{
    static $conn = null;

    if ($conn !== null) {
        return $conn;
    }

    $conn = mysqli_init();
    mysqli_report(MYSQLI_REPORT_OFF);

    if (!$conn->real_connect(DB_HOST, DB_USER, DB_PASS, DB_NAME)) {
        error_log('Database connection failed: ' . mysqli_connect_error());
        http_response_code(500);
        die('Site temporarily unavailable. Please try again shortly.');
    }

    $conn->set_charset('utf8mb4');

    return $conn;
}
