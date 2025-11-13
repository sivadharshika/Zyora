from flask import request, jsonify, Blueprint
from models import Dress, Category
from datetime import datetime
import base64
import cv2
import numpy as np
from sklearn.cluster import KMeans
from scanner import filter_dresses_by_palette

def get_dominant_color_from_bytes(image_bytes, n_colors=3):
    npimg = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)
    if img is None:
        return "#FFFFFF"

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = img.reshape((-1, 3))

    if len(img) > 5000:
        idx = np.random.choice(len(img), 5000, replace=False)
        img = img[idx]

    kmeans = KMeans(n_clusters=n_colors, n_init=10)
    kmeans.fit(img)
    counts = np.bincount(kmeans.labels_)
    dominant = kmeans.cluster_centers_[np.argmax(counts)].astype(int)
    hex_color = '#%02x%02x%02x' % tuple(dominant)
    return hex_color



dressBp = Blueprint("dressBp", __name__)

@dressBp.post('/new')
def newDress():
    try:
        data = request.form
        image_file = request.files.get("image")
        title = data.get("title")
        description = data.get("description")
        category_id = data.get("category")

        if not image_file or not title or not category_id:
            return jsonify({"status":"error", "message":"Required all the fields"}), 400

        image_bytes = image_file.read()
        image_b64 = base64.b64encode(image_bytes).decode('utf-8')

        category = Category.objects(id=category_id).first()
        if not category:
            return jsonify({"status": "error", "message" : "Category not found"}), 400

        dominant_color = get_dominant_color_from_bytes(image_bytes)

        Dress(
            image=image_b64,
            title=title,
            description=description,
            category=category,
            addedTime=datetime.now(),
            dominantColor=dominant_color
        ).save()

        return jsonify({"status": "success", "message": "Dress added successfully."})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@dressBp.put('/update')
def updateDress():
    try:
        dress_id = request.args.get("id")
        if not dress_id:
            return jsonify({"status": "error", "message":"Dress Id is required"}), 400

        data = request.form
        image_file = request.files.get("image")
        title = data.get("title")
        description = data.get("description")
        category_id = data.get("category")

        if not title or not category_id:
            return jsonify({"status":"error", "message":"Required all the fields"}), 400

        dress = Dress.objects(id=dress_id).first()
        if not dress:
            return jsonify({"status":"error", "message":"Dress not found"}), 404

        category = Category.objects(id=category_id).first()
        if not category:
            return jsonify({"status":"error", "message":"Category not found"}), 400

        dress.title = title
        dress.description = description
        dress.category = category
        dress.updatedTime = datetime.now()

        if image_file:
            image_bytes = image_file.read()
            dress.image = base64.b64encode(image_bytes).decode('utf-8')
            dress.dominantColor = get_dominant_color_from_bytes(image_bytes)

        dress.save()

        return jsonify({"status":"success", "message":"Dress updated successfully."})
    except Exception as e:
        return jsonify({"status":"error", "message": str(e)}), 500
    
@dressBp.get("/getAll")
def getAllDress():
    try:
        dresses = Dress.objects()
        dressList = []

        # Optional palette from query param (comma-separated hex values)
        palette_hex = request.args.get("palette")
        recommended_dress_ids = set()
        if palette_hex:
            palette = palette_hex.split(",")
            recommended_dress_ids = set(d.id for d in filter_dresses_by_palette(palette, dresses, threshold=80))

        for dress in dresses:
            data = {
                "id": dress.id,
                "image": dress.image,
                "title": dress.title,
                "description": dress.description,
                "category": dress.category.title,
                "isSaved": dress.isSaved,
                "shareLink": dress.shareLink,
                "availableOn": dress.availableOn,
                "addedTime": dress.addedTime,
                "updatedTime": dress.updatedTime,
                "isSelected": dress.isSelected,
                "recommended": dress.id in recommended_dress_ids
            }
            dressList.append(data)

        total = len(dressList)
        return jsonify({
            "draw": int(request.args.get("draw", 1)),
            "recordsTotal": total,
            "recordsFiltered": total,
            "status": "success",
            "message": "Dress retrieved successfully.",
            "data": dressList
        })
    except Exception as e:
        return jsonify({"status": "error", "message": f"Error {str(e)}"})


# @dressBp.put('/update')
# def updateDress():

#     try:
#         id=request.args.get("id")

#         if not id:
#             return jsonify({"status": "error", "message" : "Dress Id is required"})

#         data=request.form

#         image_file = request.files.get("image")
#         title = data.get("title")
#         description = data.get("description")
#         category = data.get("category")

#         if not title or not category:
#             return jsonify({"status":"error", "message":"Required all the messages"})
        
#         image_data = image_file.read()
#         image_b64 = base64.b64encode(image_data).decode('utf-8')

#         dress = Dress.objects(id=id).first()
#         if not dress:
#             return jsonify({"status":"error", "message":"Dress not found"})
        
#         category = Category.objects(id=category).first()
#         if not category:
#             return jsonify({"status": "error", "message" : "Category not found "})

#         dress.title = title
#         dress.image=image_b64 if image_b64 else dress.image
#         dress.description = description
#         dress.category = category
#         dress.updatedTime = datetime.now()
        
#         dress.save()

        

#         return jsonify({"status": "success", "message": "Dress updated successfully."})
#     except Exception as e:
#         return jsonify({"status": "error", "message": f"Error{str(e)}"})
    
@dressBp.delete('/delete')
def deleteDress():

    try:
        
        id=request.args.get("id")
        dress = Dress.objects(id=id).first()
        if not dress:
            return jsonify({"status":"error", "message":"Dresses not found"})
        
        dress.delete()
        return jsonify({"status": "success", "message": "Dress deleted successfully."})
    except Exception as e:
        return jsonify({"status": "error", "message": f"Error{str(e)}"})
    
@dressBp.get("/getSpecific")
def getSpecificDress():

    try:

        id=request.args.get("id")

        if not id:
            return jsonify({"status": "error", "message" : "Dress Id is required"})

        dress = Dress.objects(id=id).first()
        if not dress:
            return jsonify({"status":"error", "message":"Dress not found"})
        
        data = {
            "id": dress.id,
            "image": dress.image,
            "title": dress.title,
            "description": dress.description,
            "category": dress.category.id,
            "isSaved": dress.isSaved,
            "shareLink":dress.shareLink,
        }

        return jsonify({"status": "success", "message": "Dress retrived successfully.", "data": data})
    except Exception as e:
        return jsonify({"status": "error", "message": f"Error{str(e)}"})