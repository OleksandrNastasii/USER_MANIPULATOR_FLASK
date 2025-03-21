import requests
from dotenv import load_dotenv
import os
import pprint

load_dotenv()

def test_users_recieve():
        url = os.getenv("url") + os.getenv("endpoint_users")

        response = requests.get(url)

        if response.status_code == 200:
            pprint.pprint(response.json())
test_users_recieve()