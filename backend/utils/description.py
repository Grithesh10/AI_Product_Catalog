def generate_description(category, brand, color):
    category = category.lower()

    if color != "Unknown":
        color = color.lower()
    else:
        color = ""

    if brand != "Unknown":
        brand = brand.title()
    else:
        brand = ""

    description = (
        f"A stylish {color} {brand} {category} suitable for travel, office, "
        f"daily use, and outdoor activities. Designed with durability, comfort, "
        f"and modern aesthetics, this product offers excellent functionality "
        f"for everyday needs."
    )

    return " ".join(description.split())