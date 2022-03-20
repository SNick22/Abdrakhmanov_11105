class Room:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def __eq__(self, other):
        return self.area() == other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __ge__(self, other):
        return self.area() >= other.area()


if __name__ == '__main__':
    myRoom1 = Room(10, 5)
    myRoom2 = Room(3, 7)
    print(myRoom1 >= myRoom2)
    print(myRoom1 <= myRoom2)
    print(myRoom1 == myRoom2)
    print(myRoom1 != myRoom2)
    print(myRoom1 > myRoom2)
    print(myRoom1 < myRoom2)