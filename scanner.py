from flask import Blueprint, request, jsonify
import cv2
import numpy as np
from sklearn.cluster import KMeans
from models import Dress
import base64
import os

# Make sure you have the haarcascade file in your project
CASCADE_PATH = "haarcascade_frontalface_default.xml"
if not os.path.exists(CASCADE_PATH):
    raise FileNotFoundError("haarcascade_frontalface_default.xml not found in project root!")

scannerBp = Blueprint("scannerBp", __name__)

def extract_skin_palette(image_bytes, n_colors=3):
    # Decode image bytes
    npimg = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Detect face
    gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
    face_cascade = cv2.CascadeClassifier(CASCADE_PATH)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(60,60))

    if len(faces) == 0:
        region = img_rgb  # fallback to whole image if no face detected
    else:
        # Take largest face
        x, y, w, h = sorted(faces, key=lambda f: f[2]*f[3], reverse=True)[0]
        # Add small padding around face
        pad_w, pad_h = int(0.2*w), int(0.2*h)
        x1 = max(0, x - pad_w)
        y1 = max(0, y - pad_h)
        x2 = min(img_rgb.shape[1], x + w + pad_w)
        y2 = min(img_rgb.shape[0], y + h + pad_h)
        region = img_rgb[y1:y2, x1:x2]

    # Flatten pixels
    pixels = region.reshape(-1,3)

    # Sample if too large
    if len(pixels) > 5000:
        idx = np.random.choice(len(pixels), 5000, replace=False)
        pixels = pixels[idx]

    # KMeans
    kmeans = KMeans(n_clusters=n_colors, n_init=10)
    kmeans.fit(pixels)
    colors = kmeans.cluster_centers_.astype(int)

    hex_colors = ['#{:02x}{:02x}{:02x}'.format(c[0], c[1], c[2]) for c in colors]
    return hex_colors

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2],16) for i in (0,2,4))

def color_distance(c1, c2):
    return np.sqrt(sum((a-b)**2 for a,b in zip(c1,c2)))

def filter_dresses_by_palette(palette_hex, dresses, threshold=80):
    palette_rgb = [hex_to_rgb(c) for c in palette_hex]
    recommended = []
    for dress in dresses:
        if not dress.dominantColor:
            continue
        dress_rgb = hex_to_rgb(dress.dominantColor)
        distances = [color_distance(dress_rgb, skin_rgb) for skin_rgb in palette_rgb]
        if min(distances) < threshold:
            recommended.append(dress)
    return recommended

# ---------------- Routes ---------------- #

@scannerBp.post('/analyzeSkin')
def analyze_skin():
    try:
        file = request.files.get('image')
        if not file:
            return jsonify({"status": "error", "message": "Image required"}), 400

        image_bytes = file.read()
        palette = extract_skin_palette(image_bytes, n_colors=3)

        return jsonify({"status": "success", "palette": palette})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@scannerBp.post('/recommendDress')
def recommend_dress():
    try:
        data = request.get_json()
        palette = data.get("palette", [])
        if not palette:
            return jsonify({"status": "error", "message": "Palette required"}), 400

        dresses = Dress.objects()
        recommended = filter_dresses_by_palette(palette, dresses, threshold=80)

        dress_data = [{
            "id": d.id,
            "title": d.title,
            "description": d.description,
            "image": d.image,
            "category": d.category.title,
            "isSelected": d.isSelected,
        } for d in recommended[:10]]

        return jsonify({"status": "success", "recommended": dress_data})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
