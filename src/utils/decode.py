from base64 import b64decode


def b64_decode(string):
    return b64decode(string).decode("utf-8")
