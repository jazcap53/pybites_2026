import csv
import string
import sys
from collections import Counter, defaultdict


def format_content_lines(content_lines):
    good_lines = []
    full_speech = ''
    season, episode, speaker, speech_so_far = '', '', '', ''
    for line in content_lines:
        # if line.count(',') < 3:
        if len(line) < 3:
            continue
        if line[0] == 'Season':
            continue
        if not line:
            continue
        line[-1] = line[-1].rstrip('\n')
        if line[0][0].isdigit():  # start of speech if line.startswith('Season'):
            season, episode, speaker, speech = line
            speech = speech.strip('\n')
            good_lines.append(line)
    return good_lines


def output_dict(new_dict):
    this_sn = 0
    this_ep = 0
    for k in new_dict.keys():
        sn, ep = k[0], k[1]
        if sn > this_sn:
            this_sn = sn
            print(f'Season {this_sn}')
            this_ep = 0
        if ep > this_ep:
            this_ep = ep
            print(f'\tEpisode {this_ep}')



# with open('raw_data.txt', 'r') as f:
with open('All-seasons.csv', newline='') as f:
    csv_reader = csv.reader(f)
    structure = defaultdict(int)
    of_interest = ''
    lines = []
    for my_line in csv_reader:
        lines.append(my_line)
    # lines = f.readlines()
    content_lines = format_content_lines(lines)
    curr_season, curr_episode = 0, 0
    for line in content_lines:
        # print(line)
        season, episode, character, speech = line
        # print(speech)
        this_season, this_episode = int(season), int(episode)
        if this_season != curr_season:
            curr_season = this_season
            curr_episode = 1
        elif this_episode > curr_episode:
            curr_episode = this_episode
            # structure[curr_episode, curr_season] = ''
        for c in speech:
            # if string is (possibly weird) punctuation
            if c not in string.ascii_letters and c not in string.digits and c not in string.whitespace:
                of_interest += c
            else:
                if len(of_interest) > 1:
                    # print(of_interest)
                    structure[curr_season, curr_episode, of_interest] += len(of_interest)
                of_interest = ''

    # sorted_dict_asc = {k: v for k, v in sorted(my_dict.items(), key=lambda item: item[1])}
    # print(structure)
    # print()
    new_dict = {k: v for k, v in sorted(structure.items(), key=lambda x: x[1])}
    # print(new_dict)
    output_dict(new_dict)