from flask import request, jsonify, Blueprint
from models import User
from datetime import datetime

userBp = Blueprint("userBp", __name__)

@userBp.post('/new')
def newUser():

    try:

        data = request.get_json()

        name = data.get("name")
        email = data.get("email")
        phone = data.get("phone")
        password = data.get("password")
        gender = data.get("gender")

        if not name or not email or not password or not phone or not gender:
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


@userBp.get("/getAll")
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
    
@userBp.put('/update')
def updateuser():
    try:
        id=request.args.get("id")
        data=request.get_json()
        name=data.get("name")
        email=data.get("email")
        password=data.get("password")
        phone=data.get("phone")
        gender=data.get("gender")
        if not name or not email or not phone or not gender:
            return jsonify({"status" :"error","message" :"Required all the messages"})
        
        
        user=User.object(id=id).first()
        if not user:
            return jsonify({"status":"success","message":"User not found"})
        
        user.id=id,
        user.name=name,
        user.email=email,
        user.password=password,
        user.gender=gender,
        user.phone=phone,
        user.updatedTime=datetime.now()
        user.save()
        return jsonify({"status":"success","message":"User updated successfully"})

    except Exception as e:
        return jsonify({"status":"error","message":f"Error{str(e)}"})
    
        

@userBp.delete('/delete')
def deleteUser():
    try:
       id=request.args.get("id")
       user=User.objects(id=id).first()
       if not user:
            return jsonify({"status":"success","message":"User not found"})
       
       user.delete()
       return jsonify({"status":"success","message":"User deleted successfully"})

    except Exception as e:
        return jsonify({"status":"error","message":f"Error{str(e)}"})
    

@userBp.get("/getSpecific")
def getSpecificuser():
    try:
        id=request.args.get("id")
        user=User.object(id=id).first()
        if not user:
            return jsonify({"status":"success","message":"User not found"})
        
        data={
                "id": user.id,
                "name":user.name,
                "email": user.email,
                "phone": user.phone,
                "gender": user.gender,
            
        }

        return jsonify({"status":"success","message":"User retrived successfully","data": data})
        
    except Exception as e:
        return jsonify({"status":"error","message":f"Error{str(e)}"}) 