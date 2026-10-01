# -*- coding: utf-8 -*-
"""Generate the static site for Zining Liu's portfolio.

All content lives in ENTRIES below. Run `python3 build.py` to rewrite the
eight HTML files; assets/css/site.css and assets/js/site.js are never touched.
"""
import os, html
from PIL import Image

SITE = os.path.dirname(os.path.abspath(__file__))
NAME = "Zining Liu"
ASSET_V = "6"   # bump when an image is replaced, to bypass browser caches

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
        title="UniPS",
        sub="Unified patch similarity unlocks training-free visual place recognition",
        card="vpr.jpg",
        venue="ICLR 2027 submission (under review)",
        card_alt="Teaser figure of UniPS: trained, prior training-free and our pipelines, training cost against recall, and Recall@1 on 17 benchmarks",
        meta=[("Timeline", "Jun. – Oct. 2026"),
              ("Type", "Individual work"),
              ("Status", "ICLR 2027 submission (under review)")],
        year="2026", note="Based on comprehensive evaluation on 17 benchmarks, UniPS achieves state-of-the-art results on both the 8 standard and 9 cross-environment VPR benchmarks.",
        tags="Visual place recognition, training-free, patch similarity, frozen foundation models, DINOv2 / DINOv3",
        abstract=[
            "Visual Place Recognition (VPR) localises an image by retrieving the geo-referenced database image that shows the same place. Most VPR methods are training-based, aiming to learn effective features from annotated data. These methods achieve strong results on standard VPR benchmarks but require millions of labelled samples, making annotation cost a significant challenge. Even with such extensive training, they still fail on other VPR benchmarks that differ from their training set, such as cross-environment benchmarks. Training-free VPR methods avoid this annotation cost and generalise better. However, these methods do not fully leverage pretrained vision models, resulting in features that lack sufficient discriminative power to achieve strong performance on standard VPR benchmarks, highlighting the challenge of effectively utilising pretrained vision models.",
            "To tackle these challenges, we propose UniPS (Unified Patch Similarity), a training-free pipeline built solely on patch similarity. Given a query or database image, only a frozen backbone is applied to extract patch features. We then perform a series of patch similarity-based comparisons for VPR: self-similarity for patch importance, followed by weighted second-moment patch feature pooling for coarse ranking, and cross-image patch similarity for reranking.",
            "Based on comprehensive evaluation on 17 benchmarks, UniPS achieves state-of-the-art results on both the 8 standard and 9 cross-environment VPR benchmarks. On standard VPR benchmarks, UniPS outperforms the best training-free baseline by +12.9% and the best trained baseline by +0.2%, despite the latter’s heavy annotation requirements. On cross-environment benchmarks, UniPS outperforms the best training-free baseline by +7.1% and the best trained baseline by +11.5%. In addition, the proposed module can be easily plugged into existing methods, improving their performance by +5.6% to up to +17.8%.",
        ],
        plates=[
            ("vpr_fig01", "Figure 1", "Overview and performance (R@1). (A) Trained methods require large-scale labelled datasets, limiting their generalisation to cross-environment settings. (B) Prior training-free methods avoid this training cost and generalise better, but suffer a performance drop on standard VPR benchmarks. (C) Our training-free method instead applies frozen patch features directly, using patch similarity both within and across images for retrieval. (D) Training cost versus performance of our method and baselines on 17 benchmarks, averaged separately across standard and cross-environment VPR benchmarks. (E) Performance of the proposed method against the state-of-the-art trained and training-free baselines.",
             "Recent advanced methods achieve large performance improvements, but these gains are largely driven by increasingly large-scale annotated training sets. Even with millions of annotated samples, however, these state-of-the-art methods tend to learn environment- or domain-specific features that do not generalise well as shown in Fig. 1A, suffering a performance drop on cross-environment benchmarks, as shown in Fig. 1D&E. Training-free VPR methods often generalise better than trained methods in the cross-environment setting, but fail on standard VPR benchmarks, as shown in Fig. 1D-E. We argue that current training-free methods, which apply various strategies to obtain prior-selected features (Fig. 1B), do not fully utilise the potential of these large vision models."),
            ("vpr_fig02", "Figure 2", "Overview of the proposed method. Each image is partitioned into patches, whose features are extracted by a frozen vision encoder, and the patch similarity (PS) template is applied in three forms. PS-1 computes the self-similarity of each image, which gives the weight of every patch; features and weights are computed once and stored for both stages. PS-2 pools the weighted patch features into a second-moment matrix, reduced by whitened PCA (WPCA) to one descriptor per image, and coarse ranking shortlists the K nearest database images. PS-3 performs weighted MaxSim matching between the query and each shortlisted image, and reranking sorts the shortlist by the matching score.",
             "As illustrated in Fig. 2, the proposed method UniPS follows a training-free paradigm and requires neither model training nor annotated data. All steps of the pipeline rely on a single patch-to-patch similarity (PS) strategy, expressed in three different forms. The query and the database images are first partitioned into patches, and their patch features are extracted by a frozen pretrained vision model. Based on these features, each image computes the similarity between its own patches (PS-1), from which the weight of every patch is derived. Second-moment pooling of each image’s weighted patch features (PS-2) then yields one descriptor per image, with which the database is coarsely ranked, and patch-to-patch MaxSim matching between the query and the top-ranked database images (PS-3) refines this ranking."),
            ("vpr_fig03", "Figure 3", "Patch self-similarity weighting on a Nordland pair (query left, our rank-1 retrieval right). For each image: colour clusters indicate similar patches, and grey patches are more distinctive in the image. The heat maps show the resulting weight w = 1/n. Repetitive patches such as snow, sky and track fall into large clusters and receive low weight, while sparse, distinctive content receives high weight.",
             "What such a comparison does not say is how much each patch should count: a patch whose appearance recurs many times within its own image cannot tell one place from another. This discounts bursty content, visual elements that repeat within a single image and would otherwise dominate any similarity computed from them. Since w is the reciprocal of n, a patch that recurs frequently across the image (large n) receives a small weight, while a distinctive patch with few or no similar patches (small n) receives a large weight, up to w = 1, reflecting its higher importance (Fig. 3). The weights of an image are collected in w and applied in the coarse ranking and reranking."),
            ("vpr_tab01", "Table 1",  "The 17 benchmarks with their data type.",
             "In this paper, we evaluate the proposed method against a wide range of trained and training-free baselines on 17 benchmarks. Table 1 summarises these benchmarks in two groups, along with their data type. The first group includes 8 standard VPR benchmarks: 7 street-level ones, Pitts250k and Pitts30k, Tokyo 24/7, MSLS-val, St Lucia, Oxford RobotCar and AmsterTime, together with the Nordland railway benchmark. The second group consists of 9 cross-environment localisation benchmarks: 17 Places and Baidu Mall indoors, Gardens Point across day and night, VP-Air and Nardo-Air with its rotated variant in the air, Hawkins and Laurel Caverns underground, and the Mid-Atlantic Ridge underwater."),
            ("vpr_tab02", "Table 2",  "Comparison against training-free baselines. R@1 (%) on the 4 standard and 4 cross-environment benchmarks, with the mean over all 8 standard benchmarks, all 9 cross-environment benchmarks, and all 17 benchmarks. Dim is the dimension of the global descriptor of each method. † indicates two-stage methods. Best and second-best results are in bold and underline. Ours-D2 and Ours-D3 use a frozen DINOv2 and DINOv3 backbone.",
             "We first compare UniPS against existing training-free baselines on all 17 benchmarks: the pooling baselines, the frozen class token and GeM, and the more recent AnyLoc, SegVLAD-PreT and EffoVPR-ZS. As shown in Table 2, on the standard benchmarks, UniPS achieves a mean of 93.2 against 80.3 for EffoVPR-ZS. The largest improvement is on the Nordland benchmark, at +38.1, where most training-free methods fail. On the cross-environment benchmarks, UniPS again achieves the best results with average performance 76.6 over 69.5 for AnyLoc, whose descriptor is 24× larger than ours. Over all 17 benchmarks, UniPS achieves 84.4, +10.3 over the best prior training-free method."),
            ("vpr_tab03", "Table 3",  "Comparison against trained methods. R@1 (%) on the 4 standard and 4 cross-environment benchmarks, with the mean over all 8 standard benchmarks, all 9 cross-environment benchmarks, and all 17 benchmarks. † indicates two-stage methods; ‡ indicates inductive setting. Best and second-best results are in bold and underline. Ours-D2 and Ours-D3 use a frozen DINOv2 and DINOv3 backbone.",
             "On the standard benchmarks, UniPS achieves a mean R@1 of 93.2, surpassing the current state-of-the-art method, SAGE, at 93.0, with the best R@1 on Tokyo24/7, Nordland, and AmsterTime. On the cross-environment benchmarks, all trained methods suffer a significant performance drop, e.g., SAGE falls from 93.0 to 60.0 mean R@1, whereas UniPS drops by only 16.6 at R@1. On average, UniPS outperforms the state-of-the-art trained method, MegaLoc, with 76.6 against 65.1. Averaged over all 17 benchmarks, UniPS outperforms the second-best method, MegaLoc, by 6.8 at R@1. Notably, UniPS is training-free and requires no annotated data, while all trained methods rely on large-scale annotated training datasets. For example, as shown in Fig. 1, EigenPlaces is trained on 41.2 million images, and MegaLoc needs 45 million to reach its state-of-the-art results."),
            ("vpr_fig04", "Figure 4", "Rank-1 retrievals on 4 benchmarks among the proposed method and other baselines. Green indicates a correct result, and red ones are incorrect results.",
             "Figure 4 compares UniPS with other baselines on samples across different benchmarks. The state-of-the-art trained methods can also handle hard samples within the standard benchmarks, but fail beyond them. For example, SAGE correctly retrieves the right place under seasonal change on Nordland, and MegaLoc succeeds on AmsterTime, but both fail in the degraded Hawkins corridor. The state-of-the-art training-free method shows the opposite pattern: AnyLoc succeeds on Hawkins but fails on the 3 standard benchmarks. The proposed UniPS, however, is robust across all cases."),
            ("vpr_tab04", "Table 4",  "Robustness of the proposed reranking module. The module is plugged into different baselines and tested on 9 cross-environment benchmarks, on both two-stage and one-stage methods. All methods are with their default settings. ‡ indicates inductive setting.",
             "In addition to achieving state-of-the-art performance on its own, the proposed re-ranking module can be easily plugged into other baselines to improve their generalisation. For two-stage methods such as SelaVPR and R2Former, we simply replace their re-ranker with our patch similarity-based re-ranking, keeping the rest of the pipeline unchanged. As shown in Table 4, both methods improve their mean R@1 over the 9 cross-environment benchmarks, by +9.7% and +5.6%, respectively. For methods with no re-ranking stage (single-stage methods), our re-ranking module can be attached to the original pipeline, which is modified to return top-K candidates instead of only the top-1 result. With our re-ranking module attached, 8 single-stage methods improve their generalisation, with mean R@1 over the 9 cross-environment benchmarks increasing by +9.1% for MegaLoc to up to +17.8% for SuperVLAD. In particular, none of these improvements requires additional annotated data or further training."),
            ("vpr_tab05", "Table 5",  "Alternatives to obtain the patch importance: mean R@1 over the 8 standard (Std.), the 9 cross-environment and all 17 benchmarks.",
             "We test alternative ways to obtain the patch weights w. Table 5 reports the mean results across all benchmark groups. Our self-similarity signal leads in both groups, reaching 90.3% and 76.3% mean R@1, an improvement of +8.7% and +2.0% over unweighted MaxSim, and outperforming patch-graph centrality (88.2%, 75.4%) and class-token attention (87.8%, 71.7%). Beyond accuracy, self-similarity is also simpler to obtain: it requires only the patch features themselves, whereas the alternatives depend on an attention map from a dedicated network layer."),
            ("vpr_fig05", "Figure 5", "Contribution of each component: performance at R@1 as each component is added.",
             "We conduct an ablation study to examine the contribution of each component in UniPS: patch weighting (PS1), coarse ranking (PS2), and re-ranking (PS3). Starting from an unweighted second-moment pooling baseline, we add each component in turn, and report the resulting R@1 on 2 example benchmarks, Nordland (standard) and VP-Air (cross-environment), in Fig. 5. Patch weighting (PS1) provides the largest gain on Nordland (+34.9%), while MaxSim re-ranking (PS3) provides the largest gain on VP-Air (+12.1%), and adding patch weighting to the re-ranking stage further improves both benchmarks (+6.2% and +10.8%, respectively). These results show that every component of UniPS contributes to the final performance, though their relative importance differs between standard and cross-environment settings."),
            ("vpr_tab06", "Table 6",  "Same backbone (DINOv3) tests across 17 benchmarks including three trained methods and the proposed UniPS. Best and second-best results are in bold and underline.",
             "As most of the advanced baselines are built on DINOv2, we retrain three representative baselines, SALAD, BoQ, and CliqueMining, on DINOv3 using their released implementations and compare them against UniPS under the same backbone. Table 6 reports per-benchmark results. UniPS achieve a mean R@1 of 84.4% across all 17 benchmarks, outperforming BoQ, the best retrained baseline, at 77.3%. Combined with the DINOv2 results in Table 3, this shows that UniPS outperforms all tested baselines with the same backbone, while requiring no annotated data and using at least 8× fewer feature dimensions."),
        ],
    ),
    dict(
        slug="bodymr.html", num="02", kind="Research Project",
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
        slug="liweaving.html", num="04", kind="Research Project",
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


def plate(pg, label, caption, text=None):
    key = "p%02d" % pg if isinstance(pg, int) else pg
    src = "assets/pages/%s.jpg?v=%s" % (key, ASSET_V)
    thumb = "assets/thumbs/%s.jpg?v=%s" % (key, ASSET_V)
    with Image.open(os.path.join(SITE, "assets/pages/%s.jpg" % key)) as im:
        w, h = im.size
    lead = ('        <p class="plate__text">%s</p>\n' % e(text)) if text else ""
    return """      <figure class="plate">
%s        <button type="button" data-full="%s" data-caption="%s">
          <img src="%s" srcset="%s 760w, %s %dw" sizes="(max-width: 900px) 92vw, 1160px"
               alt="%s" loading="lazy" width="%d" height="%d">
        </button>
        <figcaption><b>%s</b> &mdash; %s</figcaption>
      </figure>""" % (lead, src, e(caption), thumb, thumb, src, w, e(caption), w, h, e(label), e(caption))


def pager(i):
    prev = ENTRIES[i - 1] if i > 0 else None
    nxt = ENTRIES[i + 1] if i < len(ENTRIES) - 1 else None
    left = ('<a href="%s">Previous<strong>%s</strong></a>' % (prev["slug"], e(prev["title"]))
            if prev else '<a href="index.html">Index<strong>All work</strong></a>')
    right = ('<a class="r" href="%s">Next<strong>%s</strong></a>' % (nxt["slug"], e(nxt["title"]))
             if nxt else '<a class="r" href="index.html">Index<strong>All work</strong></a>')
    return '<nav class="wrap pager" aria-label="Project navigation">\n  %s\n  %s\n</nav>' % (left, right)


def card(p):
    venue = ('\n      <p class="card__venue">%s</p>' % e(p["venue"])) if p.get("venue") else ""
    return """    <a class="card" href="%s">
      <div class="card__fig"><img src="assets/cards/%s?v=%s" alt="%s" loading="lazy" width="1200" height="1200"></div>
      <h3>%s</h3>
      <p class="card__sub">%s</p>%s
    </a>""" % (p["slug"], p["card"], ASSET_V, e(p["card_alt"]), e(p["title"]), e(p["sub"]), venue)


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
      <p>Each project pairs a different set of modalities with a task. UniPS asks how far a frozen vision foundation model can go on visual place recognition without a single place label, and answers with a pipeline carried entirely by patch similarity. Humanizing Mixed Reality reads tracked bodies as a social-intensity field and generates roof geometry from it. Urban Soundscape learns across street-view imagery, environmental audio and geospatial data to predict both what a place sounds like and how people say it feels. LiWeaving couples motif images with their cultural semantics through CLIP and a vision&ndash;language model, so that generation is conditioned on meaning rather than style alone. Latent Agent treats the collaborator itself as the variable, studying how a designer adapts when the agent across the table holds preferences it never states.</p>
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
