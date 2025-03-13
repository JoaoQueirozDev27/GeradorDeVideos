from openai import OpenAI
from Config import *
import requests
from google import genai

client = genai.Client(api_key="AIzaSyDXDLBkiYKkm2gLUEZJa7cviox3ysAN46E")

def SendPrompt(prompt):
    print("Entrou no 'Send prompt'")
    print("Gerou o Cliente")
    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=prompt
    )
    print("Gerou a response")
    return response.text


def CreateRoadMap(text):
    print("entrou na funcao")
    response = SendPrompt(f"crie o roteiro com {QtRows_Images} linhas(Sem identificacoes de linha) de um vídeo curto para plataformas como tiktok e shorts,sendo a primeira frase um titulo curto e a segunda a frase impactante para comecar o video baseado no texto:{text}")
    return response

def GetKeyWords(text):
    return SendPrompt(f"Siga o modelo $palavraChave1,palavraChave2$ em cada sentença de forma objetiva e direta: {text}")
