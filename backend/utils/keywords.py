def generate_keywords(category, brand, color, caption):

    keywords = set()

    if brand != "Unknown":
        keywords.add(brand)

    keywords.add(category.title())

    # Caption words
    for word in caption.title().split():
        if len(word) > 2:
            keywords.add(word)

    # Colors
    for c in color.split(","):
        c = c.strip()
        if c:
            keywords.add(c)
            keywords.add(f"{c} {category.title()}")

    # Category-specific keywords
    CATEGORY_KEYWORDS = {
        "shoe": [
            "Running Shoes",
            "Sports Shoes",
            "Athletic Footwear",
            "Sneakers"
        ],
        "backpack": [
            "Travel Backpack",
            "Laptop Backpack",
            "School Bag"
        ],
        "bottle": [
            "Water Bottle",
            "Reusable Bottle",
            "Sports Bottle"
        ],
        "laptop": [
            "Gaming Laptop",
            "Office Laptop",
            "Portable Computer"
        ],
        "mobile phone": [
            "Smartphone",
            "Android Phone",
            "Mobile Device"
        ]
    }

    if category.lower() in CATEGORY_KEYWORDS:
        keywords.update(CATEGORY_KEYWORDS[category.lower()])

    return sorted(list(keywords))