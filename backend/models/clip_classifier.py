from transformers import CLIPProcessor, CLIPModel
from PIL import Image
from pathlib import Path
import torch

processor = None
model = None
CATEGORIES = None


def load_clip():
    global processor, model, CATEGORIES

    if processor is None or model is None:

        print("Loading CLIP Model...")

        model = CLIPModel.from_pretrained(
            "openai/clip-vit-base-patch32"
        )

        processor = CLIPProcessor.from_pretrained(
            "openai/clip-vit-base-patch32"
        )

        model.eval()

        categories_path = (
            Path(__file__).resolve().parents[2]
            / "data"
            / "categories.txt"
        )

        with open(categories_path, "r") as f:
            CATEGORIES = [
                line.strip()
                for line in f
                if line.strip()
            ]

        print("CLIP Loaded Successfully!")


def classify_image(image_path):

    load_clip()

    image = Image.open(image_path).convert("RGB")

    inputs = processor(
        text=CATEGORIES,
        images=image,
        return_tensors="pt",
        padding=True
    )

    with torch.no_grad():
        outputs = model(**inputs)

    probs = outputs.logits_per_image.softmax(dim=1)[0]

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