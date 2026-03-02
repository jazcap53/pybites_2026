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
    longest = len(max(content.keys(), key=len))
    content = sorted(content.items(), key=lambda i: i[0])
    for item in content:
        item_f_str = f"{item[0]:{longest}} | {item[1]}"
        # print(item[0] + (longest-len(item[0]))*' ' +' | ' + item[1]*'+')
        print(item_f_str)


if __name__ == '__main__':
    content = get_csv()
    create_user_bar_chart(content)