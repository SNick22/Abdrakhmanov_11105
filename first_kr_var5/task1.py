# variant 5
from functools import reduce

string_list = lambda x: map(lambda y: str(y), x)
string = lambda x: reduce(lambda a, b: a + b, string_list(x))
intlist = lambda x: map(lambda a: int(a), x)
list_div3 = lambda x: list(filter(lambda a: a % 3 == 0, intlist(x)))

if __name__ == '__main__':
    print(string([1, 2, 3, 4, 5]))
    print(list_div3('123456'))
