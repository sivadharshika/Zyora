from flask import Flask, render_template, request, jsonify
from models import Dress
from app import app


@app.get('/')
def main():
    return render_template("dress.html")

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
            return({"status":"error", "message":"Required all the messages"})

        Dress(
        image = image,
        title = title,
        description = description,
        category = category,
        availableOn = availableOn,
        ).save()

        return jsonify({"status": "success", "message": "User added successfully."})
    except Exception as e:
        return({"status": "error", "message": f"Error{str(e)}"})
    
@app.get("/getAll")
def getAllDress():
    try:

        dresses = Dress.objects()
        dressesList =[]

        for dresses in Dress:
            data = {
                "id": dresses.id,
                "image": dresses.image,
                "titl": dresses.titll,
                "description": dresses.description,
                "category": dresses.category,
                "availableOn": dresses.availableOn,
                " isSaved": dresses. isSaved,
                " shareLink": dresses. shareLink,
            }

            dressesList.append(data)

        return jsonify({"status": "success", "message": "Dresses retrived successfully.", "data": dressesList})
    except Exception as e:
        return({"status": "error", "message": f"Error{str(e)}"})
    



    


