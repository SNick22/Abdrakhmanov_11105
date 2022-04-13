# variant 1
from functools import reduce

fib_gen = lambda n: fib_gen(n - 2) + fib_gen(n - 1) if n > 2 else 1 if n > 0 else 0
fib_list = lambda n: [fib_gen(i) for i in range(n)]
number_len = lambda x: number_len(x // 10) + 1 if x // 10 > 0 else 1
fib_sum = lambda n: reduce(lambda a, b: a + b ** number_len(b), fib_list(n)) if n > 0 else 0


if __name__ == '__main__':
    print(fib_list(10))
    print(fib_sum(8))
