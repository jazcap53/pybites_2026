import re


def strip_comments(code):
    # see Bite description
    ret_str = ''
    lines = code.splitlines()

    three_q_pos = None
    for line_num in range(len(lines)):
        current_line = lines[line_num]
        if three_q_pos is None:  # we've not seen triple quotes
            open_3q_pos = current_line.find('"""')
            if open_3q_pos == -1:
                ret_str += edited_line(lines[line_num])  # process the line
            else:
                three_q_pos = open_3q_pos
        else:  # we're looking for second triple quote of pair
            close_3q_pos = current_line.rfind('"""')
            if close_3q_pos == -1:
                continue  # skip this line
            else:  # we've found the second triple quote
                three_q_pos = None  # reset
                continue  # skip this line
    return ret_str.rstrip('\n')


def edited_line(line: str):
    return line + '\n'
    looking_for = "\"'#"
    open_single_quote_at = None
    close_single_quote_at = None
    return_str = ''
    hash_at = None
    for ix, ch in enumerate(line):
        if ch in looking_for:
            if ch == '\'':
                if open_single_quote_at is None:
                    open_single_quote_at = ix
                else:
                    close_single_quote_at = ix
            elif ch == '#':
                if open_single_quote_at is not None and close_single_quote_at is None:
                    continue  # hash is inside single quotes: ignore it
                else:
                    hash_at = ix
                    return_str = line[: hash_at - 2]
                    break
            elif ch == '"':
                pass

        if return_str:
            break
    return return_str


if __name__ == '__main__':
    multiline_docstring = '''
    def __init__(self, name, sound, num_legs):
        """
        Parameters
        ----------
        name : str
            The name of the animal
        sound : str
            The sound the animal makes
        num_legs : int, optional
            The number of legs the animal (default is 4)
        """
        self.name = name
        self.sound = sound
        self.num_legs = num_legs
    '''
    multiline_docstring_after_strip = '''
    def __init__(self, name, sound, num_legs):
        self.name = name
        self.sound = sound
        self.num_legs = num_legs
    '''
    after_strip = strip_comments(multiline_docstring)
    if after_strip != multiline_docstring_after_strip:
        print(f'actual:\n{after_strip}\n\nexpected:\n{multiline_docstring_after_strip}')
    else:
        print("success on test 3")
    class_with_method = '''
    class SimpleClass:
        """Class docstrings go here."""

        def say_hello(self, name: str):
            """Class method docstrings go here."""
            print(f'Hello {name}')
    '''
    class_with_method_after_strip = '''
    class SimpleClass:

        def say_hello(self, name: str):
            print(f'Hello {name}')
    '''
    after_strip = strip_comments(class_with_method)
    if after_strip != class_with_method_after_strip:
        print(f'actual:\n{after_strip}\n\nexpected:\n{class_with_method_after_strip}')
    else:
        print("success on test 2")