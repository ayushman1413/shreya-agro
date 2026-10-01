import os

def generate_about_page():
    base_dir = "/Users/ayushman/Desktop/shreya-agro/about-us"
    os.makedirs(base_dir, exist_ok=True)
    
    html_content = """<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>About Shreya Agro Foods | 26+ Years of FMCG Experience</title>
    <meta name="description" content="Shreya Agro Foods is an FMCG company with 26+ years of experience, offering quality food products and B2B business opportunities across India.">
    <link rel="canonical" href="https://www.shreyaagrofoods.com/about-us/">
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="/assets/css/style.css">
    <style>
        :root {
            --primary-green: #1a4f2e;
            --secondary-green: #4ade80;
            --bg-color: #F7F9F4;
            --text-charcoal: #333333;
        }
        body { font-family: 'Plus Jakarta Sans', sans-serif; color: var(--text-charcoal); background: var(--bg-color); }
        
        /* Hero Section */
        .hero { position: relative; padding: 120px 20px; text-align: center; color: white; background: linear-gradient(rgba(26, 79, 46, 0.8), rgba(26, 79, 46, 0.8)), url('https://images.unsplash.com/photo-1595858117769-95fb425ba473?auto=format&fit=crop&q=80') center/cover; }
        .hero-label { font-size: 14px; text-transform: uppercase; letter-spacing: 2px; font-weight: 700; color: var(--secondary-green); margin-bottom: 20px; display: block; }
        .hero h1 { font-size: 48px; font-weight: 800; margin-bottom: 24px; }
        .hero p { font-size: 20px; max-width: 800px; margin: 0 auto 40px; line-height: 1.6; }
        .hero .btn { background: var(--secondary-green); color: var(--primary-green); padding: 16px 32px; border-radius: 8px; font-weight: 700; text-decoration: none; margin: 0 10px; display: inline-block; transition: transform 0.3s ease; }
        .hero .btn:hover { transform: translateY(-3px); }
        .hero .btn-outline { background: transparent; border: 2px solid white; color: white; }

        /* Company Intro */
        .intro-section { display: flex; flex-wrap: wrap; align-items: center; padding: 100px 5%; background: white; gap: 60px; }
        .intro-img { flex: 1; min-width: 300px; border-radius: 20px; overflow: hidden; box-shadow: 0 20px 40px rgba(0,0,0,0.1); }
        .intro-img img { width: 100%; display: block; }
        .intro-content { flex: 1; min-width: 300px; }
        .intro-content h2 { font-size: 36px; color: var(--primary-green); margin-bottom: 24px; }
        .intro-content p { font-size: 18px; line-height: 1.7; margin-bottom: 20px; color: #555; }
        .stats { display: flex; gap: 30px; margin-top: 40px; }
        .stat-item h3 { font-size: 32px; color: var(--secondary-green); margin-bottom: 5px; }
        .stat-item p { font-size: 14px; font-weight: 600; text-transform: uppercase; }

        /* Vision & Mission */
        .vm-section { padding: 100px 5%; display: flex; gap: 40px; flex-wrap: wrap; }
        .vm-card { flex: 1; min-width: 300px; background: white; padding: 50px; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.05); text-align: center; border-bottom: 5px solid var(--secondary-green); transition: transform 0.3s; }
        .vm-card:hover { transform: translateY(-10px); }
        .vm-card h3 { font-size: 24px; color: var(--primary-green); margin-bottom: 20px; letter-spacing: 1px; }
        .vm-card p { font-size: 18px; line-height: 1.6; }

        /* Why Us */
        .why-section { padding: 100px 5%; background: white; text-align: center; }
        .why-section h2 { font-size: 36px; color: var(--primary-green); margin-bottom: 60px; }
        .why-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 30px; }
        .why-card { padding: 30px; background: var(--bg-color); border-radius: 16px; }
        .why-icon { font-size: 40px; margin-bottom: 20px; }
        .why-card h3 { font-size: 20px; color: var(--primary-green); margin-bottom: 15px; }
        
        /* Journey */
        .journey-section { padding: 100px 5%; overflow-x: auto; background: var(--primary-green); color: white; text-align: center; }
        .journey-section h2 { font-size: 36px; margin-bottom: 60px; color: var(--secondary-green); }
        .timeline { display: flex; justify-content: center; gap: 50px; align-items: flex-start; flex-wrap: wrap; }
        .timeline-item { width: 200px; text-align: center; position: relative; }
        .timeline-item h3 { font-size: 48px; font-weight: 800; color: rgba(255,255,255,0.2); margin-bottom: 10px; }
        .timeline-item h4 { font-size: 24px; color: var(--secondary-green); margin-bottom: 15px; }
        
        /* Quality */
        .quality-section { padding: 100px 5%; background: var(--primary-green); color: white; text-align: center; }
        .quality-section h2 { font-size: 36px; margin-bottom: 24px; }
        .quality-section p { font-size: 18px; max-width: 800px; margin: 0 auto 60px; line-height: 1.7; opacity: 0.9; }
        .q-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px; }
        .q-grid img { width: 100%; height: 250px; object-fit: cover; border-radius: 12px; }

        /* CTA */
        .cta-section { padding: 100px 5%; text-align: center; background: white; }
        .cta-section h2 { font-size: 36px; color: var(--primary-green); margin-bottom: 20px; }
        .cta-section p { font-size: 20px; margin-bottom: 40px; color: #555; }
        .cta-btn { font-size: 18px; padding: 16px 40px; background: var(--primary-green); color: white; border-radius: 8px; font-weight: 700; text-decoration: none; border: none; cursor: pointer; transition: background 0.3s; }
        .cta-btn:hover { background: #123820; }
    </style>
</head>
<body>

    <header class="site-header">
        <div class="container" style="display:flex; justify-content:space-between; align-items:center; padding: 20px 5%;">
            <a href="/" class="brand" style="text-decoration:none; display:flex; align-items:center; gap:10px;">
                <img src="/assets/images/shreya-agro-foods-logo.png" alt="Shreya Agro Foods" width="50">
                <span style="font-weight:800; font-size:24px; color:var(--primary-green);">Shreya Agro</span>
            </a>
            <nav style="display:flex; gap:30px;">
                <a href="/" style="text-decoration:none; color:var(--text-charcoal); font-weight:600;">Home</a>
                <a href="/products/" style="text-decoration:none; color:var(--text-charcoal); font-weight:600;">Products</a>
                <a href="/about-us/" style="text-decoration:none; color:var(--primary-green); font-weight:800;">About</a>
                <a href="/contact-us/" style="text-decoration:none; color:var(--text-charcoal); font-weight:600;">Contact</a>
            </nav>
        </div>
    </header>

    <section class="hero">
        <span class="hero-label">ABOUT SHREYA AGRO FOODS</span>
        <h1>26+ Years of Building Trust Through Quality</h1>
        <p>From our roots in Mumbai to becoming a trusted name in the FMCG industry, Shreya Agro Foods has been driven by a simple vision — to create quality food products that become a part of everyday lives.</p>
        <div>
            <a href="/products/" class="btn">Explore Our Products</a>
            <a href="#" class="btn btn-outline js-open-enquiry">Become a B2B Partner</a>
        </div>
    </section>

    <section class="intro-section">
        <div class="intro-img">
            <img src="https://images.unsplash.com/photo-1621415065099-31ffb91a78ee?auto=format&fit=crop&q=80" alt="Shreya Agro Foods Factory" loading="lazy">
        </div>
        <div class="intro-content">
            <h2>A Legacy Built on Quality & Trust</h2>
            <p>Shreya Agro Foods Ltd. is one of India's leading FMCG companies, with a legacy spanning over 26 years. Rooted in Mumbai, the company was built with an entrepreneurial vision and a passion for delivering quality food products to consumers across markets.</p>
            <p>Over the years, Shreya Agro Foods has grown through a strong commitment to quality, innovation, customer satisfaction and long-term relationships.</p>
            <div class="stats">
                <div class="stat-item">
                    <h3>26+</h3>
                    <p>Years of Experience</p>
                </div>
                <div class="stat-item">
                    <h3>Pan India</h3>
                    <p>Market Presence</p>
                </div>
                <div class="stat-item">
                    <h3>Quality First</h3>
                    <p>Our Commitment</p>
                </div>
            </div>
        </div>
    </section>

    <section class="vm-section">
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
    </section>

    <section class="why-section">
        <h2>Why Shreya Agro Foods?</h2>
        <div class="why-grid">
            <div class="why-card">
                <div class="why-icon">⭐</div>
                <h3>Quality Driven</h3>
                <p>Quality at every stage, from sourcing to final product.</p>
            </div>
            <div class="why-card">
                <div class="why-icon">👥</div>
                <h3>Customer Focused</h3>
                <p>Understanding customer needs and continuously improving.</p>
            </div>
            <div class="why-card">
                <div class="why-icon">💡</div>
                <h3>Innovation</h3>
                <p>Creating products that meet changing consumer preferences.</p>
            </div>
            <div class="why-card">
                <div class="why-icon">🤝</div>
                <h3>Trusted Relationships</h3>
                <p>Building long-term partnerships with distributors, retailers and businesses.</p>
            </div>
        </div>
    </section>

    <section class="journey-section">
        <h2>Our Journey</h2>
        <div class="timeline">
            <div class="timeline-item">
                <h3>1999</h3>
                <h4>Company begins its journey</h4>
                <p>Started from humble beginnings with a focus on quality.</p>
            </div>
            <div class="timeline-item">
                <h3>Growth</h3>
                <h4>Expanding products and market presence</h4>
                <p>Scaling our operations and diversifying our product line.</p>
            </div>
            <div class="timeline-item">
                <h3>Expansion</h3>
                <h4>Building stronger distribution networks</h4>
                <p>Reaching more households across the country.</p>
            </div>
            <div class="timeline-item">
                <h3>Today</h3>
                <h4>A growing FMCG company serving diverse markets</h4>
                <p>Continuing our legacy of trust and quality.</p>
            </div>
        </div>
    </section>

    <section class="quality-section">
        <h2>Quality Is at the Heart of Everything We Do</h2>
        <p>We believe quality is not just a standard — it is a responsibility. From raw material selection to manufacturing, packaging and distribution, we focus on maintaining consistent quality across every product.</p>
        <div class="q-grid">
            <img src="https://images.unsplash.com/photo-1563124508-25f05df39f37?auto=format&fit=crop&w=500&q=80" alt="Manufacturing" loading="lazy">
            <img src="https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?auto=format&fit=crop&w=500&q=80" alt="Quality Checking" loading="lazy">
            <img src="https://images.unsplash.com/photo-1587293852726-70cdb56c2866?auto=format&fit=crop&w=500&q=80" alt="Packaging" loading="lazy">
            <img src="https://images.unsplash.com/photo-1605338902581-2292f32a76f2?auto=format&fit=crop&w=500&q=80" alt="Finished Products" loading="lazy">
        </div>
    </section>

    <section class="cta-section">
        <h2>Looking for a Reliable FMCG Partner?</h2>
        <p>Partner with Shreya Agro Foods for quality products, reliable supply and long-term business opportunities.</p>
        <button class="cta-btn js-open-enquiry" data-enquiry-type="B2B Partnership">Make a B2B Enquiry</button>
    </section>

    <script src="/assets/js/main.js" defer></script>
</body>
</html>"""
    
    with open(os.path.join(base_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(html_content)
        
    print("About page generated successfully!")

if __name__ == "__main__":
    generate_about_page()
