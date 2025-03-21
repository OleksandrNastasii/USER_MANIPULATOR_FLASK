import requests
from dotenv import load_dotenv
import os
import pprint

load_dotenv()

def test_user_recieve(id):        
        url = os.getenv("url") + os.getenv("endpoint_users") + f"/{id}"

        print(url)

        response = requests.get(url)

        print(response)

        if response.status_code == 200:
            pprint.pprint(response.json())
test_user_recieve(int(input("Enter user id to get: ")))