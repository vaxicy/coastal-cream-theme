"""Coastal Cream Theme - icon candidates.

Code-drawn candidates (no AI images), a light/dark contact sheet and an inline
strip. Re-runnable: every mark is redrawn from scratch.

Run from the project root:  py -3 scripts/generate-icon-candidates.py
"""

import io
import math
import os

from PIL import Image, ImageChops, ImageDraw, ImageFont

S = 3
W = 1024

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "assets", "logo-candidates")

CREAM = (253, 249, 247, 255)
SKY = (140, 197, 232, 255)      # #8CC5E8
INK = (78, 134, 168, 255)       # #4E86A8  deeper sea blue
DEEP = (58, 106, 134, 255)      # #3A6A86
SAND = (254, 230, 187, 255)     # #FEE6BB
MINT = (206, 226, 208, 255)     # #CEE2D0
PINK = (238, 192, 210, 255)     # #EEC0D2
GREY = (230, 226, 217, 255)     # #E6E2D9

LIGHT_BG = (246, 248, 247, 255)
DARK_BG = (31, 37, 43, 255)
LIGHT_INK = (44, 62, 74, 255)
DARK_INK = (226, 240, 247, 255)

FONT_DIR = r"C:\Windows\Fonts"


def font(name, size):
    try:
        return ImageFont.truetype(os.path.join(FONT_DIR, name), size)
    except Exception:
        return ImageFont.load_default()


def scr(p):
    return (p[0] * S, p[1] * S)


def wd(v):
    return max(1, int(round(v * S)))


def canvas():
    return Image.new("RGBA", (W * S, W * S), (0, 0, 0, 0))


def finish(img):
    return img.resize((W, W), Image.LANCZOS)


def bez(p0, p1, p2, n=64):
    pts = []
    for i in range(n + 1):
        t = i / n
        u = 1.0 - t
        pts.append((u * u * p0[0] + 2 * u * t * p1[0] + t * t * p2[0],
                    u * u * p0[1] + 2 * u * t * p1[1] + t * t * p2[1]))
    return pts


def poly(draw, pts, fill):
    draw.polygon([scr(p) for p in pts], fill=fill)


def disc(draw, center, r, fill):
    draw.ellipse([center[0] * S - r * S, center[1] * S - r * S,
                  center[0] * S + r * S, center[1] * S + r * S], fill=fill)


def band(draw, x0, x1, y, amp, thick, color):
    top = bez((x0, y), ((x0 + x1) / 2, y - amp), (x1, y))
    bottom = bez((x1, y + thick), ((x0 + x1) / 2, y - amp + thick), (x0, y + thick))
    poly(draw, top + bottom, color)


def arch_mask(cx, top, half_w, bottom):
    mask = Image.new("L", (W * S, W * S), 0)
    md = ImageDraw.Draw(mask)
    r = half_w
    md.ellipse([cx * S - r * S, top * S, cx * S + r * S, (top + 2 * r) * S], fill=255)
    md.rectangle([cx * S - r * S, (top + r) * S, cx * S + r * S, bottom * S], fill=255)
    return mask


# ---------------------------------------------------------------- candidates

def cand_arch_sun():
    img = canvas()
    cx, top, half_w, bottom = 512, 300, 226, 800
    mask = arch_mask(cx, top, half_w, bottom)

    base = canvas()
    base.paste(Image.new("RGBA", base.size, SKY), (0, 0), mask)

    art = canvas()
    d = ImageDraw.Draw(art)
    disc(d, (612, 470), 92, SAND)
    # sand dunes inside the arch
    dune = bez((cx - half_w, 700), (cx - 40, 610), (cx + half_w, 690)) + \
           bez((cx + half_w, 690), (cx + 30, 760), (cx - half_w, 780))
    poly(d, dune + [(cx + half_w, 820), (cx - half_w, 820)], SAND)
    art.putalpha(ImageChops.multiply(art.getchannel("A"), mask))

    base.alpha_composite(art)

    # outline
    outline = ImageDraw.Draw(base)
    outline.arc([cx * S - half_w * S, top * S, cx * S + half_w * S,
                 (top + 2 * half_w) * S], 180, 360, fill=INK, width=wd(30))
    outline.line([scr((cx - half_w, top + half_w)), scr((cx - half_w, bottom))],
                 fill=INK, width=wd(30))
    outline.line([scr((cx + half_w, top + half_w)), scr((cx + half_w, bottom))],
                 fill=INK, width=wd(30))
    outline.line([scr((cx - half_w, bottom)), scr((cx + half_w, bottom))],
                 fill=INK, width=wd(30))
    return finish(base)


def cand_wave_stack():
    img = canvas()
    d = ImageDraw.Draw(img)

    disc(d, (694, 436), 98, SAND)
    band(d, 196, 828, 470, 44, 92, INK)
    band(d, 196, 828, 590, 40, 92, SKY)
    band(d, 196, 828, 710, 36, 92, SAND)

    return finish(img)


def cand_shell_fan():
    img = canvas()
    d = ImageDraw.Draw(img)

    hub = (512, 782)
    radius = 424
    pts = [hub]
    for a in range(-158, -21, 2):
        rad = math.radians(a)
        pts.append((hub[0] + math.cos(rad) * radius, hub[1] + math.sin(rad) * radius))
    poly(d, pts, SKY)

    for a in range(-152, -19, 26):
        rad = math.radians(a)
        tip = (hub[0] + math.cos(rad) * (radius - 8), hub[1] + math.sin(rad) * (radius - 8))
        d.line([scr(hub), scr(tip)], fill=INK, width=wd(24), joint="curve")

    arc = [((hub[0] + math.cos(math.radians(a)) * radius,
             hub[1] + math.sin(math.radians(a)) * radius)) for a in range(-158, -19, 2)]
    d.line([scr(p) for p in arc], fill=INK, width=wd(28), joint="curve")

    # hinge
    poly(d, [(462, 782), (562, 782), (540, 862), (484, 862)], PINK)

    return finish(img)


def cand_sail_boat():
    img = canvas()
    d = ImageDraw.Draw(img)

    # hull
    poly(d, [(300, 676), (724, 676), (648, 782), (376, 782)], DEEP)
    # mast
    d.line([scr((512, 292)), scr((512, 676))], fill=INK, width=wd(24))
    # main sail
    poly(d, [(534, 330), (534, 650), (712, 650)], SAND)
    # jib
    poly(d, [(490, 372), (490, 650), (350, 650)], MINT)
    # water lines
    band(d, 250, 774, 806, 24, 30, SKY)
    band(d, 320, 704, 858, 18, 24, SKY)

    return finish(img)


def cand_lemon_sprig():
    img = canvas()
    d = ImageDraw.Draw(img)

    cx, cy = 530, 560
    a, b = 196, 132
    ang = math.radians(-24)
    pts = []
    for i in range(120):
        t = 2 * math.pi * i / 120
        x, y = a * math.cos(t), b * math.sin(t)
        pts.append((cx + x * math.cos(ang) - y * math.sin(ang),
                    cy + x * math.sin(ang) + y * math.cos(ang)))
    poly(d, pts, SAND)
    d.line([scr(p) for p in pts + pts[:1]], fill=INK, width=wd(22), joint="curve")

    # stem
    stem = bez((534, 404), (486, 348), (430, 314))
    d.line([scr(p) for p in stem], fill=INK, width=wd(24), joint="curve")

    # two leaves attached to the stem
    for base, tip, width, bend in (((492, 356), (352, 268), 78, -26),
                                   ((454, 330), (566, 232), 72, 22)):
        leaf = [base]
        bx, by = base
        tx, ty = tip
        dx, dy = tx - bx, ty - by
        length = math.hypot(dx, dy)
        nx, ny = -dy / length, dx / length
        mx, my = (bx + tx) / 2 + nx * bend, (by + ty) / 2 + ny * bend
        leaf = bez(base, (mx + nx * width, my + ny * width), tip) + \
            bez(tip, (mx - nx * width, my - ny * width), base)[1:]
        poly(d, leaf, MINT)

    return finish(img)


def cand_lighthouse():
    img = canvas()
    d = ImageDraw.Draw(img)

    # tower
    poly(d, [(452, 372), (572, 372), (616, 800), (408, 800)], CREAM)
    d.line([scr((452, 372)), scr((408, 800))], fill=INK, width=wd(26))
    d.line([scr((572, 372)), scr((616, 800))], fill=INK, width=wd(26))
    d.line([scr((408, 800)), scr((616, 800))], fill=INK, width=wd(26))

    # pink stripes clipped to the tower silhouette
    tower = Image.new("L", img.size, 0)
    td = ImageDraw.Draw(tower)
    td.polygon([scr((452, 372)), scr((572, 372)), scr((616, 800)), scr((408, 800))], fill=255)
    stripes = canvas()
    sd = ImageDraw.Draw(stripes)
    for y, h in ((492, 78), (648, 78)):
        sd.rectangle([0, y * S, W * S, (y + h) * S], fill=PINK)
    stripes.putalpha(ImageChops.multiply(stripes.getchannel("A"), tower))
    img.alpha_composite(stripes)

    # lantern room
    poly(d, [(444, 296), (580, 296), (580, 372), (444, 372)], SAND)
    d.rectangle([444 * S, 296 * S, 580 * S, 372 * S], outline=INK, width=wd(22))
    poly(d, [(420, 296), (604, 296), (512, 232)], INK)

    return finish(img)


CANDIDATES = [
    ("01", "arch-sun", cand_arch_sun),
    ("02", "wave-stack", cand_wave_stack),
    ("03", "shell-fan", cand_shell_fan),
    ("04", "sail-boat", cand_sail_boat),
    ("05", "lemon-sprig", cand_lemon_sprig),
    ("06", "lighthouse", cand_lighthouse),
]


# ---------------------------------------------------------------- sheet bits

def centered_text(d, center, text, fnt, fill):
    b = d.textbbox((0, 0), text, font=fnt)
    x = center[0] - (b[2] - b[0]) / 2 - b[0]
    y = center[1] - (b[3] - b[1]) / 2 - b[1]
    d.text((x, y), text, font=fnt, fill=fill)


def contact_sheet(icons, bg, ink, path):
    cell_w, cell_h = 420, 540
    margin, gap = 40, 26
    head = 118
    sheet_w = margin * 2 + cell_w * 3 + gap * 2
    sheet_h = margin + head + cell_h * 2 + gap + margin

    sheet = Image.new("RGBA", (sheet_w, sheet_h), bg)
    d = ImageDraw.Draw(sheet)

    f_title = font("segoeuib.ttf", 40)
    f_num = font("segoeuib.ttf", 30)
    f_name = font("segoeui.ttf", 26)
    f_small = font("segoeui.ttf", 20)

    centered_text(d, (sheet_w / 2, margin + 34), "COASTAL CREAM THEME", f_title, ink)
    centered_text(d, (sheet_w / 2, margin + 82), "icon candidates", f_small, ink)

    for idx, (num, name, icon) in enumerate(icons):
        row, col = divmod(idx, 3)
        gx = margin + col * (cell_w + gap)
        gy = margin + head + row * (cell_h + gap)

        sheet.alpha_composite(icon.resize((260, 260), Image.LANCZOS),
                              (gx + (cell_w - 260) // 2, gy + 30))

        centered_text(d, (gx + cell_w / 2, gy + 330), num, f_num, ink)
        centered_text(d, (gx + cell_w / 2, gy + 372), name, f_name, ink)
        centered_text(d, (gx + cell_w / 2, gy + 404), "1024 x 1024  PNG", f_small, ink)

        thumb = icon.resize((32, 32), Image.LANCZOS)
        tx, ty = gx + cell_w - 32 - 22, gy + cell_h - 32 - 22
        d.rectangle([tx - 10, ty - 10, tx + 42, ty + 42],
                    outline=(ink[0], ink[1], ink[2], 70), width=1)
        sheet.alpha_composite(thumb, (tx, ty))

    save_png(sheet.convert("RGB"), path)


def inline_strip(icons, path):
    size, gap, margin = 150, 18, 30
    strip_w = margin * 2 + size * len(icons) + gap * (len(icons) - 1)
    strip_h = margin * 2 + size + 34
    strip = Image.new("RGBA", (strip_w, strip_h), LIGHT_BG)
    d = ImageDraw.Draw(strip)
    f_num = font("segoeuib.ttf", 20)

    for idx, (num, _name, icon) in enumerate(icons):
        x = margin + idx * (size + gap)
        strip.alpha_composite(icon.resize((size, size), Image.LANCZOS), (x, margin))
        centered_text(d, (x + size / 2, margin + size + 16), num, f_num, LIGHT_INK)

    save_png(strip.convert("RGB"), path)


def save_png(img, path):
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "wb") as fh:
        fh.write(buf.getvalue())


def main():
    os.makedirs(OUT, exist_ok=True)

    icons = []
    for num, name, fn in CANDIDATES:
        icon = fn()
        box = icon.getbbox()
        if box is None:
            raise AssertionError("%s rendered empty" % name)
        left, top, right, bottom = box
        lo, hi = 70, 954
        if left < lo or top < lo or right > hi or bottom > hi:
            raise AssertionError("%s out of safe area: %s" % (name, box))
        path = os.path.join(OUT, "%s-%s.png" % (num, name))
        save_png(icon, path)
        print("wrote", os.path.relpath(path, ROOT), box)
        icons.append((num, name, icon))

    contact_sheet(icons, LIGHT_BG, LIGHT_INK, os.path.join(OUT, "contact-light.png"))
    contact_sheet(icons, DARK_BG, DARK_INK, os.path.join(OUT, "contact-dark.png"))
    inline_strip(icons, os.path.join(OUT, "inline-strip.png"))
    print("wrote contact-light.png / contact-dark.png / inline-strip.png")


if __name__ == "__main__":
    main()
