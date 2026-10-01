import re

path = "/Users/ayushman/Desktop/shreya-agro/assets/css/style.css"
with open(path, "r") as f:
    content = f.read()

# 1. Fix mobile menu toggle functionality
# main.js has toggle logic, but nav-toggle needs to be visible
# Wait, nav-toggle is ALREADY visible in style.css:
# @media (max-width: 900px) { ... .nav-toggle { display: block; order: 3; margin-left: 8px; } }

# 2. Fix category grid on mobile
content = content.replace(
    "@media (max-width: 520px) { .category-grid { grid-template-columns: repeat(2, 1fr); } }",
    "@media (max-width: 520px) { .category-grid { grid-template-columns: 1fr; } }"
)

# 3. Fix product grid and cards on mobile
old_product_grid = """@media (max-width: 520px) { .product-grid { grid-template-columns: repeat(2, 1fr); } }"""
new_product_grid = """@media (max-width: 520px) { 
    .product-grid { grid-template-columns: repeat(2, 1fr); gap: 12px; } 
    .product-card { padding: 14px; }
    .product-card h3 { font-size: 0.95rem; margin-bottom: 4px; }
    .product-card .pack-sizes { font-size: 0.75rem; margin-bottom: 10px; }
    .product-card .btn-link { font-size: 0.8rem; margin-bottom: 8px !important; }
    .product-card .enquire-link { padding: 8px 10px; font-size: 0.8rem; }
}"""
content = content.replace(old_product_grid, new_product_grid)

# 4. Make modal responsive for tiny screens
old_modal = """@media (max-width: 520px) {
    .modal-box { padding: 16px; }
}"""
new_modal = """@media (max-width: 520px) {
    .modal-box { padding: 16px; }
    .modal-product-panel, .modal-form-panel { padding: 12px; }
    .modal-form-panel h3 { font-size: 1.15rem; }
    .form-group input, .form-group select, .form-group textarea { padding: 8px 12px; font-size: 0.85rem; }
    .modal-close { top: 10px; right: 10px; font-size: 1.1rem; }
}"""
content = content.replace(old_modal, new_modal)

with open(path, "w") as f:
    f.write(content)
print("Updated style.css for mobile responsiveness.")
