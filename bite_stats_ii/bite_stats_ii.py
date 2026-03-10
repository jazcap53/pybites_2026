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
    rating_list = []
    with open(stats, newline='', encoding='utf-8-sig') as infile:
        reader = csv.reader(infile, delimiter=';')
        for line in reader:
            if line[0] == 'Bite' or line[1] == 'None':
                continue
            # print(line)
            line[0] = line[0].lstrip()
            dot_is_at = line[0].find('.')
            bite_num = int(line[0][5:dot_is_at])
            diff_rating = float(line[1])
            rating_list.append((bite_num, diff_rating))
        rating_list.sort(key=lambda item: item[1])
        top_ratings = [item[0] for item in rating_list]
        return reversed(top_ratings[-N:])



if __name__ == '__main__':
    res = get_most_complex_bites()
    print(res)