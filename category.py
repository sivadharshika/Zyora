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
        if not title or not category:
            return jsonify({"status" : "error","message" : "Required all the fields."})
        
        Category(
            title=title,
            description=description,
            category=category,
            addedTime=datetime.now()
        ).save()
        return jsonify({"status" :"success","message" : "Category added successfully"})
    except Exception as e:
        return jsonify({"status":"error","message":f"Error{str(e)}"})
    
@categoryBp.get("/getAll")
def getAllcategory():
    try:
        categories=Category.objects()
        categoryList=[]

        for category in categories:
            data={
                "id":category.id,
                "title":category.title,
                "description":category.description,
                "category":category.category,
                "addedTime": category.addedTime,
                "updatedTime": category.updatedTime
            }

            categoryList.append(data)
            
        total=Category.objects().count()
        return jsonify({
            "draw": int(request.args.get("draw",1)),
            "recordsTotal":total,
            "recordsFiltered":total,
            "status":"success",
            "message":"category retrived successfully",
            "data": categoryList
        })
        
    except Exception as e:
        return jsonify({"status":"error","message":f"Error{str(e)}"}) 
    



@categoryBp.put('/update')
def updatecategory():
    try:
        id=request.args.get("id")

        if not id:
            return jsonify({"status":"error","message": "Category Id required"})
        
        category=Category.objects(id=id).first()
        if not category:
            return jsonify({"status": "error", "message" : "Nailart not found "})
        
        data=request.form

        title=data.get("title")
        categoryType=data.get("category")
        description=data.get("description")
        
        if not title or not categoryType:
            return jsonify({"status" :"error","message" :" All fields are required"})
        
        category.title=title
        category.description=description
        category.category=categoryType
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
        category=Category.objects(id=id).first()
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
    

@categoryBp.get("/getAllNames")
def getAllCategoryNames():
    try:
        category = request.args.get("category")
        if not category:
            jsonify({"status":"error","message":"Category not found"})

        categories= Category.objects(category=category)
        categoryList=[]

        for category in categories:
            data={
                "id":category.id,
                "title":category.title,
            }

            categoryList.append(data)

        return jsonify({"status":"success","message":"Category retrived successfully","data": categoryList})
        
    except Exception as e:
        return jsonify({"status":"error","message":f"Error{str(e)}"}) 