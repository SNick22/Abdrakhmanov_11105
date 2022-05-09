class Animal:
    kind = 'Animal'

    def __init__(self, name: str = None):
        self.name = name

    def my_name(self):
        if self.name == None:
            print(self.kind + ' dont have a name')
        else:
            print(self.kind + ' name is ' + self.name)

    @classmethod
    def is_pet(cls, name=None):
        if name == None:
            print(cls.kind + ' is wild')
        else:
            print(cls.kind + ' is a pet')

    @staticmethod
    def foo(age):
        print('I am', age, 'years old')


if __name__ == '__main__':
    myAnimal = Animal('Jack')
    myAnimal.is_pet(myAnimal.name)
    Animal.is_pet('Koko')
    Animal.foo(3)
