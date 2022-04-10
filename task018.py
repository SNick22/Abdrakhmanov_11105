import re
from task019 import text


def find_018(string):
    return re.findall(r'', string)


if __name__ == '__main__':
    for string in text:
        if find_018(string):
            print(find_018(string))
