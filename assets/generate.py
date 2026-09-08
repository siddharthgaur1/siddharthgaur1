"""Generates the animated SVG assets for this profile README.

Committed so the assets are reproducible rather than hand-tweaked blobs:
the dark and light variants must share identical geometry, so the geometry
is written once, here, and rendered twice.

Animation is SMIL. GitHub strips JS and CSS from READMEs, so an animated
SVG served through raw.githubusercontent is the only real motion available
(a GIF being the other, heavier, option).

    python assets/generate.py
"""

import math
import pathlib

OUT = pathlib.Path(__file__).parent

# --- palette -----------------------------------------------------------
# Deliberately not the black/blue/purple/pink gradient every other AI
# profile uses: ink + amber signal + teal, which reads instrument panel.
DARK = dict(
    bg0="#080C14", bg1="#05080E", edge="#22304A",
    node="#94A3B8", node_core="#E2E8F0",
    amber="#FFB627", teal="#2DD4BF",
    name="#F1F5F9", role="#94A3B8", meta="#5A6B85", frame="#141C2B",
    track="#1A2438", halo="0.16",
)
LIGHT = dict(
    # Tinted rather than pure white: on GitHub's white README background a
    # #FFFFFF card has no edge at all and the whole hero reads as washed out.
    bg0="#F7F9FC", bg1="#EAEFF6", edge="#A9BACE",
    node="#475569", node_core="#0F172A",
    amber="#B45309", teal="#0D7D72",
    name="#0B1220", role="#475569", meta="#64748B", frame="#CBD5E1",
    track="#DDE4EE", halo="0.07",
)

# --- graph geometry ----------------------------------------------------
# A small message-passing graph. Positions are hand-placed rather than
# random so the silhouette is stable and never collides with the type.
NODES = [
    (78, 96), (150, 52), (150, 148), (222, 96),
    (222, 196), (296, 56), (296, 148), (368, 104),
    (110, 210), (368, 196), (44, 150), (296, 240),
]
EDGES = [
    (0, 1), (0, 2), (1, 3), (2, 3), (2, 4), (3, 5), (3, 6),
    (5, 7), (6, 7), (4, 6), (8, 2), (8, 4), (10, 0), (10, 8),
    (7, 9), (6, 9), (4, 11), (11, 9),
]
# Edges that carry a travelling pulse: (edge index, delay seconds, colour key)
PULSES = [(2, 0.0, "amber"), (6, 0.9, "teal"), (13, 1.7, "amber"),
          (14, 2.4, "teal"), (10, 3.1, "amber"), (17, 3.8, "teal")]

W, H = 1200, 320

FAM = "'Segoe UI',Inter,system-ui,-apple-system,Helvetica,Arial,sans-serif"
MONO = "'SFMono-Regular',ui-monospace,'Cascadia Mono',Consolas,monospace"


def hero(p):
    o = []
    a = o.append
    a('<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" '
      'viewBox="0 0 %d %d" role="img" '
      'aria-label="Siddharth Gaur, AI/ML Engineer. Graph neural networks, '
      'LLM agents, retrieval systems. Mumbai or remote, open to AI-ML roles.">'
      % (W, H, W, H))

    a('<defs>')
    a('<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">'
      '<stop offset="0%%" stop-color="%s"/>'
      '<stop offset="100%%" stop-color="%s"/></linearGradient>' % (p["bg0"], p["bg1"]))
    a('<radialGradient id="halo" cx="50%%" cy="50%%" r="50%%">'
      '<stop offset="0%%" stop-color="%s" stop-opacity="%s"/>'
      '<stop offset="100%%" stop-color="%s" stop-opacity="0"/></radialGradient>'
      % (p["amber"], p["halo"], p["amber"]))
    for i, (ei, _, _) in enumerate(PULSES):
        s, e = EDGES[ei]
        x1, y1 = NODES[s]
        x2, y2 = NODES[e]
        a('<path id="p%d" d="M%s,%s L%s,%s" fill="none"/>' % (i, x1, y1, x2, y2))
    a('</defs>')

    a('<rect width="%d" height="%d" fill="url(#bg)" rx="10"/>' % (W, H))
    a('<rect x="0.5" y="0.5" width="%d" height="%d" fill="none" stroke="%s" '
      'stroke-width="1" rx="10"/>' % (W - 1, H - 1, p["frame"]))

    a('<g transform="translate(38,34)">')
    a('<circle cx="222" cy="130" r="185" fill="url(#halo)"/>')

    # edges draw themselves in
    for ei, (s, e) in enumerate(EDGES):
        x1, y1 = NODES[s]
        x2, y2 = NODES[e]
        ln = math.hypot(x2 - x1, y2 - y1)
        a('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="1.1" '
          'stroke-linecap="round" stroke-dasharray="%.1f" stroke-dashoffset="%.1f">'
          '<animate attributeName="stroke-dashoffset" from="%.1f" to="0" dur="1.1s" '
          'begin="%.2fs" fill="freeze"/></line>'
          % (x1, y1, x2, y2, p["edge"], ln, ln, ln, 0.05 * ei))

    # nodes: a slow breathing halo, then the core fades up
    for ni, (x, y) in enumerate(NODES):
        d = (ni % 6) * 0.62
        a('<circle cx="%s" cy="%s" r="7" fill="%s" opacity="0.12">'
          '<animate attributeName="r" values="7;11;7" dur="3.8s" begin="%.2fs" '
          'repeatCount="indefinite"/>'
          '<animate attributeName="opacity" values="0.12;0.03;0.12" dur="3.8s" '
          'begin="%.2fs" repeatCount="indefinite"/></circle>' % (x, y, p["node"], d, d))
        a('<circle cx="%s" cy="%s" r="3.4" fill="%s" opacity="0">'
          '<animate attributeName="opacity" values="0;0.95" dur="0.5s" begin="%.2fs" '
          'fill="freeze"/></circle>' % (x, y, p["node_core"], 0.05 * ni))

    # message passing: a pulse rides each chosen edge, forever
    for i, (ei, delay, colour) in enumerate(PULSES):
        c = p[colour]
        begin = 1.0 + delay
        a('<circle r="7" fill="%s" opacity="0.18">'
          '<animateMotion dur="1.9s" begin="%.2fs" repeatCount="indefinite">'
          '<mpath href="#p%d"/></animateMotion></circle>' % (c, begin, i))
        a('<circle r="3.6" fill="%s">'
          '<animateMotion dur="1.9s" begin="%.2fs" repeatCount="indefinite">'
          '<mpath href="#p%d"/></animateMotion>'
          '<animate attributeName="opacity" values="0;1;1;0" dur="1.9s" begin="%.2fs" '
          'repeatCount="indefinite"/></circle>' % (c, begin, i, begin))
    a('</g>')

    # --- type ------------------------------------------------------------
    tx = 500
    a('<g font-family="%s" opacity="0">'
      '<animate attributeName="opacity" from="0" to="1" dur="0.9s" begin="0.5s" '
      'fill="freeze"/>' % FAM)
    a('<text x="%d" y="128" fill="%s" font-size="52" font-weight="700" '
      'letter-spacing="1.5">SIDDHARTH GAUR</text>' % (tx, p["name"]))
    a('<text x="%d" y="176" fill="%s" font-size="20" font-weight="500">'
      'AI / ML Engineer</text>' % (tx, p["role"]))
    a('</g>')

    a('<rect x="%d" y="146" width="0" height="2.5" fill="%s" rx="1.5">'
      '<animate attributeName="width" from="0" to="118" dur="0.8s" begin="1.1s" '
      'fill="freeze"/></rect>' % (tx, p["amber"]))

    a('<g font-family="%s" opacity="0">'
      '<animate attributeName="opacity" from="0" to="1" dur="0.9s" begin="1.3s" '
      'fill="freeze"/>' % MONO)
    a('<text x="%d" y="218" font-size="15.5">'
      '<tspan fill="%s">graph neural networks</tspan>'
      '<tspan fill="%s">  ·  </tspan>'
      '<tspan fill="%s">llm agents</tspan>'
      '<tspan fill="%s">  ·  </tspan>'
      '<tspan fill="%s">retrieval systems</tspan></text>'
      % (tx, p["teal"], p["meta"], p["teal"], p["meta"], p["teal"]))
    a('<text x="%d" y="252" font-size="13.5" fill="%s">'
      'Mumbai / remote  ·  open to AI-ML roles</text>' % (tx, p["meta"]))
    a('</g>')

    # one nod to the terminal identity this replaces
    a('<rect x="%d" y="240" width="8" height="15" fill="%s" opacity="0">'
      '<animate attributeName="opacity" values="0;0;1;1;0" dur="1.1s" begin="2.2s" '
      'repeatCount="indefinite" keyTimes="0;0.45;0.5;0.95;1"/></rect>'
      % (tx + 342, p["amber"]))

    a('</svg>')
    return "\n".join(o)


# --- divider -----------------------------------------------------------
DW, DH = 1200, 12


def rule(p):
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" '
        'viewBox="0 0 %d %d" role="presentation">'
        '<line x1="0" y1="6" x2="%d" y2="6" stroke="%s" stroke-width="1"/>'
        '<circle cy="6" r="3" fill="%s">'
        '<animate attributeName="cx" values="0;%d" dur="6s" repeatCount="indefinite"/>'
        '<animate attributeName="opacity" values="0;1;1;0" dur="6s" '
        'repeatCount="indefinite"/></circle>'
        '</svg>' % (DW, DH, DW, DH, DW, p["track"], p["amber"], DW))


for name, fn in (("hero", hero), ("rule", rule)):
    for suffix, palette in (("dark", DARK), ("light", LIGHT)):
        path = OUT / ("%s-%s.svg" % (name, suffix))
        path.write_text(fn(palette), encoding="utf-8")
        print("wrote", path.name, path.stat().st_size, "bytes")
