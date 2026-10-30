from abc import ABC, abstractmethod
from pandas import DataFrame
import extract

'''
TRANSFORM.PY

This class pocesses the raw list of dictionaries into useable data as the second step in the
ETL pipeline. This class also uses a Strategy OOP Pattern to neatly slot in a transformer for
a different integration.

There is two abstract methods: transform() and transform_entry(). transform() is the overall
method that iterates through every entry wich calls trasnform_entry() to do the row level
transformation which returns a dict. All the data is appended to a dataframe.
'''

class TransformStrategy(ABC):

    @abstractmethod
    def transform(self) -> DataFrame:
        pass

    @abstractmethod
    def transform_entry(self) -> dict:
        pass


class GithubTransformer(TransformStrategy):

    def __init__(self, owner: str, repo: str):
        self.owner = owner
        self.repo = repo

    def transform(self):
        fetcher = extract.GithubFetcher()
        collection_set = fetcher.fetch(owner=self.owner, repo=self.repo)

        df = DataFrame(
                columns=[
                    'ticket_id'
                    ,'title'
                    ,'author'
                    ,'resolve_date'
                    ,'resolved'
                    ,'checks_passed'
                ]
            )

        print('Transforming data...')

        for (i, collection) in enumerate(collection_set):
            transformed_entry = self.transform_entry(collection)
            df.loc[i] = transformed_entry

        return df

    def transform_entry(self, collection) -> dict:
        reviews = collection['pr_reviews']
        resolved = False

        try:
            for review in reviews:
                if review['state'] == 'APPROVED':
                    resolved = True 
        except TypeError as e:
            raise e

        entry = {
                'ticket_id': collection['pull_request']['number']  # PR number 
                ,'title': collection['pull_request']['title'] # PR title
                ,'author': collection['pull_request']['user']['login']
                ,'resolve_date': collection['pull_request']['merged_at'] # Merge date
                ,'resolved': resolved # CR_Passed
                ,'checks_passed': collection['pr_checks']['commit']['verification']['verified']
            }

        return entry


