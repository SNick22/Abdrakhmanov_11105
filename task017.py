import re
from task019 import text


def find_017(string):
    return re.findall(r'\b[А-ЯЁ]{2,}\s[А-ЯЁ]+|[А-ЯЁ]{2,}\b', string)


if __name__ == '__main__':
    for string in text:
        if find_017(string):
            print(find_017(string))
