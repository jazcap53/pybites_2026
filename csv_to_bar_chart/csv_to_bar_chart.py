from collections import defaultdict
import csv

import requests

CSV_URL = 'https://bites-data.s3.us-east-2.amazonaws.com/community.csv'


def get_csv():
    """Use requests to download the csv and return the
       decoded content"""
    dd = defaultdict(int)
    resp = requests.get(CSV_URL)
    rdr = csv.DictReader(resp.text.split('\n'))
    for line in rdr:
        dd[line['tz']] += 1
    d = dict(dd)
    return d

def create_user_bar_chart(content):
    """Receives csv file (decoded) content and print a table of timezones
       and their corresponding member counts in pluses to standard output
    """
    pass


if __name__ == '__main__':
    contents = get_csv()
    print(contents)
    longest = max(contents.keys(), key=len)
    print(f'length of longest key {longest} is {len(longest)}')