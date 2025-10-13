from flask import request, jsonify, Blueprint, session
from models import User
from datetime import datetime

authBp = Blueprint("authBp", __name__)

@authBp.post('/register')
def register():

    try:

        data = request.get_json()

        name = data.get("name")
        email = data.get("email")
        phone = data.get("phone")
        password = data.get("password")

        if not name or not email or not password:
            return jsonify({"status": "error", "message": "All fields are required."})
        
        user = User(
            name = name,
            email = email,
            phone = phone,
            password = password,
        )
        
        user.save()


        session["user"] = {
            "id": user.id,
            "name": user.name,
            "email": user.email
        }
       

        return jsonify({"status": "success", "message": "User registered successfully."})
    
    except Exception as e:
        return jsonify({"status": "error", "message": f"Error {str(e)}"})
    

@authBp.post('/login')
def login():

    try:

        data = request.get_json()

        email = data.get("email")
        password = data.get("password")

        if not email or not password:
            return jsonify({"status": "error", "message": "All fields are required."})
        
        user = User.objects(email = email).first()

        if not user:
            return jsonify({"status": "error", "message": "User not Found."})
        
        session["user"] = {
            "id": user.id,
            "name": user.name,
            "email": user.email
        }

        return jsonify({"status": "success", "message": "User login successfully."})
    
    except Exception as e:
        return jsonify({"status": "error", "message": f"Error {str(e)}"})
    
@authBp.post('/logout')
def logout():
    user = session.get("user")
    if not user:
        return jsonify({"status": "error", "message": "User not in session."})
    session.clear()
    return jsonify({"status": "success", "message": "User logout successfully."})
