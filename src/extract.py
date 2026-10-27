import requests, os
from dotenv import load_dotenv


def fetch_pat():
    # Fetches bearer PAT.
    # Ensure that there is a valid GH PAT under .env in the src/ directory structure.
    # Format: "GITHUB_TOKEN=ghp_****"
    load_dotenv()
    return os.environ['GITHUB_TOKEN']


### FETCHERS ###
def get_pull_requests():
    token = fetch_pat()
    header = {'Authorization': f'Bearer {token}'}
    params = {'state': 'all'}

    pull_requests = requests.get('https://api.github.com/repos/home-assistant/operating-system/pulls', headers=header, params=params)

    return pull_requests.json()


def get_reviews(pull_number):
    token = fetch_pat()
    header = {'Authorization': f'Bearer {token}'}

    pr_reviews = requests.get(f'https://api.github.com/repos/home-assistant/operating-system/pulls/{pull_number}/reviews', headers=header)

    return pr_reviews.json()


def get_checks(ref):
    token = fetch_pat()
    header = {'Authorization': f'Bearer {token}'}

    pr_checks = requests.get(f'https://api.github.com/repos/home-assistant/operating-system/commits/{ref}', headers=header)

    return pr_checks.json()

