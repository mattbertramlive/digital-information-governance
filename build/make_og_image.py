# -*- coding: utf-8 -*-
"""make_og_image.py - generate the branded 1200x630 social card -> ../site/og-dig.png.
Static asset (like styles.css); not emitted by generate.py. Re-run if the brand changes."""
import os
from PIL import Image, ImageDraw, ImageFont

NAVY = (17, 75, 115)      # #114b73
GOLD = (245, 198, 54)     # #f5c636
WHITE = (255, 255, 255)
MIST = (205, 214, 223)    # light gray for subtitle
W, H = 1200, 630
M = 84                    # left margin

FONTS = r"C:\Windows\Fonts"
def font(name, size):
    for cand in (name, "georgiab.ttf", "georgia.ttf", "arialbd.ttf", "arial.ttf"):
        p = os.path.join(FONTS, cand)
        if os.path.exists(p):
            try: return ImageFont.truetype(p, size)
            except Exception: continue
    return ImageFont.load_default()

serif_b = lambda s: font("georgiab.ttf", s)
sans    = lambda s: font("arial.ttf", s)
sans_b  = lambda s: font("arialbd.ttf", s)

img = Image.new("RGB", (W, H), NAVY)
d = ImageDraw.Draw(img)

# left gold spine
d.rectangle([0, 0, 14, H], fill=GOLD)

# eyebrow
d.text((M, 70), "DIG®   ·   THE STANDARD REFERENCE", font=sans_b(28), fill=GOLD)

# headline (two lines)
d.text((M, 132), "Digital Information", font=serif_b(86), fill=WHITE)
d.text((M, 232), "Governance", font=serif_b(86), fill=WHITE)

# gold rule
d.rectangle([M, 352, M + 300, 358], fill=GOLD)

# subtitle (two lines)
d.text((M, 392), "AI decision governance: keeping AI-influenced", font=sans(34), fill=MIST)
d.text((M, 436), "decisions defensible and auditable.", font=sans(34), fill=MIST)

# footer row
d.text((M, 536), "Matthew Bertram", font=sans_b(30), fill=WHITE)
url = "digitalinformationgovernance.com"
uf = sans(28)
d.text((W - M - d.textlength(url, font=uf), 538), url, font=uf, fill=GOLD)

out = os.path.join(os.path.dirname(__file__), "..", "site", "og-dig.png")
img.save(out, "PNG", optimize=True)
print("wrote", os.path.abspath(out), "(%d bytes)" % os.path.getsize(out))
