from collections import Counter
import os
from curses.ascii import isdigit
from urllib.request import urlretrieve
from dateutil.parser import parse

commits = os.path.join(os.getenv("TMP", "/tmp"), "commits")
urlretrieve("https://bites-data.s3.us-east-2.amazonaws.com/git_log_stat.out", commits)

# you can use this constant as key to the yyyymm:count dict
YEAR_MONTH = "{y}-{m:02d}"


def parse_changes(changes: str):
    change_line = changes.split(',')
    ct_insertions = change_count(change_line[1])
    ct_deletions = change_count(change_line[2], False) if len(change_line) > 2 else 0
    return ct_insertions + ct_deletions


def change_count(segment: str, insertions:bool =True):
    segment = segment.lstrip()
    ret = int(segment[0])
    for i in range(1, len(segment)):
        if not isdigit(segment[i]):
            break
        ret = 10 * ret + int(segment[i])
    return ret


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
    ctr = Counter()
    with open(commit_log) as logfile:
        for line in logfile.readlines():
            line_list = line.rstrip('\n').split('|')
            dt_parsed = parse(line_list[0], fuzzy=True)
            if year is not None and dt_parsed.year != year:
                continue
            ctr_key = f'{dt_parsed.year:4d}-{dt_parsed.month:02d}'
            ctr[ctr_key] += parse_changes(line_list[1])
    return ctr.most_common()[-1][0], ctr.most_common()[0][0]