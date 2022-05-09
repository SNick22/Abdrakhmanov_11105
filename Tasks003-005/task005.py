import random, collections


class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.value = 0
        self.neighboring_cells = collections.deque()
        self.opened = False

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_value(self):
        return self.value

    def get_neighbors(self):
        return self.neighboring_cells

    def set_neighbor(self, neighbor):
        self.neighboring_cells.append(neighbor)

    def set_value(self):
        if self.value == 0:
            for i in self.neighboring_cells:
                if i.value == '*':
                    self.value += 1

    def set_opened(self):
        self.opened = True


class Field:
    def __init__(self, bombs=10):
        self.output: list = [['X'] * 9 for i in range(9)]
        self.real_cells = []
        self.bombs = bombs
        self.bombs_count = bombs
        self.flags_count = bombs
        self.game_status = False
        self.opened_cells_counter = 0
        for i in range(9):
            temp = []
            for k in range(9):
                temp.append(Cell(i, k))
            self.real_cells.append(temp)

    def print_field(self):
        print('  a b c d e f g h i')
        for i in range(len(self.output)):
            print(9 - i, '|', sep='', end='')
            for k in self.output[i]:
                print(k, '|', sep='', end='')
            print(9 - i)
        print('  a b c d e f g h i')
        print('flags left:', self.flags_count)

    def neighbor_setting(self):
        for i in range(9):
            for k in range(9):
                if self.real_cells[i][k].get_value() == '*':
                    continue
                if i == 0 and k == 0:
                    self.real_cells[i][k].set_neighbor(self.real_cells[i][k + 1])
                    self.real_cells[i][k].set_neighbor(self.real_cells[i + 1][k + 1])
                    self.real_cells[i][k].set_neighbor(self.real_cells[i + 1][k])
                    continue
                if i == 8 and k == 8:
                    self.real_cells[i][k].set_neighbor(self.real_cells[i][k - 1])
                    self.real_cells[i][k].set_neighbor(self.real_cells[i - 1][k - 1])
                    self.real_cells[i][k].set_neighbor(self.real_cells[i - 1][k])
                    continue
                if i == 0 and k == 8:
                    self.real_cells[i][k].set_neighbor(self.real_cells[i][k - 1])
                    self.real_cells[i][k].set_neighbor(self.real_cells[i + 1][k - 1])
                    self.real_cells[i][k].set_neighbor(self.real_cells[i + 1][k])
                    continue
                if i == 8 and k == 0:
                    self.real_cells[i][k].set_neighbor(self.real_cells[i][k + 1])
                    self.real_cells[i][k].set_neighbor(self.real_cells[i - 1][k + 1])
                    self.real_cells[i][k].set_neighbor(self.real_cells[i - 1][k])
                    continue
                if i == 0:
                    self.real_cells[i][k].set_neighbor(self.real_cells[i + 1][k])
                    self.real_cells[i][k].set_neighbor(self.real_cells[i + 1][k + 1])
                    self.real_cells[i][k].set_neighbor(self.real_cells[i + 1][k - 1])
                    self.real_cells[i][k].set_neighbor(self.real_cells[i][k - 1])
                    self.real_cells[i][k].set_neighbor(self.real_cells[i][k + 1])
                    continue
                if i == 8:
                    self.real_cells[i][k].set_neighbor(self.real_cells[i - 1][k])
                    self.real_cells[i][k].set_neighbor(self.real_cells[i - 1][k - 1])
                    self.real_cells[i][k].set_neighbor(self.real_cells[i - 1][k + 1])
                    self.real_cells[i][k].set_neighbor(self.real_cells[i][k - 1])
                    self.real_cells[i][k].set_neighbor(self.real_cells[i][k + 1])
                    continue
                if k == 0:
                    self.real_cells[i][k].set_neighbor(self.real_cells[i - 1][k])
                    self.real_cells[i][k].set_neighbor(self.real_cells[i + 1][k])
                    self.real_cells[i][k].set_neighbor(self.real_cells[i][k + 1])
                    self.real_cells[i][k].set_neighbor(self.real_cells[i - 1][k + 1])
                    self.real_cells[i][k].set_neighbor(self.real_cells[i + 1][k + 1])
                    continue
                if k == 8:
                    self.real_cells[i][k].set_neighbor(self.real_cells[i - 1][k])
                    self.real_cells[i][k].set_neighbor(self.real_cells[i + 1][k])
                    self.real_cells[i][k].set_neighbor(self.real_cells[i][k - 1])
                    self.real_cells[i][k].set_neighbor(self.real_cells[i - 1][k - 1])
                    self.real_cells[i][k].set_neighbor(self.real_cells[i + 1][k - 1])
                    continue
                self.real_cells[i][k].set_neighbor(self.real_cells[i + 1][k - 1])
                self.real_cells[i][k].set_neighbor(self.real_cells[i + 1][k + 1])
                self.real_cells[i][k].set_neighbor(self.real_cells[i + 1][k])
                self.real_cells[i][k].set_neighbor(self.real_cells[i - 1][k - 1])
                self.real_cells[i][k].set_neighbor(self.real_cells[i - 1][k + 1])
                self.real_cells[i][k].set_neighbor(self.real_cells[i - 1][k])
                self.real_cells[i][k].set_neighbor(self.real_cells[i][k + 1])
                self.real_cells[i][k].set_neighbor(self.real_cells[i][k - 1])

    def bomb_generation(self, x1, y1):
        while self.bombs != 0:
            y = random.randint(0, 8)
            x = random.randint(0, 8)
            if self.real_cells[y][x].value == '*' or (y == y1 and x == x1):
                continue
            else:
                self.real_cells[y][x].value = '*'
                self.bombs -= 1
        self.neighbor_setting()
        for i in self.real_cells:
            for k in i:
                k.set_value()
        self.game_status = True

    def open(self, x, y):
        if self.output[y][x] == 'f':
            return
        if self.real_cells[y][x].get_value() == '*':
            self.game_status = False
            for i in range(9):
                for k in range(9):
                    if self.real_cells[i][k].get_value() == '*':
                        self.output[i][k] = self.real_cells[i][k].get_value()
        if self.real_cells[y][x].get_value() != 0 and self.real_cells[y][x].opened == False:
            self.output[y][x] = self.real_cells[y][x].get_value()
            self.real_cells[y][x].set_opened()
            self.opened_cells_counter += 1
        if self.real_cells[y][x].get_value() == 0 and self.real_cells[y][x].opened == False:
            self.output[y][x] = ' '
            self.real_cells[y][x].set_opened()
            self.opened_cells_counter += 1
            for i in self.real_cells[y][x].get_neighbors():
                self.open(i.get_y(), i.get_x())
        if 81 - self.bombs_count == self.opened_cells_counter:
            self.game_status = False

    def flag(self, x, y):
        if self.real_cells[y][x].opened or self.flags_count == 0 or self.output[y][x] == 'f':
            return
        self.output[y][x] = 'f'
        self.flags_count -= 1

    def unflag(self, x, y):
        if self.output[y][x] == 'f':
            self.output[y][x] = 'X'
            self.flags_count += 1


if __name__ == '__main__':
    print('Minesweeper v1.0 by Azat Abdrakhmanov. ©All rights reserved')
    print('INSTRUCTIONS:')
    print('Enter open xy, if you want to open the cell')
    print('Enter flag xy, if you want to put the flag')
    print('Enter unflag xy, if you want to remove the flag')
    print('(x - horizontal coordinate, y - vertical coordinate)')
    print('Good game!')
    myf = Field()
    myf.print_field()

    while not myf.game_status:
        command, coords = map(str, input().split())
        x = ord(coords[0]) - 97
        y = 9 - int(coords[1])
        if command == 'open' and myf.output[y][x] != 'f':
            myf.bomb_generation(x, y)
            myf.open(x, y)
        if command == 'flag':
            myf.flag(x, y)
        if command == 'unflag':
            myf.unflag(x, y)
        myf.print_field()

    while myf.game_status:
        command, coords = map(str, input().split())
        x = ord(coords[0]) - 97
        y = 9 - int(coords[1])
        if command == 'open':
            myf.open(x, y)
        if command == 'flag':
            myf.flag(x, y)
        if command == 'unflag':
            myf.unflag(x, y)
        myf.print_field()

    if 81 - myf.bombs_count == myf.opened_cells_counter:
        print('********** YOU ARE WON!! **********')
    else:
        print('********** GAME OVER **********')
