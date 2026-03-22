from collections import namedtuple, defaultdict
from datetime import date
import os

import numpy as np
import pandas as pd
import requests




DATA_FILE = "https://bites-data.s3.us-east-2.amazonaws.com/weather-ann-arbor.csv"
STATION = namedtuple("Station", "ID Date Value")


def high_low_record_breakers_for_2015():
    """Extract the high and low record breaking temperatures for 2015

    The expected value will be a tuple with the highest and lowest record
    breaking temperatures for 2015 as compared to the temperature data
    provided.

    NOTE:
    The date values should not have any timestamps, should be a
    datetime.date() object. The temperatures in the dataset are in tenths
    of degrees Celsius, so you must divide them by 10

    Possible way to tackle this challenge:

    1. Create a DataFrame from the DATA_FILE dataset.

    2. Manipulate the data to extract the following:
       * Extract highest temperatures for each day / station pair between 2005-2015
       * Extract lowest temperatures for each  day / station  between 2005-2015
       * Remove February 29th from the dataset to work with only 365 days

    3. Separate data into two separate DataFrames:
       * high/low temperatures between 2005-2014
       * high/low temperatures for 2015

    4. Iterate over the 2005-2014 data and compare to the 2015 data:
       * For any temperature that is higher/lower in 2015 extract ID,
         Date, Value

    5. From the record breakers in 2015, extract the high/low of all the
       temperatures
       * Return those as STATION namedtuples, (high_2015, low_2015)
    """
    record_highs_by_date = defaultdict(list)
    record_lows_by_date = defaultdict(list)
    r = requests.get(f'{DATA_FILE}')
    weather_data = pd.read_csv(DATA_FILE)
    print(f'len(weather_data is {len(weather_data)}  type(weather_data) is {type(weather_data)}')
    print(f'df.shape is {weather_data.shape}')
    data_value_min = np.iinfo(np.int64).max
    data_value_max = np.iinfo(np.int64).min
    min_station = STATION('', '', 0)
    max_station = STATION('', '', 0)

    # for i in range(1, len(weather_data)):
        # station_info = weather_data.iloc[i]
    for i in range(1, len(weather_data)):

        if i < 3:
            print(weather_data.iloc[i])
            print()
        # elif not i % 10000:
        #     print(i)

        id = weather_data.iloc[i]['ID']
        date = weather_data.iloc[i]['Date']
        element = weather_data.iloc[i]['Element']
        data_value = weather_data.iloc[i]['Data_Value']
        # print(f'type(id) is {type(id)}  type(date) is {type(date)}  type(element) is {type(element)}  '
        #       f'type(data_value) is {type(data_value)}')
        # if date.startswith('2015'):
        #     continue  # for now

    return 42


if __name__ == '__main__':
    print(high_low_record_breakers_for_2015())