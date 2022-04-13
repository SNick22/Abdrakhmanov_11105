# variant 2
fact = lambda x: fact(x - 1) * x if x > 1 else 1
fact_list = lambda n: [fact(i) for i in range(1, n)]
fact_sqrt = lambda n: map(lambda x: x**0.5, fact_list(n))


if __name__ == '__main__':
    print(fact_list(8))
    print([i for i in fact_sqrt(8)])
