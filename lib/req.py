import requests

BASE_URL = 'http://127.0.0.1:5000/'


def get_form():
    return requests.get(BASE_URL)


def post_form(data):
    return requests.post(f'{BASE_URL}/result', data={'data': data})


