import re

with open('assets/css/style.css', 'r') as f:
    css = f.read()

# Replace the hero block from line 157 to 204
# We can use regex to replace everything from /* ---------- Hero ---------- */ to just before /* ---------- Section shells ---------- */

new_hero_css = """/* ---------- Hero ---------- */
#homeHero {
    position: relative;
    overflow: hidden;
    padding: 0;
    height: calc(100vh - 80px);
    min-height: 500px;
    max-height: 900px;
    display: flex;
    align-items: center;
}
.hero-picture {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    display: block;
    z-index: 0;
}
.hero-picture img {
    width: 100%;
    height: 100%;
    display: block;
    object-fit: cover;
    object-position: center bottom;
}
.hero-overlay {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    z-index: 1;
    display: flex;
    align-items: flex-start;
    justify-content: flex-start;
    flex-direction: column;
    text-align: left;
    background: linear-gradient(to right, rgba(0,0,0,0.6) 0%, rgba(0,0,0,0.2) 50%, transparent 100%);
    padding-top: max(40px, 8vh);
    padding-left: max(24px, 5vw);
    padding-right: 24px;
}
.hero-overlay h1 {
    color: #ffffff;
    text-shadow: 2px 2px 12px rgba(0,0,0,0.8);
    font-size: clamp(2.5rem, 4.5vw, 4.5rem);
    max-width: 900px;
    margin-bottom: 24px;
    margin-top: 0;
    line-height: 1.2;
}
.hero-overlay p {
    color: #ffffff;
    font-size: clamp(18px, 2.5vw, 24px);
    margin-bottom: 40px;
    text-shadow: 1px 1px 8px rgba(0,0,0,0.8);
    max-width: 600px;
    line-height: 1.5;
}
.btn-hero {
    padding: 16px 32px;
    font-size: 1.1rem;
    box-shadow: 0 4px 12px rgba(0,0,0,0.3);
}

.hero-badge {
    position: absolute; top: 8%; right: 6%;
    background: radial-gradient(circle at 30% 30%, #fbeec3, var(--color-gold));
    color: var(--color-primary-darker);
    border-radius: 50%;
    width: 112px; height: 112px;
    border: 4px solid #fff;
    display: flex; flex-direction: column; align-items: center; justify-content: center;
    text-align: center; font-weight: 700; box-shadow: 0 12px 28px rgba(0,0,0,0.25);
    z-index: 3;
}
.hero-badge .years { font-size: 1.6rem; line-height: 1; font-family: var(--font-heading); }
.hero-badge .label { font-size: 0.58rem; text-transform: uppercase; letter-spacing: 0.06em; font-weight: 700; margin-top: 2px; }

@media (max-width: 768px) {
    #homeHero {
        height: auto;
        min-height: calc(100vh - 60px);
        align-items: flex-end;
    }
    .hero-picture img {
        object-position: center;
    }
    .hero-overlay {
        position: relative;
        background: linear-gradient(to top, rgba(0,0,0,0.85) 0%, rgba(0,0,0,0.5) 40%, rgba(0,0,0,0.2) 100%);
        justify-content: flex-end;
        align-items: center;
        text-align: center;
        padding-top: 50px;
        padding-bottom: 40px;
        height: 100%;
        width: 100%;
    }
    .hero-overlay h1 {
        font-size: 2.2rem;
        text-shadow: 2px 2px 10px rgba(0,0,0,0.9);
        margin-bottom: 16px;
    }
    .hero-overlay p {
        font-size: 1.1rem;
        margin-bottom: 30px;
    }
    .hero-badge { width: 84px; height: 84px; top: 16px; right: 16px; }
}

"""

pattern = re.compile(r'/\* ---------- Hero ---------- \*/.*?/\* ---------- Section shells ---------- \*/', re.DOTALL)
css = pattern.sub(new_hero_css + "/* ---------- Section shells ---------- */", css)

with open('assets/css/style.css', 'w') as f:
    f.write(css)
