from collections import Counter
import os
from urllib.request import urlretrieve

from dateutil.parser import parse

commits = os.path.join(os.getenv("TMP", "/tmp"), "commits")
urlretrieve("https://bites-data.s3.us-east-2.amazonaws.com/git_log_stat.out", commits)

# you can use this constant as key to the yyyymm:count dict
YEAR_MONTH = "{y}-{m:02d}"


def get_min_max_amount_of_commits(
    commit_log: str = commits, year: int | None = None
) -> tuple[str, str]:
    """
    Calculate the amount of inserts / deletes per month from the
    provided commit log.

    Takes optional year arg, if provided only look at lines for
    that year, if not, use the entire file.

    Returns a tuple of (least_active_month, most_active_month)
    """
    # for line in commit_log.split('\n'):
    #     print(line)
    with open(commit_log) as logg:
        for line in logg.readlines()[:5]:
            line_list = line.rstrip('\n').split('|')
            print(line_list[0][12:])
            print(line_list[1])
            parsed_val = parse(line_list[0][12:])  # , YEAR_MONTH)
            print(parsed_val)


if __name__ == "__main__":
    get_min_max_amount_of_commits()