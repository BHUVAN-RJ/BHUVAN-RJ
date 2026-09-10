"""Matrix-green section headers, same 5x7 bitmap font as the buttons."""
import sys; sys.path.insert(0, 'tools')
from pixelfont import text_path, text_width

PX, PADX, PADY = 3, 10, 9
BG, FG, DIM = "#000000", "#00ff41", "#008f11"
W = 820

HDRS = {
 "currently-building": "CURRENTLY BUILDING",
 "research":           "RESEARCH",
 "experience":         "EXPERIENCE",
 "shipped":            "SHIPPED",
}

for slug, label in HDRS.items():
    text = "> " + label
    h  = 7 * PX + PADY * 2 + 6
    tp = text_path(text, PADX, PADY, PX)
    cx = PADX + text_width(text, PX) + 3 * PX   # blinking-cursor block
    scan = "".join(f'<rect x="0" y="{y}" width="{W}" height="1" fill="#000000" opacity="0.30"/>'
                   for y in range(0, h, 3))
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{h}" role="img" aria-label="{label}" shape-rendering="crispEdges">
  <rect width="{W}" height="{h}" fill="{BG}"/>
  <path d="{tp}" fill="{FG}"/>
  <rect x="{cx}" y="{PADY}" width="{PX*4}" height="{PX*7}" fill="{DIM}"/>
  {scan}
  <rect x="0" y="{h-3}" width="{W}" height="3" fill="{DIM}"/>
</svg>
'''
    open(f"assets/hdr-{slug}.svg", "w").write(svg)
    print(f"hdr-{slug}.svg {W}x{h}")
