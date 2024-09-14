import requests


URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'cad98f9e03fa48e0caeec22121897bc0'
HEADER = {'Content-Type':'application/json',
          'trainer_token': TOKEN}

body_create_pokemon = {
    "name": "Foxy",
    "photo_id": 26
}

body_rename_pokemon = {
    "pokemon_id": "70465",
    "name": "Foxidze",
    "photo_id": 26
}

body_pokemon_in_pokeball = {
    "pokemon_id": "70465"
}

response = requests.post(url= f'{URL}/pokemons', headers = HEADER, json = body_create_pokemon)
print(response.text)

response = requests.put(url= f'{URL}/pokemons', headers = HEADER, json = body_rename_pokemon)
print(response.text)

response = requests.post(url= f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokemon_in_pokeball)
print(response.text)
