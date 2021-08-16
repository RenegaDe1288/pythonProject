import requests
import json

req = requests.get('https://swapi.dev/api/people/3/')
print(req.text)
data = json.loads(req.text)
print(data)
req2 = requests.get(data['homeworld'])
data2 = json.loads(req2.text)

print('\n',data2,'\n')

data['name'] = 'Vasia'

with open('swapi.json', 'w') as file:
    json.dump(data, file, indent=4)


with open('swapi.json', 'r') as file:
    print(json.load(file))
