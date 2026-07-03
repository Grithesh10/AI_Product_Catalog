import easyocr

reader = easyocr.Reader(['en'], gpu=False)

KNOWN_BRANDS = [
    "nike",
    "adidas",
    "puma",
    "apple",
    "samsung",
    "dell",
    "hp",
    "lenovo",
    "north face",
    "asus",
    "acer",
    "sony",
    "boat",
    "realme",
    "oppo",
    "vivo"
]

def detect_brand(image_path):
    results = reader.readtext(image_path)

    if not results:
        return "Unknown"

    detected_text = " ".join([item[1] for item in results]).lower()

    for brand in KNOWN_BRANDS:
        if brand in detected_text:
            return brand.title()

    return "Unknown"