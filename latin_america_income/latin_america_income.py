import os
from collections import defaultdict
from pathlib import Path
from urllib.request import urlretrieve
import xml.etree.ElementTree as ET

# import the countries xml file
tmp = Path(os.getenv("TMP", "/tmp"))
countries = tmp / 'countries.xml'

if not countries.exists():
    urlretrieve(
        'https://bites-data.s3.us-east-2.amazonaws.com/countries.xml',
        countries
    )


def get_income_distribution(xml=countries):
    """
    - Read in the countries xml as stored in countries variable.
    - Parse the XML
    - Return a dict of:
      - keys = incomes (wb:incomeLevel)
      - values = list of country names (wb:name)
    """
    latin_dd = defaultdict(list)

    tree = ET.parse(xml)
    root = tree.getroot()
    for child in root:
        latin_dd[child[4].text].append(child[1].text)
    return latin_dd


if __name__ == '__main__':
    print(get_income_distribution())