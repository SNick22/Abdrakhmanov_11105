# variant 1
import re


def find_001_end(string: str):
    return re.findall(r'\b\d*011\b', string)


def find_11(string: str):
    return re.findall(r'\b\d*11\d*\b', string)


def find_00_and_11(string: str):
    return re.findall(r'\b\d*(?:00\d*11)|(?:11\d*00)\d*\b', string)


if __name__ == '__main__':
    print(find_001_end('01101100011 1111111 000000 10010101011 01 011 11111011'))
    print(find_11('01101100011 1111111 000000 10010101011 01 011 11111011 1 11'))
    print(find_00_and_11('01101100011 1111111 000000 10010101011 01 011 11111011 1 11 1100 0011'))
