from collections import defaultdict
import csv
import os
from urllib.request import urlretrieve

TMP = os.getenv("TMP", "/tmp")
DATA = 'battle-table.csv'
BATTLE_DATA = os.path.join(TMP, DATA)
if not os.path.isfile(BATTLE_DATA):
    urlretrieve(
        f'https://bites-data.s3.us-east-2.amazonaws.com/{DATA}',
        BATTLE_DATA
    )


def _create_defeat_mapping():
    """Parse battle-table.csv building up a defeat_mapping dict
       with keys = attackers / values = who they defeat.
    """
    mapping = defaultdict(list)
    with open(BATTLE_DATA) as bats:
        data = csv.DictReader(bats)
        for row in data:
            attacker = row['Attacker']
            for k, v in row.items():
                if k != 'Attacker' and v == 'win':
                    mapping[attacker].append(k)
    return mapping


def get_winner(player1, player2, defeat_mapping=None):
    """Given player1 and player2 determine game output returning the
       appropriate string:
       Tie
       Player1
       Player2
       (where Player1 and Player2 are the names passed in)

       Raise a ValueError if invalid player strings are passed in.
    """
    defeat_mapping = defeat_mapping or _create_defeat_mapping()
    if player1 not in defeat_mapping.keys() or player2 not in defeat_mapping.keys():
        raise ValueError
    if player1 == player2:
        return 'Tie'
    elif player2 in defeat_mapping[player1]:
        return player1
    return player2