from datetime import date
from abc import abstractmethod, ABC
import requests, os
from dotenv import load_dotenv


class Entry:
    ticket_id: str # PR number
    title: str # PR title
    author: str
    resolve_date: date # Merge date
    resolved: bool # CR_Passed
    checks_passed: bool

class FetcherStrategy(ABC):

    @abstractmethod
    def fetch(self) -> Entry:
        pass

    @abstractmethod
    def fetch_auth(self) -> str:
        pass

class GithubFetcher(FetcherStrategy):

    def __init__(self):
        self.token = self.fetch_auth()

    def fetch(self, owner: str, repo: str):
        header = {'Authorization': f'Bearer {self.token}'}
        params = {'state': 'all'}

        try:
            pull_requests = requests.get(f'https://api.github.com/repos/{owner}/{repo}/pulls', headers=header, params=params)
        except Exception as e:
            raise e

        pull_number = pull_requests.json()['number']

        pr_reviews = requests.get(f'https://api.github.com/repos/{owner}/{repo}/pulls/{pull_number}/reviews', headers=header)

        pr_checks = requests.get(f'https://api.github.com/repos/{owner}/{repo}/commits/{ref}', headers=header)


    def fetch_auth():
        # Fetches GH bearer PAT.
        # Ensure that there is a valid GH PAT under .env in the src/ directory structure.
        # Format: "GITHUB_TOKEN=ghp_****"
        try:
            load_dotenv()
            return os.environ['GITHUB_TOKEN']
        except Exception as e:
            raise e


