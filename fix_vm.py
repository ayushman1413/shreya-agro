import os

base_dir = "/Users/ayushman/Desktop/shreya-agro"
about_script = os.path.join(base_dir, "generate_about.py")

with open(about_script, "r", encoding="utf-8") as f:
    content = f.read()

# Replace VM Section CSS
old_vm_css = """        /* Vision & Mission */
        .vm-section { padding: 100px 5%; display: flex; gap: 40px; flex-wrap: wrap; }
        .vm-card { flex: 1; min-width: 300px; background: white; padding: 50px; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.05); text-align: center; border-bottom: 5px solid var(--secondary-green); transition: transform 0.3s; }
        .vm-card:hover { transform: translateY(-10px); }
        .vm-card h3 { font-size: 24px; color: var(--primary-green); margin-bottom: 20px; letter-spacing: 1px; }
        .vm-card p { font-size: 18px; line-height: 1.6; }"""

new_vm_css = """        /* Vision & Mission */
        .vm-section { padding: 80px 5%; display: flex; gap: 30px; flex-wrap: wrap; justify-content: center; background: var(--bg-color); }
        .vm-card { flex: 1; min-width: 300px; max-width: 600px; padding: 60px 40px; border-radius: 24px; box-shadow: 0 20px 40px rgba(0,0,0,0.1); text-align: center; color: white; position: relative; overflow: hidden; transition: transform 0.4s ease, box-shadow 0.4s ease; border: 1px solid rgba(255,255,255,0.1); }
        .vm-card:hover { transform: translateY(-10px); box-shadow: 0 30px 60px rgba(0,0,0,0.2); }
        .vm-card::before { content: ''; position: absolute; inset: 0; background: linear-gradient(135deg, rgba(26, 79, 46, 0.85) 0%, rgba(17, 51, 30, 0.95) 100%); z-index: 1; }
        .vm-card-bg { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; z-index: 0; filter: grayscale(20%); transition: transform 0.8s ease; }
        .vm-card:hover .vm-card-bg { transform: scale(1.05); }
        .vm-content { position: relative; z-index: 2; display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100%; }
        .vm-icon { width: 80px; height: 80px; background: rgba(255,255,255,0.1); border-radius: 50%; display: flex; align-items: center; justify-content: center; margin-bottom: 24px; backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.2); }
        .vm-icon svg { width: 40px; height: 40px; fill: var(--secondary-green); }
        .vm-card h3 { font-size: 28px; color: white; margin-bottom: 20px; letter-spacing: 2px; font-weight: 800; }
        .vm-card p { font-size: 18px; line-height: 1.7; color: rgba(255,255,255,0.9); font-weight: 400; margin: 0; }"""

if old_vm_css in content:
    content = content.replace(old_vm_css, new_vm_css)

# Replace VM HTML
old_vm_html = """    <section class="vm-section">
        <div class="vm-card">
            <span style="font-size:40px; margin-bottom:20px; display:block;">👁️</span>
            <h3>OUR VISION</h3>
            <p>To build a trusted FMCG brand that brings quality, innovation and value to consumers across India and beyond.</p>
        </div>
        <div class="vm-card">
            <span style="font-size:40px; margin-bottom:20px; display:block;">🎯</span>
            <h3>OUR MISSION</h3>
            <p>To consistently deliver high-quality products while building lasting relationships with customers, partners and communities.</p>
        </div>
    </section>"""

new_vm_html = """    <section class="vm-section">
        <div class="vm-card">
            <img src="/assets/images/products/Shreya Farm-to-Table Product Showcase.png" class="vm-card-bg" alt="Vision Background">
            <div class="vm-content">
                <div class="vm-icon">
                    <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M12 4.5C7 4.5 2.73 7.61 1 12c1.73 4.39 6 7.5 11 7.5s9.27-3.11 11-7.5c-1.73-4.39-6-7.5-11-7.5zM12 17c-2.76 0-5-2.24-5-5s2.24-5 5-5 5 2.24 5 5-2.24 5-5 5zm0-8c-1.66 0-3 1.34-3 3s1.34 3 3 3 3-1.34 3-3-1.34-3-3-3z"/></svg>
                </div>
                <h3>OUR VISION</h3>
                <p>To build a trusted FMCG brand that brings quality, innovation and value to consumers across India and beyond.</p>
            </div>
        </div>
        <div class="vm-card">
            <img src="/assets/images/products/Shreya Wheat Flour Kitchen Still Life-1.png" class="vm-card-bg" alt="Mission Background">
            <div class="vm-content">
                <div class="vm-icon">
                    <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8zm3-8c0 1.66-1.34 3-3 3s-3-1.34-3-3 1.34-3 3-3 3 1.34 3 3zm-3-1.5c-.83 0-1.5.67-1.5 1.5s.67 1.5 1.5 1.5 1.5-.67 1.5-1.5-.67-1.5-1.5-1.5z"/><path d="M12 6c-3.31 0-6 2.69-6 6h2c0-2.21 1.79-4 4-4v-2zm0 12c3.31 0 6-2.69 6-6h-2c0 2.21-1.79 4-4 4v2z"/></svg>
                </div>
                <h3>OUR MISSION</h3>
                <p>To consistently deliver high-quality products while building lasting relationships with customers, partners and communities.</p>
            </div>
        </div>
    </section>"""

if old_vm_html in content:
    content = content.replace(old_vm_html, new_vm_html)

with open(about_script, "w", encoding="utf-8") as f:
    f.write(content)

print("Vision & Mission section updated successfully.")
