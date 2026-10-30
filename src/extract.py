from requests.models import ConnectionError
from sys import exit
from abc import abstractmethod, ABC
import requests, os
from dotenv import load_dotenv

'''
EXTRACT.PY

This class manages all fetch scripts for the extract step in the ETL pipeline
It uses a Strategy Pattern to allow for simple integrations with different platforms.
Add your integration fetcher strategy as a subclass of the abstract class FetcherStrategy.

It has two abstract methods that's required by the integration, fetch() and fetch_auth().
fetch() gets all the data and stores it in a list of dictionaries that contains the raw
extracted data. This data could be directly stored if and ELT pipline is required later on.

The fetch_auth() abstract method retrieves the credentials necessary for the fetch() method.
It can be a simple token in the .env file, or full user credentials like email and password
from a different source.
'''

class FetcherStrategy(ABC):

    @abstractmethod
    def fetch() -> list[dict[str, any]]:
        pass

    @abstractmethod
    def fetch_auth():
        pass


class GithubFetcher(FetcherStrategy):

    def __init__(self):
        self.token = self.fetch_auth()

    def fetch(self, owner: str, repo: str):
        header = {'Authorization': f'Bearer {self.token}'}
        params = {'state': 'all'}
        collection_set = []

        requests_link = f'https://api.github.com/repos/{owner}/{repo}/pulls'
        print(f'Fetching requests from {requests_link}...')
        try:
            pull_requests = requests.get(
                    requests_link
                    ,headers=header
                    ,params=params
                ).json()
        except ConnectionError:
            print(f'Connection error when trying to connect to {requests_link}')
            exit(1)
        except ConnectionRefusedError:
            print(f'Connection refused {requests_link}')
            exit(1)

        self.verify_connection(pull_requests)

        for (index, pull_request) in enumerate(pull_requests):

            pull_number = pull_request['number']
            ref = pull_request['merge_commit_sha']

            reviews_link = f'https://api.github.com/repos/{owner}/{repo}/pulls/{pull_number}/reviews'
            print(f'Fetching reviews from {reviews_link}...')
            try:
                pr_reviews = requests.get(
                        reviews_link
                        ,headers=header
                    ).json()
            except ConnectionError:
                print(f'Connection error when trying to connect to {reviews_link}')
                exit()
            except ConnectionRefusedError:
                print(f'Connection refused for {reviews_link}')
                exit()
            self.verify_connection(pr_reviews)

            commits_link = f'https://api.github.com/repos/{owner}/{repo}/commits/{ref}'
            print(f'Fetching commits from {commits_link}...')
            try:
                pr_checks = requests.get(
                        commits_link
                        ,headers=header
                    ).json()
            except ConnectionError:
                print(f'Connection error when trying to connect to {commits_link}')
                exit()
            except ConnectionRefusedError:
                print(f'Connection refused {commits_link}')
                exit()
            self.verify_connection(pr_checks)

            collection_set.append({
                    'index': index
                    ,'pull_request': pull_request
                    ,'pr_reviews': pr_reviews
                    ,'pr_checks': pr_checks
                })

        return collection_set

    # Fetches GH bearer PAT.
    # Ensure that there is a valid GH PAT under .env in the src/ directory structure.
    # Format: "GITHUB_TOKEN=ghp_****"
    def fetch_auth(self):
        try:
            load_dotenv()
            return os.environ['GITHUB_TOKEN']
        except Exception as e:
            print('No valid token found in environment. Check your .env file or environment variables.\nEnsure you set a variable in the format \"GITHUB_TOKEN=ghp_****\".')
            exit()

    def verify_connection(self, body):
        try:
            if body['status'] != '200':
                print(f'{body['status']}: {body['message']}')
                exit(1)
        except Exception as e:
            pass

