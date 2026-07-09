import string

def filter_accents(text):
    """Return a sequence of accented characters found in
       the passed in lowercased text string
    """
    return sorted(list(set(c.lower() for c in text if c not in string.ascii_letters and c not in string.whitespace
               and c not in string.punctuation and c not in string.digits)))