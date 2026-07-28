import requests
from bs4 import BeautifulSoup

cached_so_url = 'https://bites-data.s3.us-east-2.amazonaws.com/so_python.html'


def has_link_votes_views(tag):
    return tag.has_attr("question-hyperlink") and tag.has_attr("vote-count-post")


def top_python_questions(url=cached_so_url):
    """Use requests to retrieve the url / html,
       parse the questions out of the html with BeautifulSoup,
       filter them by >= 1m views ("..m views").
       Return a list of (question, num_votes) tuples ordered
       by num_votes descending (see tests for expected output).
    """
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    question_link = soup.find_all(class_="question-hyperlink")
    for q_l in question_link:
        print(q_l)
    votes = soup.find_all(class_="vote-count-post")
    views = soup.find_all(class_="views")
    print(len(question_link))
    print(len(votes))
    print(len(views))
        # print(question.get('href'))
        # link = question(class_="question-hyperlink")
        # votes = question(class_="vote-count-post")
        # views = question(HTML="..m")
        # print((link, votes, views))
        # break



if __name__ == '__main__':
    top_python_questions()