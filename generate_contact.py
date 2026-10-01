import os

def generate_contact_page():
    base_dir = "/Users/ayushman/Desktop/shreya-agro/contact-us"
    os.makedirs(base_dir, exist_ok=True)
    
    html_content = """<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Contact Shreya Agro Foods | B2B & Business Enquiries</title>
    <meta name="description" content="Get in touch with Shreya Agro Foods for business partnerships, product enquiries, distribution opportunities, and career openings.">
    <link rel="canonical" href="https://www.shreyaagrofoods.com/contact-us/">
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
        .hero { position: relative; padding: 120px 20px; text-align: center; color: white; background: linear-gradient(rgba(26, 79, 46, 0.8), rgba(26, 79, 46, 0.8)), url('https://images.unsplash.com/photo-1542838132-92c53300491e?auto=format&fit=crop&q=80') center/cover; }
        .hero h1 { font-size: 48px; font-weight: 800; margin-bottom: 24px; }
        .hero p { font-size: 20px; max-width: 800px; margin: 0 auto 40px; line-height: 1.6; }
        .hero .btn { background: var(--secondary-green); color: var(--primary-green); padding: 16px 32px; border-radius: 8px; font-weight: 700; text-decoration: none; margin: 0 10px; display: inline-block; transition: transform 0.3s ease; }
        .hero .btn-outline { background: transparent; border: 2px solid white; color: white; }

        /* Contact Section */
        .contact-section { display: flex; flex-wrap: wrap; padding: 100px 5%; background: white; gap: 60px; justify-content: space-between; }
        .contact-info { flex: 1; min-width: 300px; }
        .contact-info h2 { font-size: 36px; color: var(--primary-green); margin-bottom: 30px; }
        .info-item { display: flex; align-items: flex-start; gap: 15px; margin-bottom: 30px; }
        .info-icon { font-size: 24px; }
        .info-text h4 { font-size: 18px; margin-bottom: 5px; color: var(--primary-green); }
        .info-text p { font-size: 16px; color: #555; }
        
        .contact-form-wrapper { flex: 1; min-width: 300px; background: var(--bg-color); padding: 40px; border-radius: 16px; box-shadow: 0 10px 30px rgba(0,0,0,0.05); }
        .contact-form-wrapper h3 { font-size: 28px; margin-bottom: 24px; color: var(--primary-green); }
        .form-group { margin-bottom: 20px; }
        .form-group label { display: block; margin-bottom: 8px; font-weight: 600; font-size: 14px; }
        .form-control { width: 100%; padding: 12px 16px; border: 1px solid #ccc; border-radius: 8px; font-family: inherit; font-size: 16px; }
        .submit-btn { width: 100%; padding: 16px; background: var(--primary-green); color: white; border: none; border-radius: 8px; font-size: 18px; font-weight: 700; cursor: pointer; transition: background 0.3s; }
        .submit-btn:hover { background: #123820; }

        /* B2B Banner */
        .b2b-banner { padding: 80px 5%; background: var(--primary-green); color: white; text-align: center; }
        .b2b-banner h2 { font-size: 36px; margin-bottom: 20px; color: var(--secondary-green); }
        .b2b-banner p { font-size: 20px; margin-bottom: 30px; opacity: 0.9; }
        .b2b-banner .btn { background: white; color: var(--primary-green); padding: 16px 32px; border-radius: 8px; font-weight: 700; text-decoration: none; display: inline-block; }

        /* Careers Section */
        .careers-intro { padding: 100px 5% 50px; text-align: center; background: #eef2eb; }
        .careers-intro h2 { font-size: 36px; color: var(--primary-green); margin-bottom: 20px; }
        .careers-intro p { font-size: 18px; max-width: 700px; margin: 0 auto; color: #555; line-height: 1.6; }

        /* Why Work With Us */
        .why-work { padding: 50px 5% 100px; background: #eef2eb; }
        .why-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 30px; }
        .why-card { background: white; padding: 30px; border-radius: 12px; box-shadow: 0 5px 15px rgba(0,0,0,0.05); text-align: center; }
        .why-icon { font-size: 40px; margin-bottom: 15px; }
        .why-card h3 { font-size: 20px; color: var(--primary-green); margin-bottom: 10px; }

        /* Current Openings */
        .openings-section { padding: 100px 5%; background: white; }
        .openings-section h2 { font-size: 36px; color: var(--primary-green); margin-bottom: 40px; text-align: center; }
        .job-card { display: flex; justify-content: space-between; align-items: center; padding: 30px; border: 1px solid #eee; border-radius: 12px; margin-bottom: 20px; transition: box-shadow 0.3s; flex-wrap: wrap; gap: 20px; }
        .job-card:hover { box-shadow: 0 10px 20px rgba(0,0,0,0.05); }
        .job-info h3 { font-size: 24px; margin-bottom: 10px; }
        .job-meta { color: #666; font-size: 15px; display: flex; gap: 15px; }
        .job-card .btn { padding: 12px 24px; background: var(--secondary-green); color: var(--primary-green); font-weight: 700; border-radius: 6px; text-decoration: none; border: none; cursor: pointer; }

        /* Map Section */
        .map-section { width: 100%; height: 500px; background: #ddd; }
        .map-section iframe { width: 100%; height: 100%; border: none; }

        /* Modal Styles */
        .modal { display: none; position: fixed; z-index: 1000; left: 0; top: 0; width: 100%; height: 100%; background-color: rgba(0,0,0,0.6); overflow: auto; }
        .modal-content { background-color: white; margin: 5% auto; padding: 40px; border-radius: 16px; width: 90%; max-width: 600px; position: relative; }
        .close-modal { position: absolute; right: 20px; top: 15px; font-size: 28px; font-weight: bold; cursor: pointer; color: #aaa; }
        .close-modal:hover { color: #333; }
        .success-msg { display: none; text-align: center; padding: 40px 20px; }
        .success-msg h3 { color: var(--primary-green); font-size: 28px; margin-bottom: 15px; }
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
                <a href="/about-us/" style="text-decoration:none; color:var(--text-charcoal); font-weight:600;">About</a>
                <a href="/contact-us/" style="text-decoration:none; color:var(--primary-green); font-weight:800;">Contact</a>
            </nav>
        </div>
    </header>

    <section class="hero">
        <h1>Let's Connect</h1>
        <p>Whether you're looking for a business partnership, product enquiry, distribution opportunity or career with us, we'd love to hear from you.</p>
        <div>
            <a href="#contact-form" class="btn">Make a B2B Enquiry</a>
            <a href="#careers" class="btn btn-outline">View Careers</a>
        </div>
    </section>

    <section class="contact-section">
        <div class="contact-info">
            <h2>Get in Touch</h2>
            <div class="info-item">
                <div class="info-icon">📍</div>
                <div class="info-text">
                    <h4>Our Office</h4>
                    <p>Mumbai, Maharashtra, India</p>
                </div>
            </div>
            <div class="info-item">
                <div class="info-icon">📞</div>
                <div class="info-text">
                    <h4>Phone</h4>
                    <p>+91 98765 43210</p>
                </div>
            </div>
            <div class="info-item">
                <div class="info-icon">✉️</div>
                <div class="info-text">
                    <h4>Email</h4>
                    <p>info@shreyaagrofoods.com</p>
                </div>
            </div>
            <div style="margin-top: 50px; padding-top: 30px; border-top: 1px solid #eee;">
                <h4 style="font-size: 20px; color: var(--primary-green); margin-bottom: 10px;">Business Enquiries</h4>
                <p style="color: #666; line-height: 1.6;">For products, distribution and partnerships.</p>
            </div>
        </div>
        
        <div class="contact-form-wrapper" id="contact-form">
            <h3>Send Us an Enquiry</h3>
            <form onsubmit="event.preventDefault(); alert('Enquiry Submitted!');">
                <div class="form-group">
                    <label>Name*</label>
                    <input type="text" class="form-control" placeholder="Enter your name" required>
                </div>
                <div class="form-group">
                    <label>Company Name</label>
                    <input type="text" class="form-control" placeholder="Enter company name">
                </div>
                <div style="display:flex; gap:20px;">
                    <div class="form-group" style="flex:1;">
                        <label>Mobile Number*</label>
                        <input type="tel" class="form-control" placeholder="Enter mobile number" required>
                    </div>
                    <div class="form-group" style="flex:1;">
                        <label>Email</label>
                        <input type="email" class="form-control" placeholder="Enter email address">
                    </div>
                </div>
                <div style="display:flex; gap:20px;">
                    <div class="form-group" style="flex:1;">
                        <label>Location*</label>
                        <input type="text" class="form-control" placeholder="City / State" required>
                    </div>
                    <div class="form-group" style="flex:1;">
                        <label>Enquiry Type</label>
                        <select class="form-control">
                            <option>Product Enquiry</option>
                            <option>B2B / Wholesale</option>
                            <option>Distribution</option>
                            <option>Business Partnership</option>
                            <option>General Enquiry</option>
                            <option>Career</option>
                        </select>
                    </div>
                </div>
                <div class="form-group">
                    <label>Message</label>
                    <textarea class="form-control" rows="4" placeholder="Tell us how we can help you..."></textarea>
                </div>
                <button type="submit" class="submit-btn">Submit Enquiry</button>
            </form>
        </div>
    </section>

    <section class="b2b-banner">
        <h2>Looking for a Long-Term FMCG Partner?</h2>
        <p>Connect with Shreya Agro Foods for B2B, wholesale, distribution and business opportunities.</p>
        <a href="#contact-form" class="btn js-open-enquiry" data-enquiry-type="B2B Partnership">Become a B2B Partner &rarr;</a>
    </section>

    <section class="careers-intro" id="careers">
        <h2>Build Your Career With Shreya Agro Foods</h2>
        <p>We are always looking for passionate, talented and motivated people who want to grow with a growing FMCG organization. Explore opportunities. Grow with us. Make an impact.</p>
    </section>

    <section class="why-work">
        <div class="why-grid">
            <div class="why-card">
                <div class="why-icon">🌱</div>
                <h3>Growth</h3>
                <p>Opportunities to learn, develop and grow.</p>
            </div>
            <div class="why-card">
                <div class="why-icon">🤝</div>
                <h3>Collaboration</h3>
                <p>Work with a team that values ideas and teamwork.</p>
            </div>
            <div class="why-card">
                <div class="why-icon">💡</div>
                <h3>Innovation</h3>
                <p>Be part of a company continuously evolving with the market.</p>
            </div>
            <div class="why-card">
                <div class="why-icon">🚀</div>
                <h3>Opportunity</h3>
                <p>Build your career in a growing FMCG environment.</p>
            </div>
        </div>
    </section>

    <section class="openings-section">
        <h2>Current Openings</h2>
        
        <div class="job-card">
            <div class="job-info">
                <h3>Sales & Business Development Executive</h3>
                <div class="job-meta">
                    <span>📍 Mumbai</span>
                    <span>💼 Full Time</span>
                </div>
            </div>
            <button class="btn js-apply-btn" data-job="Sales & Business Development Executive">View Details &rarr;</button>
        </div>
        
        <div class="job-card">
            <div class="job-info">
                <h3>Marketing Executive</h3>
                <div class="job-meta">
                    <span>📍 Mumbai</span>
                    <span>💼 Full Time</span>
                </div>
            </div>
            <button class="btn js-apply-btn" data-job="Marketing Executive">View Details &rarr;</button>
        </div>
        
        <div class="job-card">
            <div class="job-info">
                <h3>Accounts Executive</h3>
                <div class="job-meta">
                    <span>📍 Mumbai</span>
                    <span>💼 Full Time</span>
                </div>
            </div>
            <button class="btn js-apply-btn" data-job="Accounts Executive">View Details &rarr;</button>
        </div>
    </section>
    
    <section class="map-section">
        <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d241316.6433258416!2d72.7410999553648!3d19.082522321482813!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3be7c6306644edc1%3A0x5da4ed8f8d648c69!2sMumbai%2C%20Maharashtra!5e0!3m2!1sen!2sin!4v1690000000000!5m2!1sen!2sin" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
    </section>

    <!-- Career Application Modal -->
    <div id="careerModal" class="modal">
        <div class="modal-content">
            <span class="close-modal">&times;</span>
            <div id="applicationFormContainer">
                <h3 style="font-size:24px; color:var(--primary-green); margin-bottom:20px;">Apply for this Position</h3>
                <p style="margin-bottom:20px; font-weight:600; color:#555;">Position: <span id="jobTitleSpan"></span></p>
                <form id="careerForm">
                    <div class="form-group">
                        <label>Full Name*</label>
                        <input type="text" class="form-control" required placeholder="Enter your name">
                    </div>
                    <div style="display:flex; gap:20px;">
                        <div class="form-group" style="flex:1;">
                            <label>Mobile Number*</label>
                            <input type="tel" class="form-control" required placeholder="Enter mobile number">
                        </div>
                        <div class="form-group" style="flex:1;">
                            <label>Email*</label>
                            <input type="email" class="form-control" required placeholder="Enter email">
                        </div>
                    </div>
                    <div style="display:flex; gap:20px;">
                        <div class="form-group" style="flex:1;">
                            <label>Current Location*</label>
                            <input type="text" class="form-control" required placeholder="City">
                        </div>
                        <div class="form-group" style="flex:1;">
                            <label>Experience</label>
                            <input type="text" class="form-control" placeholder="Years of experience">
                        </div>
                    </div>
                    <div class="form-group">
                        <label>Resume*</label>
                        <input type="file" class="form-control" accept=".pdf,.doc,.docx" required>
                        <small style="color:#666;">Upload PDF / DOC</small>
                    </div>
                    <div class="form-group">
                        <label>Message</label>
                        <textarea class="form-control" rows="3" placeholder="Tell us briefly about yourself..."></textarea>
                    </div>
                    <button type="submit" class="submit-btn">Submit Application</button>
                </form>
            </div>
            <div id="applicationSuccess" class="success-msg">
                <h3>Application Submitted Successfully! 🎉</h3>
                <p style="color:#555; line-height:1.6; font-size:18px;">Thank you for your interest in joining Shreya Agro Foods. Our team will review your application and contact you if your profile matches an available opportunity.</p>
                <button class="btn close-success" style="margin-top:20px; padding:12px 24px; background:var(--primary-green); color:white; border:none; border-radius:6px; cursor:pointer;">Close</button>
            </div>
        </div>
    </div>

    <script>
        // Career Modal Logic
        const modal = document.getElementById("careerModal");
        const span = document.getElementsByClassName("close-modal")[0];
        const closeSuccess = document.querySelector(".close-success");
        const applyBtns = document.querySelectorAll(".js-apply-btn");
        const jobTitleSpan = document.getElementById("jobTitleSpan");
        const formContainer = document.getElementById("applicationFormContainer");
        const successContainer = document.getElementById("applicationSuccess");
        const careerForm = document.getElementById("careerForm");

        applyBtns.forEach(btn => {
            btn.addEventListener("click", function() {
                jobTitleSpan.textContent = this.getAttribute("data-job");
                formContainer.style.display = "block";
                successContainer.style.display = "none";
                careerForm.reset();
                modal.style.display = "block";
            });
        });

        span.onclick = function() { modal.style.display = "none"; }
        closeSuccess.onclick = function() { modal.style.display = "none"; }
        
        window.onclick = function(event) {
            if (event.target == modal) {
                modal.style.display = "none";
            }
        }

        careerForm.addEventListener("submit", function(e) {
            e.preventDefault();
            formContainer.style.display = "none";
            successContainer.style.display = "block";
        });
    </script>

    <script src="/assets/js/main.js" defer></script>
</body>
</html>"""
    
    with open(os.path.join(base_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(html_content)
        
    print("Contact page generated successfully!")

if __name__ == "__main__":
    generate_contact_page()
