digits = {
    "0": "۰",
    "1": "۱",
    "2": "۲",
    "3": "۳",
    "4": "۴",
    "5": "۵",
    "6": "۶",
    "7": "۷",
    "8": "۸",
    "9": "۹",
}


def convert_digits(x: str) -> str:
    """
    Convert english digits to persian digits.
    :param x: string with english digits
    :return: string with persian digits
    """
    trans = str.maketrans(digits)

    if not isinstance(x, str):
        raise Exception("x is not string")
    return x.translate(trans)
