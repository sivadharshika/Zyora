from flask import Flask, render_template, request, jsonify, session
from models import *
from mongoengine import connect, connection

app=Flask(__name__)
app.config["SECRET_KEY"] = "a13inaso73920n730"

try:
    connect(host="mongodb://localhost:27017/Zyora")
    if connection.get_connection():
        print({"status": "success", "message": "Database connected successfully."})
    else:
        print({"status": "error", "message": "Database not connected."})
except Exception as e:
    print({"status": "error", "message": f"Error {str(e)}"})

from dress import dressBp
app.register_blueprint(dressBp, url_prefix="/dress")

from ornaments import ornamentBp
app.register_blueprint(ornamentBp, url_prefix="/ornament")

from hairstyle import hairStyleBp
app.register_blueprint(hairStyleBp, url_prefix="/hairStyle")

from nailart import nailArtBp
app.register_blueprint(nailArtBp, url_prefix="/nailArt")

from user import userBp
app.register_blueprint(userBp, url_prefix="/user")

from auth import authBp
app.register_blueprint(authBp, url_prefix="/auth")

from category import categoryBp
app.register_blueprint(categoryBp, url_prefix="/category")

from scanner import scannerBp
app.register_blueprint(scannerBp, url_prefix="/scanner")



@app.get('/')
def main():
    return render_template("dress.html")

@app.get('/<page>')
def loadPages(page):
    return render_template(f"{page}.html")

@app.get('/admin/<page>')
def loadAdminPages(page):
    return render_template(f"/admin/{page}.html")

@app.get("/select")
def select():
    try:
        id = request.args.get("id")
        category = request.args.get("category")

        if not id:
            return jsonify({"status": "error", "message" : "Id is required"})
        if not category:
            return jsonify({"status": "error", "message" : "Category is required"})
        

        sessionUser = session.get("user")
        if not sessionUser:
            return jsonify({"status": "error", "message" : "User not logged in. Please login to continue"})
        
        userId = sessionUser.get('id')
        user = User.objects(id=userId).first()

        selectedItems = SelectedItems.objects(user=user).first()
        if not selectedItems:
            return jsonify({"status": "error", "message" : "Selected Items not found"})

        dress = selectedItems.dress if selectedItems.dress else None
        ornament = selectedItems.ornaments if selectedItems.ornaments else None
        nailArt = selectedItems.nailart if selectedItems.nailart else None
        hairStyle = selectedItems.hairstyle if selectedItems.hairstyle else None
        url = None

        if category == "dress":
            dress = Dress.objects(id=id).first()
            if not dress:
                return jsonify({"status": "error", "message" : "Dress not found"})
            
            Dress.objects(isSelected=True).update(isSelected=False)
            
            dress.isSelected = True
            dress.updatedTime = datetime.now()
            dress.save()

            url = "dress.html"
        elif category == "ornament":
            ornament = Ornaments.objects(id=id).first()
            if not ornament:
                return jsonify({"status": "error", "message" : "Ornament not found"})
            
            Ornaments.objects(isSelected=True).update(isSelected=False)
            
            ornament.isSelected = True
            ornament.updatedTime = datetime.now()
            ornament.save()

            url = "ornaments.html"
        elif category == "nailArt":
            nailArt = NailArt.objects(id=id).first()
            if not nailArt:
                return jsonify({"status": "error", "message" : "Nail Art not found"})
            
            NailArt.objects(isSelected=True).update(isSelected=False)

            nailArt.isSelected = True
            nailArt.updatedTime = datetime.now()
            nailArt.save()

            url = "nailArt.html"
        elif category == "hairStyle":
            hairStyle = HairStyle.objects(id=id).first()
            if not hairStyle:
                return jsonify({"status": "error", "message" : "Hair Style not found"})
            
            HairStyle.objects(isSelected=True).update(isSelected=False)

            hairStyle.isSelected = True
            hairStyle.updatedTime = datetime.now()
            hairStyle.save()

            url = "hairstyle.html"
    
        
        selectedItems.dress = dress
        selectedItems.ornaments = ornament
        selectedItems.nailart = nailArt
        selectedItems.hairstyle = hairStyle
        selectedItems.updatedTime = datetime.now()
        selectedItems.save()


        return render_template(url)
    except Exception as e:
        return jsonify({"status": "error", "message": f"Error {str(e)}"})
    

@app.get("/select/getAll")
def getAllNailart():
    try:

        sessionUser = session.get("user")
        if not sessionUser:
            return jsonify({"status": "error", "message" : "User not logged in. Please login to continue"})
        
        userId = sessionUser.get('id')
        user = User.objects(id=userId).first()

        selectedItems = SelectedItems.objects(user=user).first()
        if not selectedItems:
            return jsonify({"status": "error", "message" : "Selected Items not found"})

        dress = selectedItems.dress if selectedItems.dress else None
        ornament = selectedItems.ornaments if selectedItems.ornaments else None
        nailArt = selectedItems.nailart if selectedItems.nailart else None
        hairStyle = selectedItems.hairstyle if selectedItems.hairstyle else None
        
        selectedItemsList = []

        if dress:
            dress = Dress.objects(id=dress.id).first()
            if not dress:
                return jsonify({"status": "error", "message" : "Dress not found"})
            
            data={
                "id":dress.id,
                "image": dress.image,
                "title": dress.title,
                "description": dress.description,
                "category":dress.category.title,
                "isSaved": dress.isSaved,
                "shareLink":dress.shareLink,
                "availableOn":dress.availableOn,
                "addedTime": dress.addedTime,
                "updatedTime": dress.updatedTime,
                "isSelected": dress.isSelected
            }
            selectedItemsList.append(data)
            
            
        if ornament:
            ornament = Ornaments.objects(id=ornament.id).first()
            if not ornament:
                return jsonify({"status": "error", "message" : "Dress not found"})
            
            data={
                "id":ornament.id,
                "image": ornament.image,
                "title": ornament.title,
                "description": ornament.description,
                "category":ornament.category.title,
                "isSaved": ornament.isSaved,
                "shareLink":ornament.shareLink,
                "availableOn":ornament.availableOn,
                "addedTime": ornament.addedTime,
                "updatedTime": ornament.updatedTime,
                "isSelected": ornament.isSelected
            }
            selectedItemsList.append(data)
        
        if hairStyle:
            hairStyle = HairStyle.objects(id=hairStyle.id).first()
            if not hairStyle:
                return jsonify({"status": "error", "message" : "hairStyle not found"})
            
            data={
                "id":hairStyle.id,
                "image": hairStyle.image,
                "title": hairStyle.title,
                "description": hairStyle.description,
                "category":hairStyle.category.title,
                "isSaved": hairStyle.isSaved,
                "shareLink":hairStyle.shareLink,
                "addedTime": hairStyle.addedTime,
                "updatedTime": hairStyle.updatedTime,
                "isSelected": hairStyle.isSelected
            }

            selectedItemsList.append(data)

        if nailArt:
            nailArt = NailArt.objects(id=nailArt.id).first()
            if not nailArt:
                return jsonify({"status": "error", "message" : "nailArt not found"})
            
            data={
                "id":nailArt.id,
                "image": nailArt.image,
                "title": nailArt.title,
                "description": nailArt.description,
                "category":nailArt.category.title,
                "isSaved": nailArt.isSaved,
                "shareLink":nailArt.shareLink,
                "availableOn":nailArt.availableOn,
                "addedTime": nailArt.addedTime,
                "updatedTime": nailArt.updatedTime,
                "isSelected": nailArt.isSelected
            }
            selectedItemsList.append(data)
            
        total = SelectedItems.objects().count()
        return jsonify({
            "draw" : int(request.args.get ("draw", 1)),
            "recordsTotal" : total,
            "recordsFiltered" :total,
            "status":"success", 
            "message":"Selected Items retrived successfully.",
            "data": selectedItemsList })
    except Exception as e:
        return jsonify({"status":"error", "message": f"Error{str(e)}"})

if __name__=="__main__":
    app.run(debug=True)
