from flask import Flask, render_template, request, jsonify
from models import *

app=Flask(__name__)

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