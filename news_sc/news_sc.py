from collections import namedtuple
import re

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
    entries = []
    points = comments = 0
    i = 1
    for title in span_titles:
        next_link = title.find_next("a")
        next_string = next_link.string
        print(i, next_link.string)
        for sibling in next_link.find_next_siblings(True):
            # if "href" in sibling.attrs:
            if sibling.string is not None:
                sub_url = sibling.string
                title += ' ' + str(sub_url)
                print(f'title is now {title}')
        previous_tr = title.find_previous("tr")
        following_tr = previous_tr.find_next_sibling("tr")
        following_span_smaller = following_tr.find_next("span", class_="smaller")
        bunch_of_strings_for_debug = []
        for s in following_span_smaller.strings:
            # if s.strip()[0].isdigit():
            bunch_of_strings_for_debug.append(s.strip())
            match = re.match(r'(^\d+) points', s.strip())
                # print(s)
                # break
            if match:
                points = int(match.group(1))
                print(points)
                # break
            other_match = re.match(r'(^\d+) comments', s.strip())
            if other_match:
                comments = int(other_match.group(1))
                print(f'also {comments} too')

        entries.append(Entry(next_string, points, comments))

        i += 1

    # pass
    sorted_entries = sorted(entries, key=lambda entry: (-entry[1], -entry[2]))
    print(soup.prettify())
    return sorted_entries



if __name__ == '__main__':
    get_top_titles('https://bites-data.s3.us-east-2.amazonaws.com/news.python.sc/index.html')