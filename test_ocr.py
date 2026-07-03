from backend.utils.ocr import detect_text

result = detect_text("uploads/backpack.jpg")

print("Detected Text:", result)