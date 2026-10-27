from datetime import date
import extract

def transform_json():
    json_content = extract.get_pull_requests()

    # first_entry = json_content.pop()
    for entry in json_content:
        print(entry['number'])
        print(entry['title'])
        print(entry['user']['login'])
        print(entry['merged_at'])

        try:
            reviews = extract.get_reviews(entry['number'])
            for review in reviews:
                print(review['state'])
        except TypeError as e:
            print('No reviews in progress')
            continue

        checks = extract.get_checks(entry['merge_commit_sha'])
        print(checks['commit']['verification']['verified'])

        print(' ')



# class Entry():
#     pr_number: str
#     pr_title: str
#     author: str
#     merge_date: date
#     cr_passed: bool
#     checks_passed: bool



transform_json()
