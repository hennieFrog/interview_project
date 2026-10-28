from abc import abstractmethod, ABC
import requests, os
from dotenv import load_dotenv

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

        try:
            pull_requests = requests.get(
                    f'https://api.github.com/repos/{owner}/{repo}/pulls'
                    ,headers=header
                    ,params=params
                ).json()
        except Exception as e:
            raise e

        collection_set = []

        for (index, pull_request) in enumerate(pull_requests):

            pull_number = pull_request['number']
            ref = pull_request['merge_commit_sha']

            pr_reviews = requests.get(
                    f'https://api.github.com/repos/{owner}/{repo}/pulls/{pull_number}/reviews'
                    ,headers=header
                ).json()

            pr_checks = requests.get(
                    f'https://api.github.com/repos/{owner}/{repo}/commits/{ref}'
                    ,headers=header
                ).json()

            collection_set.append({
                    'index': index
                    ,'pull_request': pull_request
                    ,'pr_reviews': pr_reviews
                    ,'pr_checks': pr_checks
                })

        return collection_set

    def fetch_auth(self):
        # Fetches GH bearer PAT.
        # Ensure that there is a valid GH PAT under .env in the src/ directory structure.
        # Format: "GITHUB_TOKEN=ghp_****"
        try:
            load_dotenv()
            return os.environ['GITHUB_TOKEN']
        except Exception as e:
            raise e


