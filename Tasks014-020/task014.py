import re


def find_014(string):
    return re.findall(r"\ba+[^b]\b", string)


if __name__ == '__main__':
    print(find_014('aaab aaaac aaad ae ad b aed'))
