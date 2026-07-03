from backend.models.clip_classifier import classify_image

# Path to your uploaded image
image_path = "uploads/backpack.jpg"

category = classify_image(image_path)

print("Predicted Category:", category)