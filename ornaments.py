from flask import Flask, render_template, request, jsonify
from models import Ornaments
from app import app
from datetime import datetime 


@app.get('/')
def main():
    return render_template("ornaments.html")

@app.post('/new')
def Ornaments():

    try:
        data= request.get_json()

        image = data.get("image")
        title = data.get("title")
        description = data.get("description")
        category = data.get("category")
        availableon = data.get("availableon")

        if not image or not title or not description or not category or not availableon:
            return({"status":"error", "message":"Required all the messages"})
        
        Ornaments(
            image = image,
            title = title,
            description = description,
            category = category,
            availableon = availableon,
        ).save()

        return jsonify({"status": "success" , "message": "Ornament added successfully"})
    except Exception as e:
        return({"status" : "error" , "message":f"Error{str(e)}"})
    
@app.get("/getAll")
def getAllOrnaments():
    try:

        ornament = Ornaments.objects()

        ornamentList = []

        for Ornament in Ornaments:
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
    
@app.post('/update')
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
            return({"status":"error", "message":"Required all the messages"})
        
   

        ornament = Ornaments.object(id=id).first()
        if not ornament:
            return({"status":"error", "message":"Ornament not found"})
        ornament.image=image
        ornament.title=title
        ornament.description=description
        ornament.category=category
        ornament.availabeOn=availableon

        ornament.updatedtime = datetime.now()
        
        return jsonify({"status": "success" , "message": "Ornament added successfully"})
    except Exception as e:
        return({"status" : "error" , "message":f"Error{str(e)}"})
    