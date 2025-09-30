from flask import Flask, render_template, request, jsonify
app=Flask(__name__)

@app.get('/')
def main():
    return render_template("dress.html")

if __name__=="__main__":
    app.run(debug=True)
