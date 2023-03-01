import requests
from pprint import pprint

def client():
    credentials = {
        'username': 'rest_rest_user6',
        'email': 'test6@test.com',
        'password1': 'testing321..',
        'password2': 'testing321..'
    }
    print('Start request')
    response = requests.post(
        url = 'http://localhost:8000/api/dj-rest-auth/registration/',
        data = credentials
    )

    print('status code:', response.status_code)

    if response.status_code != 204: #no content
        response_data = response.json()
        pprint(response_data)

if __name__ == '__main__':
    client()