import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '1b08d2faaf333d248b0c029d54926b6f'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN }
TRAINR_ID = '4834'

def test_status_code():
    response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINR_ID })
    assert response.status_code == 200

def test_name_trainer():
    response_name = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINR_ID })
    assert response_name.json()["data"][0]["name"] == 'Oleshechka'
