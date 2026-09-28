-- Shreya Agro Foods — Database Schema
-- Import this in hPanel → phpMyAdmin after creating the MySQL database.

CREATE TABLE IF NOT EXISTS categories (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(120) NOT NULL,
    slug VARCHAR(140) NOT NULL UNIQUE,
    short_description VARCHAR(255) DEFAULT NULL,
    image VARCHAR(255) DEFAULT NULL,
    sort_order INT NOT NULL DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    category_id INT NOT NULL,
    name VARCHAR(160) NOT NULL,
    slug VARCHAR(180) NOT NULL UNIQUE,
    short_description VARCHAR(255) DEFAULT NULL,
    description TEXT DEFAULT NULL,
    pack_sizes VARCHAR(120) DEFAULT NULL,       -- e.g. "500g | 1kg | 5kg"
    product_type VARCHAR(120) DEFAULT NULL,
    available_for VARCHAR(120) DEFAULT 'B2B / Wholesale',
    moq VARCHAR(80) DEFAULT 'On Enquiry',
    main_image VARCHAR(255) DEFAULT NULL,
    is_popular TINYINT(1) NOT NULL DEFAULT 0,
    is_active TINYINT(1) NOT NULL DEFAULT 1,
    meta_title VARCHAR(180) DEFAULT NULL,
    meta_description VARCHAR(255) DEFAULT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS product_images (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT NOT NULL,
    image VARCHAR(255) NOT NULL,
    alt_text VARCHAR(255) DEFAULT NULL,
    sort_order INT NOT NULL DEFAULT 0,
    FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS enquiries (
    id INT AUTO_INCREMENT PRIMARY KEY,
    enquiry_type VARCHAR(60) NOT NULL DEFAULT 'General Enquiry', -- Product Enquiry, B2B/Wholesale, Distribution, Business Partnership, General Enquiry, Career
    product_id INT DEFAULT NULL,
    name VARCHAR(160) NOT NULL,
    company_name VARCHAR(160) DEFAULT NULL,
    location VARCHAR(160) DEFAULT NULL,
    mobile VARCHAR(30) NOT NULL,
    email VARCHAR(160) DEFAULT NULL,
    requirement TEXT DEFAULT NULL,
    message TEXT DEFAULT NULL,
    status VARCHAR(30) NOT NULL DEFAULT 'new', -- new, contacted, closed
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS careers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(160) NOT NULL,
    slug VARCHAR(180) NOT NULL UNIQUE,
    location VARCHAR(120) NOT NULL DEFAULT 'Mumbai',
    employment_type VARCHAR(60) NOT NULL DEFAULT 'Full Time',
    description TEXT DEFAULT NULL,
    is_active TINYINT(1) NOT NULL DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS career_applications (
    id INT AUTO_INCREMENT PRIMARY KEY,
    career_id INT DEFAULT NULL,
    full_name VARCHAR(160) NOT NULL,
    mobile VARCHAR(30) NOT NULL,
    email VARCHAR(160) NOT NULL,
    current_location VARCHAR(160) DEFAULT NULL,
    experience VARCHAR(80) DEFAULT NULL,
    resume_path VARCHAR(255) DEFAULT NULL,
    message TEXT DEFAULT NULL,
    status VARCHAR(30) NOT NULL DEFAULT 'new',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (career_id) REFERENCES careers(id) ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS admin_users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(80) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Seed categories (matches the 12-tile "A Taste for Every Occasion" grid)
INSERT INTO categories (name, slug, short_description, image, sort_order) VALUES
('Masalas', 'masalas', 'Authentic spice blends for everyday Indian cooking.', 'shreya-agro-foods-masalas.webp', 1),
('Biscuits', 'biscuits', 'Crisp, wholesome biscuits for every occasion.', 'shreya-agro-foods-biscuits.webp', 2),
('Sweets', 'sweets', 'Traditional Indian sweets made with authentic recipes.', 'shreya-agro-foods-sweets.webp', 3),
('Soan Papdi', 'soan-papdi', 'Flaky, melt-in-the-mouth soan papdi.', 'shreya-agro-foods-soan-papdi.webp', 4),
('Jams', 'jams', 'Fruit jams made with quality natural ingredients.', 'shreya-agro-foods-jams.webp', 5),
('Syrups', 'syrups', 'Refreshing syrups for every season.', 'shreya-agro-foods-syrups.webp', 6),
('Chikky', 'chikky', 'Crunchy jaggery and nut chikky.', 'shreya-agro-foods-chikky.webp', 7),
('Jaggery', 'jaggery', 'Pure, naturally processed jaggery.', 'shreya-agro-foods-jaggery.webp', 8),
('Chutneys', 'chutneys', 'Flavourful chutneys for every meal.', 'shreya-agro-foods-chutneys.webp', 9),
('Oils', 'oils', 'Quality cooking oils for households and businesses.', 'shreya-agro-foods-oils.webp', 10),
('Flour', 'flour', 'Finely milled flour for daily cooking.', 'shreya-agro-foods-flour.webp', 11),
('Rice', 'rice', 'Premium quality rice varieties.', 'shreya-agro-foods-rice.webp', 12);

-- Seed popular products (matches "Our Popular Products" row)
INSERT INTO products (category_id, name, slug, short_description, description, pack_sizes, available_for, moq, main_image, is_popular) VALUES
((SELECT id FROM categories WHERE slug='jams'), 'Mix Fruit Jam', 'mix-fruit-jam', 'Made with the finest fruits, our Mix Fruit Jam brings the perfect blend of taste, richness and natural goodness.', 'Made with the finest fruits, our Mix Fruit Jam brings the perfect blend of taste, richness and natural goodness.', '500g | 1kg | 5kg', 'B2B | Wholesale | Distribution', 'On Enquiry', 'shreya-agro-foods-mix-fruit-jam.webp', 1),
((SELECT id FROM categories WHERE slug='masalas'), 'Garam Masala', 'garam-masala', 'A rich, aromatic blend of traditional Indian spices.', 'A rich, aromatic blend of traditional Indian spices, crafted for authentic home-style flavour at scale.', '100g | 200g | 500g', 'B2B | Wholesale | Distribution', 'On Enquiry', 'shreya-agro-foods-garam-masala.webp', 1),
((SELECT id FROM categories WHERE slug='soan-papdi'), 'Soan Papdi', 'soan-papdi-sweet', 'Flaky, melt-in-the-mouth traditional Indian sweet.', 'Our Soan Papdi is prepared using traditional methods for an authentic, flaky texture and rich taste.', '250g | 500g | 1kg', 'B2B | Wholesale | Distribution', 'On Enquiry', 'shreya-agro-foods-soan-papdi-product.webp', 1),
((SELECT id FROM categories WHERE slug='chutneys'), 'Tomato Ketchup', 'tomato-ketchup', 'Rich, tangy tomato ketchup made from quality tomatoes.', 'Rich, tangy tomato ketchup made from quality tomatoes, perfect for households and foodservice.', '500g | 1kg', 'B2B | Wholesale | Distribution', 'On Enquiry', 'shreya-agro-foods-tomato-ketchup.webp', 1);

-- Seed careers (matches "Current Openings")
INSERT INTO careers (title, slug, location, employment_type, description, is_active) VALUES
('Sales & Business Development Executive', 'sales-business-development-executive', 'Mumbai', 'Full Time', 'Drive B2B sales and business development for Shreya Agro Foods across assigned territories.', 1),
('Marketing Executive', 'marketing-executive', 'Mumbai', 'Full Time', 'Support marketing campaigns, brand visibility and lead generation for Shreya Agro Foods.', 1),
('Accounts Executive', 'accounts-executive', 'Mumbai', 'Full Time', 'Manage day-to-day accounting, invoicing and financial records.', 1);
