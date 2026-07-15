from itertools import zip_longest
from textwrap import wrap
import re



COL_WIDTH = 20


def text_to_columns(text):
    """Split text (input arg) to columns, the amount of double
       newlines (\n\n) in text determines the amount of columns.
       Return a string with the column output like:
       line1\nline2\nline3\n ... etc ...
       See also the tests for more info."""
    n_cols = text.count('\n\n') + 1
    print(f'n_cols is {n_cols}')

    buffer = [column.strip() for column in text.split('\n\n')]
    # columns = text.split('\n\n')
    # columns = [col.strip() for col in columns]
    # print(f'columns is {columns}')
    print(f'buffer is {buffer}')
    if len(buffer) != n_cols:
        raise ValueError
    for i, col in enumerate(buffer):
        buffer[i] = wrap(buffer[i], COL_WIDTH)
    print(f'buffer is now {buffer}')
    intermediate = zip_longest(buffer)
    for line in  intermediate:
        print(*line)


if __name__ == '__main__':
    my_lines = text_to_columns("""My house is small but cosy.

    It has a white kitchen and an empty fridge.""")
    print(f'the type of my_lines is {type(my_lines)}')

    for line in my_lines:
        print(line)