from itertools import chain


def chunks(arr, n=2):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(arr), n):
        yield arr[i:i + n]


def flatten(arr):
    """Flatten a array"""
    result = []
    for item in arr:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result
