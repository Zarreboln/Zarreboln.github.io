# Zining Liu — Portfolio site

Static site generated from `Zining's portfolio.pdf` (35 pages, InDesign export).
No build step is required to view or deploy it — plain HTML, CSS and one small JS file,
with Inter Tight self-hosted so nothing is fetched from a CDN.

Layout: a landing page with the name, a short bio and a three-column grid of all six
works (two columns under 1040 px, one under 700 px); each work then has its own page —
three-column title block, abstract, and the portfolio spreads as full-width plates. Pure white ground
throughout, square corners, hairline frames around every image.

```
index.html                 Landing: name, bio, work grid, About
liweaving.html             01  LiWeaving
soundscape.html            02  Urban Soundscape
bodymr.html                03  Humanizing Mixed Reality
latent-agent.html          04  Latent Agent
medusa.html                05  MEDUSA
reading-the-heritage.html  06  Reading the Heritage
favicon.svg
assets/
  css/site.css        Whole design system
  fonts/*.woff2       Inter Tight, self-hosted (no external requests at runtime)
  js/site.js          Plate lightbox — click any plate, arrow keys to page,
                      Esc to close
  pages/pNN.jpg       Portfolio page NN rendered at 1998 px wide  (full-res view)
  thumbs/pNN.jpg      Same page at 760 px                        (small screens)
                      Only the pages still referenced are kept in the repo.
  cards/*.jpg         1200x1200 square cover for each project — a square crop of
                      that project's own opening page, filling the tile edge to
                      edge. Cut by make_covers.py.
build.py              Regenerates all seven HTML files from the ENTRIES list inside it
make_covers.py        Re-cuts assets/cards/*.jpg from the page renders; crop boxes
                      live in the COVERS dict at the top
```

## View locally

Open `index.html` in a browser, or serve it:

```sh
python3 -m http.server 8000     # then visit http://localhost:8000
```

## Editing

Small text or layout tweaks: edit the `.html` files directly.
Structural changes (adding a project, reordering, changing captions): edit the
`PROJECTS` / `OTHER` lists at the top of `build.py`, then run `python3 build.py`
— it overwrites all seven HTML files. `assets/css/site.css` is never touched by the build.

A project is one dict in `RESEARCH` (numbered 01–04) or `WORKS` (05–06); its
`plates` list is `(PDF page, short label, caption)`. To add a new project you also
need its page images in `assets/pages/` + `assets/thumbs/`, and an entry in the
`COVERS` dict of `make_covers.py` to cut its square cover.

To reframe an existing cover, edit its crop box in `make_covers.py` and re-run it —
`build.py` does not need to run again unless the project list changed.

## Deploy to GitHub Pages

```sh
git init && git add -A && git commit -m "portfolio site"
git branch -M main
git remote add origin git@github.com:<user>/<repo>.git
git push -u origin main
```

Then in the repo: **Settings → Pages → Source: Deploy from a branch → `main` / `/ (root)`**.
The site appears at `https://<user>.github.io/<repo>/`.
Naming the repo `<user>.github.io` instead publishes it at the bare domain.

Total asset weight is about 11 MB, well inside GitHub Pages limits.

## Not included

The 65 MB source PDF is not in this repo. To offer it as a download, drop a
compressed copy at `assets/Zining-Liu-Portfolio.pdf` and link it from the About
block in `index.html`.
