import requests

def CriarVideo(conteudo,images):
    print(images)
    url = "https://api.creatomate.com/v1/renders"
    api_key = "c1811026273842ffb37cdc46405ee10a0ffd91acfe44eb82e5cd2196d4f332e2807d1b3023126b8d8cf243c4e16bf351"

    data = {
      "template_id": "62802c44-5984-4bfd-8922-1544397b36c3",
      "modifications": {
        "Image-1.source": images[0][1],
        "Voiceover-1.source": conteudo[0],
        "Image-2.source": images[2][1],
        "Voiceover-2.source": conteudo[1],
        "Image-3.source": images[2][1],
        "Voiceover-3.source": conteudo[2],
        "Image-4.source": images[3][1],
        "Voiceover-4.source": conteudo[3]
      }
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    response = requests.post(url, json=data, headers=headers)
    return response.text