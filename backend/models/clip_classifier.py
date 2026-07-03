from transformers import CLIPProcessor, CLIPModel
from PIL import Image
import torch

# Load CLIP model from local cache
model = CLIPModel.from_pretrained(
    "openai/clip-vit-base-patch32",
    local_files_only=True
)

processor = CLIPProcessor.from_pretrained(
    "openai/clip-vit-base-patch32",
    local_files_only=True
)

# Load categories
with open("data/categories.txt", "r") as f:
    CATEGORIES = [line.strip() for line in f if line.strip()]


def classify_image(image_path):
    image = Image.open(image_path).convert("RGB")

    inputs = processor(
        text=CATEGORIES,
        images=image,
        return_tensors="pt",
        padding=True
    )

    with torch.no_grad():
        outputs = model(**inputs)

    logits = outputs.logits_per_image
    probs = logits.softmax(dim=1)[0]

    # Get top 5 predictions (or fewer if categories are less than 5)
    k = min(5, len(CATEGORIES))
    top_probs, top_indices = torch.topk(probs, k)

    top_predictions = []

    for score, idx in zip(top_probs.tolist(), top_indices.tolist()):
        top_predictions.append({
            "category": CATEGORIES[idx],
            "confidence": round(score, 3)
        })

    return {
        "category": top_predictions[0]["category"],
        "confidence": top_predictions[0]["confidence"],
        "top_predictions": top_predictions
    }