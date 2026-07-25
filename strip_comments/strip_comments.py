import re


def strip_comments(code):
    # see Bite description
    ret_str = ''
    lines = code.splitlines()

    # left_3q_posn = right_3q_posn = None
    in_docstring = False
    for line_num in range(len(lines)):
        current_line = lines[line_num]

        if not in_docstring:
            left_3q_posn = find_left_triple_quote_at(current_line)
            if left_3q_posn == -1:
                left_3q_posn = None
                ret_str += edited_line(current_line)  # process the line
            # found left, look for right on same line
            elif (right_3q_posn := find_right_triple_quote_at(current_line)) > left_3q_posn:
                left_3q_posn = right_3q_posn = None
                in_docstring = False  # found both 3q's in this line
            else:
                right_3q_posn = None
                in_docstring = True
        else:  # if we're in a docstring
            if (right_3q_posn := find_right_triple_quote_at(current_line)) > -1:
                left_3q_posn = right_3q_posn = None
                in_docstring = False

    return ret_str.rstrip('\n')


def find_left_triple_quote_at(line):
    return line.find('"""')

def find_right_triple_quote_at(line):
    return line.rfind('"""')



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