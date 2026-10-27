import requests, os
from dotenv import load_dotenv

def get_request():

    load_dotenv()

    token = os.environ['GITHUB_TOKEN']
    header = {'Authorization': f'Bearer {token}'}
    r = requests.get('https://api.github.com/repos/home-assistant/operating-system/pulls', headers=header)

    print(r.status_code)
    print(r.json())

