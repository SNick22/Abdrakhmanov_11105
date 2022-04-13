# variant 2
import re


def find_start_011(string):
    return re.findall(r'\b011\d*\b', string)


def find_010(string):
    return re.findall(r'\b\d*010\d*\b', string)


def find_00_and_11(string: str):
    return re.findall(r"\b\d*(?:00\d*11)|(?:11\d*00)\d*\b", string)


if __name__ == '__main__':
    print(find_start_011('011000, 1111, 000, 011, 011111'))
    print(find_010('011000, 1111, 000, 011, 011111 010 0000010000 1111010000 01000'))
    print(find_00_and_11('01101100011 1111111 000000 10010101011 01 011 11111011 1 11 1100 0011'))
