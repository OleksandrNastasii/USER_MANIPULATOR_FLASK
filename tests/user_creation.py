import requests

def test_user_creation():
    url = "http://127.0.0.1:5000/users"
    data = {
        "name": "Jasoffk",
        "email": "mahfrf@example.com"
        }

    response = requests.post(url, json=data)

    if response.status_code == 201:
        print(response.json())
test_user_creation()