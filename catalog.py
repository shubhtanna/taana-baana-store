"""Taana Baana's range. Garment art: shape + fabric colour + weave pattern."""

CATEGORIES = [
    {"slug": "kurtas", "name": "Kurtas", "blurb": "Handwoven cotton and khadi kurtas for every day"},
    {"slug": "shirts", "name": "Shirts", "blurb": "Easy handloom shirts for warm days"},
    {"slug": "sarees", "name": "Sarees", "blurb": "Handwoven sarees from weaving clusters across India"},
    {"slug": "dupattas", "name": "Dupattas & stoles", "blurb": "Light layers in cotton, mul and silk"},
]

ALPHA = ["S", "M", "L", "XL", "XXL"]

PRODUCTS = [
    # ---- kurtas
    {"sku": "TB-KU-01", "slug": "indigo-cotton-kurta", "name": "Indigo Handblock Cotton Kurta", "category": "kurtas", "price": 1290, "mrp": 1590,
     "fabric": "Handloom cotton, hand-block printed in Bagru", "fit": "Straight, knee length", "sizes": ALPHA, "soldout": ["XXL"],
     "shape": "kurta", "colour": "#2c3e7a", "pattern": "dots", "featured": True,
     "description": "A deep indigo kurta block-printed by hand in Bagru, Rajasthan. Soft, breathable and better with every wash."},
    {"sku": "TB-KU-02", "slug": "white-chikankari-cotton-kurta", "name": "White Chikankari Cotton Kurta", "category": "kurtas", "price": 1490, "mrp": 1890,
     "fabric": "Cotton mul with Lucknowi chikankari", "fit": "Relaxed, knee length", "sizes": ALPHA, "soldout": [],
     "shape": "kurta", "colour": "#f4f1ea", "pattern": "flowers", "featured": True,
     "description": "Fine shadow-work chikankari hand-embroidered in Lucknow on a feather-light cotton mul."},
    {"sku": "TB-KU-03", "slug": "rust-khadi-kurta", "name": "Rust Khadi Kurta", "category": "kurtas", "price": 1390, "mrp": 1690,
     "fabric": "Hand-spun, handwoven khadi cotton", "fit": "Straight, mid-thigh", "sizes": ALPHA, "soldout": ["S"],
     "shape": "kurta", "colour": "#b0532c", "pattern": "plain", "featured": False,
     "description": "Earthy rust khadi with a gentle slub texture. Cool in summer, warm in winter."},
    {"sku": "TB-KU-04", "slug": "mustard-ikat-cotton-kurta", "name": "Mustard Ikat Cotton Kurta", "category": "kurtas", "price": 1690, "mrp": 2090,
     "fabric": "Pochampally ikat cotton", "fit": "A-line, calf length", "sizes": ALPHA, "soldout": [],
     "shape": "kurta", "colour": "#c99a1f", "pattern": "ikat", "featured": True,
     "description": "Double ikat woven in Pochampally, Telangana. The pattern is dyed into the threads before weaving."},
    {"sku": "TB-KU-05", "slug": "green-kalamkari-kurta", "name": "Green Kalamkari Cotton Kurta", "category": "kurtas", "price": 1590, "mrp": 1990,
     "fabric": "Cotton, natural-dye kalamkari from Pedana", "fit": "Straight, knee length", "sizes": ALPHA, "soldout": ["XL", "XXL"],
     "shape": "kurta", "colour": "#3f6b4a", "pattern": "flowers", "featured": False,
     "description": "Vegetable-dyed kalamkari motifs on a soft green cotton. Each piece varies slightly."},
    {"sku": "TB-KU-06", "slug": "black-handloom-kurta", "name": "Black Handloom Cotton Kurta", "category": "kurtas", "price": 1190, "mrp": 1490,
     "fabric": "Handloom cotton", "fit": "Straight, mid-thigh", "sizes": ALPHA, "soldout": [],
     "shape": "kurta", "colour": "#26231f", "pattern": "stripes", "featured": False,
     "description": "A clean black kurta with a subtle self-stripe weave. Pairs with everything."},
    {"sku": "TB-KU-07", "slug": "maroon-tussar-kurta", "name": "Maroon Tussar Silk Kurta", "category": "kurtas", "price": 3290, "mrp": 3990,
     "fabric": "Tussar silk from Bhagalpur", "fit": "Straight, knee length", "sizes": ALPHA, "soldout": ["S"],
     "shape": "kurta", "colour": "#6e1e2b", "pattern": "plain", "featured": False,
     "description": "A festive kurta in natural tussar silk with a rich, uneven sheen."},

    # ---- shirts
    {"sku": "TB-SH-01", "slug": "sky-blue-handloom-shirt", "name": "Sky Blue Handloom Shirt", "category": "shirts", "price": 1390, "mrp": 1690,
     "fabric": "Handloom cotton", "fit": "Regular, half sleeves", "sizes": ALPHA, "soldout": [],
     "shape": "shirt", "colour": "#7fa7cf", "pattern": "plain", "featured": True,
     "description": "A soft, airy shirt for long summers. Coconut-shell buttons."},
    {"sku": "TB-SH-02", "slug": "olive-khadi-shirt", "name": "Olive Khadi Shirt", "category": "shirts", "price": 1490, "mrp": 1790,
     "fabric": "Khadi cotton", "fit": "Relaxed, full sleeves", "sizes": ALPHA, "soldout": ["XXL"],
     "shape": "shirt", "colour": "#6b6b3a", "pattern": "plain", "featured": False,
     "description": "Textured olive khadi with a mandarin collar. Roll the sleeves up and go."},
    {"sku": "TB-SH-03", "slug": "checked-madras-shirt", "name": "Red Madras Check Shirt", "category": "shirts", "price": 1290, "mrp": 1590,
     "fabric": "Handwoven Madras cotton", "fit": "Regular, half sleeves", "sizes": ALPHA, "soldout": [],
     "shape": "shirt", "colour": "#a8322d", "pattern": "checks", "featured": False,
     "description": "Classic Madras checks woven in Tamil Nadu, light enough for a Chennai afternoon."},

    # ---- sarees
    {"sku": "TB-SA-01", "slug": "maheshwari-silk-cotton-saree", "name": "Maheshwari Silk-Cotton Saree", "category": "sarees", "price": 3490, "mrp": 4290,
     "fabric": "Silk-cotton from Maheshwar", "fit": "5.5 m with blouse piece", "sizes": ["Free size"], "soldout": [],
     "shape": "saree", "colour": "#8a4f9e", "pattern": "border", "featured": True,
     "description": "A light, crisp Maheshwari with a reversible border, woven on the banks of the Narmada."},
    {"sku": "TB-SA-02", "slug": "bengal-tant-cotton-saree", "name": "Bengal Tant Cotton Saree", "category": "sarees", "price": 1890, "mrp": 2290,
     "fabric": "Tant cotton from Shantipur", "fit": "5.5 m without blouse piece", "sizes": ["Free size"], "soldout": [],
     "shape": "saree", "colour": "#d9c7a0", "pattern": "border", "featured": False,
     "description": "The everyday Bengal classic: crisp, airy cotton with a bright woven border."},
    {"sku": "TB-SA-03", "slug": "chanderi-saree-peach", "name": "Peach Chanderi Saree", "category": "sarees", "price": 4290, "mrp": 4990,
     "fabric": "Chanderi silk-cotton with zari buttis", "fit": "5.5 m with blouse piece", "sizes": ["Free size"], "soldout": ["Free size"],
     "shape": "saree", "colour": "#e8a98a", "pattern": "dots", "featured": False,
     "description": "Sheer Chanderi with tiny gold buttis. Back in stock after the next loom cycle."},

    # ---- dupattas
    {"sku": "TB-DU-01", "slug": "ajrakh-cotton-dupatta", "name": "Ajrakh Cotton Dupatta", "category": "dupattas", "price": 890, "mrp": 1090,
     "fabric": "Cotton, Ajrakh block print from Kutch", "fit": "2.4 m × 1 m", "sizes": ["One size"], "soldout": [],
     "shape": "dupatta", "colour": "#7b2430", "pattern": "ikat", "featured": True,
     "description": "Deep madder red and indigo Ajrakh, printed in Kutch using a 14-step natural-dye process."},
    {"sku": "TB-DU-02", "slug": "mul-cotton-stole-white", "name": "Mul Cotton Stole, Ivory", "category": "dupattas", "price": 690, "mrp": 790,
     "fabric": "Mul cotton", "fit": "2 m × 0.7 m", "sizes": ["One size"], "soldout": [],
     "shape": "dupatta", "colour": "#efe8da", "pattern": "stripes", "featured": False,
     "description": "A barely-there mul stole for hot evenings."},
    {"sku": "TB-DU-03", "slug": "bandhani-silk-dupatta", "name": "Bandhani Silk Dupatta", "category": "dupattas", "price": 1990, "mrp": 2390,
     "fabric": "Gaji silk, hand-tied bandhani from Jamnagar", "fit": "2.4 m × 1 m", "sizes": ["One size"], "soldout": [],
     "shape": "dupatta", "colour": "#d8452e", "pattern": "dots", "featured": False,
     "description": "Thousands of hand-tied dots on a glowing silk. A wedding-season favourite."},
]

FREE_SHIPPING_FROM = 1499
SHIPPING_FEE = 99

BY_SKU = {p["sku"]: p for p in PRODUCTS}
BY_SLUG = {p["slug"]: p for p in PRODUCTS}


def in_category(slug):
    return [p for p in PRODUCTS if p["category"] == slug]


def category(slug):
    return next((c for c in CATEGORIES if c["slug"] == slug), None)


def available_sizes(p):
    return [s for s in p["sizes"] if s not in p["soldout"]]
