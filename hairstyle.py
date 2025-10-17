from flask import request, jsonify, Blueprint
from models import HairStyle
from datetime import datetime
import base64

hairStyleBp = Blueprint("hairStyleBp", __name__)

@hairStyleBp.post('/new')
def newHairStyle():
    try:
        data=request.form
       
        title=data.get("title")
        description=data.get("description")
        category=data.get("category")
        image_file=request.files.get("image")
        
        if not category or not title  or not description or not image_file:
            return jsonify({"status": "error", "message" : "All field are required"})
        
        image_data = image_file.read()
        image_b64 = base64.b64encode(image_data).decode('utf-8')
        
            
        
        HairStyle(
            image=image_b64,
            title=title,
            description=description,
            category=category,

        ).save()
        return jsonify({"status" :"success","message" : "User added successfully"})
    except Exception as e:
        return jsonify({"status":"error","message":f"Error{str(e)}"})
    
@hairStyleBp.get("/getAll")
def getAllHairStyle():
    try:
        hairStyles=HairStyle.object()
        hairStylesList=[]

        for hairstyle  in hairStyles:
            data={
                "id":hairstyle.id,
                "image":hairstyle.image,
                "title":hairstyle.title,
                "description":hairstyle.description,
                "category":hairstyle.category,
                "isSaved":hairstyle.isSaved,
                "shareLink":hairstyle.shareLink,

            }

            hairStylesList.append(data)

            return jsonify({"status":"success","message":"hairStyles retrived successfully","data": hairStylesList})
        
    except Exception as e:
        return jsonify({"status":"error","message":f"Error{str(e)}"}) 
    



@hairStyleBp.put('/update')
def updateHairStyle():
    try:
        id=request.args.get("id")
        data=request.get_json()
        image=data.get("image")
        title=data.get("title")
        description=data.get("description")
        category=data.get("category")
        if not image or not title or not description or not category:
            return jsonify({"status" :"error","message" :"required all  the messages"})
        
        
        hairStyle=HairStyle.object(id=id).first()
        if not hairStyle:
            return jsonify({"status":"success","message":"hairstyle not found"})
        
        hairStyle.image=image,
        hairStyle.title=title,
        hairStyle.description=description,
        hairStyle.category=category,
        hairStyle.updatedTime=datetime.now()
        hairStyle.save()
        return jsonify({"status":"success","message":"hairstyle updated successfully"})

    except Exception as e:
        return jsonify({"status":"error","message":f"Error{str(e)}"})
    

@hairStyleBp.delete('/delete')
def deleteHairStyle():
    try:
       id=request.args.get("id")
       hairStyle=HairStyle.objects(id=id).first()
       if not hairStyle:
            return jsonify({"status":"success","message":"hairstyle not found"})
       
       hairStyle.delete()
       return jsonify({"status":"success","message":"hairstyle deleted successfully"})

    except Exception as e:
        return jsonify({"status":"error","message":f"Error{str(e)}"})
    

@hairStyleBp.get("/getSpecific")
def getSpecificHairStyle():
    try:
        id=request.args.get("id")
        hairStyle=HairStyle.object(id=id).first()
        if not hairStyle:
            return jsonify({"status":"success","message":"hairstyle not found"})
        
        data={
            "id":hairStyle.id,
            "image":hairStyle.image,
            "title":hairStyle.title,
            "description":hairStyle.description,
            "category":hairStyle.category,
            "isSaved":hairStyle.isSaved,
            "shareLink":hairStyle.shareLink,

        }

        return jsonify({"status":"success","message":"hairStyle retrived successfully","data": data})
        
    except Exception as e:
        return jsonify({"status":"error","message":f"Error{str(e)}"}) 