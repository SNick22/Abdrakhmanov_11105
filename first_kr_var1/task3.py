# variant 1
def numbers_gen(n):
    for i in range(1, n):
        if i < 10:
            yield i
        else:
            numbers_in_number = []
            k = i
            while k//10 > 0:
                numbers_in_number.append(k % 10)
                k //= 10
            numbers_in_number.append(k % 10)
            summ = sum(map(lambda x: x**len(numbers_in_number), numbers_in_number))
            if summ == i:
                yield i


if __name__ == '__main__':
    for i in numbers_gen(10000):
        print(i)
