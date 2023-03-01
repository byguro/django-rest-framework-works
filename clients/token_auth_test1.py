import requests
from pprint import pprint

def client():
    credentials = {
        'username': 'rest_rest_user6',
        'password': 'testing321..'
    }

    response = requests.post(
        url = 'http://localhost:8000/dj-rest-auth/login/',
        data = credentials
    )

    print('status code:', response.status_code)

    response_data = response.json()
    pprint(response_data)

if __name__ == '__main__':
    client()