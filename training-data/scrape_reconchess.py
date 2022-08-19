import requests
import os 

url = 'https://rbc.jhuapl.edu/api/games/429828/game_history/download'
r = requests.get(url, allow_redirects=True)

filename = 'json-files/download.json'
os.makedirs(os.path.dirname(filename), exist_ok=True)
with open(filename, 'wb') as f:
    f.write(r.content)