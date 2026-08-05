from collections import namedtuple

from bs4 import BeautifulSoup, NavigableString
import requests

# feed = https://news.python.sc/, to get predictable results we cached
# first two pages - use these:
# https://bites-data.s3.us-east-2.amazonaws.com/news.python.sc/index.html
# https://bites-data.s3.us-east-2.amazonaws.com/news.python.sc/index2.html

Entry = namedtuple('Entry', 'title points comments')


def _create_soup_obj(url):
    """Need utf-8 to properly parse emojis"""
    resp = requests.get(url)
    resp.encoding = "utf-8"
    return BeautifulSoup(resp.text, "html.parser")


def get_top_titles(url, top=5):
    """Parse the titles (class 'title') using the soup object.
       Return a list of top (default = 5) titles ordered descending
       by number of points and comments.
    """
    soup = _create_soup_obj(url)

    span_titles = soup.find_all("span", class_="title")

    i = 1
    for title in span_titles:
        next_link = title.find_next("a")
        print(i, next_link.string)
        previous_tr = title.find_previous("tr")
        following_tr = previous_tr.find_next_sibling("tr")
        following_span_smaller = following_tr.find_next("span", class_="smaller")
        print(f'following_span_smaller.name is {following_span_smaller.name}')
        print(f'following_span_smaller.attrs is {following_span_smaller.attrs}')
        for s in following_span_smaller.strings:
            if s.strip()[0].isdigit():
                print(s)
                break

        i += 1

    # print(soup.prettify())



if __name__ == '__main__':
    get_top_titles('https://bites-data.s3.us-east-2.amazonaws.com/news.python.sc/index.html')