import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'd5a447d2ac3e1c93fc1df70edb9170c6'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' :TOKEN}
TRAINER_ID = '13079'


def test_status_code():
    response = requests.get(url= f'{URL}/trainers', params= {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url= f'{URL}/trainers', params={'trainer_id' : TRAINER_ID})
    assert response_get.json()["data"][0]["trainer_name"] == 'Aleksandrina'