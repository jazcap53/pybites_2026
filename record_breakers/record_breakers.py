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
    station_record_highs_by_day = defaultdict(dict)
    station_record_lows_by_day = defaultdict(dict)
    hi_data = []
    lo_data = []
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
                    # print(weather_data)
                    # print(f'len(weather_data) is {len(weather_data)}  type(weather_data) is {type(weather_data)}')
                    station_id, reading_date, element, data_value = weather_data.split(',')
                    day = reading_date[5:]
                    if element == 'TMAX':
                        replaced = False
                        this_days_hi = {day: STATION(station_id, reading_date, data_value)}
                        for list_item in hi_data:
                            if replaced:
                                break
                            item_key = next(iter(list_item.keys()))
                            if day == item_key and list_item[item_key].Value < data_value:
                            # if day in hi_data and hi_data[day][data_value] < data_value:
                                list_item[item_key][data_value] = data_value
                                # hi_data[day][data_value] = data_value
                                replaced = True
                        if not replaced:
                            hi_data.append(this_days_hi)
                    elif element == 'TMIN':
                        replaced = False
                        this_days_lo = {day: STATION(station_id, reading_date, data_value)}
                        for list_item in lo_data:
                            if replaced:
                                break
                            item_key = next(iter(list_item.keys()))
                            if day == item_key and list_item[item_key].Value > data_value:
                                list_item[item_key][data_value] = data_value
                                replaced = True
                        if not replaced:
                            lo_data.append(this_days_lo)
                    else:
                        raise ValueError('ValueError: element not TMAX or TMIN')
                    # print(f'id is {id}, day is {day}, date is {date}, element is {element}, '
                    #       f'data_value is {data_value}')
                    # if element == 'TMAX':
                    #     if station_record_highs_by_day[day] == {}:  # we have no data for 'day'
                    #         station_record_highs_by_day[day] = {id: data_value}
                    #     else:
                    #         # if we have data for today for this station
                    #         if station_record_highs_by_day[day].get(id) is not None:
                    #             high_temp_so_far = station_record_highs_by_day[day][id]
                    #             if data_value > high_temp_so_far:
                    #                 station_record_highs_by_day[day][id] = data_value
                    # elif element == 'TMIN':
                    #     if station_record_lows_by_day[day] == {}:  # we have no data for 'day'
                    #         station_record_lows_by_day[day] = {id: data_value}
                    #     else:
                    #         # if we have data for today for this station
                    #         if station_record_lows_by_day[day].get(id) is not None:
                    #             low_temp_so_far = station_record_lows_by_day[day][id]
                    #             if data_value < low_temp_so_far:
                    #                 station_record_lows_by_day[day][id] = data_value
                    # else:
                    #     raise ValueError('ValueError: element not TMAX or TMIN')

    except requests.exceptions.RequestException as e:
        print(f'An error occurred: {e}')

    # return station_record_highs_by_day, station_record_lows_by_day
    return hi_data, lo_data


if __name__ == '__main__':
    hi, lo = high_low_record_breakers_for_2015()
    print(sorted(hi.items(), key=lambda item: item[0]))
    print(sorted(lo.items(), key=lambda item: item[0]))