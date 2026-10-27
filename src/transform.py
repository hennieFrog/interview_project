from datetime import date
import extract

def transform_json():
    json_content = extract.get_request()

    first_entry = json_content.pop()

    print(first_entry['number'])
    print(first_entry['title'])
    print(first_entry['user']['login'])
    print(first_entry['merged_at'])



# class Entry():
#     pr_number: str
#     pr_title: str
#     author: str
#     merge_date: date
#     cr_passed: bool
#     checks_passed: bool



transform_json()
