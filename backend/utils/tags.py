CATEGORY_TAGS = {
    "shoe": [
        "Footwear",
        "Sports",
        "Casual",
        "Outdoor",
        "Fashion"
    ],
    "backpack": [
        "Travel",
        "Office",
        "School",
        "Outdoor",
        "Bag"
    ],
    "laptop": [
        "Electronics",
        "Office",
        "Gaming",
        "Portable"
    ],
    "mobile phone": [
        "Electronics",
        "Smartphone",
        "Communication"
    ],
    "watch": [
        "Fashion",
        "Accessories",
        "Lifestyle"
    ],
    "bottle": [
        "Kitchen",
        "Fitness",
        "Travel",
        "Reusable"
    ]
}


def generate_tags(category, brand, color):

    tags = set()

    if brand != "Unknown":
        tags.add(brand)

    for c in color.split(","):
        c = c.strip()
        if c:
            tags.add(c)

    if category.lower() in CATEGORY_TAGS:
        tags.update(CATEGORY_TAGS[category.lower()])

    tags.add(category.title())

    return sorted(list(tags))