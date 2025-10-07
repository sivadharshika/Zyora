from flask import Flask, render_template, request, jsonify
from models import User
from app import app

@app.post('/new')
def newUser():

    try:

        data = request.get_json()

        name = data.get("name")
        email = data.get("email")
        phone = data.get("phone")
        password = data.get("password")
        gender = data.get("gender")

        if not name or not email or not password or not gender:
            return jsonify({"status": "error", "message": "All fields are required."})
        
        User(
            name = name,
            email = email,
            phone = phone,
            password = password,
            gender = gender
        ).save()

       

        return jsonify({"status": "success", "message": "User added successfully."})
    
    except Exception as e:
        return jsonify({"status": "error", "message": f"Error {str(e)}"})


@app.get("/getAll")
def getAllUser():
    try:

        users = User.objects()

        userList = []

        for user in users:
            data = {
                "id": user.id,
                "name": user.name,
                "email": user.email,
                "phone": user.phone,
                "gender": user.gender,
            }

            userList.append(data)
        

        return jsonify({"status": "success", "message": "User retrieved successfully.", "data": userList})
    except Exception as e:
        return jsonify({"status": "error", "message": f"Error {str(e)}"})