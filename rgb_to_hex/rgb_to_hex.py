def rgb_to_hex(rgb):
    """Receives (r, g, b)  tuple, checks if each rgb int is within RGB
       boundaries (0, 255) and returns its converted hex, for example:
       Silver: input tuple = (192,192,192) -> output hex str = #C0C0C0"""
    try:
        for v in rgb:
            assert 0 <= v <= 255
    except:
        raise ValueError("value out of range")
    return '#' + '{:0>2X}{:0>2X}{:0>2X}'.format(*rgb)