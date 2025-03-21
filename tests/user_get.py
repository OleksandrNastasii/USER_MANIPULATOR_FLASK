import requests
import pprint

def test_user_recieve():
    id = 2
    
    url = f"http://127.0.0.1:5000/users/{1}"

    response = requests.get(url)

    print(response)

    if response.status_code == 200:
        pprint.pprint(response.json())
test_user_recieve()