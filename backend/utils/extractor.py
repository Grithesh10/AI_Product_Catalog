def extract_attributes(caption):
    caption = caption.lower()

    categories = [
        "backpack",
        "handbag",
        "shoe",
        "shirt",
        "watch",
        "bottle",
        "chair",
        "laptop",
        "phone"
    ]

    colors = [
        "black",
        "white",
        "blue",
        "red",
        "green",
        "yellow",
        "brown",
        "grey"
    ]

    brands = [
        "nike",
        "adidas",
        "puma",
        "apple",
        "samsung",
        "north face"
    ]

    category = "Unknown"
    color = "Unknown"
    brand = "Unknown"

    for item in categories:
        if item in caption:
            category = item.title()

    for item in colors:
        if item in caption:
            color = item.title()

    for item in brands:
        if item in caption:
            brand = item.title()

    return {
        "category": category,
        "color": color,
        "brand": brand
    }