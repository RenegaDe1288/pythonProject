import requests
import json

req = requests.get('https://breakingbadapi.com/api/deaths')
data = json.loads(req.text)


max_death = 0
for i in data:
    if max_death < i["number_of_deaths"]:
        episode, max_death = i['episode'], i["number_of_deaths"]

with open('breaking_bad.json', 'w', encoding='Utf-8') as file:
    file.write('Эпизод: {}  смертей: {}'.format(episode, max_death))

print('Эпизод: {}  смертей: {}'.format(episode, max_death))
