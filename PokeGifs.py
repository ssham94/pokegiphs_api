import json
import requests
import os

# Pokemon API
res = requests.get("http://pokeapi.co/api/v2/pokemon/pikachu/")
body = json.loads(res.content)
print(body["name"]) # should be "pikachu"
print('')

# Giphy API
key = os.environ.get('GIPHY_KEY')
url = (f"https://api.giphy.com/v1/gifs/search?api_key={key}&q=pikachu&rating=g")
giphy_res = requests.get(url)
body = json.loads(giphy_res.content)
giph_url = body['data'][0]['url']
print(giph_url)