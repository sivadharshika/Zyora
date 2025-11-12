from flask import request, jsonify, Blueprint
from models import Ornaments , Category
from datetime import datetime 
import base64


ornamentBp = Blueprint("ornamentBp", __name__)

@ornamentBp.post('/new')
def newOrnaments():

    try:
        data= request.form

        image_file =request.files.get("image")
        title = data.get("title")
        description = data.get("description")
        category = data.get("category")
        

        if not image_file or not title or not category:
            return jsonify({"status":"error", "message":"Required all the fields"})
        
        image_data = image_file.read()
        image_b64 = base64.b64encode(image_data).decode('utf-8')
        
        category  = Category.objects(id=category).first()
        if not category:
            return jsonify({"status": "error", "message" : "Category not found "})

        Ornaments(
            image = image_b64,
            title = title,
            description = description,
            category = category,
            addedTime = datetime.now()
        ).save()

        return jsonify({"status": "success" , "message": "Ornament added successfully"})
    except Exception as e:
        return jsonify({"status" : "error" , "message":f"Error{str(e)}"})
    
@ornamentBp.get("/getAll")
def getAllOrnaments():
    try:

        ornaments = Ornaments.objects()

        ornamentList = []

        for ornament in ornaments:
            data = {
                "id": ornament.id,
                "image": ornament.image,
                "title": ornament.title,
                "description": ornament.description,
                "category": ornament.category.title,
                "shareLink":ornament.shareLink,
                "availableOn":ornament.availableOn,
                "isSaved":ornament.isSaved,
                "addedTime": ornament.addedTime,
                "updatedTime": ornament.updatedTime,
                "isSelected": ornament.isSelected
            }

            ornamentList.append(data)
        
        total = Ornaments.objects().count()
        return jsonify({
            "draw": int(request.args.get("draw", 1)),
            "recordsTotal": total,
            "recordsFiltered": total,
            "status": "success", 
            "message": "Ornaments retrieved successfully.", 
            "data": ornamentList
        })
    except Exception as e:
        return jsonify({"status": "error", "message": f"Error {str(e)}"})
    
@ornamentBp.put('/update')
def updateOrnaments():

    try:
        id = request.args.get("id")

        if not id:
            return jsonify({"status": "error", "message" : "Ornament Id is required"})

        data= request.form

        image_file = request.files.get("image")
        title = data.get("title")
        description = data.get("description")
        category = data.get("category")
        

        if not category or not title:
            return jsonify({"status":"error", "message":"Required all the messages"})
        
        image_data = image_file.read()
        image_b64 = base64.b64encode(image_data).decode('utf-8')
        
   

        ornament = Ornaments.objects(id=id).first()
        if not ornament:
            return jsonify({"status":"error", "message":"Ornament not found"})
        
        category = Category.objects(id=category).first()
        if not category:
            return jsonify({"status": "error", "message" : "Category not found "})
        
        ornament.image=image_b64 if image_b64 else ornament.image
        ornament.title=title
        ornament.description=description
        ornament.category=category
        ornament.updatedTime = datetime.now()

        ornament.save()
        
        return jsonify({"status": "success" , "message": "Ornament updated successfully"})
    
    except Exception as e:
        return jsonify({"status" : "error" , "message":f"Error{str(e)}"})
     

@ornamentBp.delete('/delete')
def deleteOrnaments():

    try:
        id = request.args.get("id")
        
        ornament = Ornaments.objects(id=id).first()
        if not ornament:
            return jsonify({"status":"error", "message":"Ornament not found"})
            
        
        ornament.delete()
        return jsonify({"status": "success" , "message": "Ornament deleted successfully"})
    except Exception as e:
        return jsonify({"status" : "error" , "message":f"Error{str(e)}"})
    
@ornamentBp.get("/getSpecific")
def getSpecificOrnaments():
    try:

        id = request.args.get("id")

        if not id:
            return jsonify({"status": "error", "message" : "NailArt Id is required"})
        ornament = Ornaments.objects(id=id).first()
        if not ornament:
            return({"status":"error", "message":"Ornament not found"})
        
        data = {
            "id": ornament.id,
            "image": ornament.image,
            "title": ornament.title,
            "description": ornament.description,
            "category": ornament.category.id,
            "shareLink":ornament.shareLink,
            "availableOn":ornament.availableOn,
            "isSaved":ornament.isSaved,
        }

        return jsonify({"status": "success", "message": "Ornaments retrieved successfully.", "data": data})
    except Exception as e:
        return jsonify({"status": "error", "message": f"Error {str(e)}"})
    
        