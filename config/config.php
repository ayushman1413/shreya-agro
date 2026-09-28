<?php
// Shreya Agro Foods — Site configuration
// Update DB credentials from hPanel → Databases → MySQL Databases after creating the database.

define('DB_HOST', getenv('DB_HOST') ?: 'localhost');
define('DB_NAME', getenv('DB_NAME') ?: 'shreya_agro');
define('DB_USER', getenv('DB_USER') ?: 'shreya_agro_user');
define('DB_PASS', getenv('DB_PASS') ?: '');

define('SITE_NAME', 'Shreya Agro Foods');
define('SITE_URL', getenv('SITE_URL') ?: 'https://www.shreyaagrofoods.com');
define('SITE_TAGLINE', 'Authentic Taste. Trusted Quality.');
define('SITE_PHONE', '+91 XXXXX XXXXX');
define('SITE_EMAIL', 'info@shreyaagrofoods.com');
define('SITE_ADDRESS', 'Mumbai, Maharashtra, India');

error_reporting(E_ALL);
ini_set('display_errors', getenv('APP_DEBUG') === '1' ? '1' : '0');
