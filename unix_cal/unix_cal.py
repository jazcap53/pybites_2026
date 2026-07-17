from calendar import firstweekday

DAY_START = 0
DAY_END = 21


def get_weekdays(calendar_output):
    """Receives a multiline Unix cal output and returns a mapping (dict) where
       keys are int days and values are the 2 letter weekdays (Su Mo Tu ...)"""
    weekdays = ['Su', 'Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa']
    dates = calendar_output.splitlines()[2:]  # ignore the header
    dates[-1] = dates[-1].ljust(DAY_END)  # append spaces to last week if needed
    print(f'weekdays is {weekdays}')
    print(f'dates is {dates}')
    text_date_index = dates[0].find('1')
    text_date_offset = (text_date_index - 1) // 3
    ret = {}
    for i in range(len(dates)):
        for j in range(DAY_START, DAY_END, 3):
            text_date = dates[i][j] + dates[i][j+1]
            if text_date != '  ':
                ret[int(text_date)] = weekdays[(text_date_offset + int(text_date) - 1) % 7 ]
    print(calendar_output)
    print(f'ret is {ret}')
    return ret


if __name__ == '__main__':
    calendar_output = april_1981 = """     April 1981
Su Mo Tu We Th Fr Sa
          1  2  3  4
 5  6  7  8  9 10 11
12 13 14 15 16 17 18
19 20 21 22 23 24 25
26 27 28 29 30
"""

    get_weekdays(calendar_output)