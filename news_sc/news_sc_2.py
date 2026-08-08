import re
from collections import namedtuple

import requests
from bs4 import BeautifulSoup

# feed = https://news.python.sc/, to get predictable results we cached
# first two pages - use these:
# https://bites-data.s3.us-east-2.amazonaws.com/news.python.sc/index.html
# https://bites-data.s3.us-east-2.amazonaws.com/news.python.sc/index2.html

Entry = namedtuple('Entry', 'title points comments')

POINTS_RE = re.compile(r'^(\d+) points')
COMMENTS_RE = re.compile(r'^(\d+) comments')


def _create_soup_obj(url):
    """Need utf-8 to properly parse emojis"""
    resp = requests.get(url)
    resp.encoding = "utf-8"
    return BeautifulSoup(resp.text, "html.parser")


def _build_title(link):
    """Start from the link's own text, then append any '(...)' suffix
    found in a sibling tag right after it (e.g. a source domain)."""
    title = link.string
    for sibling in link.find_next_siblings(True):
        for child in sibling.children:
            if child.next.string is not None:
                title += f' ({child.next.string})'
                break
    return title


def _parse_points_and_comments(title_span):
    """Locate the 'N points' / 'N comments' text that belongs to this
    title's row, and extract both numbers."""
    row = title_span.find_previous("tr")
    next_row = row.find_next_sibling("tr")
    meta_span = next_row.find_next("span", class_="smaller")

    points = comments = 0
    for text in meta_span.strings:
        text = text.strip()
        if match := POINTS_RE.match(text):
            points = int(match.group(1))
        elif match := COMMENTS_RE.match(text):
            comments = int(match.group(1))
    return points, comments


def get_top_titles(url, top=5):
    """Parse the titles (class 'title') using the soup object.
       Return a list of top (default = 5) titles ordered descending
       by number of points and comments.
    """
    soup = _create_soup_obj(url)
    entries = []

    for title_span in soup.find_all("span", class_="title"):
        link = title_span.find_next("a")
        title = _build_title(link)
        points, comments = _parse_points_and_comments(title_span)
        entries.append(Entry(title, points, comments))

    return sorted(entries, key=lambda e: (-e.points, -e.comments))[:top]