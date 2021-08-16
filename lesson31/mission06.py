import requests
import json

req = requests.get('https://swapi.dev/api/films/1/')
data = json.loads(req.text)
print(data["opening_crawl"])