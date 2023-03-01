import requests
from pprint import pprint

def client():
    token = 'Token 970076811f09f38fc681887469f23aece5520046'
    headers = {
        'Authorization': token,
    }

    response = requests.get(
        url = 'http://localhost:8000/api/kullanici-profilleri/',
        headers = headers,
    )

    print('status code:', response.status_code)

    response_data = response.json()
    pprint(response_data)

if __name__ == '__main__':
    client()