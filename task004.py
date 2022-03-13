from functools import reduce
words = input().split()


def check(wrd):
    letters = []
    for i in wrd:
        if i.upper() not in letters:
            letters.append(i.upper())
    if len(letters) > 3:
        return True
    return False


if __name__ == '__main__':
    filtred_words = list(filter(check, words))
    print(list(map(lambda x: x[0].swapcase() + x[1:], filtred_words)))
    filtred_words_1 = list(filter(lambda x: 'foo' in x, words))
    print(reduce(lambda x, y: len(x) + len(y), filtred_words_1))
