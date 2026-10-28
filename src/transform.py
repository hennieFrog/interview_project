from abc import abstractmethod
from abc import ABC
from datetime import date
import extract


class DataEntry:

    def __init__(self, index:int, ticket_id:str, title:str, author:str, resolve_date:date, resolved:bool, checks_passed:bool):
        self.index = index
        self.ticket_id = ticket_id  # PR number
        self.title = title # PR title
        self.author = author
        self.resolve_date = resolve_date # Merge date
        self.resolved = resolved # CR_Passed
        self.checks_passed = checks_passed

    def __str__(self):
        return f'Index: {self.index},\nPR number: {self.ticket_id}\nPR title: {self.title}\nAuthor: {self.author}\nMerge date: {self.resolve_date}\nCR passed: {self.resolved}\nChecks passed: {self.checks_passed}'

class TransformStrategy(ABC):

    @abstractmethod
    def transform(self):
        pass

    @abstractmethod
    def transform_entry(self, **kwargs) -> DataEntry:
        pass


class GithubTransformer(TransformStrategy):

    def __init__(self, owner: str, repo: str):
        self.owner = owner
        self.repo = repo

    def transform(self):
        fetcher = extract.GithubFetcher()
        collction_set = fetcher.fetch(owner=self.owner, repo=self.repo)

        data = []
        for collection in collction_set:
            transformed_entry = self.transform_entry(collection)
            data.append(transformed_entry)

        return data

    def transform_entry(self, collection):

        reviews = collection['pr_reviews']
        resolved = False

        try:
            for review in reviews:
                if review['state'] == 'APPROVED':
                    resolved = True 
        except TypeError as e:
            pass

        checks_passed = True if collection['pr_checks']['commit']['verification']['verified'] == 'True' else False

        entry = DataEntry(
                index= collection['index']
                ,ticket_id= collection['pull_request']['number']
                ,title= collection['pull_request']['title']
                ,author= collection['pull_request']['user']['login']
                ,resolve_date= collection['pull_request']['user']['login']
                ,resolved= resolved
                ,checks_passed= checks_passed
            )

        return entry


# def transform_json():
#     json_content = extract.get_pull_requests()
#
#     list = []
#
#     # first_entry = json_content.pop()
#     for entry in json_content:
#         pr_number = entry['number']
#         pr_title = entry['title']
#         author = entry['user']['login']
#         merge_date = entry['merged_at']
#
#         try:
#             reviews = extract.get_reviews(entry['number'])
#             for review in reviews:
#                 print(review['state'])
#         except TypeError as e:
#             print('No reviews in progress')
#             continue
#
#         checks = extract.get_checks(entry['merge_commit_sha'])
#         print(checks['commit']['verification']['verified'])
#
#         print(' ')

