from Models.Noticia import Noticia
from WebScrapping.Images import *

from bs4 import BeautifulSoup as Bs
import  requests

def GetPage(link) :
    requisicao = requests.get(link)
    site = Bs(requisicao.text,"html.parser")
    requisicao.close()
    return site

def GetLinksOnPage():
    site = GetPage("https://g1.globo.com/")
    Noticias = site.find_all("a",class_="feed-post-link")
    links = [Noticia.get("href") for Noticia in Noticias if Noticia.get("href")]
    return links

def Scrapping(link):
    site = GetPage(link)
    titulo = site.find("h1",class_="content-head__title")
    paragrafos = site.find_all("p",class_="content-text__container")
    texto = '\n'.join([paragrafo.text for paragrafo in paragrafos if paragrafo.text])
    novaNoticia = Noticia(titulo,texto)
    return novaNoticia

def GetNews():
   Noticias = []
   Links = GetLinksOnPage()
   for Link in Links :
       if not(Link.__contains__("/playlist")):
           Noticias.append(Scrapping(Link))
   return Noticias
