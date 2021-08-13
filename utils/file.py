import os


def filext(path: str) -> str:
    """
    Return the file extension.
    If file has not extension, return empty string.
    :return str
    """
    return os.path.splitext(os.path.basename(path))[1]


def filename(path: str):
    """
    Return the filename without extension.
    :return str
    """
    return os.path.splitext(os.path.basename(path))[0]
