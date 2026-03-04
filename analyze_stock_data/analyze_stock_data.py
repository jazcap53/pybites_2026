from collections import defaultdict
import requests

STOCK_DATA = 'https://bites-data.s3.us-east-2.amazonaws.com/stocks.json'

# pre-work: load JSON data into program

with requests.Session() as s:
    data = s.get(STOCK_DATA).json()


# your turn:
def _cap_str_to_mln_float(cap):
    """If cap = 'n/a' return 0, else:
       - strip off leading '$',
       - if 'M' in cap value, strip it off and return value as float,
       - if 'B', strip it off, multiply by 1,000 and return
         value as float"""
    if cap == 'n/a':
        return 0
    cap = cap.lstrip('$')
    if cap.endswith('M'):
        return float(cap.rstrip('M'))
    return 1000.0 * float(cap.rstrip('B'))


def get_industry_cap(industry):
    """Return the sum of all cap values for given industry, use
       the _cap_str_to_mln_float to parse the cap values,
       return a float with 2 digit precision"""
    industry_sum = 0.0
    for listing in data:
        if listing['industry'] == industry:
            industry_sum += _cap_str_to_mln_float(listing['cap'])
    return round(industry_sum, 2)

def get_stock_symbol_with_highest_cap():
    """Return the stock symbol (e.g. PACD) with the highest cap, use
       the _cap_str_to_mln_float to parse the cap values"""
    max_cap = 0.0
    max_symbol = ''

    for listing in data:
        cap_mln = _cap_str_to_mln_float(listing['cap'])
        if cap_mln > max_cap:
            max_cap = cap_mln
            max_symbol = listing['symbol']

    return max_symbol


def get_sectors_with_max_and_min_stocks():
    """Return a tuple of the sectors with most and least stocks,
       discard n/a"""
    sector_counts = defaultdict(int)
    for listing in data:
        if listing['sector'] != 'n/a':
            sector_counts[listing['sector']] += 1
    sector_count_tuples = sorted(sector_counts.items(), key=lambda x: x[1], reverse=True)
    return sector_count_tuples[0][0], sector_count_tuples[-1][0]
