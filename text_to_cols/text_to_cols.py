from itertools import zip_longest
import textwrap


COL_WIDTH = 20

def text_to_columns(text):
    """Split text (input arg) to columns, the amount of double
       newlines (\n\n) in text determines the amount of columns.
       Return a string with the column output like:
       line1\nline2\nline3\n ... etc ...
       See also the tests for more info."""
    n_cols = text.count('\n\n') + 1

    buffer = [column.strip() for column in text.split('\n\n')]
    if len(buffer) != n_cols:
        raise ValueError
    buffer = [textwrap.wrap(buffer_item, COL_WIDTH) for buffer_item in buffer]
    zipped = zip_longest(*buffer, fillvalue=' '*COL_WIDTH)
    buffer = [inner_item.ljust(COL_WIDTH, ' ') + '    ' for outer_item in zipped for inner_item in outer_item]
    buffer = ''.join(buffer)
    return buffer


if __name__ == '__main__':
    my_lines = text_to_columns("""My house is small but cosy.

    It has a white kitchen and an empty fridge.""")
    # print(f'the type of my_lines is {type(my_lines)}')

    for line in my_lines:
        print(line, end='')