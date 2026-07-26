from collections import Counter

from bs4 import BeautifulSoup
import requests

AMAZON = "amazon.com"
# static copy
TIM_BLOG = ('https://bites-data.s3.us-east-2.amazonaws.com/'
            'tribe-mentors-books.html')
MIN_COUNT = 3


def load_page():
    """Download the blog html and return its decoded content"""
    with requests.Session() as session:
        return session.get(TIM_BLOG).content.decode('utf-8')


def get_top_books(content=None):
    """Make a BeautifulSoup object loading in content,
       find all links that contain AMAZON, extract the book title
       (stripping spacing characters), and count them.
       Return a list of (title, count) tuples where
       count is at least MIN_COUNT
    """
    if content is None:
        content = load_page()
    soup = BeautifulSoup(content, 'html.parser')
    kids = [bolded for bolded in soup.find_all('b')]
    for kid in kids:
        if kid:
            print(kid)
        else:
            print("no kidding")
    kid_books = [kid.next_sibling for kid in kids]
    for item in kid_books:
        if item is not None and (next_item := item.find_next("span", style="font-weight:400;")) is not None:
            print(f'item is {item}  next_item is {next_item}')
            # print(f'kid_book.find_next("span", style="font-weight:400;") is {kid_book.find_next("span", style="font-weight:400;")}')




if __name__ == '__main__':
    get_top_books()
