import requests
from bs4 import BeautifulSoup
import re

cached_so_url = 'https://bites-data.s3.us-east-2.amazonaws.com/so_python.html'


def is_span_has_vote_count_post(tag):
    is_ok = (tag.name == "span"
             and tag.has_attr("class")
             and tag.attrs["class"][0] == "vote-count-post")
    return is_ok


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
    print(soup.prettify())
    question_links = soup.find_all(has_unique_class_value)

    vote_count_posts = soup.find_all(is_span_has_vote_count_post)

    vote_count_post = []
    # for ql in question_links:
    #     print(ql)
    #     vcp = ql.find_next("span")
    #     if vcp is not None:
    #         print("it's not None")
    #     if vcp.has_attr("class"):
    #         print("has class")
    #     if "vote-count-post" not in vcp["class"]:
    #         continue
    #     else:
    #         print("has vote count post")
    #     vote_count_post.append(vcp)
    #     print(vcp)

    print(len(question_links))
    print(len(vote_count_posts))






if __name__ == '__main__':
    top_python_questions()