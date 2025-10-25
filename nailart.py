from flask import request, jsonify, Blueprint
from models import NailArt, Category
from datetime import datetime
import base64

nailArtBp = Blueprint("nailArtBp", __name__)

@nailArtBp.post('/new')
def newNailArt():
    try:
        data=request.form

        category =data.get("category")
        title=data.get("title")
        image_file =request.files.get("image")
        description = data.get("description")

        if not category or not title  or not image_file:
            return jsonify({"status": "error", "message" : "All field are required"})
        
        image_data = image_file.read()
        image_b64 = base64.b64encode(image_data).decode('utf-8')

        category = Category.objects(id=category).first()
        if not category:
            return jsonify({"status": "error", "message" : "Category not found "})
        
        NailArt(
            category=category,
            title=title,
            image=image_b64,
            description = description
        ).save()
        return jsonify({"status": "success","message":"Nailart added successfully"})
    except Exception as e:
        return jsonify({"status":"error","message":f"Error{ str(e)}"})
    
    
@nailArtBp.get("/getAll")
def getAllNailart():
    try:
        nailArts = NailArt.objects()
        nailArtlist =[]

        for nailart in nailArts:
            data={
                "id":nailart.id,
                "image": nailart.image,
                "title": nailart.title,
                "description": nailart.description,
                # "category":nailart.category,
                "isSaved": nailart.isSaved,
                "shareLink":nailart.shareLink,
                "availableOn":nailart.availableOn,
                "addedTime": nailart.addedTime,
                "updatedTime": nailart.updatedTime,
            }

            nailArtlist.append(data)

            return jsonify({"status":"success", "message":"NailArt retrived successfully.","data": nailArtlist })
    except Exception as e:
        return jsonify({"status":"error", "message": f"Error{str(e)}"})
    
    
@nailArtBp.put('/update')
def updateNailArt():
    try:
        id=request.args.get("id")

        if not id:
            return jsonify({"status": "error", "message" : "NailArt Id is required"})

        data=request.form

        category =data.get("category")
        title=data.get("title")
        image_file =request.files.get("image")
        description = data.get("description")
        # isSaved=data.get("isSaved")
        # availableOn=data.get("availableOn")
        if not category or not title:
            return jsonify({"status": "error", "message" : "All feild are required"})
        
        image_data = image_file.read()
        image_b64 = base64.b64encode(image_data).decode('utf-8')
        
        nailArt=NailArt.objects(id=id).first()
        if not nailArt:
            return jsonify({"status": "error", "message" : "Nailart not found "})

        category = Category.objects(id=category).first()
        if not category:
            return jsonify({"status": "error", "message" : "Category not found "})

        nailArt.category=category
        nailArt.title=title
        nailArt.image=image_b64 if image_b64 else nailArt.image
        nailArt.description = description
        # nailArt.isSaved=isSaved
        # nailArt.availableOn=availableOn
        nailArt.updatedtime=datetime.now()

        nailArt.save()
        return jsonify({"status":"success","message":"Nailart updated successfully"})
    
    except Exception as e:
        return jsonify({"status":"error","message":f"Error{ str(e)}"})
    

@nailArtBp.delete('/delete')
def deleteNailArt():
    
    try:
        id=request.args.get("id")
        nailArt=NailArt.objects(id=id).first()
        if not nailArt:
            return jsonify({"status": "error", "message" : "nailart not found "})



        NailArt.delete()
        return jsonify ({"status":"success","message":"Nailart Deleted Successfully"})
    except Exception as e:
        return jsonify({"status":"error","message":f"Error{ str(e)}"})
    


@nailArtBp.get("/getSpecific")
def getspecificNailart():
    try:
        id=request.args.get("id")

        if not id:
            return jsonify({"status": "error", "message" : "NailArt Id is required"})

        nailArt=NailArt.objects(id=id).first()
        if not nailArt:
            return jsonify({"status": "error", "message" : "nailart not found "})
        
        data={
            "id":nailArt.id,
            "image": nailArt.image,
            "category":nailArt.category.id,
            # "isSaved": nailArt.isSaved,
            # "shareLink":nailArt.shareLink,
            # "availableOn":nailArt.availableOns,
            "description": nailArt.description,
            "title": nailArt.title,
        }


        return jsonify({"status":"success", "message":"NailArt retrived successfully.","data": data })
    except Exception as e:
        return jsonify({"status":"error", "message": f"Error{str(e)}"})