import requests
from dotenv import load_dotenv
import os

load_dotenv()

def test_user_create(name, email):
        
        url = os.getenv("url") + os.getenv("endpoint_users")
        print(url)

        data = {}

        data["name"] = name
        data["email"] = email

        response = requests.post(url, json=data)
        print(response)

        if response.status_code == 201:
            print(response.json())
name = input("Enter your name: ")
email = input("Enter your email: ")
test_user_create(name, email)