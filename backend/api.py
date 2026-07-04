from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
import shutil

from backend.models.blip import generate_caption
from backend.models.clip_classifier import classify_image

from backend.utils.extractor import extract_attributes
from backend.utils.color_detector import detect_color
from backend.utils.description import generate_description
from backend.utils.ocr import detect_brand
from backend.utils.title_generator import generate_title
from backend.utils.keywords import generate_keywords
from backend.utils.tags import generate_tags

app = FastAPI(
    title="AI Product Catalog Generator",
    description="AI-powered Product Catalog Generator",
    version="1.0.0"
)

# ==========================
# CORS
# ==========================
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "https://ai-product-catalog.vercel.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# ==========================
# Upload Folder
# ==========================
BASE_DIR = Path(__file__).resolve().parent.parent
UPLOAD_FOLDER = BASE_DIR / "uploads"
UPLOAD_FOLDER.mkdir(parents=True, exist_ok=True)

# ==========================
# Home
# ==========================
@app.get("/")
def home():
    return {
        "message": "Welcome to AI Product Catalog Generator",
        "status": "API Running Successfully"
    }

# ==========================
# Upload API
# ==========================
@app.post("/upload")
async def upload_image(file: UploadFile = File(...)):

    file_path = UPLOAD_FOLDER / file.filename

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    image_path = str(file_path)

    # Generate caption
    caption = generate_caption(image_path)

    # Classify image
    classification = classify_image(image_path)

    # Extract attributes
    attributes = extract_attributes(caption)

    # Detect brand
    ocr_brand = detect_brand(image_path)

    if ocr_brand != "Unknown":
        brand = ocr_brand
    else:
        brand = attributes.get("brand", "Unknown")

    # Detect color
    color = detect_color(image_path)

    # Generate title
    title = generate_title(
        classification["category"],
        brand,
        color,
        caption
    )

    # Generate keywords
    keywords = generate_keywords(
        classification["category"],
        brand,
        color,
        caption
    )

    # Generate description
    description = generate_description(
        classification["category"],
        brand,
        color
    )

    # Generate tags
    tags = generate_tags(
        classification["category"],
        brand,
        color
    )

    return {
        "filename": file.filename,
        "title": title,
        "caption": caption,
        "category": classification["category"],
        "confidence": round(classification["confidence"], 3),
        "brand": brand,
        "color": color,
        "keywords": keywords,
        "description": description,
        "tags": tags,
        "top_predictions": classification["top_predictions"]
    }