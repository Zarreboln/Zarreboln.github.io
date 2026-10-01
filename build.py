# -*- coding: utf-8 -*-
"""Generate the static site for Zining Liu's portfolio.

All content lives in ENTRIES below. Run `python3 build.py` to rewrite the
eight HTML files; assets/css/site.css and assets/js/site.js are never touched.
"""
import os, html
from PIL import Image

SITE = os.path.dirname(os.path.abspath(__file__))
NAME = "Zining Liu"
ASSET_V = "3"   # bump when an image is replaced, to bypass browser caches

NAV = [
    ("liweaving.html",    "01 LiWeaving"),
    ("soundscape.html",   "02 Soundscape"),
    ("bodymr.html",       "03 Mixed Reality"),
    ("latent-agent.html", "04 Latent Agent"),
    ("index.html#other",  "Other Works"),
    ("index.html#about",  "About"),
]

RESEARCH = [
    dict(
        slug="vpr.html", num="01", kind="Research Project",
        title="Patches Are Enough",
        sub="Simple and effective training-free visual place recognition",
        card="vpr.jpg",
        card_alt="Radar chart of Recall@1 across fourteen place-recognition benchmarks, comparing the method against MegaLoc and AnyLoc",
        meta=[("Timeline", "Jun. – Oct. 2026"),
              ("Type", "Individual work"),
              ("Status", "Paper under review")],
        year="2026", note="Evaluated on thirteen benchmarks spanning urban streets, seasonal railways, and degraded, subterranean, indoor, aerial and underwater imagery, all under one fixed configuration.",
        tags="Visual place recognition, foundation models, training-free retrieval, late interaction, DINOv2 / DINOv3",
        abstract=[
            "Visual place recognition asks where a photograph was taken by retrieving the most similar image from a geo-tagged database. Training a representation for it calls for a place-labelled corpus running to tens of millions of images, produces features that shift with the domain, and ties the result to the one backbone it was trained on. Methods built on frozen foundation models avoid all three and need no place label, yet they still trail supervised ones: they choose what to keep from an image by salience, which is not the property that separates places.",
            "This project removes that criterion and lets the patches of the two images being compared supply every quantity in the pipeline. Two tables of patch-to-patch similarity carry it. The self-similarity of one image weights each patch by how many of that image’s own patches resemble it, in closed form, so a facade of identical windows counts once rather than once per window. The cross-similarity of the pair is reduced two ways: one factoring into a per-image covariance that scans a whole database, the other not factoring and re-ranking a shortlist. Nothing is fitted between the frozen network and the ranking — no codebook, segmentation, learned saliency or place label.",
            "Across thirteen benchmarks spanning urban streets, seasonal railways, and degraded, subterranean, indoor, aerial and underwater imagery, one fixed configuration reaches the highest mean Recall@1, and it is level with the strongest supervised method on the urban benchmarks its supervision targets. As a drop-in scoring rule, it also improves published two-stage pipelines when it replaces their own re-ranker, and single-stage ones when it is added to them.",
        ],
        plates=[
            ("vpr_teaser", "Overview",          "Three ways of deciding what an image contributes — place labels, a criterion fixed elsewhere, or the patches themselves; supervision cost against out-of-distribution recall, and Recall@1 on fourteen benchmarks at one fixed configuration"),
            ("vpr_method", "Pipeline",          "A frozen vision encoder, a per-image self-similarity module that weights each patch in closed form, a second-moment descriptor for coarse ranking over the database, and MaxSim patch interaction for fine ranking of the shortlist"),
            ("vpr_weight", "Why Weight First",  "Near-duplicate patches stretch a VLAD residual or a covariance toward themselves; down-weighting each duplicate before the sum lets every scene element count once, with no spectral fix needed afterwards"),
            ("vpr_qual",   "Qualitative",       "Top-1 retrievals under viewpoint, day–night, seasonal, degraded, subterranean, aerial and indoor change, against AnyLoc, SAGE, MegaLoc and BoQ"),
            ("vpr_stage2", "Drop-in Re-ranker", "Replacing the re-ranker of published two-stage pipelines, or adding one to single-stage pipelines, on nine out-of-distribution benchmarks"),
        ],
    ),
    dict(
        slug="liweaving.html", num="02", kind="Research Project",
        title="LiWeaving",
        sub="Generative AI for Li brocade design supporting cultural interpretability and creative expression",
        card="liweaving.jpg",
        card_alt="Detail of a hand-woven Hainan Li brocade textile in indigo, ochre and cream",
        meta=[("Timeline", "Jun. – Aug. 2025"),
              ("My role", "50% Group conceptual design<br>80% Data analysis<br>70% Model training<br>50% User study"),
              ("Group member", "Zining Liu, Yunfan Zhao"),
              ("Video", '<a href="https://youtu.be/YdIIAA9SFBw" target="_blank" rel="noopener">youtu.be/YdIIAA9SFBw</a>')],
        year="2025", note='Full project video at <a href="https://youtu.be/YdIIAA9SFBw" target="_blank" rel="noopener">youtu.be/YdIIAA9SFBw</a>.',
        tags="Generative AI, cultural heritage, diffusion models, CLIP annotation, user study",
        abstract=[
            "Li brocade weaving, a national intangible cultural heritage of China, embodies cultural symbolism through motifs that express rituals, beliefs, and daily life. Yet its transmission and innovation face challenges: databases lack systematic semantic annotation, AI design emphasises aesthetics over meaning, and production still depends on inheritors’ manual experience.",
            "We present LiWeaving, a generative AI-driven system designed to support Li brocade inheritors and learners in creating culturally meaningful motifs, and further enabling Li brocade design in contemporary contexts.",
            "Our findings demonstrate that LiWeaving balances cultural interpretability and creative expression: by scaffolding cultural semantics, the system allowed novices to engage with the craft’s symbolic layer, not just its surface aesthetics — where AI does not simply generate outputs, but supports users in reasoning about cultural constraints, symbolism and variation during the creative process.",
        ],
        plates=[
            (3,  "Overview",           "Project statement and Li brocade reference"),
            (4,  "Field Study",        "Comprehensive study of Hainan Li brocade — motif taxonomy, weaving methods, tools, fibres, costumes and plant dyes — and the semantic mapping of motifs"),
            (5,  "Research Framework", "A. Dataset · B. Model (forward and reverse diffusion) · C. User interaction"),
            (6,  "System / A1–A3",     "LiGeneration, CLIP retrieval with similarity scoring, and LiQwen motif explanation"),
            (7,  "System / A4–A7",     "Colour editing, digital collage, weaving simulation and situated cultural application"),
            (8,  "Expert Evaluation",  "N = 4, scored across structure, creativity, aesthetic, cultural and semantic dimensions"),
            (9,  "User Study",         "N = 20, baseline versus LiWeaving comparison and evaluation"),
            (10, "Participants",       "Participant profiles and discussion of the findings"),
        ],
    ),
    dict(
        slug="soundscape.html", num="03", kind="Research Project",
        title="Urban Soundscape",
        sub="A two-stage framework for urban sound composition and perceptual prediction",
        card="soundscape.jpg",
        card_alt="Line drawing of a city as contour islands, each marked with a sound icon — birdsong, music, traffic, wind, footsteps",
        meta=[("Date", "Aug. – Nov. 2025"),
              ("Type", "Individual work")],
        year="2025", note="Built on 40,000 street-view samples, 2,000 crowd-sourced audio recordings and 200 perception ratings.",
        tags="Machine learning, geospatial data, sound source separation, XGBoost, CNN14",
        abstract=[
            "Sound, as a pervasive yet often underrepresented dimension of urban environments, plays a crucial role in shaping everyday experience, environmental comfort and well-being. This project investigates the relationship between urban form, sound composition and human perception, using data-driven methods to make urban soundscapes measurable, predictable and designable. The study begins with large-scale data collection, integrating street-view imagery, environmental audio recordings and structured geospatial information to capture both the physical and acoustic characteristics of urban spaces.",
            "Building on this dataset, pre-trained sound source separation and semantic segmentation models are used to decompose audio recordings and extract visual features from street-view images. These features are then combined with land-use and POI data to train machine learning models that predict urban sound source composition. In a second stage, synthesised sound scenes are used to train CNN-based models to predict multidimensional soundscape perception. By linking urban features to both sound composition and perceptual outcomes, this framework supports sound-based urban exploration for the public and provides designers with a predictive tool to inform sound-aware urban design decisions.",
        ],
        plates=[
            (11, "Overview",                 "Project statement"),
            (12, "Introduction & Framework", "Why sound matters in urban research, the six urban sound sources, and the two-stage data-to-perception framework"),
            (13, "Sound Mixtures",           "Synthesised sound scenes composed from the six sources"),
            (14, "Land Use & POI",           "Sample sites described by land-use composition and POI density"),
            (15, "Prediction / Composition", "City-wide prediction of sound source composition via an XGBoost ensemble"),
            (16, "Prediction / Perception",  "CNN prediction of multidimensional soundscape perception — eventful, calm, pleasant, chaotic"),
            (17, "Feature Attribution",      "Street-view segmentation ratios paired with the predicted sound composition"),
        ],
    ),
    dict(
        slug="bodymr.html", num="04", kind="Research Project",
        title="Humanizing Mixed Reality",
        sub="Interactive design with behavioral computation",
        card="bodymr.jpg",
        card_alt="Wireframe drawing of generated shell roof forms built from dense coloured lines",
        meta=[("Location", "Tianjin, China"),
              ("Date", "Jun. – Jul. 2025"),
              ("My role", "50% Group conceptual design<br>70% Module development<br>50% User study"),
              ("Group member", "Zining Liu, Yiying Wang, Leding Hu, Lu Xu, Yifan Xu")],
        year="2025", note="Tracked with ZED depth cameras (34 skeletal keypoints per person) and visualised on a Quest 3 headset.",
        tags="Behavioral computation, pix2pix GAN, mixed reality, depth sensing",
        abstract=[
            "BodyMR is an embodied interaction system that translates real-time social behaviors into spatial form. Using ZED depth cameras, the system tracks participants’ movements and extracts 34 three-dimensional skeletal keypoints per individual. Socially intensified interactions are computed and accumulated into dynamic social heatmaps, revealing latent socio-behavioral structures within small-scale environments.",
            "A paired dataset of heatmaps and roof geometries is then used to train a conditional pix2pix GAN, enabling the generation of architectural roof forms driven by social interaction patterns. These forms are visualised in real time through an XR environment using a Quest 3 headset, allowing users to perceive how their everyday social relationships are algorithmically embedded into spatial configurations.",
        ],
        plates=[
            (18, "Overview",               "Project statement"),
            (19, "Behavioral Computation", "Five indices — distance proximity, velocity coherence, gaze relation, attitude engagement and micro-action evaluation — weighted into a single social-intensity field"),
            (20, "Heatmaps to Form",       "Dataset of 40 roof forms paired with accumulated social heatmaps, and the pix2pix training progression"),
            (21, "XR Visualization",       "The generated roof geometry perceived in situ through a Quest 3 headset"),
        ],
    ),
    dict(
        slug="latent-agent.html", num="05", kind="Research Project",
        title="Latent Agent",
        sub="Co-designing with robotic arms of different preferences",
        card="latentagent.jpg",
        card_alt="A small green robotic arm beside a laptop showing a block model, with red, blue and yellow blocks on the table",
        meta=[("Timeline", "Sep. – Dec. 2025"),
              ("Type", "Individual work")],
        year="2025", note="Four participants, three robot preferences, three rounds each.",
        tags="Human–robot interaction, shape grammar, co-design, behavioral preference",
        abstract=[
            "This project investigates human–robot co-design by examining how different robotic behavioral preferences influence human design decisions and perceptions of collaboration within a shared design task.",
            "In a 3×3×3 block-building game, a human and a robotic arm take turns placing coloured blocks to jointly generate a structure. The robotic arm participates with distinct behavioral preferences. These preferences are not explicitly revealed, but gradually emerge through its placement actions and the resulting forms. An embedded shape grammar links block colours to visible faces, allowing the structure to continuously evolve through interaction.",
            "By comparing interaction processes under different robotic preferences, the project focuses on how humans adapt their design strategies during co-design, and how their perceptions of collaboration, trust and design agency are formed over time.",
        ],
        plates=[
            (22, "Overview",      "Project statement"),
            (23, "Preferences",   "Robot A consistency-driven, Robot B symmetry-oriented, Robot C diversity-maximising"),
            (24, "Shape Grammar", "Basic units, structural prototypes and the connection rule linking block colour to visible faces"),
            (25, "User Study",    "Design results, shape-grammar outcomes and inferred preference across three rounds and four participants"),
            (26, "Setup",         "Human–robot turn-taking in the 3×3×3 block-building game"),
        ],
    ),
]

WORKS = []

ENTRIES = RESEARCH + WORKS


def e(s):
    return html.escape(s, quote=True)


NAV_ITEMS = [("index.html#works", "Works"), ("index.html#about", "About"),
             ("mailto:ziningl@mit.edu", "Contact")]


def head(title, desc):
    nav = "\n".join('        <a href="%s">%s</a>' % (h, e(t)) for h, t in NAV_ITEMS)
    return """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%s</title>
<meta name="description" content="%s">
<meta property="og:title" content="%s">
<meta property="og:description" content="%s">
<meta property="og:type" content="website">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="preload" href="assets/fonts/InterTight-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="assets/css/site.css">
</head>
<body>

<header class="topbar">
  <div class="wrap">
    <a class="brand" href="index.html">Zining Liu</a>
    <nav class="nav" aria-label="Primary">
%s
    </nav>
  </div>
</header>
""" % (e(title), e(desc), e(title), e(desc), nav)


FOOT = """
<footer class="foot">
  <div class="wrap">
    <p class="statement">Invisible. Measurable. Designable.</p>
    <div class="foot__cols">
      <div>
        <span>&copy; Zining Liu 2021&ndash;2026.</span>
        <span>All rights reserved.</span>
      </div>
      <div>
        <a href="mailto:ziningl@mit.edu">ziningl@mit.edu</a>
      </div>
      <div>
        <a href="index.html#works">Works</a>
        <a href="index.html#about">About</a>
        <a href="mailto:ziningl@mit.edu">Contact</a>
      </div>
      <div>
        <span>SMArchS Computation, MIT</span>
      </div>
    </div>
  </div>
</footer>

<script src="assets/js/site.js"></script>
</body>
</html>
"""


def plate(pg, label, caption):
    key = "p%02d" % pg if isinstance(pg, int) else pg
    src = "assets/pages/%s.jpg?v=%s" % (key, ASSET_V)
    thumb = "assets/thumbs/%s.jpg?v=%s" % (key, ASSET_V)
    with Image.open(os.path.join(SITE, "assets/pages/%s.jpg" % key)) as im:
        w, h = im.size
    return """      <figure class="plate">
        <button type="button" data-full="%s" data-caption="%s">
          <img src="%s" srcset="%s 760w, %s %dw" sizes="(max-width: 900px) 92vw, 1160px"
               alt="%s" loading="lazy" width="%d" height="%d">
        </button>
        <figcaption><b>%s</b> &mdash; %s</figcaption>
      </figure>""" % (src, e(caption), thumb, thumb, src, w, e(caption), w, h, e(label), e(caption))


def pager(i):
    prev = ENTRIES[i - 1] if i > 0 else None
    nxt = ENTRIES[i + 1] if i < len(ENTRIES) - 1 else None
    left = ('<a href="%s">Previous<strong>%s</strong></a>' % (prev["slug"], e(prev["title"]))
            if prev else '<a href="index.html">Index<strong>All work</strong></a>')
    right = ('<a class="r" href="%s">Next<strong>%s</strong></a>' % (nxt["slug"], e(nxt["title"]))
             if nxt else '<a class="r" href="index.html">Index<strong>All work</strong></a>')
    return '<nav class="wrap pager" aria-label="Project navigation">\n  %s\n  %s\n</nav>' % (left, right)


def card(p):
    return """    <a class="card" href="%s">
      <div class="card__fig"><img src="assets/cards/%s?v=%s" alt="%s" loading="lazy" width="1200" height="1200"></div>
      <p class="card__meta">%s <i></i> %s</p>
      <h3>%s</h3>
      <p class="card__sub">%s</p>
      <p class="card__tags">%s</p>
    </a>""" % (p["slug"], p["card"], ASSET_V, e(p["card_alt"]), p["year"], e(p["kind"]),
               e(p["title"]), e(p["sub"]), e(p["tags"]))


# ------------------------------------------------------------- entry pages
for i, p in enumerate(ENTRIES):
    rest = p["plates"]
    doc = [head("%s — %s" % (p["title"], NAME), p["sub"])]
    doc.append('<main>\n\n<section class="wrap titleblock">')
    doc.append("  <div>\n    <h1>%s</h1>\n    <p class=\"sub\">%s</p>\n    <p class=\"tags\">%s</p>\n  </div>"
               % (e(p["title"]), e(p["sub"]), e(p["tags"])))
    half = (len(p["meta"]) + 1) // 2
    for group in (p["meta"][:half], p["meta"][half:]):
        rows = "".join("      <dt>%s</dt><dd>%s</dd>\n" % (e(k), v) for k, v in group)
        doc.append("  <dl>\n%s  </dl>" % rows)
    doc.append("</section>\n")

    if p["note"]:
        doc.append('<section class="wrap"><p class="note"><b>Note:</b> %s</p></section>\n' % p["note"])
    else:
        doc.append('<section class="wrap"><p class="divider"></p></section>\n')

    doc.append('<section class="wrap body">')
    doc.append("  <h2>Abstract</h2>")
    doc.extend("  <p>%s</p>" % e(t) for t in p["abstract"])
    doc.append("</section>\n")

    if rest:
        doc.append('<section class="wrap plates">')
        doc.extend(plate(*pl) for pl in rest)
        doc.append("</section>\n")

    doc.append(pager(i))
    doc.append("\n</main>")
    doc.append(FOOT)
    open(os.path.join(SITE, p["slug"]), "w").write("\n".join(doc))

# ------------------------------------------------------------------- index
idx = [head("Zining Liu",
            "Selected works of 2021–2026 by Zining Liu — multimodal learning, vision–language models, agentic systems and computational design.")]
idx.append("""<main>

<section class="wrap intro">
  <h1>Zining Liu</h1>
  <p class="bio">I'm a SMArchS Computation student at MIT. My research focuses on artificial intelligence and computational design, with interests in multimodal learning, vision-language models, and agentic systems. I investigate how multimodal information can be integrated to model complex real-world environments and support design decision-making.</p>
  <p class="bio">The projects below run the full loop: collecting and annotating data, training generative or predictive models or reading frozen ones, and putting the result back in front of people to study how they use it.</p>
</section>

<section class="wrap" id="works">
  <div class="grid">
%s
  </div>
</section>

<section class="wrap block" id="about">
  <h2>About</h2>
  <div class="cols">
    <div>
      <p>Each project pairs a different set of modalities with a task. Patches Are Enough asks how far a frozen vision foundation model can go on visual place recognition without a single place label, and answers with a pipeline carried entirely by patch-to-patch similarity. LiWeaving couples motif images with their cultural semantics through CLIP and a vision&ndash;language model, so that generation is conditioned on meaning rather than style alone. Urban Soundscape learns across street-view imagery, environmental audio and geospatial data to predict both what a place sounds like and how people say it feels. Humanizing Mixed Reality reads tracked bodies as a social-intensity field and generates roof geometry from it. Latent Agent treats the collaborator itself as the variable, studying how a designer adapts when the agent across the table holds preferences it never states.</p>
    </div>
    <dl class="facts">
      <dt>Education</dt>
      <dd>SMArchS Computation, MIT</dd>
      <dt>Interests</dt>
      <dd>Multimodal learning, visual place recognition, vision&ndash;language models, agentic systems, computational design, human&ndash;AI co-creativity</dd>
      <dt>Methods</dt>
      <dd>Frozen foundation-model features, image retrieval and re-ranking, diffusion &amp; GAN models, CLIP / VLM annotation, machine learning on geospatial data, shape grammar, XR, user studies</dd>
      <dt>Contact</dt>
      <dd><a href="mailto:ziningl@mit.edu">ziningl@mit.edu</a></dd>
    </dl>
  </div>
</section>

</main>
""" % "\n".join(card(p) for p in ENTRIES))
idx.append(FOOT)
open(os.path.join(SITE, "index.html"), "w").write("\n".join(idx))

print("built: index.html, " + ", ".join(p["slug"] for p in ENTRIES))
