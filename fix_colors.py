import os

base_dir = "/Users/ayushman/Desktop/shreya-agro"
about_script = os.path.join(base_dir, "generate_about.py")

with open(about_script, "r", encoding="utf-8") as f:
    content = f.read()

# Replace Journey CSS
old_journey = """        /* Journey */
        .journey-section { padding: 100px 5%; overflow-x: auto; background: var(--primary-green); color: white; text-align: center; }
        .journey-section h2 { font-size: 36px; margin-bottom: 60px; color: var(--secondary-green); }
        .timeline { display: flex; justify-content: center; gap: 50px; align-items: flex-start; flex-wrap: wrap; }
        .timeline-item { width: 200px; text-align: center; position: relative; }
        .timeline-item h3 { font-size: 48px; font-weight: 800; color: rgba(255,255,255,0.2); margin-bottom: 10px; }
        .timeline-item h4 { font-size: 24px; color: var(--secondary-green); margin-bottom: 15px; }"""

new_journey = """        /* Journey */
        .journey-section { padding: 100px 5%; overflow-x: auto; background: linear-gradient(135deg, #11331e 0%, #1a4f2e 100%); color: white; text-align: center; }
        .journey-section h2 { font-size: 42px; margin-bottom: 60px; color: white !important; }
        .journey-section h2 span { color: var(--secondary-green); }
        .timeline { display: flex; justify-content: center; gap: 50px; align-items: flex-start; flex-wrap: wrap; }
        .timeline-item { width: 200px; text-align: center; position: relative; padding: 20px; background: rgba(255,255,255,0.03); border-radius: 16px; border: 1px solid rgba(255,255,255,0.1); box-shadow: 0 10px 30px rgba(0,0,0,0.2); transition: transform 0.3s; }
        .timeline-item:hover { transform: translateY(-5px); background: rgba(255,255,255,0.06); }
        .timeline-item h3 { font-size: 48px; font-weight: 800; background: linear-gradient(to right, #4ade80, #22c55e); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-bottom: 10px; }
        .timeline-item h4 { font-size: 22px; color: white; margin-bottom: 15px; font-weight: 600; }
        .timeline-item p { color: rgba(255,255,255,0.8); font-size: 15px; line-height: 1.6; }"""

if old_journey in content:
    content = content.replace(old_journey, new_journey)

# Replace Quality CSS
old_quality = """        /* Quality */
        .quality-section { padding: 100px 5%; background: var(--primary-green); color: white; text-align: center; }
        .quality-section h2 { font-size: 36px; margin-bottom: 24px; }
        .quality-section p { font-size: 18px; max-width: 800px; margin: 0 auto 60px; line-height: 1.7; opacity: 0.9; }"""

new_quality = """        /* Quality */
        .quality-section { padding: 100px 5%; background: linear-gradient(135deg, #1a4f2e 0%, #11331e 100%); color: white; text-align: center; }
        .quality-section h2 { font-size: 42px; margin-bottom: 24px; color: var(--secondary-green) !important; }
        .quality-section p { font-size: 18px; max-width: 800px; margin: 0 auto 60px; line-height: 1.7; color: rgba(255,255,255,0.9) !important; }"""

if old_quality in content:
    content = content.replace(old_quality, new_quality)

with open(about_script, "w", encoding="utf-8") as f:
    f.write(content)

print("CSS updated successfully.")
