import requests
from dotenv import load_dotenv
import os

load_dotenv()


def test_user_update(id, name, email):
        url = os.getenv("url") + os.getenv("endpoint_users") + f"/{id}"
        
        data = {}
        
        data["name"] = name
        data["email"] = email

        response = requests.put(url, json=data)

        print(response)

        if response.status_code == 200:
            print(response.json())
id = int(input("Input id of user for update: "))
name = input("Input new name: ")
email = input("Input new email: ")
test_user_update(id, name, email)