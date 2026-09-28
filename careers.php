<?php
// Careers is combined into the Contact page per the design brief.
// Redirect keeps the clean /careers/ URL working without duplicate content.
header('Location: /contact-us/#careers', true, 301);
exit;
