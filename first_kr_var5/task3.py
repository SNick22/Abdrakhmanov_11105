# variant 5
def generator(st: str):
    while True:
        yield ' '
        for i in range(len(st)):
            yield st[:i+1]


if __name__ == '__main__':
    gen = generator('General')
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
