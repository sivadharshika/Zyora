from flask import request, jsonify, Blueprint
from models import Ornaments
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
        availableon = data.get("availableon")

        if not image_file or not title or not description or not category or not availableon:
            return jsonify({"status":"error", "message":"Required all the fields"})
        
        image_data = image_file.read()
        image_b64 = base64.b64encode(image_data).decode('utf-8')
        
        Ornaments(
            image = image_b64,
            title = title,
            description = description,
            category = category,
            availableon = availableon,
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
                "category": ornament.category,
                "sharelink":ornament.sharelink,
                "availableOn":ornament.availableOn,
                "isSaved":ornament.isSaved,
            }

            ornamentList.append(data)
        

        return jsonify({"status": "success", "message": "Ornaments retrieved successfully.", "data": ornamentList})
    except Exception as e:
        return jsonify({"status": "error", "message": f"Error {str(e)}"})
    
@ornamentBp.put('/update')
def updateOrnaments():

    try:
        id = request.args.get("id")
        data= request.get_json()

        image = data.get("image")
        title = data.get("title")
        description = data.get("description")
        category = data.get("category")
        availableon = data.get("availableon")

        if not image or not title or not description or not category or not availableon:
            return jsonify({"status":"error", "message":"Required all the messages"})
        
   

        ornament = Ornaments.objects(id=id).first()
        if not ornament:
            return jsonify({"status":"error", "message":"Ornament not found"})
        
        ornament.image=image
        ornament.title=title
        ornament.description=description
        ornament.category=category
        ornament.availabeOn=availableon
        ornament.updatedtime = datetime.now()

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
        ornament = Ornaments.objects(id=id).first()
        if not ornament:
            return({"status":"error", "message":"Ornament not found"})
        
        data = {
            "id": ornament.id,
            "image": ornament.image,
            "title": ornament.title,
            "description": ornament.description,
            "category": ornament.category,
            "sharelink":ornament.sharelink,
            "availableOn":ornament.availableOn,
            "isSaved":ornament.isSaved,
        }

        return jsonify({"status": "success", "message": "Ornaments retrieved successfully.", "data": data})
    except Exception as e:
        return jsonify({"status": "error", "message": f"Error {str(e)}"})
    
        