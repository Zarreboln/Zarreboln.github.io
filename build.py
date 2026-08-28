# -*- coding: utf-8 -*-
"""Generate the static site for Zining Liu's portfolio.

All content lives in ENTRIES below. Run `python3 build.py` to rewrite the
eight HTML files; assets/css/site.css and assets/js/site.js are never touched.
"""
import os, html

SITE = os.path.dirname(os.path.abspath(__file__))
NAME = "Zining Liu"

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
        slug="liweaving.html", num="01", kind="Research Project",
        title="LiWeaving",
        sub="Generative AI for Li brocade design supporting cultural interpretability and creative expression",
        card="liweaving.jpg",
        card_alt="Detail of a hand-woven Hainan Li brocade textile in indigo, ochre and cream",
        meta=[("Timeline", "Jun. – Aug. 2025"),
              ("Instructor", "Rushi Dai (HKUST), Da Chen (University of Bath)"),
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
        slug="soundscape.html", num="02", kind="Research Project",
        title="Urban Soundscape",
        sub="A two-stage framework for urban sound composition and perceptual prediction",
        card="soundscape.jpg",
        card_alt="Line drawing of a city as contour islands, each marked with a sound icon — birdsong, music, traffic, wind, footsteps",
        meta=[("Date", "Aug. – Nov. 2025"),
              ("Instructor", "Da Chen (University of Bath)"),
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
        slug="bodymr.html", num="03", kind="Research Project",
        title="Humanizing Mixed Reality",
        sub="Interactive design with behavioral computation",
        card="bodymr.jpg",
        card_alt="Wireframe drawing of generated shell roof forms built from dense coloured lines",
        meta=[("Location", "Tianjin, China"),
              ("Date", "Jun. – Jul. 2025"),
              ("Instructor", "Chao Yan (Tongji University)"),
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
        slug="latent-agent.html", num="04", kind="Research Project",
        title="Latent Agent",
        sub="Co-designing with robotic arms of different preferences",
        card="latentagent.jpg",
        card_alt="A small green robotic arm beside a laptop showing a block model, with red, blue and yellow blocks on the table",
        meta=[("Timeline", "Sep. – Dec. 2025"),
              ("Instructor", "Yiqing Wang (MIT)"),
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

WORKS = [
    dict(
        slug="plug-in.html", num="05", kind="Selected Work",
        title="PLUG-IN",
        sub="A kindergarten plugged into an existing industrial shed",
        card="plugin.jpg",
        card_alt="Sectional model of an industrial shed with exposed steel truss, brick walls and inserted white volumes",
        meta=[("Course", "Architectural Design 3"),
              ("Term", "2023 Fall"),
              ("Type", "Studio project")],
        year="2023", note="",
        tags="Adaptive reuse, kindergarten, plan and section, physical model",
        abstract=[
            "A kindergarten and community activity programme inserted into an existing industrial fabric. The damaged brick wall and the steel truss are kept as found; new lightweight volumes are plugged in between them, so that the old structure stays legible and the new programme reads as an addition rather than a replacement.",
            "The scheme is tested through plan and section, and through a detailed physical model of the renovated east district.",
        ],
        plates=[
            (27, "Plan & Section", "Floor plan and section of the kindergarten and activity programme"),
            (28, "Model",          "Model photo of the damaged brick wall after renovation"),
            (29, "Model",          "Model photos of the renovated east district"),
        ],
    ),
    dict(
        slug="shelter.html", num="06", kind="Selected Work", hero_is_page=True,
        title="SHELTER",
        sub="From vulnerability to resilience — form derived from body motion",
        card="shelter.jpg",
        card_alt="White paper model of layered curved walls lit dramatically on a plinth against a black ground",
        meta=[("Course", "Basis of Architectural Design 2"),
              ("Term", "2022 Spring"),
              ("Type", "Studio project")],
        year="2022", note="",
        tags="Body-driven form, form-freeze, sectional study, physical model",
        abstract=[
            "Six frames of a body in motion — sliding, crouching, turning — are frozen and lofted into a single continuous path. The resulting surface becomes the shelter itself: its section is not composed and then occupied, but derived directly from how a person moves inside it.",
            "The study runs from body-motion diagrams in plan and elevation, through the form-freeze operation, to sections that register the body at each moment and a final physical model.",
        ],
        plates=[
            (30, "Concept",      "Shelter — from vulnerability to resilience"),
            (31, "Body Motions", "Body motions in slide and top view"),
            (32, "Form-Freeze",  "Six frames of a person frozen into a continuous path, and the resulting section"),
            (33, "Model",        "Model photo and body behaviour in section"),
        ],
    ),
    dict(
        slug="medusa.html", num="07", kind="Selected Work",
        title="MEDUSA",
        sub="A folded petal-shell canopy with embedded sensing and light",
        card="medusa.jpg",
        card_alt="Illuminated dome of folded white petals over a breadboard and wiring",
        meta=[("Recognition", "Finalist, China Spatial Art Construction Exhibition"),
              ("Term", "2022 Fall"),
              ("Type", "Built prototype")],
        year="2022", note="Finalist, China Spatial Art Construction Exhibition.",
        tags="Geodesic geometry, folded shell, embedded sensing, built prototype",
        abstract=[
            "A lightweight shell assembled from folded petals over a triangulated geodesic frame. The geometry is developed from a single triangle, subdivided and wrapped into a dome; each petal is a repeated unit that stiffens the surface as it curves.",
            "The piece was built as a physical prototype with embedded sensing and lighting, and was a finalist in the China Spatial Art Construction Exhibition.",
        ],
        plates=[
            (34, "Prototype & Geometry", "Built prototype and the underlying geometry study"),
        ],
    ),
    dict(
        slug="reading-the-heritage.html", num="08", kind="Selected Work", hero_is_page=True,
        title="Reading the Heritage",
        sub="A timber-frame survey redrawn as an exploded reading",
        card="heritage.jpg",
        card_alt="Exploded axonometric of a white timber-frame hall on black, with brackets, beams and ornament drawn as line work beside a phone",
        meta=[("Course", "Survey of Architecture Heritage"),
              ("Term", "2023 Fall"),
              ("Type", "Survey & interface study")],
        year="2023", note="",
        tags="Heritage survey, timber frame, exploded axonometric, mobile interface",
        abstract=[
            "A measured survey of a traditional timber-frame building, taken apart into an exploded axonometric — brackets, beams, roof and ornament each drawn as a separate component and linked back to its position in the whole.",
            "The drawing is paired with a mobile interface that lets the same components be read against the building on site, turning the survey from a record into something you can look through.",
        ],
        plates=[
            (35, "Survey", "Exploded axonometric of the timber frame and the mobile reading interface"),
        ],
    ),
]

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
        <span>&copy; Zining Liu 2021&ndash;2025.</span>
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
    src = "assets/pages/p%02d.jpg" % pg
    thumb = "assets/thumbs/p%02d.jpg" % pg
    return """      <figure class="plate">
        <button type="button" data-full="%s" data-caption="%s">
          <img src="%s" srcset="%s 760w, %s 1998w" sizes="(max-width: 900px) 92vw, 1160px"
               alt="%s" loading="lazy" width="1998" height="1332">
        </button>
        <figcaption><b>%s</b> &mdash; %s</figcaption>
      </figure>""" % (src, e(caption), thumb, thumb, src, e(caption), e(label), e(caption))


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
      <div class="card__fig"><img src="assets/cards/%s" alt="%s" loading="lazy" width="1200" height="1200"></div>
      <p class="card__meta">%s <i></i> %s</p>
      <h3>%s</h3>
      <p class="card__sub">%s</p>
      <p class="card__tags">%s</p>
    </a>""" % (p["slug"], p["card"], e(p["card_alt"]), p["year"], e(p["kind"]),
               e(p["title"]), e(p["sub"]), e(p["tags"]))


# ------------------------------------------------------------- entry pages
for i, p in enumerate(ENTRIES):
    rest = p["plates"][1:] if p.get("hero_is_page") else p["plates"]
    doc = [head("%s — %s" % (p["title"], NAME), p["sub"])]
    doc.append('<main>\n\n<section class="wrap phero">')
    doc.append('  <button type="button" class="phero__img" data-full="assets/pages/p%02d.jpg" data-caption="%s">'
               '<img src="assets/art/%s" alt="%s"></button>'
               % (p["plates"][0][0], e(p["title"] + " — opening page"), p["card"], e(p["card_alt"])))
    doc.append("</section>\n")

    doc.append('<section class="wrap titleblock">')
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
            "Selected works of 2021–2025 by Zining Liu — multimodal learning, vision–language models, agentic systems and computational design.")]
idx.append("""<main>

<section class="wrap intro">
  <h1>Zining Liu</h1>
  <p class="bio">I'm a SMArchS Computation student at MIT. My research focuses on artificial intelligence and computational design, with interests in multimodal learning, vision-language models, and agentic systems. I investigate how multimodal information can be integrated to model complex real-world environments and support design decision-making.</p>
  <p class="bio">The projects below run the full loop: collecting and annotating data, training generative or predictive models, and putting the result back in front of people to study how they use it.</p>
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
      <p>Each project pairs a different set of modalities with a design task. LiWeaving couples motif images with their cultural semantics through CLIP and a vision&ndash;language model, so that generation is conditioned on meaning rather than style alone. Urban Soundscape learns across street-view imagery, environmental audio and geospatial data to predict both what a place sounds like and how people say it feels. Humanizing Mixed Reality reads tracked bodies as a social-intensity field and generates roof geometry from it. Latent Agent treats the collaborator itself as the variable, studying how a designer adapts when the agent across the table holds preferences it never states.</p>
      <p>Earlier design work &mdash; adaptive reuse, body-driven form, a built prototype, a heritage survey &mdash; runs from 2021 to 2023 and sits at the end of the list above.</p>
    </div>
    <dl class="facts">
      <dt>Education</dt>
      <dd>SMArchS Computation, MIT</dd>
      <dt>Interests</dt>
      <dd>Multimodal learning, vision&ndash;language models, agentic systems, computational design, human&ndash;AI co-creativity</dd>
      <dt>Methods</dt>
      <dd>Diffusion &amp; GAN models, CLIP / VLM annotation, machine learning on geospatial data, shape grammar, XR, user studies</dd>
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
