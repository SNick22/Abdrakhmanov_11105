# variant 3
class MyIterator:
    def __init__(self, st, n):
        self.st = st
        self.n = n

    def __iter__(self):
        reversed_st = self.st[::-1]
        while self.n > 0:
            for i in self.st:
                if self.n == 0:
                    break
                yield i
                self.n -= 1
            for i in reversed_st:
                if self.n == 0:
                    break
                yield i
                self.n -= 1


if __name__ == '__main__':
    for i in MyIterator('mythic', 20):
        print(i)
    print('----')
    a = iter(MyIterator('mythic', 20))
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
