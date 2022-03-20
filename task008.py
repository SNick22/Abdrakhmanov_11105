class Faculty:
    def __init__(self, name: str):
        self.name = name

    def print_name(self):
        print(self.name)


class University:
    def __init__(self, element: list):
        self.element = element

    def __iter__(self):
        return iter(self.element)


if __name__ == '__main__':
    fac1 = Faculty('ITIS')
    fac2 = Faculty('ICMIT')
    fac3 = Faculty('IMEF')
    kfu = University([fac1, fac2, fac3])
    for i in kfu:
        i.print_name()
