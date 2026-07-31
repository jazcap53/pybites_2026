import requests
from bs4 import BeautifulSoup
import re

cached_so_url = 'https://bites-data.s3.us-east-2.amazonaws.com/so_python.html'


# def has_link_votes_views(tag):
#     return tag.has_attr("question-hyperlink") and tag.has_attr("vote-count-post")


def has_unique_class_value(tag):
   is_ok = ((tag.name == 'a')
            and (tag.has_attr("class"))
            and (tag.attrs["class"][0] == "question-hyperlink"))

   return is_ok


def top_python_questions(url=cached_so_url):
    """Use requests to retrieve the url / html,
       parse the questions out of the html with BeautifulSoup,
       filter them by >= 1m views ("..m views").
       Return a list of (question, num_votes) tuples ordered
       by num_votes descending (see tests for expected output).
    """
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    question_links = soup.find_all(has_unique_class_value)

    for ql in question_links:
        print(ql)
    print(len(question_links))






if __name__ == '__main__':
    top_python_questions()