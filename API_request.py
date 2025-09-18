import requests
import json

# Configurações do Canal ThingSpeak
CHANNEL_ID = ""
READ_API_KEY = ""

# URL da API
url = f"https://api.thingspeak.com/channels/{CHANNEL_ID}/feeds.json?api_key={READ_API_KEY}&results=5"

# Requisição à API
try:
    response = requests.get(url, timeout=10)

    if response.status_code == 200:
        data = response.json()
        feeds = data.get("feeds", [])

        print("\n=== Últimos dados recebidos do ThingSpeak ===")
        for feed in feeds:
            hora = feed.get("created_at", "N/A")
            temperatura = feed.get("field1", "N/A")
            umidade = feed.get("field2", "N/A")

            print(f"Hora: {hora} | Temperatura: {temperatura} °C | Umidade: {umidade} %")

    else:
        print(f"Erro na requisição: {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"Erro de conexão: {e}")