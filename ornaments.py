from flask import Flask, render_template, request, jsonify
from models import Ornaments
from app import app

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

        return jsonify({"status": "success" , "message": "User added successfully"})
    except Exception as e:
        return({"status" : "error" , "message":f"Error{str(e)}"})
    
@app.get("/getAll")
def getAllOrnaments():
    try:

        Ornament = Ornaments.objects()

        OrnamentList = []

        for Ornament in Ornaments:
            data = {
                "id": Ornament.id,
                "image": Ornament.image,
                "title": Ornament.title,
                "description": Ornament.description,
                "category": Ornament.category,
                "sharelink":Ornament.sharelink,
                "availableOn":Ornament.availableOn,
                "isSaved":Ornament.isSaved,
            }

            OrnamentList.append(data)
        

        return jsonify({"status": "success", "message": "Ornaments retrieved successfully.", "data": OrnamentList})
    except Exception as e:
        return jsonify({"status": "error", "message": f"Error {str(e)}"})