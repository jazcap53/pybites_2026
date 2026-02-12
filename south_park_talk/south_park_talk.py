from collections import Counter, defaultdict
import csv
import re
import requests
import string

CSV_URL = 'https://raw.githubusercontent.com/pybites/SouthParkData/master/by-season/Season-{}.csv'  # noqa E501


def get_season_csv_file(season):
    """Receives a season int, and downloads loads in its
       corresponding CSV_URL"""
    with requests.Session() as s:
        download = s.get(CSV_URL.format(season))
        return download.content.decode('utf-8')


def format_content_lines(content_lines):
    good_lines = []
    full_speech = ''
    season, episode, speaker, speech_so_far = '', '', '', ''
    for line in content_lines:
        line = line.rstrip()
        if not line:
            continue
        if line[0].isdigit():  # start of speech
            season, episode, speaker, speech_so_far = line.split(',', maxsplit=3)
        elif line == '"':  # reached end of speech; store and reset
            full_speech = speech_so_far.lstrip('"')
            good_lines.append((season, episode, speaker, full_speech))
            full_speech = ''
            season, episode, speaker, speech_so_far = '', '', '', ''
        else:  # we have another line of the speech; add it to speech
            full_speech += speech_so_far if not full_speech else ' ' + speech_so_far
    for i in range(5):
        print(good_lines[i])
    return good_lines


def clean_up_line(line):
    ret_line = ''
    for c in line:
        if c in string.ascii_letters or c == '-' or c in string.whitespace:
            ret_line += c
        elif c == '&':
            ret_line += 'and'
        else:
            continue
    return ret_line


def line_to_list_of_words(line):
    matches = re.findall(r'([a-zA-Z\'-]+)', line)
    return matches


def get_num_words_spoken_by_character_per_episode(content):
    """Receives loaded csv content (str) and returns a dict of
       keys=characters and values=Counter object,
       which is a mapping of episode=>words spoken"""

    content_lines = content.split('\n')[1:]

    formatted_content = format_content_lines(content_lines)

    character_dict = defaultdict(Counter)

    for line in formatted_content:
        season, episode, speaker, speech = line
        speech = clean_up_line(speech)
        character_dict[speaker].update({episode: len(line_to_list_of_words(speech))})
        if (season, episode, speaker) == ('1', '1', 'Cartman'):
            print(speech, ' | ', len(line_to_list_of_words(speech)))
    return character_dict


if __name__ == '__main__':
    get_num_words_spoken_by_character_per_episode(get_season_csv_file(1))