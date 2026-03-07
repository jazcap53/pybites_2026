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

    with open(xml) as xml_file:
        xml_data = xml_file.read()
    root = ET.fromstring(xml_data)
    print(root.tag)
    print(root.attrib)
    for child in root:
        print(child.attrib)
        print(child[1].text)
        print(child[4].text)




if __name__ == '__main__':
    get_income_distribution()