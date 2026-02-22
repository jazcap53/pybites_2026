from collections import defaultdict
import os
from urllib.request import urlretrieve

from bs4 import BeautifulSoup


# prep data
tmp = os.getenv("TMP", "/tmp")
page = 'us_holidays.html'
holidays_page = os.path.join(tmp, page)
urlretrieve(
    f'https://bites-data.s3.us-east-2.amazonaws.com/{page}',
    holidays_page
)

with open(holidays_page) as f:
    content = f.read()

holidays = defaultdict(list)


def get_us_bank_holidays(content=content):
    """Receive scraped html output, make a BS object, parse the bank
       holiday table (css class = list-table), and return a dict of
       keys -> months and values -> list of bank holidays"""
    soup = BeautifulSoup(content, 'html.parser')
    days_off = soup.find(class_='list-table')
    dates = days_off.find_all('td')
    month = ''
    for date in dates:
        if date.time:
            month = date.time.text.split('-')[1]
        elif date.a:
            day_off = date.a.text.strip()
            holidays[month].append(day_off)
    return holidays


if __name__ == '__main__':
    get_us_bank_holidays()