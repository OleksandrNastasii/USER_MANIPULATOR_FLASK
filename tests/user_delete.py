import requests

def test_user_update():
    id = 2
    url = f"http://127.0.0.1:5000/users/{id}"

    response = requests.delete(url)

    print(response)

    if response.status_code == 200:
        print(response.json())
test_user_update()