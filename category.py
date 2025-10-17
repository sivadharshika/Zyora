from flask import request, jsonify, Blueprint
from models import Category
from datetime import datetime

categoryBp = Blueprint("categoryBp", __name__)

@categoryBp.post('/new')
def newcategory():
    try:
        data=request.get_json()
        title=data.get("title")
        description=data.get("description")
        category=data.get("category")
        if  title or not description or not category:
            return jsonify({"status" : "error","message" : "required all  the messages"})
        
        Category(
            title=title,
            description=description,
            category=category,

        ).save()
        return jsonify({"status" :"success","message" : "Category added successfully"})
    except Exception as e:
        return jsonify({"status":"error","message":f"Error{str(e)}"})
    
@categoryBp.get("/getAll")
def getAllcategory():
    try:
        category=category.object()
        categoryList=[]

        for category  in category:
            data={
                "title":category.title,
                "description":category.description,
                "category":category.category,
            }

            categoryList.append(data)

            return jsonify({"status":"success","message":"category retrived successfully","data": categoryList})
        
    except Exception as e:
        return jsonify({"status":"error","message":f"Error{str(e)}"}) 
    



@categoryBp.put('/update')
def updatecategory():
    try:
        id=request.args.get("id")
        data=request.get_json()
        title=data.get("title")
        description=data.get("description")
        category=data.get("category")
        if title or not description or not category:
            return jsonify({"status" :"error","message" :"required all  the messages"})
        
        
        category=Category.object(id=id).first()
        if not category:
            return jsonify({"status":"success","message":"category not found"})
        
        category.title=title,
        category.description=description,
        category.category=category,
        category.updatedTime=datetime.now()
        category.save()
        return jsonify({"status":"success","message":"Category updated successfully"})

    except Exception as e:
        return jsonify({"status":"error","message":f"Error{str(e)}"})
    

@categoryBp.delete('/delete')
def deleteHairStyle():
    try:
       id=request.args.get("id")
       category=Category.objects(id=id).first()
       if not category:
            return jsonify({"status":"success","message":"category not found"})
    
       category.delete()
       return jsonify({"status":"success","message":"category deleted successfully"})

    except Exception as e:
        return jsonify({"status":"error","message":f"Error{str(e)}"})
    

@categoryBp.get("/getSpecific")
def getSpecificCategory():
    try:
        id=request.args.get("id")
        category=Category.object(id=id).first()
        if not category:
            return jsonify({"status":"success","message":"category not found"})
        
        data={
            "id":category.id,
            "title":category.title,
            "description":category.description,
            "category":category.category,
        }

        return jsonify({"status":"success","message":"Category retrived successfully","data": data})
        
    except Exception as e:
        return jsonify({"status":"error","message":f"Error{str(e)}"}) 