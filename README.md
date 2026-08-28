# Zining Liu — Portfolio site

Static site generated from `Zining's portfolio.pdf` (35 pages, InDesign export).
No build step is required to view or deploy it — plain HTML, CSS and one small JS file,
with Inter Tight self-hosted so nothing is fetched from a CDN.

Layout: a landing page with the name, a short bio and a three-column grid of all eight
works (two columns under 1040 px, one under 700 px); each work then has its own page —
three-column title block, abstract, and the portfolio spreads as full-width plates. Pure white ground
throughout, square corners, hairline frames around every image.

```
index.html                 Landing: name, bio, work grid, About
liweaving.html             01  LiWeaving
soundscape.html            02  Urban Soundscape
bodymr.html                03  Humanizing Mixed Reality
latent-agent.html          04  Latent Agent
plug-in.html               05  PLUG-IN
shelter.html               06  SHELTER
medusa.html                07  MEDUSA
reading-the-heritage.html  08  Reading the Heritage
favicon.svg
assets/
  css/site.css        Whole design system
  fonts/*.woff2       Inter Tight, self-hosted (no external requests at runtime)
  js/site.js          Plate lightbox — click any plate, arrow keys to page,
                      Esc to close
  pages/pNN.jpg       Portfolio page NN rendered at 1998 px wide  (full-res view)
  thumbs/pNN.jpg      Same page at 760 px                        (small screens)
  cards/*.jpg         1200x1200 square tile for each project — the artwork from
                      that project's own opening page, fitted on white. Index grid.
build.py              Regenerates all nine HTML files from the ENTRIES list inside it
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
— it overwrites all nine HTML files. `assets/css/site.css` is never touched by the build.

A project is one dict in `RESEARCH` (numbered 01–04) or `WORKS` (05–08); its
`plates` list is `(PDF page, short label, caption)`. To add a new project you also
need its page images in `assets/pages/` + `assets/thumbs/`, and a cover crop in
`assets/cards/`.

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

Total asset weight is about 13 MB, well inside GitHub Pages limits.

## Not included

The 65 MB source PDF is not in this repo. To offer it as a download, drop a
compressed copy at `assets/Zining-Liu-Portfolio.pdf` and link it from the About
block in `index.html`.
