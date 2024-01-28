import requests
import pytest

URL = 'https://api.pokemonbattle.me:9104'
HEADER = {'Content-Type' : 'application/json','trainer_token' : '8bbcb5f483c3ffd8f64615fd8c2e5776'}

def test_get_trainers_level():
    
    """"
   Тест на код 200
    """
    response = requests.get(url=f'{URL}/trainers', params={'level': 1}, timeout=5 )
    assert response.status_code == 200,  'Unexpected status code'

def test_get_trainers_trainer_id():
    
    """"
   Тест на id
    """
    response = requests.get(url=f'{URL}/trainers', params={'trainer_id':3463}, timeout=5 )
    assert response.json()['trainer_name'] == 'Колобок', ''