import re


def find_015(string):
    return re.findall(r"\ba(?:a{2})*(?:c{0}|c{3}|c{5})(?:b{2})+\b", string)


if __name__ == '__main__':
    print(find_015('b a ab aaabbb aaacccbbbb aaaccccbbbb aaacccccbb aaaabb aaaaabb'))
