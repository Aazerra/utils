charmap_ar_to_fa = {
    "ي": "ی",
    "ك": "ک",
}
charmap_fa_to_ar = {"ی": "ي", "ک": "ك"}


def ar_to_fa(x: str) -> str:
    """
    Convert Arabic characters to Persian
    :param x: A string, will be converted
    :return:
    """

    trans = str.maketrans(charmap_ar_to_fa)

    return x.translate(trans)


def fa_to_ar(x: str) -> str:
    """
    Convert Persian characters to Arabic
    :param x: A string, will be converted
    :rtype: str
    """

    trans = str.maketrans(charmap_fa_to_ar)

    return x.translate(trans)
