import re


def strip_comments(code):
    # see Bite description
    ret_str = ''
    lines = code.splitlines()

    for line_num in range(len(lines)):
        three_q_pos = None
        current_line = lines[line_num]
        if three_q_pos is None:  # we've seen no triple quotes
            open_3q_pos = current_line.find('"""')
            if open_3q_pos == -1:
                ret_str += edited_line(lines[line_num])  # process the line
            else:
                three_q_pos =  open_3q_pos
        else:  # we're looking for second triple quote of pair
            close_3q_pos = current_line.rfind('"""')
            if close_3q_pos == -1:
                continue  # skip this line
            else:
                three_q_pos = None  # reset
                continue  # skip this line
    return ret_str






def edited_line(line: str):
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


