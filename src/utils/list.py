from itertools import chain


def chunks(arr, n=2):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(arr), n):
        yield arr[i:i + n]


def flatten(arr):
    return list(chain(*arr))
