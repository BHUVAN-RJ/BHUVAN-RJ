"""Matrix digital-rain banner GIF. Katakana glyph columns + burned-in name."""
import random, sys
from PIL import Image, ImageDraw, ImageFont
sys.path.insert(0, 'tools')
from pixelfont import text_path, text_width, F, GW, ADV

W, H      = 1000, 180
FRAMES    = 30
COL_W     = 18
FONT_SZ   = 17
BG        = (0, 0, 0)
HEAD      = (200, 255, 210)
BRIGHT    = (0, 255, 65)
DIM       = (0, 143, 17)
JP = "/System/Library/Fonts/ヒラギノ角ゴシック W3.ttc"
GLYPHS = "ｱｲｳｴｵｶｷｸｹｺｻｼｽｾｿﾀﾁﾂﾃﾄﾅﾆﾇﾈﾉﾊﾋﾌﾍﾎﾏﾐﾑﾒﾓﾔﾕﾖﾗﾘﾙﾚﾛﾜﾝ0123456789"

random.seed(7)
font = ImageFont.truetype(JP, FONT_SZ)
rows = H // FONT_SZ + 2
cols = W // COL_W + 1

streams = []
for c in range(cols):
    streams.append({
        "y":     random.uniform(-rows, rows),
        "speed": random.uniform(0.45, 1.15),
        "trail": random.randint(6, rows),
        "chars": [random.choice(GLYPHS) for _ in range(rows + 4)],
    })

def blend(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))

def pixel_text(draw, s, x, y, px, colour):
    """Draw the 5x7 bitmap font as real pixel blocks, matching the buttons."""
    for i, ch in enumerate(s.upper()):
        glyph = F.get(ch, F[' ']).split(',')
        gx = x + i * ADV * px
        for r, row in enumerate(glyph):
            for c in range(GW):
                if row[c] == '1':
                    draw.rectangle([gx + c*px, y + r*px, gx + c*px + px - 1, y + r*px + px - 1], fill=colour)

NAME = "BHUVAN RAJANAHALLY JAYAKUMAR"
PX   = 4
nw   = text_width(NAME, PX)
nx   = (W - nw) // 2
ny   = H // 2 - (7 * PX) // 2

frames = []
for f in range(FRAMES):
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    for c, st in enumerate(streams):
        head = st["y"] + st["speed"] * f * 1.6
        for t in range(st["trail"]):
            r = head - t
            ry = int(r % (rows + 4))
            if not (0 <= ry * FONT_SZ < H):
                continue
            ch = st["chars"][(ry + f // 3) % len(st["chars"])]
            if t == 0:
                col = HEAD
            else:
                fade = 1 - (t / st["trail"])
                col = blend(DIM, BRIGHT, fade * fade)
            d.text((c * COL_W, ry * FONT_SZ), ch, font=font, fill=col)
    # dim band behind the name so it stays legible over the rain
    band = Image.new("RGB", (W, 7 * PX + 26), BG)
    img.paste(band, (0, ny - 13))
    d = ImageDraw.Draw(img)
    pixel_text(d, NAME, nx, ny, PX, BRIGHT)
    frames.append(img.quantize(colors=48, method=Image.MEDIANCUT))

frames[0].save("assets/banner.gif", save_all=True, append_images=frames[1:],
               duration=90, loop=0, optimize=True, disposal=2)
print("assets/banner.gif")
