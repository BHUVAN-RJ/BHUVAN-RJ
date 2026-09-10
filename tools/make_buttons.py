import sys; sys.path.insert(0, 'tools')
from pixelfont import text_path, text_width

PX   = 3          # pixel size
PADX = 5 * PX
PADY = 5 * PX
BORD = PX         # chunky square border

BG, FG, DIM = "#000000", "#00ff41", "#008f11"

BTNS = {
 "portfolio": "PORTFOLIO",
 "resume":    "RESUME.PDF",
 "linkedin":  "LINKEDIN",
 "email":     "EMAIL",
 "essays":    "ESSAYS",
 "webstore":  "AUDITEX / CHROME WEB STORE",
 "npm":       "NPM / EXTENSION-TESTER-MCP",
}

for slug, label in BTNS.items():
    tw = text_width(label, PX)
    w  = tw + PADX * 2
    h  = 7 * PX + PADY * 2
    scan = "".join(
        f'<rect x="0" y="{y}" width="{w}" height="1" fill="#000000" opacity="0.18"/>'
        for y in range(0, h, 3))
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" role="img" aria-label="{label}" shape-rendering="crispEdges">
  <rect width="{w}" height="{h}" fill="{BG}"/>
  <path d="{text_path(label, PADX, PADY, PX)}" fill="{FG}"/>
  {scan}
  <path d="M0 0h{w}v{BORD}H0z M0 {h-BORD}h{w}v{BORD}H0z M0 0h{BORD}v{h}H0z M{w-BORD} 0h{BORD}v{h}h-{BORD}z" fill="{FG}"/>
  <path d="M0 0h{PX}v{PX}H0z M{w-PX} 0h{PX}v{PX}h-{PX}z M0 {h-PX}h{PX}v{PX}H0z M{w-PX} {h-PX}h{PX}v{PX}h-{PX}z" fill="{BG}"/>
</svg>
'''
    open(f"assets/btn-{slug}.svg", "w").write(svg)
    print(f"btn-{slug}.svg {w}x{h}")
