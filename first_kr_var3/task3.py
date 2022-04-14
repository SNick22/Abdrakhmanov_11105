# variant 3
def s1_letters(st1):
    while True:
        for i in st1:
            yield i


def s2_letters(st2):
    while True:
        for i in st2:
            yield i


def gen(st1, st2):
    gen_st1 = s1_letters(st1)
    gen_st2 = s2_letters(st2)
    while True:
        yield next(gen_st1)
        yield next(gen_st2)


if __name__ == '__main__':
    generate = gen('summer', 'fall')
    print(next(generate))
    print(next(generate))
    print(next(generate))
    print(next(generate))
    print(next(generate))
    print(next(generate))
    print(next(generate))
    print(next(generate))
    print(next(generate))
    print(next(generate))
    print(next(generate))
    print(next(generate))
    print(next(generate))
