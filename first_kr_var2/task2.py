# variant 2
class MyIterator:
    def __init__(self, st: str, n: int):
        self.st = st
        self.n = n

    def __iter__(self):
        vowels = "aeiou"
        vowels_letters = []
        for i in self.st:
            if i in vowels:
                vowels_letters.append(i)
        while self.n > 0:
            for i in vowels_letters:
                if self.n == 0:
                    break
                yield i
                self.n -= 1


if __name__ == '__main__':
    for i in MyIterator('spider-man', 20):
        print(i)
    a = iter(MyIterator('spider-man', 20))
    print('----')
    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))
