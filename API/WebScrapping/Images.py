from bs4 import BeautifulSoup as bs
import  requests
import os

def GetPage(Conteudo) :
    requisicao = requests.get(f"https://www.google.com/search?q={Conteudo}&sca_esv=73dfc33bc1dc2409&udm=2&sxsrf=AHTn8zoKcLqyeQo9LoF6SQ-kdU9684D2-Q:1740049535734&source=lnt&tbs=sur:cl&sa=X&ved=2ahUKEwjiheDTjdKLAxWlLrkGHf-2Mp0QpwV6BAgDECA&biw=1920&bih=953&dpr=1")
    site = bs(requisicao.text,"html.parser")
    requisicao.close()
    return site

def GetLinksOfImages(Conteudo) :
    site = GetPage(Conteudo)
    return [imagem.attrs.get("src") for imagem in site.find_all("img")]

def DownLoadImages(links):
    del links[0]
    i = 1
    for link in links:
        Arquivo = requests.get(link)
        with open(f"../ImagensTemporarias/NovaImagem{i}.jpg", "wb") as Imagem:
            Imagem.write(Arquivo.content)
        i += 1

def RemoveImagesFromDir(n):
    os.remove(path=f"../ImagensTemporarias/NovaImagem{n}.jpg")
    if n == 1:
        return
    RemoveImagesFromDir(n-1)
