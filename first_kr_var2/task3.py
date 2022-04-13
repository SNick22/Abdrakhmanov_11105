# variant 2
def generate(st: str):
    reversed_st = st[::-1]
    while True:
        for i in st:
            yield i
        for i in reversed_st:
            yield i


if __name__ == '__main__':
    gen = generate('string')
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
