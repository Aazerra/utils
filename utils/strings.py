from typing import Union


def is_null_or_empty(string: Union[str, None]) -> bool:
    """
    Is checking string is none or empty
    :param string:
    :return: bool
    """
    return string is None or string == ""


def translate(x: str, d: dict) -> str:
    """
    Convert english digits to persian digits.
    :param x: string to translate
    :param d: dict for using on translate
    :return: translated string
    """
    if not isinstance(x, str):
        raise TypeError("x is not string")
    if not isinstance(d, dict):
        raise TypeError("d is not dict")

    trans = str.maketrans(d)
    return x.translate(trans)
