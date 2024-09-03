import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '1b08d2faaf333d248b0c029d54926b6f'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN }


body_create = {
    "name": "Oleshka",
    "photo_id": 716
}

body_put = {
    "pokemon_id": "67080",
    "name": "Oleshechka",
    "photo_id": 716
}

body_add = {
    "pokemon_id": "67080"
}

'''response_create = requests.post(url = f'{URL}/pokemons', headers=HEADER, json = body_create)
print(response_create.text)'''

'''response_put = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_put)
print(response_put.text)'''

response_add = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add)
print(response_add.text)