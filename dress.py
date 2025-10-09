from flask import Flask, render_template, request, jsonify
from models import Dress
from app import app
from datetime import datetime

@app.post('/new')
def Dress():

    try:
        data=request.get_json()

        image = data.get("image")
        title = data.get("title")
        description = data.get("description")
        category = data.get("category")
        availableOn = data.get("availableOn")

        if not image or not title or not description or not category or not availableOn:
            return jsonify({"status":"error", "message":"Required all the messages"})

        Dress(
            image = image,
            title = title,
            description = description,
            category = category,
            availableOn = availableOn,
        ).save()

        return jsonify({"status": "success", "message": "User added successfully."})
    except Exception as e:
        return jsonify({"status": "error", "message": f"Error{str(e)}"})
    
@app.get("/getAll")
def getAllDress():
    try:

        dresses = Dress.objects()
        dressesList =[]

        for dress in dresses:
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

            dressesList.append(data)

        return jsonify({"status": "success", "message": "Dresses retrived successfully.", "data": dressesList})
    except Exception as e:
        return jsonify({"status": "error", "message": f"Error{str(e)}"})

@app.post('/update')
def UpdateDress():

    try:
        id=request.args.get("id")
        data=request.get_json()

        image = data.get("image")
        title = data.get("title")
        description = data.get("description")
        category = data.get("category")
        availableOn = data.get("availableOn")

        if not image or not title or not description or not category or not availableOn:
            return jsonify({"status":"error", "message":"Required all the messages"})


        dresses = Dress.objects(id=id).first()
        if not Dress:
            return jsonify({"status":"error", "message":"Dresses not found"})
        dresses.image = image
        dresses.title = title
        dresses.descriptio = description
        dresses.category = category
        dresses. availableOn = availableOn
        dresses.updatetime = datetime.now()
        
        dresses.save()

        

        return jsonify({"status": "success", "message": "Dress updated successfully."})
    except Exception as e:
        return jsonify({"status": "error", "message": f"Error{str(e)}"})
    
@app.put('/delete')
def DeleteDress():

    try:
        
        id=request.args.get("id")
        dresses = Dress.objects(id=id).first()
        if not Dress:
            return jsonify({"status":"error", "message":"Dresses not found"})
        
        dresses.delete()
        return jsonify({"status": "success", "message": "Dress deleted successfully."})
    except Exception as e:
        return jsonify({"status": "error", "message": f"Error{str(e)}"})
    
@app.get("/getSpecific")
def getSpecificDress():

    try:

        id=request.args.get("id")
        dress = Dress.objects(id=id).first()
        if not Dress:
            return jsonify({"status":"error", "message":"Dresses not found"})
        
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

        return jsonify({"status": "success", "message": "Dresses retrived successfully.", "data": data})
    except Exception as e:
        return jsonify({"status": "error", "message": f"Error{str(e)}"})


       



    

    
    



    


