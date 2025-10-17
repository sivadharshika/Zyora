from flask import request, jsonify, Blueprint
from models import Dress
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
        availableOn = data.get("availableOn")

        if not image_file or not title or not description or not category or not availableOn:
            return jsonify({"status":"error", "message":"Required all the messages"})
        
        image_data = image_file.read()
        image_b64 = base64.b64encode(image_data).decode('utf-8')

        Dress(
            image = image_b64,
            title = title,
            description = description,
            category = category,
            availableOn = availableOn,
        ).save()

        return jsonify({"status": "success", "message": "User added successfully."})
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
                "category": dress.category,
                "availableOn": dress.availableOn,
                "isSaved": dress.isSaved,
                "shareLink": dress.shareLink,
            }

            dressList.append(data)

        return jsonify({"status": "success", "message": "Dress retrived successfully.", "data": dressList})
    except Exception as e:
        return jsonify({"status": "error", "message": f"Error{str(e)}"})

@dressBp.put('/update')
def updateDress():

    try:
        id=request.args.get("id")
        data=request.get_json()

        image = data.get("image")
        title = data.get("title")
        description = data.get("description")
        category = data.get("category")
        availableOn = data.get("availableOn")
        isSaved = data.get("isSaved")

        if not image or not title or not description or not category or not availableOn:
            return jsonify({"status":"error", "message":"All field are required"})


        dress = Dress.objects(id=id).first()
        if not dress:
            return jsonify({"status":"error", "message":"Dress not found"})
        dress.image = image
        dress.title = title
        dress.description = description
        dress.category = category
        dress. availableOn = availableOn
        dress.isSaved = isSaved
        dress.updatetime = datetime.now()
        
        dress.save()

        

        return jsonify({"status": "success", "message": "Dress updated successfully."})
    except Exception as e:
        return jsonify({"status": "error", "message": f"Error{str(e)}"})
    
@dressBp.delete('/delete')
def deleteDress():

    try:
        
        id=request.args.get("id")
        dress = Dress.objects(id=id).first()
        if not dress:
            return jsonify({"status":"error", "message":"Dresses not found"})
        
        Dress.delete()
        return jsonify({"status": "success", "message": "Dress deleted successfully."})
    except Exception as e:
        return jsonify({"status": "error", "message": f"Error{str(e)}"})
    
@dressBp.get("/getSpecific")
def getSpecificDress():

    try:

        id=request.args.get("id")
        dress = Dress.objects(id=id).first()
        if not dress:
            return jsonify({"status":"error", "message":"Dress not found"})
        
        data = {
            "id": dress.id,
            "image": dress.image,
            "title": dress.title,
            "description": dress.description,
            "category": dress.category,
            "availableOn": dress.availableOn,
            "isSaved": dress. isSaved,
            "shareLink": dress. shareLink,
        }

        return jsonify({"status": "success", "message": "Dress retrived successfully.", "data": data})
    except Exception as e:
        return jsonify({"status": "error", "message": f"Error{str(e)}"})