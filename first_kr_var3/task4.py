# variant 3
import re


def find_00start_11end(string):
    return re.findall(r'\b00[01]*11\b', string)


def find_01(string):
    return re.findall(r'\b[01]*01[01]*\b', string)


def find_00_and_11(string: str):
    return re.findall(r"\b\d*(?:00\d*11)|(?:11\d*00)\d*\b", string)


if __name__ == '__main__':
    print(find_00start_11end('0011 1100 00111101010111 000001111'))
    print(find_01('0011 1100 00000 1111 010101 00111101010111 000001111'))
    print(find_00_and_11('0011 1100 00000 1111 010101 00111101010111 000001111'))
