from flask import Flask, render_template, request, jsonify
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



@app.get('/')
def main():
    return render_template("dress.html")

@app.get('/<page>')
def loadPages(page):
    return render_template(f"{page}.html")

@app.get('/admin/<page>')
def loadAdminPages(page):
    return render_template(f"/admin/{page}.html")

if __name__=="__main__":
    app.run(debug=True)
