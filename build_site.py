"""
Builds the Vichar Manch website into ./site

    python build_site.py

Edit the DATA section below (phones, clients, services, videos, photos) and
re-run. Every page shares one header, footer and contact block, so a change
here updates the whole site.
"""
import html
import json
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "site")

# =============================================================== DATA ======
NAME = "Vichar Manch"
FULL_NAME = "Vichar Manch – The Nukkad Natak Team"
EMAIL = "vicharmanch04@gmail.com"
PHONES = [  # (digits for links, display)
    ("8169184646", "+91 81691 84646"),
    ("8796257902", "+91 87962 57902"),
]
WHATSAPP = "918169184646"  # number used by WhatsApp buttons & enquiry form
YOUTUBE = "https://www.youtube.com/@Vicharmanchnukkadteam"
SITE_URL = "https://vicharmanchnukkadnatak.netlify.app"  # change if a custom domain is added

STATS = [("150+", "Trained artists"), ("150+", "Cities across India"),
         ("20–30 min", "Per performance"), ("Multilingual", "Hindi, English & local languages")]

CLIENTS = [
    ("Tata", "Conglomerate"), ("HPCL", "Oil & gas"), ("BPCL", "Oil & gas"),
    ("Yes Bank", "Banking"), ("Asian Paints", "Manufacturing"), ("NSDL", "Financial services"),
    ("Aditya Birla Group", "Conglomerate"), ("Häfele", "Hardware & fittings"), ("Hero", "Automotive"),
    ("John Cockerill", "Engineering"), ("Seamex", "Services"), ("Hindustan Platinum", "Precious metals"),
]

VIDEOS = {
    "ZhKOpwPU5Lg": ("Where Values Come Alive", "Hindustan Platinum · values & culture play"),
    "gt7EYAoapiI": ("POSH Awareness Play", "Aditya Birla Group"),
    "mkxtY8oDsKo": ("POSH Awareness Nukkad Natak", "Hindustan Platinum"),
    "T2Czo59FmxE": ("Corporate Nukkad Natak – POSH", "John Cockerill"),
    "7sW5ql3PZnI": ("Swachhta Abhiyan Nukkad Natak", "Cleanliness awareness"),
    "qHWdW-m7j_0": ("Women Safety Awareness Play", "Rehearsal"),
}

# (file, caption, sub-caption, filter categories)
# The first 6 also appear on the home page (the first one large).
PHOTOS = [
    ("plant-hall-performance-3.jpg", "Live for the plant workforce", "Performance in the plant hall", "performance industrial"),
    ("bpcl-mumbai-refinery.jpg", "BPCL", "Mumbai Refinery", "industrial"),
    ("asian-paints-stage.jpg", "Asian Paints", "On stage at a company event", "performance corporate"),
    ("office-floor-performance-2.jpg", "Right on the office floor", "No stage needed", "performance corporate"),
    ("hafele-warehouse.jpg", "Häfele", "With the warehouse team", "industrial"),
    ("hindustan-platinum.jpg", "Hindustan Platinum", "Corporate campaign", "corporate"),
    ("plant-hall-performance-1.jpg", "Every shift, every worker", "Performance in the plant hall", "performance industrial"),
    ("hafele-lean-corner.jpg", "Häfele", "Session at the Lean Corner", "performance corporate"),
    ("stage-performance-1.jpg", "Big-stage performance", "Company event", "performance corporate"),
    ("plant-hall-performance-2.jpg", "Song, rhythm and story", "Performance in the plant hall", "performance industrial"),
    ("stage-event-audience.jpg", "Facing a full house", "Large audience event", "performance corporate"),
    ("asian-paints-khandala.jpg", "Asian Paints", "Khandala", "corporate team"),
    ("plant-hall-performance-4.jpg", "Audience in the round", "Performance in the plant hall", "performance industrial"),
    ("office-floor-performance-1.jpg", "Office-floor performance", "Employees at their desks", "performance corporate"),
    ("plant-floor-quality-campaign.jpg", "On the plant floor", "Quality & safety campaign", "industrial team"),
    ("john-cockerill.jpg", "John Cockerill", "Site visit & performance", "industrial"),
    ("hafele.jpg", "Häfele", "Corporate campaign", "corporate"),
    ("aditya-birla-seamex.jpg", "Aditya Birla Group | Seamex", "POSH awareness", "corporate"),
    ("team-with-client-staff-2.jpg", "With the client's team", "Campaign day", "industrial team"),
    ("team-with-client-staff.jpg", "With the client's plant team", "Campaign day", "industrial team"),
    ("nsdl-1.jpg", "NSDL", "Corporate campaign", "corporate"),
    ("nsdl-2.jpg", "NSDL", "Corporate campaign", "corporate"),
    ("team-dhol.jpg", "The Vichar Manch team", "Ready to perform", "team"),
]

THEMES = ["Workplace Safety", "Road Safety", "POSH & Workplace Behaviour", "Cyber Awareness",
          "Financial Awareness", "Vigilance Awareness", "Health & Hygiene", "Women Safety",
          "Swachhta (Cleanliness)", "Water Conservation", "Environment & CSR", "Other Social Issues"]

SERVICES = [
    {
        "slug": "plant-mine-safety-plays",
        "title": "Plant & Mine Safety Plays",
        "nav": "Plant & Mine Safety",
        "icon": "helmet",
        "img": "john-cockerill.jpg",
        "short": "Working at height, confined space, LOTO, vehicle movement, fire safety, housekeeping and PPE — acted out where the risk actually lives.",
        "seo": "Safety nukkad natak for plants, mines and factories: working at height, confined space, lockout-tagout, fire safety and PPE awareness street plays across India.",
        "intro": [
            "Safety rules are usually known. What fails is the moment someone decides a shortcut is fine “just this once”. Our safety plays put that moment in front of the workforce — the skipped harness, the bypassed lock, the missing permit — and show what follows, in a language and setting every worker recognises.",
            "Performances happen right on site: at the gate, in the canteen, near the shop floor or in an open yard. No stage, no sound rig, no disruption to operations.",
        ],
        "topics": ["Working at height", "Confined space entry", "Lockout-tagout (LOTO)",
                   "Mobile equipment & vehicle movement", "Fire safety & emergency response",
                   "Housekeeping", "PPE discipline", "Permit-to-work"],
        "good_for": ["National Safety Week", "Plant safety drives & audits", "Induction of new workers",
                     "Post-incident awareness", "Shift-wise coverage of the full workforce"],
    },
    {
        "slug": "road-safety-contractor-awareness",
        "title": "Road Safety & Contractor Awareness",
        "nav": "Road Safety & Contractors",
        "icon": "truck",
        "img": "bpcl-mumbai-refinery.jpg",
        "short": "Safe loading and unloading, driving discipline and site rules for contract workers, drivers and transporters.",
        "seo": "Road safety street plays and contractor safety awareness for drivers, transporters and contract workers at plants, refineries and logistics sites.",
        "intro": [
            "Contract workers and drivers are often the hardest group to reach — they rotate, they work odd hours, and classroom sessions rarely land. A short, loud, funny play at the truck bay or the main gate does.",
            "We build each play around your own site rules — speed limits, reversing, parking, loading bays, seat belts, fatigue and drink-driving — so the message is specific, not generic.",
        ],
        "topics": ["Safe loading & unloading", "Reversing & blind spots", "Speed limits & site traffic rules",
                   "Seat belts & helmets", "Fatigue and drink-driving", "Site entry & gate rules for contractors"],
        "good_for": ["Road Safety Month", "Driver & transporter meets", "Contractor onboarding",
                     "Refineries, depots, plants and warehouses"],
    },
    {
        "slug": "behavioural-safety",
        "title": "Behavioural Safety Plays",
        "nav": "Behavioural Safety",
        "icon": "hand",
        "img": "plant-hall-performance-1.jpg",
        "short": "Stop-work authority, near-miss reporting, speaking up and looking out for co-workers.",
        "seo": "Behaviour-based safety theatre: stop-work authority, near-miss reporting and speaking-up culture plays for industrial and corporate teams.",
        "intro": [
            "Most incidents are preceded by someone who noticed something and stayed quiet. Behavioural safety plays focus on that silence — why people hesitate to stop a job, report a near miss or correct a senior — and make speaking up feel normal.",
            "The audience recognises their own workplace in the characters, laughs at the excuses, and leaves with simple phrases they can actually use on the floor.",
        ],
        "topics": ["Stop-work authority", "Near-miss reporting", "Speaking up & intervention",
                   "Responsibility towards co-workers", "Complacency & shortcuts", "Supervisor–worker communication"],
        "good_for": ["BBS programmes", "Safety culture surveys follow-up", "Leadership & supervisor sessions",
                     "Toolbox talk reinforcement"],
    },
    {
        "slug": "posh-corporate-awareness",
        "title": "POSH & Corporate Awareness",
        "nav": "POSH & Corporate Awareness",
        "icon": "shield",
        "img": "aditya-birla-seamex.jpg",
        "short": "POSH, workplace behaviour, values, cyber, financial and vigilance awareness for offices and plants.",
        "seo": "POSH awareness nukkad natak and corporate awareness plays on workplace behaviour, values, cyber safety, financial awareness and vigilance for employees.",
        "intro": [
            "Sensitive topics like POSH are hard to discuss in a training room. Theatre lets employees see a situation from the outside — what crosses a line, how it feels to the person on the receiving end, and what the right response and reporting route look like — without anyone feeling singled out.",
            "We have performed POSH awareness plays for teams at Aditya Birla Group, Hindustan Platinum and John Cockerill, and values-and-culture plays for Hindustan Platinum.",
        ],
        "topics": ["POSH – prevention of sexual harassment", "Respectful workplace behaviour",
                   "Company values & code of conduct", "Cyber awareness & phishing",
                   "Financial awareness & fraud", "Vigilance Awareness Week"],
        "good_for": ["POSH compliance calendars", "Vigilance Awareness Week", "Cyber Security Awareness Month",
                     "Values & culture launches", "Townhalls and employee events"],
        "clients": ["Aditya Birla Group", "Hindustan Platinum", "John Cockerill"],
        "videos": ["gt7EYAoapiI", "mkxtY8oDsKo", "T2Czo59FmxE", "ZhKOpwPU5Lg"],
    },
    {
        "slug": "social-awareness-csr-government",
        "title": "Social Awareness, CSR & Government Campaigns",
        "nav": "Social, CSR & Government",
        "icon": "megaphone",
        "img": "team-dhol.jpg",
        "short": "Swachhta, water conservation, health, women safety and other public campaigns for government, CSR and NGOs.",
        "seo": "Social awareness street plays for government, CSR and NGO campaigns: Swachhta, Jal Sanrakshan, health and hygiene, women safety and environment.",
        "intro": [
            "Nukkad natak was born on the street, and it is still the fastest way to gather a crowd and hold its attention. We perform in markets, bastis, schools, villages and public spaces to carry a campaign message directly to the people it is meant for.",
            "We have performed awareness programmes on Swachhta (cleanliness), Jal Sanrakshan (water conservation) and other social causes, including projects associated with the Delhi Government and the Government of India.",
        ],
        "topics": ["Swachhta (cleanliness)", "Jal Sanrakshan (water conservation)", "Health & hygiene",
                   "Women safety", "Environment & plastic-free drives", "Community CSR programmes"],
        "good_for": ["Government awareness drives", "CSR community programmes", "NGO outreach campaigns",
                     "Multi-city public campaigns"],
        "videos": ["7sW5ql3PZnI", "qHWdW-m7j_0"],
    },
    {
        "slug": "brand-promotions-corporate-theatre",
        "title": "Brand Promotions & Corporate Theatre",
        "nav": "Brand Promotions & Corporate Theatre",
        "icon": "spark",
        "img": "stage-performance-1.jpg",
        "short": "Theatre-led brand activations, role plays, interactive shows and themed performances for events.",
        "seo": "Brand promotion street plays, BTL theatre activations, corporate role plays and interactive themed performances for employee engagement.",
        "intro": [
            "A live performance stops people in a way a banner or a flyer cannot. We write short, energetic pieces around your product, launch or message and perform them where your audience already is — malls, campuses, dealer meets, townhalls or office floors.",
            "For internal audiences we also create role plays, interactive scenes and themed presentations for townhalls, offsites and engagement days.",
        ],
        "topics": ["Brand activation street plays", "Product & launch storytelling", "Dealer & channel meets",
                   "Role plays & interactive scenes", "Themed performances for events", "Employee engagement days"],
        "good_for": ["Launches & BTL activations", "Annual days & townhalls", "Offsites and engagement weeks",
                     "Campus and mall activations"],
    },
]

STEPS = [
    ("Understand", "We learn your objective, audience, site, language and any incident learnings or SOPs."),
    ("Develop the concept", "We propose a storyline and characters that match your message and workforce."),
    ("Write the script", "A custom script written around your message, site and audience."),
    ("Rehearse & coordinate", "Artists are cast, rehearsed and scheduled for your locations and shifts."),
    ("Perform", "Live on site, followed by audience interaction to reinforce the key points."),
]

FAQ = [
    ("How long is each play?", "Each performance runs about 20 to 30 minutes. We can make it shorter for shift change-overs or add interaction time for a longer session."),
    ("Do you need a stage, sound system or equipment?", "No. Nukkad natak is performed in the open with live voice and traditional instruments. A clear space at the gate, canteen, shop floor or an open yard is enough."),
    ("Which languages do you perform in?", "Hindi, English, or the local language of your site, so the audience connects immediately."),
    ("Can the play be customised to our site?", "Yes. We build scripts around your own SOPs, site rules, incident learnings and terminology so every performance feels like it belongs to your workplace."),
    ("Can you cover all our shifts or multiple locations?", "Yes. We can schedule several performances across shifts in a day, and with 150+ artists across 150+ cities we can run campaigns at multiple locations across India."),
    ("How do we book a performance?", "Call or WhatsApp us, or send the enquiry form with your location, dates, number of shows and topic. We will share our company profile and suggest suitable plays."),
]

# =============================================================== ICONS =====
ICONS = {
    "helmet": '<path d="M3 17h18M5 17v-2a7 7 0 0 1 14 0v2M10 8V5h4v3M12 5v3"/>',
    "truck": '<path d="M2 6h11v9H2zM13 9h4l3 3v3h-7"/><circle cx="6" cy="17" r="2"/><circle cx="17" cy="17" r="2"/>',
    "hand": '<path d="M7 11V6a1.5 1.5 0 0 1 3 0v4M10 10V4.5a1.5 1.5 0 0 1 3 0V10M13 10V5.5a1.5 1.5 0 0 1 3 0V12M16 9.5a1.5 1.5 0 0 1 3 0V14a7 7 0 0 1-7 7h-1a6 6 0 0 1-5-2.7L3.5 14a1.6 1.6 0 0 1 2.6-1.8L7 13.5"/>',
    "shield": '<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><path d="M8.5 12l2.5 2.5 4.5-5"/>',
    "megaphone": '<path d="M3 10v4h3l9 5V5L6 10zM18 9a4 4 0 0 1 0 6M6 14l1.5 5h3L9 15"/>',
    "spark": '<path d="M12 2l2.4 6.6L21 11l-6.6 2.4L12 20l-2.4-6.6L3 11l6.6-2.4z"/>',
    "phone": '<path d="M5 3h4l2 5-2.5 1.5a11 11 0 0 0 6 6L16 13l5 2v4a2 2 0 0 1-2 2A17 17 0 0 1 3 5a2 2 0 0 1 2-2z"/>',
    "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>',
    "pin": '<path d="M12 21s7-6.3 7-12a7 7 0 0 0-14 0c0 5.7 7 12 7 12z"/><circle cx="12" cy="9" r="2.5"/>',
    "play": '<rect x="2" y="5" width="20" height="14" rx="4"/><path d="M10 9l5 3-5 3z"/>',
    "users": '<circle cx="9" cy="8" r="3.5"/><path d="M2 20a7 7 0 0 1 14 0M16 4.5a3.5 3.5 0 0 1 0 7M18 13.5a7 7 0 0 1 4 6.5"/>',
    "map": '<path d="M9 4l6 2 6-2v16l-6 2-6-2-6 2V6zM9 4v16M15 6v16"/>',
    "script": '<path d="M6 3h9l4 4v14H6zM14 3v5h5M9 12h7M9 16h7"/>',
    "lang": '<path d="M4 5h9M8.5 3v2M6 5c0 4 3 7 6 8M11 5c0 4-3 7-7 9M13 21l4-9 4 9M14.5 18h5"/>',
    "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    "layers": '<path d="M12 3l9 5-9 5-9-5zM3 13l9 5 9-5"/>',
}


def icon(name, cls=""):
    return (f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[name]}</svg>')


WA_SVG = ('<svg viewBox="0 0 32 32" aria-hidden="true"><path fill="#fff" d="M16 3a13 13 0 0 0-11.2 19.6L3 29l6.6-1.7A13 13 0 1 0 16 3zm0 23.6c-2 0-4-.5-5.7-1.6l-.4-.2-3.9 1 1-3.8-.3-.4A10.6 10.6 0 1 1 16 26.6zm5.8-7.9c-.3-.2-1.9-.9-2.2-1-.3-.1-.5-.2-.7.2l-1 1.2c-.2.2-.4.2-.7.1a8.7 8.7 0 0 1-4.3-3.8c-.3-.6.3-.5.9-1.7.1-.2 0-.4 0-.6l-1-2.4c-.3-.6-.5-.5-.7-.5h-.6a1.2 1.2 0 0 0-.9.4 3.6 3.6 0 0 0-1.1 2.7 6.3 6.3 0 0 0 1.3 3.3 14.4 14.4 0 0 0 5.5 4.9c2 .9 2.8.9 3.9.8.6-.1 1.9-.8 2.2-1.6.3-.8.3-1.4.2-1.6-.1-.1-.3-.2-.6-.4z"/></svg>')

LOGO_SVG = """<svg viewBox="0 0 200 200" role="img" aria-label="Vichar Manch logo">
<circle cx="100" cy="100" r="98" fill="#2b2b2e"/>
<path d="M78 28c-30 0-54 22-54 50 0 14 6 27 16 36l-10 22 26-12c7 3 14 4 22 4 30 0 54-22 54-50S108 28 78 28z" fill="#fbe6e3"/>
<path d="M78 35c-26 0-47 19-47 43 0 12 5 23 14 31l-6 15 17-8c7 3 14 5 22 5 26 0 47-19 47-43S104 35 78 35z" fill="none" stroke="#2b2b2e" stroke-width="1.6" stroke-dasharray="4 3"/>
<text x="78" y="90" text-anchor="middle" font-family="'Baloo 2','Mukta',sans-serif" font-weight="800" font-size="36" fill="#1d1d1f" transform="rotate(-14 78 80)">विचार</text>
<text x="130" y="162" text-anchor="middle" font-family="'Mukta',Arial,sans-serif" font-weight="800" font-size="30" letter-spacing="1" fill="#f2c4bb">MANCH</text>
</svg>"""

E = html.escape

# =============================================================== LAYOUT ====


def nav_html(p, current):
    sub = "".join(f'<li><a href="{p}services/{s["slug"]}.html">{E(s["nav"])}</a></li>' for s in SERVICES)
    items = [("index.html", "Home"), ("about.html", "About"), ("services.html", "Services"),
             ("clients.html", "Clients"), ("gallery.html", "Our Work"), ("contact.html", "Contact")]
    lis = []
    for href, label in items:
        cur = ' aria-current="page"' if current == href else ""
        if href == "services.html":
            lis.append(f'<li class="has-sub"><a href="{p}{href}"{cur}>{label}</a><ul class="submenu">{sub}</ul></li>')
        else:
            lis.append(f'<li><a href="{p}{href}"{cur}>{label}</a></li>')
    return "".join(lis)


def page(filename, title, description, body, current=None, depth=0, og_image="bpcl-mumbai-refinery.jpg"):
    p = "../" * depth
    full_title = f"{title} | {NAME}" if title != NAME else f"{FULL_NAME} | Nukkad Natak & Corporate Theatre, Pan India"
    url_path = "" if filename == "index.html" else filename
    canonical = f'<link rel="canonical" href="{SITE_URL}/{url_path}">' if SITE_URL else ""
    og_img = f"{SITE_URL}/assets/img/{og_image}" if SITE_URL else f"{p}assets/img/{og_image}"
    ld = {
        "@context": "https://schema.org", "@type": "PerformingGroup", "name": FULL_NAME,
        "alternateName": NAME, "email": EMAIL, "telephone": [f"+91{d}" for d, _ in PHONES],
        "areaServed": "India", "sameAs": [YOUTUBE],
        "address": {"@type": "PostalAddress", "addressLocality": "Delhi", "addressCountry": "IN"},
        "description": "Nukkad natak (street theatre) team for corporate safety, POSH, CSR, government and brand awareness campaigns across India.",
    }
    phones_footer = "".join(f'<li><a href="tel:+91{d}">{v}</a></li>' for d, v in PHONES)
    svc_footer = "".join(f'<li><a href="{p}services/{s["slug"]}.html">{E(s["nav"])}</a></li>' for s in SERVICES)
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(full_title)}</title>
<meta name="description" content="{E(description)}">
{canonical}
<meta property="og:type" content="website">
<meta property="og:title" content="{E(full_title)}">
<meta property="og:description" content="{E(description)}">
<meta property="og:image" content="{og_img}">
<meta name="theme-color" content="#7a1f2b">
<link rel="icon" href="{p}assets/img/logo.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Baloo+2:wght@600;700;800&family=Mukta:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{p}assets/css/style.css">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <div class="wrap nav">
    <a class="brand" href="{p}index.html" aria-label="{NAME} home">{LOGO_SVG}<span><span class="brand-name">Vichar Manch</span><span class="brand-sub">The Nukkad Natak Team</span></span></a>
    <button class="nav-toggle" aria-label="Open menu" aria-expanded="false" aria-controls="menu"><span></span><span></span><span></span></button>
    <ul class="menu" id="menu">
      {nav_html(p, current)}
    </ul>
  </div>
</header>
<main id="main">
{body}
</main>
<footer class="site-footer">
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <a class="brand" href="{p}index.html">{LOGO_SVG}<span><span class="brand-name">Vichar Manch</span><span class="brand-sub">The Nukkad Natak Team</span></span></a>
        <p>Theatre-led awareness for corporates, plants, government and NGOs. Head office in Delhi, operations in Mumbai, performing across India.</p>
        <p><a href="{YOUTUBE}" target="_blank" rel="noopener">▶ Watch us on YouTube</a></p>
      </div>
      <div><h4>Services</h4><ul>{svc_footer}</ul></div>
      <div><h4>Explore</h4><ul>
        <li><a href="{p}about.html">About us</a></li><li><a href="{p}clients.html">Clients</a></li>
        <li><a href="{p}gallery.html">Photos & videos</a></li><li><a href="{p}contact.html">Contact</a></li></ul></div>
      <div><h4>Get in touch</h4><ul>{phones_footer}
        <li><a href="mailto:{EMAIL}">{EMAIL}</a></li><li>Delhi · Mumbai · Pan India</li></ul></div>
    </div>
    <div class="foot-bottom"><span>© <span id="year">2026</span> {FULL_NAME}</span></div>
  </div>
</footer>
<a class="float-call" href="tel:+91{PHONES[0][0]}" aria-label="Call Vichar Manch">{icon("phone")}</a>
<a class="float-wa" href="https://wa.me/{WHATSAPP}?text={E('Hello Vichar Manch, I would like to know more about your nukkad natak performances.')}" target="_blank" rel="noopener" aria-label="Chat on WhatsApp">{WA_SVG}</a>
<script src="{p}assets/js/main.js" defer></script>
</body>
</html>
"""

# =============================================================== BLOCKS ====


def hero(p, img, eyebrow, h1, lead, buttons, tags=None, crumbs=None, small=False, tagline=None, home=False):
    """`lead` may be a string (one paragraph) or a list of paragraphs."""
    tag_html = f'<ul class="hero-tags">{"".join(f"<li>{E(t)}</li>" for t in tags)}</ul>' if tags else ""
    crumb_html = f'<div class="crumbs">{crumbs}</div>' if crumbs else ""
    paras = lead if isinstance(lead, list) else [lead]
    lead_html = "".join(f'<p class="lead">{t}</p>' for t in paras)
    tagline_html = f'<p class="hero-tagline">{E(tagline)}</p>' if tagline else ""
    classes = "hero" + (" page-hero" if small else "") + (" home-hero" if home else "")
    return f"""<section class="{classes}">
  <div class="hero-bg" style="background-image:url('{p}assets/img/{img}')" aria-hidden="true"></div>
  <div class="wrap">
    {crumb_html}<span class="eyebrow">{eyebrow}</span>
    <h1>{h1}</h1>
    {lead_html}
    {tagline_html}
    {tag_html}
    <div class="btn-row">{buttons}</div>
  </div>
</section>"""


def contact_buttons(p, light=True):
    ghost = "btn-ghost" if light else "btn-ghost-dark"
    return (f'<a class="btn btn-gold" href="tel:+91{PHONES[0][0]}">{icon("phone")}Call {PHONES[0][1]}</a>'
            f'<a class="btn {ghost}" href="https://wa.me/{WHATSAPP}" target="_blank" rel="noopener">{icon("mail")}WhatsApp us</a>')


def stats_block():
    cells = "".join(f'<div class="stat"><b>{v}</b><span>{l}</span></div>' for v, l in STATS)
    return f'<section class="stats" aria-label="Key facts"><div class="wrap stats-grid">{cells}</div></section>'


def section_head(kicker, title, text="", center=False):
    t = f"<p>{text}</p>" if text else ""
    return f'<div class="section-head{" center" if center else ""} reveal"><span class="kicker">{kicker}</span><h2>{title}</h2>{t}</div>'


def service_cards(p, with_tags=False):
    out = []
    for s in SERVICES:
        tags = f'<div class="tags">{" · ".join(E(t) for t in s["topics"][:3])}</div>' if with_tags else ""
        out.append(f'<a class="card reveal" href="{p}services/{s["slug"]}.html"><span class="icon">{icon(s["icon"])}</span>'
                   f'<h3>{E(s["title"])}</h3><p>{E(s["short"])}</p>{tags}<span class="more">Learn more</span></a>')
    return f'<div class="grid grid-3">{"".join(out)}</div>'


def format_block():
    items = [("20–30 minutes", "Short enough for a shift change, long enough to stick."),
             ("No stage needed", "No equipment, sound system or set-up time."),
             ("Any open space", "Plant, gate, canteen, office floor or yard."),
             ("Hindi or local language", "English too, for corporate audiences."),
             ("Across all shifts", "Multiple shows a day to cover everyone.")]
    cells = "".join(f"<div><b>{a}</b><span>{b}</span></div>" for a, b in items)
    return f'<div class="format reveal">{cells}</div>'


LOGO_DIR = os.path.join(OUT, "assets", "img", "clients")


def client_slug(name):
    import re
    return re.sub(r"[^a-z0-9]+", "-", name.lower().replace("ä", "a")).strip("-")


def client_logo(name):
    """Return the logo's site path if an official logo file has been added, else None.
    Drop files named e.g. aditya-birla-group.svg / hafele.png into site/assets/img/clients/."""
    for ext in ("svg", "png", "webp", "jpg"):
        f = f"{client_slug(name)}.{ext}"
        if os.path.exists(os.path.join(LOGO_DIR, f)):
            return f"assets/img/clients/{f}"
    return None


def client_tile(p, name, sector=None, reveal=True, alt=True):
    logo = client_logo(name)
    sub = f"<small>{E(sector)}</small>" if sector else ""
    rv = " reveal" if reveal else ""
    if logo:
        alt_text = f"{E(name)} logo" if alt else ""
        return (f'<div class="client has-logo{rv}"><img src="{p}{logo}" alt="{alt_text}" loading="lazy">'
                f'<span class="client-name">{E(name)}</span>{sub}</div>')
    return f'<div class="client{rv}"><span class="client-name">{E(name)}</span>{sub}</div>'


def clients_marquee(p="", with_sector=True):
    """All client logos in one row moving right-to-left in a seamless loop (#13).
    The set is rendered twice; the track slides by exactly one set width, so the
    second copy lands where the first started and the loop has no visible jump."""
    one = "".join(client_tile(p, n, s if with_sector else None, reveal=False) for n, s in CLIENTS)
    dup = "".join(client_tile(p, n, s if with_sector else None, reveal=False, alt=False) for n, s in CLIENTS)
    # load marquee logos eagerly: lazy-loading can leave blanks as tiles slide in from the right
    one, dup = one.replace(' loading="lazy"', ''), dup.replace(' loading="lazy"', '')
    return (f'<div class="marquee reveal" role="region" aria-label="Our clients">'
            f'<div class="marquee-track"><div class="marquee-set">{one}</div>'
            f'<div class="marquee-set" aria-hidden="true">{dup}</div></div></div>')


def clients_block(with_sector=True, p=""):
    return f"""{clients_marquee(p, with_sector)}
<div class="gov-band reveal"><h3>Government projects</h3>
<p>Awareness programmes and street plays on <b>Swachhta</b> (cleanliness), <b>Jal Sanrakshan</b> (water conservation) and other social causes, including projects associated with the <b>Delhi Government</b> and the <b>Government of India</b>.</p></div>"""


def gallery_block(p, photos, filters=False, captions=True):
    figs = []
    for i, (f, cap, sub, cat) in enumerate(photos):
        cls = "reveal wide" if (not filters and i == 0) else "reveal"
        figs.append(f'<figure class="{cls}" data-cat="{cat}"><img src="{p}assets/img/{f}" alt="Vichar Manch team – {E(cap)}" loading="lazy">'
                    + (f'<figcaption>{E(cap)}<small>{E(sub)}</small></figcaption>' if captions else '') + '</figure>')
    filt = ""
    if filters:
        opts = [("all", "All"), ("performance", "Live performances"), ("corporate", "Corporate & events"),
                ("industrial", "Plants & sites"), ("team", "Team")]
        filt = '<div class="filters" role="group" aria-label="Filter photos">' + "".join(
            f'<button type="button" data-filter="{k}" aria-pressed="{"true" if k == "all" else "false"}">{v}</button>' for k, v in opts) + "</div>"
    return f'{filt}<div class="gallery">{"".join(figs)}</div><div class="lightbox" role="dialog" aria-label="Photo viewer"><button type="button" aria-label="Close">×</button><div><img alt=""><p></p></div></div>'


FEATURED_PROJECT = {
    "img": "industrial-team-work.jpg",
    "title": "Industrial Safety & Workplace Awareness",
    "category": "Corporate Events / Nukkad Natak",
    "text": "An interactive workplace awareness initiative focused on promoting safety, quality, teamwork, and responsible workplace behaviour through engaging performances and activities.",
    "alt": "Vichar Manch artists on a factory floor beside a safety and quality vision-statement banner",
}


def project_card(p):
    f = FEATURED_PROJECT
    return f"""<article class="project-card reveal" tabindex="0" role="button" aria-label="View photo: {E(f['title'])}">
  <div class="project-img"><img src="{p}assets/img/{f['img']}" alt="{E(f['alt'])}" loading="lazy" width="1440" height="1080"></div>
  <div class="project-body">
    <span class="project-cat">{E(f['category'])}</span>
    <h3>{E(f['title'])}</h3>
    <p>{E(f['text'])}</p>
    <span class="more">View photo</span>
  </div>
</article>"""


def videos_block(ids):
    out = []
    for vid in ids:
        t, sub = VIDEOS[vid]
        out.append(f'<div class="video reveal"><div class="video-frame"><button type="button" data-id="{vid}" aria-label="Play video: {E(t)}">'
                   f'<img src="https://i.ytimg.com/vi/{vid}/hqdefault.jpg" alt="" loading="lazy"><span class="play"></span></button></div>'
                   f'<h3>{E(t)}</h3><p>{E(sub)}</p></div>')
    return f'<div class="videos">{"".join(out)}</div>'


def steps_block():
    lis = "".join(f'<li class="reveal"><h3>{E(a)}</h3><p>{E(b)}</p></li>' for a, b in STEPS)
    return f'<ol class="steps">{lis}</ol>'


def faq_block(items):
    return '<div class="faq">' + "".join(f'<details class="reveal"><summary>{E(q)}</summary><p>{E(a)}</p></details>' for q, a in items) + "</div>"


def cta_block(p, title="Planning a safety week or awareness campaign?", text=""):
    text_html = f"<p>{text}</p>" if text else ""
    return f"""<section class="cta"><div class="wrap">
  <div><h2>{title}</h2>{text_html}</div>
  <div class="btn-row">{contact_buttons(p)}<a class="btn btn-ghost" href="{p}contact.html">Send an enquiry</a></div>
</div></section>"""

# =============================================================== PAGES =====


def build_home():
    p = ""
    body = hero(p, "industrial-team-work.jpg", "Nukkad Natak · Corporate Theatre · Pan India",
                "Vichar Manch – <em>Where Thoughts Find a Voice.</em>",
                ["We are a leading provider of professionally curated Nukkad Natak and Street Play performances across India, creating meaningful experiences that inform, engage, and inspire audiences.",
                 "We collaborate with corporates, NGOs, educational institutions, and government organizations to deliver powerful, customized performances that turn public spaces into platforms for awareness, dialogue, and positive social change.",
                 "With creativity, powerful storytelling, and impactful performances at our core, we are committed to making every message count and every performance create an impact."],
                contact_buttons(p) + f'<a class="btn btn-ghost" href="{p}gallery.html">{icon("play")}Watch our work</a>',
                tags=["Workplace Safety", "Road Safety", "POSH", "CSR & Government", "Brand Promotions"],
                tagline="Bringing Stories to Streets. Creating Awareness. Inspiring Change.", home=True)
    body += stats_block()
    body += f"""<section class="section"><div class="wrap split">
  <div class="reveal">
    <span class="kicker">About Vichar Manch</span>
    <h2>Who We Are</h2>
    <p><b>Vichar Manch – The Nukkad Natak Team</b> is a collective of passionate theatre artists united by one belief: theatre has the power to influence minds, spark conversations, and inspire change.</p>
    <p>Through the power of storytelling and live performances, we bring important social messages closer to people. Our work goes beyond the stage, addressing real-world issues through thought-provoking, engaging, and impactful performances.</p>
    <p>From corporate awareness campaigns and educational programmes to social initiatives and community engagement, we create performances that inform, connect, and leave a lasting impression.</p>
    <p>Rooted in Delhi and performing across India, Vichar Manch transforms everyday spaces into stages where voices are heard, ideas are shared, and meaningful conversations begin.</p>
    <p class="statement">We don't just perform stories; we bring ideas to life, give voices to important issues, and use theatre as a medium to create meaningful change.</p>
    <a class="btn btn-maroon" href="{p}about.html">More about us</a>
  </div>
  <div class="photo-stack reveal"><img src="{p}assets/img/industrial-team-work.jpg" alt="Vichar Manch artists on a factory floor beside a safety and quality vision-statement banner" loading="lazy">
    <div class="badge"><b>150+</b>artists, Pan India</div></div>
</div></section>"""
    body += f"""<section class="section alt"><div class="wrap">
  {section_head("What we do", "Plays built for your workplace and your cause", "Every play is written for the audience in front of it — your site, your rules, your language.")}
  {service_cards(p)}
</div></section>"""
    body += f"""<section class="section dark"><div class="wrap">
  {section_head("The format", "Made to fit a working plant", "No stage, no equipment, no downtime. We come to your people instead of pulling them into a hall.")}
  {format_block()}
</div></section>"""
    body += f"""<section class="section"><div class="wrap">
  {section_head("Trusted by", "Organisations we have performed for", "From refineries and engineering sites to corporate offices and public campaigns.")}
  {clients_block(with_sector=False)}
</div></section>"""
    body += f"""<section class="section alt"><div class="wrap">
  {section_head("On the ground", "Glimpses from our campaigns")}
  {gallery_block(p, PHOTOS[:6])}
  <p style="margin-top:26px"><a class="btn btn-ghost-dark" href="{p}gallery.html">See all photos & videos</a></p>
</div></section>"""
    body += f"""<section class="section dark"><div class="wrap">
  {section_head("Watch", "See a performance", "Recent plays for our corporate and public campaigns.")}
  {videos_block(["gt7EYAoapiI", "ZhKOpwPU5Lg", "7sW5ql3PZnI"])}
  <p style="margin-top:26px"><a class="btn btn-gold" href="{YOUTUBE}" target="_blank" rel="noopener">{icon("play")}More on our YouTube channel</a></p>
</div></section>"""
    body += f"""<section class="section"><div class="wrap">
  {section_head("How we work", "From your brief to a live performance")}
  {steps_block()}
</div></section>"""
    body += cta_block(p)
    return page("index.html", NAME,
                "Vichar Manch is a Pan-India nukkad natak team with 150+ artists. Workplace safety, road safety, POSH, CSR, government and brand awareness street plays in Hindi, English and local languages.",
                body, current="index.html")


def build_about():
    p = ""
    strengths = [
        ("users", "150+ artists network", "A large pool of trained actors, writers and directors, so we can staff projects of any scale."),
        ("map", "150+ cities, Pan India", "Head office in Delhi, operations in Mumbai, and artists across the country for multi-location campaigns."),
        ("script", "Custom scripts", "Every script is written around your objective, your audience and your site."),
        ("lang", "Your audience’s language", "Hindi, English or the local language of the site, so the message lands instantly."),
        ("layers", "Multi-sector experience", "Plants, refineries, engineering sites, corporate offices, government and NGO campaigns."),
        ("clock", "Flexible execution", "Formats adapted to the audience, venue and schedule — including back-to-back shows across shifts."),
    ]
    cards = "".join(f'<div class="card reveal"><span class="icon">{icon(i)}</span><h3>{E(t)}</h3><p>{E(d)}</p></div>' for i, t, d in strengths)
    body = hero(p, "team-dhol.jpg", "About Vichar Manch", "Theatre that carries a message from the stage to the shop floor",
                "We are a nukkad natak team that helps organisations communicate what matters — safety, respect, responsibility and social change — through short, powerful live performances.",
                contact_buttons(p), small=True)
    body += f"""<section class="section"><div class="wrap split">
  <div class="reveal">
    <span class="kicker">Who we are</span>
    <h2>Vichar Manch – The Nukkad Natak Team</h2>
    <p>Vichar Manch is a theatre-based campaign and communication team specialising in corporate awareness programmes, workplace safety, social impact initiatives, NGO projects and brand promotions.</p>
    <p>With our head office in Delhi and operations in Mumbai, we have a strong Pan-India presence: <b>150+ trained artists across 150+ cities</b>. Our network includes experienced actors, writers and directors who create performances around each client’s specific requirements.</p>
    <p>Our name says what we do — <i>vichar</i> means thought, <i>manch</i> means stage. We put the ideas that matter on a stage where everyone can see them.</p>
  </div>
  <div class="photo-stack reveal"><img src="{p}assets/img/nsdl-1.jpg" alt="Vichar Manch team at NSDL" loading="lazy"></div>
</div></section>"""
    body += f"""<section class="section dark"><div class="wrap split reverse">
  <div class="reveal">
    <span class="kicker">Why live theatre</span>
    <h2>A play is remembered.</h2>
    <p>Most workplace communication is one-way: a circular, a slide deck, a banner at the gate. People see it, nod, and forget it.</p>
    <p>A nukkad natak is different. The audience stands in a circle, close to the actors. They laugh, they recognise their colleagues and themselves in the characters, and they see the consequence of a bad decision play out in front of them. That emotional connection is what changes behaviour.</p>
    <ul class="checks"><li>Reaches every level — from senior managers to contract workers</li><li>Works in any language and any literacy level</li><li>Starts conversations that continue after the show</li></ul>
  </div>
  <div class="photo-stack reveal"><img src="{p}assets/img/plant-hall-performance-4.jpg" alt="Plant workers standing in a circle around a Vichar Manch performance" loading="lazy"></div>
</div></section>"""
    body += f"""<section class="section"><div class="wrap">
  {section_head("Our strengths", "Why organisations choose Vichar Manch")}
  <div class="grid grid-3">{cards}</div>
</div></section>"""
    body += f"""<section class="section alt"><div class="wrap">
  {section_head("Themes we perform", "From the shop floor to the street")}
  <ul class="pills reveal">{"".join(f"<li>{E(t)}</li>" for t in THEMES)}</ul>
</div></section>"""
    body += f"""<section class="section"><div class="wrap">
  {section_head("Our approach", "Every campaign starts with understanding your objective")}
  {steps_block()}
</div></section>"""
    body += cta_block(p, "Let’s plan your next campaign together")
    return page("about.html", "About Us",
                "About Vichar Manch, a Delhi and Mumbai based nukkad natak team with 150+ artists across 150+ cities, creating custom awareness plays for corporates, government and NGOs.",
                body, current="about.html", og_image="team-dhol.jpg")


def build_services():
    p = ""
    body = hero(p, "john-cockerill.jpg", "Our services", "Street plays for safety, awareness and engagement",
                "Six ways we work with your teams — each one customised around your own SOPs, incident learnings, policies and local language.",
                contact_buttons(p), small=True)
    body += f"""<section class="section"><div class="wrap">
  {section_head("What we offer", "Choose the programme that fits your goal")}
  {service_cards(p, with_tags=True)}
</div></section>"""
    body += f"""<section class="section dark"><div class="wrap">
  {section_head("Play format", "Simple to organise, easy to scale")}
  {format_block()}
</div></section>"""
    body += f"""<section class="section alt"><div class="wrap">
  {section_head("Campaign support", "We plug into your safety and awareness calendar", "Book us for a single show or a full campaign across sites and shifts.")}
  <ul class="pills light reveal"><li>National Safety Week</li><li>Road Safety Month</li><li>Fire Service Week</li><li>Vigilance Awareness Week</li><li>POSH training cycles</li><li>World Environment Day</li><li>Swachhta Pakhwada</li><li>CSR community drives</li><li>Annual days & townhalls</li></ul>
</div></section>"""
    body += f"""<section class="section"><div class="wrap">
  {section_head("Themes", "Topics we regularly perform")}
  <ul class="pills reveal">{"".join(f"<li>{E(t)}</li>" for t in THEMES)}</ul>
</div></section>"""
    body += f"""<section class="section alt"><div class="wrap" style="max-width:900px">
  {section_head("FAQ", "Frequently asked questions", center=True)}
  {faq_block(FAQ)}
</div></section>"""
    body += cta_block(p)
    return page("services.html", "Services",
                "Nukkad natak services: plant and mine safety plays, road safety and contractor awareness, behavioural safety, POSH and corporate awareness, CSR and government campaigns, brand promotions.",
                body, current="services.html", og_image="john-cockerill.jpg")


def build_service(s):
    p = "../"
    crumbs = f'<a href="{p}index.html">Home</a> / <a href="{p}services.html">Services</a> / {E(s["nav"])}'
    intro = "".join(f"<p>{E(t)}</p>" for t in s["intro"])
    topics = "".join(f"<li>{E(t)}</li>" for t in s["topics"])
    good = "".join(f"<li>{E(t)}</li>" for t in s["good_for"])
    others = [o for o in SERVICES if o["slug"] != s["slug"]]
    other_cards = "".join(f'<a class="card reveal" href="{o["slug"]}.html"><span class="icon">{icon(o["icon"])}</span><h3>{E(o["title"])}</h3><span class="more">Explore</span></a>' for o in others)

    body = hero(p, s["img"], "Our service", E(s["title"]), E(s["short"]), contact_buttons(p), crumbs=crumbs, small=True)
    body += f"""<section class="section"><div class="wrap split">
  <div class="reveal"><span class="kicker">Overview</span><h2>Why this works</h2>{intro}</div>
  <div class="photo-stack reveal"><img src="{p}assets/img/{s['img']}" alt="Vichar Manch – {E(s['title'])}" loading="lazy"></div>
</div></section>"""
    body += f"""<section class="section alt"><div class="wrap">
  <div class="grid grid-2">
    <div class="card reveal"><h3>What we cover</h3><ul class="checks">{topics}</ul></div>
    <div class="card reveal"><h3>Ideal for</h3><ul class="checks">{good}</ul>
      <p>Every script is customised around your SOPs, site rules and local language.</p></div>
  </div>
</div></section>"""
    if s.get("clients"):
        cl = "".join(client_tile(p, c) for c in s["clients"])
        body += f"""<section class="section"><div class="wrap">
  {section_head("Track record", "Teams we have performed this for")}
  <div class="clients">{cl}</div>
</div></section>"""
    if s.get("videos"):
        body += f"""<section class="section dark"><div class="wrap">
  {section_head("Watch", "See it in action")}
  {videos_block(s["videos"])}
</div></section>"""
    body += f"""<section class="section dark"><div class="wrap">
  {section_head("Format", "How the performance runs")}
  {format_block()}
</div></section>""" if not s.get("videos") else ""
    body += f"""<section class="section"><div class="wrap">
  {section_head("Process", "From brief to performance")}
  {steps_block()}
</div></section>"""
    body += f"""<section class="section alt"><div class="wrap">
  {section_head("More services", "Explore other programmes")}
  <div class="grid grid-3">{other_cards}</div>
</div></section>"""
    body += cta_block(p, "Ready to plan this for your teams?")
    return page(f"services/{s['slug']}.html", s["title"], s["seo"], body, current="services.html", depth=1, og_image=s["img"])


def build_clients():
    p = ""
    site_files = ["asian-paints-stage.jpg", "bpcl-mumbai-refinery.jpg", "hindustan-platinum.jpg", "john-cockerill.jpg",
                  "hafele-warehouse.jpg", "aditya-birla-seamex.jpg", "asian-paints-khandala.jpg", "hafele.jpg", "nsdl-2.jpg"]
    site_photos = [next(ph for ph in PHOTOS if ph[0] == f) for f in site_files]
    body = hero(p, "hafele.jpg", "Clients", "Trusted by leading companies and public campaigns",
                "We have performed for reputed brands, corporates and organisations across India — from refineries and engineering sites to corporate headquarters.",
                contact_buttons(p), small=True)
    body += f"""<section class="section"><div class="wrap">
  {section_head("Corporate clients", "Brands and organisations we have worked with")}
  {clients_block()}
</div></section>"""
    body += f"""<section class="section alt"><div class="wrap">
  {section_head("On site", "Our team at client locations")}
  {gallery_block(p, site_photos)}
</div></section>"""
    body += f"""<section class="section dark"><div class="wrap">
  {section_head("Client work on video", "Performances for our clients")}
  {videos_block(["gt7EYAoapiI", "mkxtY8oDsKo", "T2Czo59FmxE"])}
</div></section>"""
    body += cta_block(p, "Join the organisations that trust Vichar Manch")
    return page("clients.html", "Clients",
                "Vichar Manch clients include Tata, HPCL, BPCL, Yes Bank, Asian Paints, NSDL, Aditya Birla Group, Häfele, Hero, John Cockerill, Seamex and Hindustan Platinum, plus Delhi Government and Government of India campaigns.",
                body, current="clients.html", og_image="hafele.jpg")


def build_gallery():
    p = ""
    body = hero(p, "nsdl-1.jpg", "Our work", "Photos and videos from the field",
                "A look at our team at client sites, corporate offices and public campaigns across India.",
                contact_buttons(p), small=True)
    body += f"""<section class="section"><div class="wrap">
  {section_head("Our work", "Featured project")}
  {project_card(p)}
  <div style="height:64px"></div>
  {section_head("Photos", "Campaign gallery")}
  {gallery_block(p, PHOTOS, filters=True, captions=False)}
</div></section>"""
    body += f"""<section class="section dark"><div class="wrap">
  {section_head("Videos", "Watch our performances")}
  {videos_block(list(VIDEOS.keys()))}
  <p style="margin-top:26px"><a class="btn btn-gold" href="{YOUTUBE}" target="_blank" rel="noopener">{icon("play")}Subscribe on YouTube</a></p>
</div></section>"""
    body += cta_block(p)
    return page("gallery.html", "Our Work – Photos & Videos",
                "Photos and videos of Vichar Manch nukkad natak performances for BPCL, Hindustan Platinum, John Cockerill, Häfele, Aditya Birla Group, NSDL and public awareness campaigns.",
                body, current="gallery.html", og_image="nsdl-1.jpg")


def build_contact():
    p = ""
    phone_links = "".join(f'<a href="tel:+91{d}">{v}</a>' for d, v in PHONES)
    svc_opts = "".join(f"<option>{E(s['title'])}</option>" for s in SERVICES)
    body = hero(p, "aditya-birla-seamex.jpg", "Contact", "Let’s plan your next campaign",
                "Share your dates, locations and topic. We’ll send our company profile and suggest suitable plays.",
                contact_buttons(p), small=True)
    body += f"""<section class="section"><div class="wrap contact-grid">
  <div class="reveal">
    <span class="kicker">Get in touch</span>
    <h2>Talk to Vichar Manch</h2>
    <ul class="contact-list">
      <li><span class="ic">{icon("phone")}</span><div class="phones"><b>Call us</b>{phone_links}</div></li>
      <li><span class="ic">{icon("mail")}</span><div><b>Email</b><a href="mailto:{EMAIL}">{EMAIL}</a></div></li>
      <li><span class="ic">{icon("pin")}</span><div><b>Locations</b><span style="font-weight:600;font-size:1.08rem">Head office: Delhi<br>Operations: Mumbai<br>Performing Pan India</span></div></li>
      <li><span class="ic">{icon("play")}</span><div><b>YouTube</b><a href="{YOUTUBE}" target="_blank" rel="noopener">@Vicharmanchnukkadteam</a></div></li>
    </ul>
  </div>
  <form class="form reveal" id="enquiry" data-wa="{WHATSAPP}" data-email="{EMAIL}" novalidate>
    <h3>Send an enquiry</h3>
    <p class="hint">Fill this in and send it to us on WhatsApp or by email.</p>
    <div class="field-row">
      <div class="field"><label for="f-name">Your name *</label><input id="f-name" name="name" required autocomplete="name"></div>
      <div class="field"><label for="f-org">Organisation</label><input id="f-org" name="org" autocomplete="organization"></div>
    </div>
    <div class="field-row">
      <div class="field"><label for="f-phone">Phone *</label><input id="f-phone" name="phone" type="tel" required autocomplete="tel"></div>
      <div class="field"><label for="f-city">City / site</label><input id="f-city" name="city"></div>
    </div>
    <div class="field"><label for="f-service">What do you need?</label><select id="f-service" name="service"><option>Not sure yet</option>{svc_opts}</select></div>
    <div class="field"><label for="f-msg">Dates, number of shows, language, anything else</label><textarea id="f-msg" name="message" rows="4"></textarea></div>
    <div class="btn-row">
      <button class="btn btn-wa" type="submit" value="wa">Send on WhatsApp</button>
      <button class="btn btn-maroon" type="submit" value="email">Send by email</button>
    </div>
  </form>
</div></section>"""
    body += f"""<section class="section alt"><div class="wrap" style="max-width:900px">
  {section_head("Before you call", "Common questions", center=True)}
  {faq_block(FAQ)}
</div></section>"""
    return page("contact.html", "Contact Us",
                f"Contact Vichar Manch for nukkad natak and corporate awareness plays anywhere in India. Call {' or '.join(v for _, v in PHONES)}, or email {EMAIL}.",
                body, current="contact.html", og_image="aditya-birla-seamex.jpg")


def write(rel, content):
    path = os.path.join(OUT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)
    print("wrote", rel)


def main():
    write("index.html", build_home())
    write("about.html", build_about())
    write("services.html", build_services())
    for s in SERVICES:
        write(f"services/{s['slug']}.html", build_service(s))
    write("clients.html", build_clients())
    write("gallery.html", build_gallery())
    write("contact.html", build_contact())
    if SITE_URL:
        pages = ["index.html", "about.html", "services.html", "clients.html", "gallery.html", "contact.html"] + \
                [f"services/{s['slug']}.html" for s in SERVICES]
        urls = "".join(f"<url><loc>{SITE_URL}/{'' if pg == 'index.html' else pg}</loc></url>" for pg in pages)
        write("sitemap.xml", f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>')
        write("robots.txt", f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}/sitemap.xml\n")


if __name__ == "__main__":
    main()
