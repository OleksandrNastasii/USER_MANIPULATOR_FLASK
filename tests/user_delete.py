import requests
from dotenv import load_dotenv
import os

load_dotenv()

def test_user_delete(id):
        url = os.getenv("url") + os.getenv("endpoint_users") + f"/{id}"

        response = requests.delete(url)

        print(response)

        if response.status_code == 200:
            print(response.json())
test_user_delete(int(input("Enter user id to delete: ")))