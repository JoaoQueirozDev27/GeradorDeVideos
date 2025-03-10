from openai import OpenAI
from Config import *

def SendPrompt(prompt,text):
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key="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",
    )

    completion = client.chat.completions.create(
        model="deepseek/deepseek-chat:free",
        messages=[
            {
                "role": "user",
                "content": f"{prompt} {text}"
            }
        ]
    )
    return completion.choices[0].message.content.split("\n")

def CreateRoadMap(text):
    return SendPrompt(f"crie o roteiro com {QtRows_Images} linhas(Apenas as frases,sem descricoes) de um vídeo curto para plataformas como tiktok e shorts,sendo a primeira frase um titulo curto e a segunda a frase impactante para comecar o video baseado no texto:",text)

def GetKeyWords(text):
    return SendPrompt(f"Siga o modelo $palavraChave1,palavraChave2$ em cada sentença de forma objetiva e direta: ",text)