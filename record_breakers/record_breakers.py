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
    try:
        with requests.get(f'{DATA_FILE}', stream=True) as r:
            # r = requests.get(f'{DATA_FILE}')
            r.raise_for_status()

            is_header_line = True
            for line in r.iter_lines():
                if is_header_line:
                    print(line)
                    print(f'len(line) is {len(line)}  type(line) is {type(line)}')
                    is_header_line = False
                    continue
                else:
                    weather_data = line.decode('utf-8')  # pd.read_csv(DATA_FILE)
                    print(weather_data)
                    print(f'len(weather_data) is {len(weather_data)}  type(weather_data) is {type(weather_data)}')
                    id, date, element, data_value = weather_data.split(',')
                    day = date[5:]
                    print(f'id is {id}, day is {day}, date is {date}, element is {element}, '
                          f'data_value is {data_value}')
                    if element == 'TMAX':
                        if station_record_highs_by_day[day] is not None:
                            if station_record_highs_by_day[day].get(id) is not None:
                                record_high_so_far = station_record_highs_by_day[day].get(id).get(data_value)
                                if record_high_so_far and data_value > record_high_so_far:
                                    pass
                    return station_record_highs_by_day['04-10'], station_record_lows_by_day['04-10']
                # print(f'df.shape is {weather_data.shape}')
                # data_value_min = np.iinfo(np.int64).max
                # data_value_max = np.iinfo(np.int64).min
                data_value_min = float('inf')
                data_value_max = float('-inf')
                min_station = STATION('', '', 0)
                max_station = STATION('', '', 0)

                # for i in range(1, len(weather_data)):
                    # station_info = weather_data.iloc[i]
                for i in range(1, len(weather_data)):

                    if i < 3:
                        # print(weather_data.iloc[i])
                        print(weather_data)
                        print()
                    elif not i % 10000:
                        print(i)

                    # id = weather_data.iloc[i]['ID']
                    # date = weather_data.iloc[i]['Date']
                    # day = date[5:]
                    # element = weather_data.iloc[i]['Element']
                    # data_value = float(weather_data.iloc[i]['Data_Value'])/10.0
                    # print(f'type(id) is {type(id)}  type(date) is {type(date)}  type(element) is {type(element)}  '
                    #       f'type(data_value) is {type(data_value)}')
                    if date.startswith('2015'):
                        continue  # for now
                    if element == 'TMAX':
                        if (day not in station_record_highs_by_day.keys() or
                                id not in station_record_highs_by_day[day] or
                                data_value > station_record_highs_by_day[day][id].Value):
                            station_record_highs_by_day[day][id] = STATION(id, date, data_value)
                    elif element == 'TMIN':
                        if (day not in station_record_lows_by_day.keys() or
                                id not in station_record_lows_by_day[day] or
                                data_value < station_record_lows_by_day[day][id].Value):
                            station_record_lows_by_day[day][id] = STATION(id, date, data_value)
                    else:
                        continue
    except requests.exceptions.RequestException as e:
        print(f'An error occurred: {e}')

    return station_record_highs_by_day['04-10'], station_record_lows_by_day['04-10']


if __name__ == '__main__':
    print(high_low_record_breakers_for_2015())