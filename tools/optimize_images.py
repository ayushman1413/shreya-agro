#!/usr/bin/env python3
"""One-off image pipeline: turns the large source PNG/WebP artwork into compressed,
responsive WebP files with SEO-friendly names (shreya-agro-foods-<name>-<width>.webp).

Usage:  python3 tools/optimize_images.py <source-dir> [<extra-source-dir>]

<source-dir> is searched (recursively) for the original files listed in SOURCES below.
Outputs go to assets/images/ and assets/images/og/. Re-running is safe (files are overwritten).
"""
import os
import sys
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "assets", "images")
OG = os.path.join(OUT, "og")

# name -> (source file name, [output widths])
PRODUCT_W = [480, 960]
SOURCES = {
    # product photography
    "basmati-rice": ("Premium-Basmati-Rice-Still-Life.png", PRODUCT_W),
    "mango-pickle": ("Rustic-Shreya-Pickle-Product-Display.png", PRODUCT_W),
    "mango-mix-pickle-display": ("Shreya-Mango-and-Mix-Pickle-Display.png", PRODUCT_W),
    "pickles-fresh-ingredients": ("Shreya-Pickles-with-Fresh-Ingredients.png", PRODUCT_W),
    "farm-fresh-pickles": ("Shreya-Pickles_-Farm-Fresh-Flavour.png", PRODUCT_W),
    "besan-chakki-atta": ("Shreya-Besan-Chakki-Ka-Atta-Package.png", PRODUCT_W),
    "hardball-candy": ("Shreya-Candy-Sweetscape.png", PRODUCT_W),
    "ginger-garlic-paste": ("Shreya-Ginger-Garlic-Paste-Still-Life.png", PRODUCT_W),
    "gulab-jamun-rasgulla": ("Shreya-Gulab-Jamun-and-Rasgulla-Duo.png", PRODUCT_W),
    "jaggery-cubes-powder": ("Shreya-Jaggery-Cubes-and-Powder-Duo.png", PRODUCT_W),
    "jaggery-jars": ("Shreya-Jaggery-Cubes-and-Powder-Jars.png", PRODUCT_W),
    "chicken-meat-masalas": ("Shreya-Masalas_-Taste-the-Difference.png", PRODUCT_W),
    "mix-fruit-jam": ("Shreya-Mix-Fruits-Jam-Jars.png", PRODUCT_W),
    "rusk-toast-display": ("Shreya-Rusk-Toast-Product-Display.png", PRODUCT_W),
    "rusk-toast-tea-time": ("Shreya-Rusk-Toast-Tea-Time-Still-Life.png", PRODUCT_W),
    "soan-papdi-collection": ("Shreya-Soan-Papdi-Flavour-Collection.png", PRODUCT_W),
    "spice-powder-collection": ("Shreya-Spice-Powder-Collection.png", PRODUCT_W),
    "spice-powders-poster": ("Shreya-Spice-Powders-Poster.png", PRODUCT_W),
    "wheat-flour-atta": ("Shreya-Wheat-Flour-Atta-Still-Life-2.png", PRODUCT_W),
    "wheat-flour-kitchen": ("Shreya-Wheat-Flour-Kitchen-Still-Life-1.png", PRODUCT_W),
    # category / extra photography that already existed as WebP in images.zip
    "biscuits": ("shreya-agro-foods-biscuits.webp", PRODUCT_W),
    "chikki": ("shreya-agro-foods-chikky.webp", PRODUCT_W),
    "mint-chutney": ("shreya-agro-foods-chutneys.webp", PRODUCT_W),
    "tomato-ketchup": ("tomato-ketchup.webp", PRODUCT_W),
    "jam-jar-closeup": ("mix-fruit-jam.webp", PRODUCT_W),
    "soan-papdi-box": ("shreya-agro-foods-soan-papdi.webp", PRODUCT_W),
    "rice-sack": ("shreya-agro-foods-rice.webp", PRODUCT_W),
    "spices-still-life": ("shreya-agro-foods-masalas.webp", [480, 800]),
    # site-wide imagery
    "hero-desktop": ("Shreya-Spices-at-Golden-Hour.png", [1200, 1800]),
    "hero-mobile": ("Shreya-Farm-to-Table-Collection.png", [640, 887]),
    "quality-facility": ("shreya-agro-foods-quality-facility.webp", [480, 900]),
}

# OG (social share) images: name -> (source key from SOURCES, background colour)
OG_BG = (247, 249, 244)


def find(src_dirs, filename):
    for d in src_dirs:
        for dirpath, _dirs, files in os.walk(d):
            if "__MACOSX" in dirpath:
                continue
            if filename in files:
                return os.path.join(dirpath, filename)
    return None


def save_webp(im, path, width, quality=78):
    if im.width > width:
        h = round(im.height * width / im.width)
        im = im.resize((width, h), Image.LANCZOS)
    im.save(path, "WEBP", quality=quality, method=6)
    return os.path.getsize(path)


def main():
    src_dirs = sys.argv[1:]
    if not src_dirs:
        sys.exit(__doc__)
    os.makedirs(OUT, exist_ok=True)
    os.makedirs(OG, exist_ok=True)
    total = 0
    for name, (fname, widths) in SOURCES.items():
        p = find(src_dirs, fname)
        if not p:
            print("MISSING", fname)
            continue
        im = Image.open(p).convert("RGB")
        for w in widths:
            out = os.path.join(OUT, f"shreya-agro-foods-{name}-{w}.webp")
            total += save_webp(im, out, w)
        # 1200x630 JPG for link previews (WhatsApp / LinkedIn / Facebook)
        if name not in ("hero-mobile", "quality-facility"):
            canvas = Image.new("RGB", (1200, 630), OG_BG)
            if name == "hero-desktop":
                c = im.copy()
                c = c.resize((1200, round(c.height * 1200 / c.width)))
                canvas.paste(c, (0, (630 - c.height) // 2))
            else:
                c = im.copy()
                c.thumbnail((1100, 590))
                canvas.paste(c, ((1200 - c.width) // 2, (630 - c.height) // 2))
            canvas.save(os.path.join(OG, f"shreya-agro-foods-{name}.jpg"), "JPEG", quality=82, optimize=True)
    # logo (transparent) + favicon set
    logo_src = find(src_dirs, "shreya-agro-foods-logo.png")
    if logo_src:
        lg = Image.open(logo_src).convert("RGBA")
        bbox = lg.getbbox()
        lg = lg.crop(bbox)
        for w in (160, 320):
            h = round(lg.height * w / lg.width)
            lg.resize((w, h), Image.LANCZOS).save(os.path.join(OUT, f"shreya-agro-foods-logo-{w}.webp"), "WEBP", quality=88, method=6)
        sq = Image.new("RGBA", (max(lg.size),) * 2, (255, 255, 255, 0))
        sq.paste(lg, ((sq.width - lg.width) // 2, (sq.height - lg.height) // 2))
        sq.resize((192, 192), Image.LANCZOS).save(os.path.join(OUT, "shreya-agro-foods-icon-192.png"), optimize=True)
        sq.resize((48, 48), Image.LANCZOS).save(os.path.join(OUT, "shreya-agro-foods-icon-48.png"), optimize=True)
        white = Image.new("RGB", sq.size, "white")
        white.paste(sq, mask=sq.split()[3])
        white.resize((180, 180), Image.LANCZOS).save(os.path.join(OUT, "shreya-agro-foods-apple-touch-icon.png"), optimize=True)
        print("logo size", lg.size)
    print("total webp bytes: %d KB" % (total // 1024))


if __name__ == "__main__":
    main()
