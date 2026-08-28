# -*- coding: utf-8 -*-
"""Cut the square cover tiles in assets/cards/ from the rendered portfolio pages.

Each cover is a square crop of that project's opening page, scaled to fill the
tile edge to edge — no margin. Run `python3 make_covers.py` after changing a
crop box; then `python3 build.py` if the project list itself changed.
"""
import os
from PIL import Image

SITE = os.path.dirname(os.path.abspath(__file__))
PAGES = os.path.join(SITE, "assets/pages")
CARDS = os.path.join(SITE, "assets/cards")
SIZE = 1200

# name -> (page, box)
#   box = (x0, y0, x1, y1, ax, ay) as page fractions; the largest square that
#         fits the box is taken, ax/ay place it when a side has to be cropped
#         (0 = left/top, 0.5 = centre, 1 = right/bottom)
#   box = ("px", left, top, side) to cut an exact square in page pixels instead
COVERS = {
    "liweaving":   (3,  (0.104, 0.158, 0.415, 0.802, 0.50, 0.50)),
    "soundscape":  (11, (0.062, 0.165, 0.478, 0.845, 0.50, 0.50)),
    "bodymr":      (18, (0.094, 0.230, 0.432, 0.778, 0.50, 0.50)),
    "latentagent": (22, (0.107, 0.163, 0.413, 0.845, 0.50, 0.70)),
    "medusa":      (34, (0.037, 0.182, 0.485, 0.848, 0.50, 0.50)),
    # cut below the printed "Other Work4" label so it stays out of the cover
    "heritage":    (35, ("px", 0, 172, 1160)),
}


def cut(page, box):
    im = Image.open(os.path.join(PAGES, "p%02d.jpg" % page)).convert("RGB")
    if box[0] == "px":
        _, left, top, side = box
        return im.crop((left, top, left + side, top + side))
    x0, y0, x1, y1, ax, ay = box
    pw, ph = im.size
    art = im.crop((round(x0 * pw), round(y0 * ph), round(x1 * pw), round(y1 * ph)))
    side = min(art.size)
    left = round((art.width - side) * ax)
    top = round((art.height - side) * ay)
    return art.crop((left, top, left + side, top + side))


if __name__ == "__main__":
    for name, (page, box) in COVERS.items():
        sq = cut(page, box).resize((SIZE, SIZE), Image.LANCZOS)
        sq.save(os.path.join(CARDS, name + ".jpg"), "JPEG", quality=87, optimize=True)
        print("%-12s <- p%02d" % (name, page))
