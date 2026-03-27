from collections import namedtuple, defaultdict
from datetime import date
import os

import numpy as np
import pandas as pd
import requests

DATA_FILE = "https://bites-data.s3.us-east-2.amazonaws.com/weather-ann-arbor.csv"
STATION = namedtuple("Station", "ID Date Value")

# def _place_in_records(weather_data: str):



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
    ten_year_station_record_highs_by_day = defaultdict(list)  # [tuple])
    ten_year_station_record_lows_by_day = defaultdict(list)  # [tuple])
    latest_station_record_highs_by_day = defaultdict(list)  # [tuple])
    latest_station_record_lows_by_day = defaultdict(list)  # [tuple])
    try:
        with requests.get(f'{DATA_FILE}', stream=True) as r:
            # r = requests.get(f'{DATA_FILE}')
            r.raise_for_status()

            is_header_line = True
            for line in r.iter_lines():
                if is_header_line:
                    # print(line)
                    # print(f'len(line) is {len(line)}  type(line) is {type(line)}')
                    is_header_line = False
                    continue
                else:
                    weather_data = line.decode('utf-8')  # pd.read_csv(DATA_FILE)
                    station_id, observed_date, element, data_value = weather_data.split(',')
                    observed_day = observed_date[5:]
                    observed_year = observed_date.lstrip()[:4]
                    if observed_day == '02-29':
                        continue
                    observation = (station_id, observed_date, data_value)
                    if element == 'TMAX':# print(f'id is {id}, day is {day}, date is {date}, element is {element}, '
                        if observed_year != '2015':
                            ten_year_station_record_highs_by_day[observed_day].append(observation)
                        else:
                            if latest_station_record_highs_by_day.get(observed_day) is None:
                                latest_station_record_highs_by_day[observed_day].append(observation)
                            else:
                                if float(data_value) > float(latest_station_record_highs_by_day[observed_day][0][2]):
                                    latest_station_record_highs_by_day[observed_day] = [observation]
                                else:
                                    pass
                    elif element == 'TMIN':
                        # observation = STATION(station_id, observed_date, data_value)
                        if observed_year != '2015':
                            ten_year_station_record_lows_by_day[observed_day].append(observation)
                        else:
                            latest_station_record_lows_by_day[observed_day].append(observation)
                    else:
                        raise ValueError('ValueError: element not TMAX or TMIN')

    except requests.exceptions.RequestException as e:
        print(f'An error occurred: {e}')

    best_hi_day = ''
    best_hi_id = ''
    best_hi_date = ''
    best_hi_temp = float('-inf')
    best_lo_day = ''
    best_lo_id = ''
    best_lo_date = ''
    best_lo_temp = float('inf')
    for k, v in latest_station_record_highs_by_day.items():
        if float(v[0][2]) > best_hi_temp:  # v[0][2] is a temperature in tenths of a degree Celsus
            best_hi_day = k
            best_hi_id = v[0][0]
            best_hi_date = v[0][1]
            best_hi_temp = float(v[0][2])
    for k, v in latest_station_record_lows_by_day.items():
        if float(v[0][2]) > best_lo_temp:  # v[0][2] is a temperature in tenths of a degree Celsus
            best_lo_day = k
            best_lo_id = v[0][0]
            best_lo_date = v[0][1]
            best_lo_temp = float(v[0][2])

    hi_named_tuple = STATION(best_hi_id, best_hi_date, best_hi_temp)
    lo_named_tuple = STATION(best_lo_id, best_lo_date, best_lo_temp)


    return hi_named_tuple, lo_named_tuple


if __name__ == '__main__':
    hi, lo = high_low_record_breakers_for_2015()
    print(hi)
    print(lo)