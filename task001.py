from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def go(self):
        pass

    def voice(self):
        print('I growl')


class Spider(Animal):
    def __init__(self, name, weight, toxicity):
        super().__init__(name, weight)
        self.toxicity = toxicity

    def weave_a_web(self):
        print('I wove a web')

    def voice(self):
        print('I cant make sounds')

    def eat(self):
        print('I ate a fly')

    def go(self):
        print('I crawled')


class Bird(Animal):
    def __init__(self, name, weight, size_of_wings):
        super().__init__(name, weight)
        self.size_of_wings = size_of_wings

    def build_a_nest(self):
        print('I built a nest')

    def voice(self):
        print('I start to croak')

    def eat(self):
        print('I ate bread in the square')

    def go(self):
        print('I flew')


if __name__ == '__main__':
    objects = [Spider('PeterParker', 75, False), Bird('Pigeon', 0.5, 13)]
    for i in objects:
        i.go()
    for i in objects:
        i.voice()
    for i in objects:
        i.eat()

