from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image

print("Loading BLIP Model...")

processor = BlipProcessor.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)

model = BlipForConditionalGeneration.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)

print("BLIP Loaded Successfully!")


def generate_caption(image_path):
    """
    Generate caption from image
    """

    image = Image.open(image_path).convert("RGB")

    inputs = processor(image, return_tensors="pt")

    output = model.generate(**inputs)

    caption = processor.decode(output[0], skip_special_tokens=True)

    return caption