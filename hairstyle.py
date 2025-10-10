from flask import Flask, render_template, request, jsonify
from app import app
from models import HairStyle
from datetime import datetime

@app.post('/new')
def newHairStyle():
    try:
        data=request.get_json()
        image=data.get("image")
        title=data.get("title")
        description=data.get("description")
        category=data.get("category")
        if not image or not title or not description or not category:
            return jsonify({"status" : "error","message" : "required all  the messages"})
        
        HairStyle(
            image=image,
            title=title,
            description=description,
            category=category,

        ).save()
        return jsonify({"status" :"success","message" : "User added successfully"})
    except Exception as e:
        return jsonify({"status":"error","message":f"Error{str(e)}"})
    
@app.get("/getAll")
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
    



@app.put('/update')
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
    

@app.delete('/delete')
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
    

@app.get("/getSpecific")
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