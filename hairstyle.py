from flask import Flask, render_template, request, jsonify
app=Flask(__name__)
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
            return jsonify({"status:error","message:required all  the messages"})
        
        HairStyle(
            image=image,
            title=title,
            description=description,
            category=category,

        ).save()
        return jsonify({"status:success","message:User added successfully"})
    except Exception as e:
        return({"status":"error","message":f"Error{str(e)}"})
    
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
        return({"status":"error","message":f"Error{str(e)}"}) 
    



@app.post('/update')
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
        
        
        hairStyles=HairStyle.object(id=id).first()
        if not hairStyles:
            return jsonify({"status":"success","message":"hairstyle not found"})
        
        hairStyles.image=image,
        hairStyles.title=title,
        hairStyles.description=description,
        hairStyles.category=category,
        hairStyles.updatedTime=datetime.now()
        return jsonify({"status":"success","message":"hairstyle updated successfully"})

    except Exception as e:
        return({"status":"error","message":f"Error{str(e)}"})
    