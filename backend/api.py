from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import os
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
    title="AI Product Catalog Generator"
)

# ==========================
# CORS Middleware
# ==========================
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://localhost:3001",
        "http://127.0.0.1:3000",
        "http://127.0.0.1:3001",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.get("/")
def home():
    return {
        "message": "Welcome to AI Product Catalog Generator",
        "status": "API Running Successfully"
    }


@app.post("/upload")
async def upload_image(file: UploadFile = File(...)):

    # Save uploaded image
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Generate Caption
    caption = generate_caption(file_path)

    # Classify Image
    classification = classify_image(file_path)

    # Extract Attributes
    attributes = extract_attributes(caption)

    # Detect Brand using OCR
    ocr_brand = detect_brand(file_path)

    if ocr_brand != "Unknown":
        brand = ocr_brand
    else:
        brand = attributes["brand"]

    # Detect Color
    color = detect_color(file_path)

    # Generate Title
    title = generate_title(
        classification["category"],
        brand,
        color,
        caption
    )

    # Generate Keywords
    keywords = generate_keywords(
        classification["category"],
        brand,
        color,
        caption
    )

    # Generate Description
    description = generate_description(
        classification["category"],
        brand,
        color
    )

    # Generate Tags
    tags = generate_tags(
        classification["category"],
        brand,
        color
    )

    # Return Response
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