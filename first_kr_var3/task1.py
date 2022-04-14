# variant 3
from functools import reduce

leo = lambda x: 1 if x == 1 or x == 2 else leo(x - 1) + leo(x - 2) + 1
leo_list = lambda n: [leo(i) for i in range(1, n+1)]
sum_leo_div3 = lambda n: reduce(lambda a, b: a + b, filter(lambda x: x % 3 == 0, leo_list(n)))

if __name__ == '__main__':
    print(leo_list(20))
    print(sum_leo_div3(6))
