import itertools
from typing import Generator
from itertools import islice


def chunks(arr: list, n: int) -> Generator:
    """
    Yield successive n-sized chunks from arr.
    :param arr
    :param n
    :return generator
    """
    for i in range(0, len(arr), n):
        yield arr[i:i + n]


def take(arr: list, n: int):
    """
    Returns n element of the arr.
    :param arr:
    :param n:
    :return: list of n element
    """
    return list(islice(arr, n))


def sublists(arr: list, *n) -> list:
    """
    Returns a list with sublists with length specified in n
    :param arr:
    :param n:
    :return list:
    """
    arr = iter(arr)
    return [list(islice(arr, x)) for x in n]


def flatten(arr: list) -> list:
    """
    Returns flatten list
    :param arr:
    :return:
    """
    return list(itertools.chain(*arr))
