from Models.Noticia import Noticia
from WebScrapping.Globo import *
from WebScrapping.Images import *
from ResumirAI import *

from bs4 import BeautifulSoup as bs
import  requests

def GetPage(link) :
    requisicao = requests.get(link)
    site = bs(requisicao.text,"html.parser")
    requisicao.close()
    return site

def GetLinksOnPage():
    site = GetPage("https://g1.globo.com/")
    Noticias = site.find_all("a",class_="feed-post-link")
    links = [Noticia.get("href") for Noticia in Noticias if Noticia.get("href")]
    return links

def Scrapping(link):
    site = GetPage(link)
    Titulo = site.find("h1",class_="content-head__title")
    paragrafos = site.find_all("p",class_="content-text__container")
    Texto = '\n'.join([paragrafo.text for paragrafo in paragrafos if paragrafo.text])
    RoadMap = CreateRoadMap(Texto)
    KeyWords = GetKeyWords(RoadMap)
    Images = [GetLinksOfImages(KeyWord) for KeyWord in KeyWords]
    NovaNoticia = Noticia(Titulo.text,Texto,Images)
    return NovaNoticia

def GetNews():
   Noticias = []
   Links = GetLinksOnPage()
   for Link in Links :
       if not(Link.__contains__("/playlist")):
           Noticias.append(Scrapping(Link))
   return Noticias
