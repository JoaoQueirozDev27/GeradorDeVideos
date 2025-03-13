from flask import Flask,jsonify
from flask_cors import CORS
from WebScrapping.Globo import *
from ResumirAI import *

app = Flask(__name__)
CORS(app)
@app.route("/", methods=["GET"])
def getallnews():
    print("Chamou a API")
    Noticias = GetNews()
    print("Pegou as noticias")
    images = []
    notices = []
    for Noticia in Noticias:
        print("Entrou no loop")
        #print(Noticia.texto)
        RoadMap = CreateRoadMap(Noticia.texto)
        print("Criou o roadmap")
        KeyWords = GetKeyWords(RoadMap)
        print("Criou as keyWords")
        images.append([GetLinksOfImages(KeyWord) for KeyWord in KeyWords])
        print("Adicionou imagem")
        Notice = {
            'Title': Noticia.titulo,
            'Text' : RoadMap,
            'Images' : images
        }
        print(f"Notice preenchida com: \n {Noticia.titulo},{RoadMap},{images}")
        notices.append(Notice)
    print(notices)
    return jsonify(notices)


#@app.route("/CriarVideo/<>")
#def GetImages():
#    return main.GetImages()

app.run()