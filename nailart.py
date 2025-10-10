from flask import Flask, render_template,request,jsonify
from models import NailArt
from app import app
from datetime import datetime


@app.post('/new')
def newNailArt():
    try:
        data=request.get_json()

        category =data.get("category")
        title=data.get("title")
        image=data.get("image")
        isSaved=data.get("isSaved")
        availableOn=data.get("availableOn")
        if not category or not title or not availableOn or not image or not isSaved:
            return jsonify({"status": "error", "message" : "All feild are requred"})
        
        NailArt(
            category=category,
            title=title,
            availableOn=availableOn,
            image=image,

        ).save()
        return jsonify({"status": "success","message":"User added successgully"})
    except Exception as e:
        return jsonify({"status":"error","message":f"Error{ str(e)}"})
    
    
@app.get("/getAll")
def getAllNailart():
    try:
        nailArts = NailArt.objects()
        nailArtlist =[]

        for nailart in nailArts:
            data={
                "id":nailart.id,
                "image": nailart.image,
                "category":nailart.category,
                "isSaved": nailart.isSaved,
                "shareLink":nailart.shareLink,
                "availableOn":nailart.availableOns,
            }

            nailArtlist.append(data)

            return jsonify({"status":"success", "message":"NailArt retrived successfully.","data": nailArtlist })
    except Exception as e:
        return jsonify({"status":"error", "message": f"Error{str(e)}"})
    
    
@app.put('/update')
def updateNailArt():
    try:
        id=request.args.get("id")
        data=request.get_json()
        category =data.get("category")
        title=data.get("title")
        image=data.get("image")
        isSaved=data.get("isSaved")
        availableOn=data.get("availableOn")
        if not category or not title or not availableOn or not image:
            return jsonify({"status": "error", "message" : "All feild are requred"})
        
        nailArt=NailArt.object(id=id).first()
        if not nailArt:
            return jsonify({"status": "error", "message" : "nailart not found "})
    
        nailArt.category=category,
        nailArt.title=title, 
        nailArt.image=image,
        nailArt.isSaved=isSaved,
        nailArt.availableOn=availableOn,
        nailArt.updatetime=datetime.now()

        nailArt.save()
        return jsonify({"status":"success","message":"Nailart updated successfully"})
    
    except Exception as e:
        return jsonify({"status":"error","message":f"Error{ str(e)}"})
    

@app.delete('/delete')
def deleteNailArt():
    
    try:
        id=request.args.get("id")
        nailArt=NailArt.object(id=id).first()
        if not nailArt:
            return jsonify({"status": "error", "message" : "nailart not found "})



        NailArt.delete()
        return jsonify ({"status":"success","message":"Nailart Deleted Successfully"})
    except Exception as e:
        return jsonify({"status":"error","message":f"Error{ str(e)}"})
    


@app.get("/getspecific")
def getspecificNailart ():
    try:
        id=request.args.get("id")
        nailArt=NailArt.object(id=id).first()
        if not nailArt:
            return jsonify({"status": "error", "message" : "nailart not found "})
        
        data={
            "id":nailArt.id,
            "image": nailArt.image,
            "category":nailArt.category,
            "isSaved": nailArt.isSaved,
            "shareLink":nailArt.shareLink,
            "availableOn":nailArt.availableOns,
        }


        return jsonify({"status":"success", "message":"NailArt retrived successfully.","data": data })
    except Exception as e:
        return jsonify({"status":"error", "message": f"Error{str(e)}"})
    
    






    









    

