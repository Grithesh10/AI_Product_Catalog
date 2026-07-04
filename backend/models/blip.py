from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import torch

processor = None
model = None


def load_blip():
    global processor, model

    if processor is None or model is None:
        print("Loading BLIP Model...")

        processor = BlipProcessor.from_pretrained(
            "Salesforce/blip-image-captioning-base"
        )

        model = BlipForConditionalGeneration.from_pretrained(
            "Salesforce/blip-image-captioning-base"
        )

        model.eval()

        print("BLIP Loaded Successfully!")


def generate_caption(image_path):
    """
    Generate image caption using BLIP
    """

    load_blip()

    image = Image.open(image_path).convert("RGB")

    inputs = processor(images=image, return_tensors="pt")

    with torch.no_grad():
        output = model.generate(**inputs)

    caption = processor.decode(
        output[0],
        skip_special_tokens=True
    )

    return caption