import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'cad98f9e03fa48e0caeec22121897bc0'
HEADER = {'Content-Type':'application/json'}
TRAINER_ID = 6782


def test_status_code_trainers():
    response = requests.get(url= f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200
   
def test_trainer_name():
    response_get = requests.get(url= f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_get.json ()['trainer_name'] == 'Darth El'