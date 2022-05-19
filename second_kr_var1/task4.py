import threading
from time import sleep
from random import randint


class Player(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.hp = 10
        self.alive = True

    def set_enemy(self, enemy):
        self.enemy = enemy

    def run(self):
        while True:
            sleep(randint(0, 100) * 0.01)
            if not self.alive:
                break
            self.enemy.hp -= 1
            print(f'{self.name} ударил {self.enemy.name} у него осталось {self.enemy.hp} хп')
            if self.enemy.hp == 0:
                self.alive = False
                self.enemy.alive = False
                print(f'Я, {self.name}, выиграл, у меня осталось {self.hp} хп')
                print(f'Я, {self.enemy.name}, проиграл, у меня осталось {self.enemy.hp} хп')


if __name__ == '__main__':
    p1 = Player('Jon')
    p2 = Player('Jack')
    p1.set_enemy(p2)
    p2.set_enemy(p1)
    p1.start()
    p2.start()
