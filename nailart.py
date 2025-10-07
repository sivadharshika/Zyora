from flask import Flask, render_template,request,jsonify
app=Flask(__name__)
from models import NailArt

@app.post('/new')
def newNailArt():
    try:
        data=request.get_json()
        category =data.get("category")
        title=data.get("title")
        image=data.get("image")
        isSaved=data.get("isSaved")
        availableOn=data.get("availableOn")

        if not category or not title or not availableOn or not image:
            return jsonify({"status": "error", "message" : "All feild are requred"})
        NailArt(
            category=category,
            title=title,
            availableOn=availableOn,
            image=image,

        ).save()
        return jsonify ({"status:success","message:User added successgully"})
    except Exception as e:
        return({"status":"error","message":f"Error{ str(e)}"})
    
    
@app.get("/getAll")
def getAllnailart ():
    try:
        nailArts = NailArt.objects()
        NailArtlist =[]

        for nailart in nailArts:
            data={
                "id":nailart.id,
                "image": nailart.image,
                "category":nailart.category,
                "isSaved": nailart.isSaved,
                "shareLink":nailart.shareLink,
                "availableOn":nailart.availableOns,
            }

            NailArtlist.append(data)

            return jsonify({"status":"success", "message":"NailArt retrived successfully.","data": NailArtlist })
    except Exception as e:
        return({"status":"error", "message": f"Error{str(e)}"})





    
