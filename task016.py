import re
from task019 import text


def find_016(string):
    return re.findall(r"\b(?:[01]\d|2[0-3]):[0-5]\d\b", string)


if __name__ == '__main__':
    for string in text:
        if find_016(string):
            print(find_016(string))
