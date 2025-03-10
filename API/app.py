from flask import Flask,jsonify
from flask_cors import CORS
from WebScrapping.Globo import *

app = Flask(__name__)
CORS(app)
@app.route("/", methods=["GET"])
def GetNews():
    return jsonify(GetNews())


#@app.route("/CriarVideo/<>")
#def GetImages():
#    return main.GetImages()

app.run()