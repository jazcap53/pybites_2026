from collections import defaultdict
from datetime import date
from typing import Dict, Sequence, NamedTuple


class MovieRented(NamedTuple):
    title: str
    price: int
    date: date


RentingHistory = Sequence[MovieRented]
STREAMING_COST_PER_MONTH = 12
STREAM, RENT = 'stream', 'rent'


def stringify(date):
    return f'{date.year:4d}-{date.month:2d}'


def rent_or_stream(
    renting_history: RentingHistory,
    streaming_cost_per_month: int = STREAMING_COST_PER_MONTH
) -> Dict[str, str]:
    """Function that calculates if renting movies one by one is
       cheaper than streaming movies by months.

       Determine this PER MONTH for the movies in renting_history.

       Return a dict of:
       keys = months (YYYY-MM)
       values = 'rent' or 'stream' based on what is cheaper

       Check out the tests for examples.
    """
    tally_dict = defaultdict(int)
    for rental in renting_history:
        tally_dict[stringify(rental.date)] += rental.price
    result_dict = {}
    for k in sorted(tally_dict.keys()):
        if tally_dict[k] <= 12:
            result_dict[k] = 'rent'
        else:
            result_dict[k] = 'stream'
    return result_dict
