"""
... etc ...
                                   '13': 621,
                                   '10': 669,
               'Cartman': Counter({'1': 735,
...
               'Anthropologist': Counter({'12': 101}),
...
# Counter k,v here = (episode, # number of words spoken)
...
              {'Agent 1': Counter({'8': 48, '2': 1}),
"""


    # formatted_content = format_content_lines(content_lines)


    get_num_words_spoken_by_character_per_episode(get_season_csv_file(1))
if __name__ == '__main__':

    return character_dict
        character_dict[line["Character"]][line["Episode"]] += len(line["Line"].split())
    for line in content_reader:
    character_dict = defaultdict(Counter)
    content_reader = csv.DictReader(content_lines)
    content_lines = content.split('\n')  # a list of str
       which is a mapping of episode=>words spoken"""
       keys=characters and values=Counter object,
    """Receives loaded csv content (str) and returns a dict of
def get_num_words_spoken_by_character_per_episode(content):


        return download.content.decode('utf-8')
        download = s.get(CSV_URL.format(season))
    with requests.Session() as s:
       corresponding CSV_URL"""
    """Receives a season int, and downloads loads in its
def get_season_csv_file(season):


CSV_URL = 'https://raw.githubusercontent.com/pybites/SouthParkData/master/by-season/Season-{}.csv' # noqa E501

import requests

import csv
from collections import Counter, defaultdict