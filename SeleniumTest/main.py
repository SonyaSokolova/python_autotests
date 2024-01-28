import requests

URL = 'https://api.pokemonbattle.me:9104'

HEADER = {'Content-Type' : 'application/json','trainer_token' : '8bbcb5f483c3ffd8f64615fd8c2e5776'}

body = {
   "name": "Автотест питон",
    "photo": "https://dolnikov.ru/pokemons/albums/111.png"
 }

response = requests.post(url=f'{URL}/pokemons', json=body, headers=HEADER, timeout=5 )
print(f' Ответ json: {response.text}.Статус код: {response.status_code}')

body = {
    "pokemon_id": "28483",
    "name": "New Pyton",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}

response = requests.put(url=f'{URL}/pokemons', json=body, headers=HEADER, timeout=5 )
print(f' Ответ json: {response.text}.Статус код: {response.status_code}')

body = {
    "pokemon_id": "28483"
}

response = requests.post(url=f'{URL}/trainers/add_pokeball', json=body, headers=HEADER, timeout=5 )
print(f' Ответ json: {response.text}.Статус код: {response.status_code}')