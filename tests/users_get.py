import requests
import pprint

def test_users_recieve():
    url = "http://127.0.0.1:5000/users"

    response = requests.get(url)

    if response.status_code == 200:
        pprint.pprint(response.json())
test_users_recieve()