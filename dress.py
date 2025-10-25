from flask import request, jsonify, Blueprint
from models import Dress, Category
from datetime import datetime
import base64

dressBp = Blueprint("dressBp", __name__)

@dressBp.post('/new')
def newDress():

    try:
        data=request.form

        image_file =request.files.get("image")
        title = data.get("title")
        description = data.get("description")
        category = data.get("category")

        if not image_file or not title or not category:
            return jsonify({"status":"error", "message":"Required all the fields"})
        
        image_data = image_file.read()
        image_b64 = base64.b64encode(image_data).decode('utf-8')

        category = Category.objects(id=category).first()
        if not category:
            return jsonify({"status": "error", "message" : "Category not found "})


        Dress(
            image = image_b64,
            title = title,
            description = description,
            category = category,
            addedTime=datetime.now()
        ).save()

        return jsonify({"status": "success", "message": "Dress added successfully."})
    except Exception as e:
        return jsonify({"status": "error", "message": f"Error{str(e)}"})
    
@dressBp.get("/getAll")
def getAllDress():
    try:

        dresses = Dress.objects()
        dressList =[]

        for dress in dresses:
            data = {
                "id": dress.id,
                "image": dress.image,
                "title": dress.title,
                "description": dress.description,
                "isSaved": dress.isSaved,
                "addedTime": dress.addedTime,
                "updatedTime": dress.updatedTime,
            }

            dressList.append(data)

        total = Dress.objects().count()
        return jsonify({
            "draw": int(request.args.get("draw", 1)),
            "recordsTotal": total,
            "recordsFiltered": total,
            "status": "success", 
            "message": "Dress retrived successfully.", 
            "data": dressList
            })
    except Exception as e:
        return jsonify({"status": "error", "message": f"Error{str(e)}"})

@dressBp.put('/update')
def updateDress():

    try:
        id=request.args.get("id")

        if not id:
            return jsonify({"status": "error", "message" : "Dress Id is required"})

        data=request.form

        image_file = request.files.get("image")
        title = data.get("title")
        description = data.get("description")
        category = data.get("category")

        if not title or not category:
            return jsonify({"status":"error", "message":"Required all the messages"})
        
        image_data = image_file.read()
        image_b64 = base64.b64encode(image_data).decode('utf-8')

        dress = Dress.objects(id=id).first()
        if not dress:
            return jsonify({"status":"error", "message":"Dress not found"})
        
        category = Category.objects(id=category).first()
        if not category:
            return jsonify({"status": "error", "message" : "Category not found "})

        dress.title = title
        dress.image=image_b64 if image_b64 else dress.image
        dress.description = description
        dress.category = category
        dress.updatedTime = datetime.now()
        
        dress.save()

        

        return jsonify({"status": "success", "message": "Dress updated successfully."})
    except Exception as e:
        return jsonify({"status": "error", "message": f"Error{str(e)}"})
    
@dressBp.delete('/delete')
def deleteDress():

    try:
        
        id=request.args.get("id")

        if not id:
            return jsonify({"status": "error", "message" : "Dress Id is required"})

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
        }

        return jsonify({"status": "success", "message": "Dress retrived successfully.", "data": data})
    except Exception as e:
        return jsonify({"status": "error", "message": f"Error{str(e)}"})