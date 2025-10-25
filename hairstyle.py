from flask import request, jsonify, Blueprint
from models import HairStyle, Category
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
        
        if not category or not title:
            return jsonify({"status": "error", "message" : "All field are required"})
        
        image_data = image_file.read()
        image_b64 = base64.b64encode(image_data).decode('utf-8')

        category = Category.objects(id=category).first()
        if not category:
            return jsonify({"status": "error", "message" : "Category not found "})
        
        HairStyle(
            image=image_b64,
            title=title,
            description=description,
            category=category,
            addedTime=datetime.now()

        ).save()
        return jsonify({"status" :"success","message" : "Hairstyle added successfully"})
    except Exception as e:
        return jsonify({"status":"error","message":f"Error{str(e)}"})
    
@hairStyleBp.get("/getAll")
def getAllHairStyle():
    try:
        hairStyles=HairStyle.objects()
        hairStylesList=[]

        for hairstyle  in hairStyles:
            data={
                "id":hairstyle.id,
                "image":hairstyle.image,
                "title":hairstyle.title,
                "description":hairstyle.description,
                "category":hairstyle.category.id,
                # "isSaved":hairstyle.isSaved,
                # "shareLink":hairstyle.shareLink,
                "addedTime": hairstyle.addedTime,
                "updatedTime": hairstyle.updatedTime,

            }

            hairStylesList.append(data)
        
        total=HairStyle.objects().count()

        return jsonify({
            "draw":int(request.args.get("draw", 1)),
            "recordsTotal":total,
            "recordsFiltered":total,
            "status":"success",
            "message":"hairStyles retrived successfully",
            "data": hairStylesList
            })
        
    except Exception as e:
        return jsonify({"status":"error","message":f"Error{str(e)}"}) 
    



@hairStyleBp.put('/update')
def updateHairStyle():
    try:
        id=request.args.get("id")

        if not id:
            return jsonify({"status": "error", "message" : "Hairstyle Id is required"})
        data=request.form
        print(data)
        image_file =request.files.get("image")
        title=data.get("title")
        description=data.get("description")
        category=data.get("category")
        # isSaved=data.get("isSaved")
        if not title or not category:
            return jsonify({"status" :"error","message" :"All feild are required"})
        
        image_data = image_file.read()
        image_b64 = base64.b64encode(image_data).decode('utf-8')
        
        
        hairStyle=HairStyle.objects(id=id).first()
        if not hairStyle:
            return jsonify({"status":"success","message":"hairstyle not found"})
        
        category = Category.objects(id=category).first()
        if not category:
            return jsonify({"status": "error", "message" : "Category not found "})

        print(title, description, category)
       
        hairStyle.title=title
        hairStyle.description=description
        hairStyle.category=category
        hairStyle.image=image_b64 if image_b64 else hairStyle.image
        hairStyle.updatedTime=datetime.now()
        hairStyle.save()
        return jsonify({"status":"success","message":"hairstyle updated successfully"})

    except Exception as e:
        return jsonify({"status":"error","message":f"Error{str(e)}"})
    

@hairStyleBp.delete('/delete')
def deleteHairStyle():
    try:
       id=request.args.get("id")
       if not id:
            return jsonify({"status": "error", "message" : "Hairstyle Id is required"})

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
        
        if not id:
            return jsonify({"status": "error", "message" : "NailArt Id is required"})
        
        hairStyle=HairStyle.objects(id=id).first()
        if not hairStyle:
            return jsonify({"status":"success","message":"hairstyle not found"})
        
        data={
            "id":hairStyle.id,
            "image":hairStyle.image,
            "title":hairStyle.title,
            "description":hairStyle.description,
            "category":hairStyle.category.id,
            # "isSaved":hairStyle.isSaved,
            # "shareLink":hairStyle.shareLink,

        }

        return jsonify({"status":"success","message":"hairStyle retrived successfully","data": data})
        
    except Exception as e:
        return jsonify({"status":"error","message":f"Error{str(e)}"}) 