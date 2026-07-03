from transformers import CLIPModel, CLIPProcessor

print("Downloading CLIP model... Please wait.")

model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

print("✅ CLIP model downloaded successfully!")