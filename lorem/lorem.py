from bs4 import BeautifulSoup
import requests
import re
from random import choice, randint

# FEATURED_ARTICLE = ('https://en.wikipedia.org/wiki/Wikipedia:Today%27s_featured_article/January_1,_2022')
FEATURED_ARTICLE = ('https://bites-data.s3.us-east-2.amazonaws.com/wiki_features_article_2022-01-01.html')
CONTENT = requests.get(FEATURED_ARTICLE).text


def wiki_lorem_ipsum(article: str = CONTENT, number_of_sentences: int = 5):
    """Create a lorem ipsum block of sentences from the words scraped from today's Wikipedia featured article

    :param number_of_sentences
    :type number_of_sentences: int
    :return: lorem ipsum text (Lorem ipsum is nonsense text used to test layouts for documents or websites)
    rtype: str
    """
    pass