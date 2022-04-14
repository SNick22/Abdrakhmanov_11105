# variant 5
class ShapeIterator:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        if self.n % 2 == 0:
            for i in range(self.n):
                yield '(' * self.n
        else:
            for i in range(self.n // 2):
                yield ' ' * (self.n // 2 - i) + '/' * (2 * i + 1) + ' ' * (self.n // 2 - i)
            yield '/' * self.n
            for i in range(self.n // 2 - 1, -1, -1):
                yield ' ' * (self.n // 2 - i) + '/' * (2 * i + 1) + ' ' * (self.n // 2 - i)
        # raise StopIteration


if __name__ == '__main__':
    for i in ShapeIterator(5):
        print(i)
    print('-----')
    a = iter(ShapeIterator(5))
    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))
