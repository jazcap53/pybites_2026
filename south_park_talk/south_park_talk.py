from collections import Counter, defaultdict
import csv

import requests

CSV_URL = 'https://raw.githubusercontent.com/pybites/SouthParkData/master/by-season/Season-{}.csv' # noqa E501


def get_season_csv_file(season):
    """Receives a season int, and downloads loads in its
       corresponding CSV_URL"""
    with requests.Session() as s:
        download = s.get(CSV_URL.format(season))
        return download.content.decode('utf-8')


def get_num_words_spoken_by_character_per_episode(content):
    """Receives loaded csv content (str) and returns a dict of
       keys=characters and values=Counter object,
       which is a mapping of episode=>words spoken"""
    content_lines = content.split('\n')  # a list of str
    content_reader = csv.DictReader(content_lines)
    character_dict = defaultdict(Counter)
    for line in content_reader:
        character_dict[line["Character"]][line["Episode"]] += len(line["Line"].split())
    return character_dict

if __name__ == '__main__':
    get_num_words_spoken_by_character_per_episode(get_season_csv_file(1))


    # formatted_content = format_content_lines(content_lines)


"""
              {'Agent 1': Counter({'8': 48, '2': 1}),
...
# Counter k,v here = (episode, # number of words spoken)
...
               'Anthropologist': Counter({'12': 101}),
...
               'Cartman': Counter({'1': 735,
                                   '10': 669,
                                   '13': 621,
... etc ...
"""