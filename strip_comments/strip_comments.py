import re


def strip_comments(code):
    # see Bite description

    lines = code.splitlines()


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

                single_quote_pos = ix

