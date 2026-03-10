from collections import defaultdict
import csv
import os
from pathlib import Path
from urllib.request import urlretrieve

data = 'https://bites-data.s3.us-east-2.amazonaws.com/bite_levels.csv'
TMP = Path(os.getenv("TMP", "/tmp"))
stats = TMP / 'bites.csv'

if not stats.exists():
    urlretrieve(data, stats)


def get_most_complex_bites(N=10, stats=stats):
    """Parse the bites.csv file (= stats variable passed in), see example
       output in the Bite description.
       Return a list of Bite IDs (int or str values are fine) of the N
       most complex Bites.
    """
    top_ratings = []
    rating_dict = defaultdict(list)
    with open(stats, newline='', encoding='utf-8-sig') as infile:
        reader = csv.reader(infile, delimiter=';')
        for line in reader:
            if line[0] == 'Bite' or line[1] == 'None':
                continue
            line[0] = line[0].lstrip()
            dot_is_at = line[0].find('.')
            bite_num = int(line[0][5:dot_is_at])
            diff_rating = float(line[1])
            rating_dict[diff_rating].append(bite_num)
        for k, v in rating_dict.items():
            rating_dict[k] = sorted(v)
        for k in sorted(rating_dict.keys(), reverse=True):
            for i in range(len(rating_dict[k])):
                if len(top_ratings) < N:
                    top_ratings.append(rating_dict[k][i])
            if len(top_ratings) == N:
                break

        return top_ratings




if __name__ == '__main__':
    res = get_most_complex_bites()
    print(res)