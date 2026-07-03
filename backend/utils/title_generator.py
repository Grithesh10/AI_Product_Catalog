def generate_title(category, brand, color, caption):
    """
    Generate a clean professional product title.
    """

    caption = caption.title().strip()

    # Remove brand from caption if it already exists
    if brand != "Unknown":
        if caption.lower().startswith(brand.lower()):
            caption = caption[len(brand):].strip()

    if brand == "Unknown":
        title = caption
    else:
        title = f"{brand} {caption}"

    return title.strip()