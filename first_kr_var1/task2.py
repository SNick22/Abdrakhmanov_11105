# variant 1
class MyIterator:
    def __init__(self, lst: list[int], n: int, c: int):
        self.lst = lst
        self.n = n
        self.c = c

    def __iter__(self):
        elems = list(filter(lambda x: x % self.c == 0, self.lst))
        counter = 0
        while counter < self.n:
            for i in elems:
                if counter == self.n:
                    break
                yield i
                counter += 1
            if counter == 0:
                raise StopIteration


if __name__ == '__main__':
    for i in MyIterator([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 20, 3):
        print(i)
    print('---------')
    a = iter(MyIterator([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 20, 3))
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
