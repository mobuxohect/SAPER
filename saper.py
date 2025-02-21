import random as r

class Cell:
    def __init__(self, around_mines=0, mine=False, fl_open=False, flag=False):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = fl_open
        self.flag = flag

    def open(self):
        self.fl_open = True

    def mark_mine(self):
        self.flag = True

class GamePole:
    def __init__(self, N, M):
        self.N = N
        self.M = M
        self.init()

    def generate_mines(self):
        cnt = 0
        while cnt < self.M:
            x = r.randint(0, self.N-1)
            y = r.randint(0, self.N-1)
            if not self.pole[x][y].mine:
                self.pole[x][y].mine = True
                if 0 < x < self.N - 1 and 0 < y < self.N - 1:
                    self.pole[x+1][y+1].around_mines += 1
                    self.pole[x+1][y-1].around_mines += 1
                    self.pole[x+1][y].around_mines += 1
                    self.pole[x][y+1].around_mines += 1
                    self.pole[x][y-1].around_mines += 1
                    self.pole[x-1][y+1].around_mines += 1
                    self.pole[x-1][y-1].around_mines += 1
                    self.pole[x-1][y].around_mines += 1
                elif x == 0 and y == 0:
                    self.pole[x][y+1].around_mines += 1
                    self.pole[x+1][y+1].around_mines += 1
                    self.pole[x+1][y].around_mines += 1
                elif x == self.N - 1 and y == self.N - 1:
                    self.pole[x-1][y-1].around_mines += 1
                    self.pole[x-1][y].around_mines += 1
                    self.pole[x][y-1].around_mines += 1
                elif x == 0 and y == self.N - 1:
                    self.pole[x+1][y].around_mines += 1
                    self.pole[x+1][y-1].around_mines += 1
                    self.pole[x][y-1].around_mines += 1
                elif x == self.N - 1 and y == 0:
                    self.pole[x][y+1].around_mines += 1
                    self.pole[x-1][y-1].around_mines += 1
                    self.pole[x-1][y].around_mines += 1
                elif x == 0 and 0 < y < self.N - 1:
                    self.pole[x+1][y+1].around_mines += 1
                    self.pole[x+1][y-1].around_mines += 1
                    self.pole[x+1][y].around_mines += 1
                    self.pole[x][y+1].around_mines += 1
                    self.pole[x][y-1].around_mines += 1
                elif 0 < x < self.N - 1 and y == 0:
                    self.pole[x+1][y+1].around_mines += 1
                    self.pole[x+1][y].around_mines += 1
                    self.pole[x][y+1].around_mines += 1
                    self.pole[x-1][y].around_mines += 1
                    self.pole[x-1][y+1].around_mines += 1
                elif x == self.N - 1 and 0 < y < self.N - 1:
                    self.pole[x][y+1].around_mines += 1
                    self.pole[x][y-1].around_mines += 1
                    self.pole[x-1][y+1].around_mines += 1
                    self.pole[x-1][y-1].around_mines += 1
                    self.pole[x-1][y].around_mines += 1
                elif y == self.N - 1 and 0 < x < self.N - 1:
                    self.pole[x+1][y].around_mines += 1
                    self.pole[x+1][y-1].around_mines += 1
                    self.pole[x-1][y].around_mines += 1
                    self.pole[x-1][y-1].around_mines += 1
                    self.pole[x][y-1].around_mines += 1
                cnt += 1
            else:
                continue

    def init(self):
        self.pole = [[Cell() for _ in range(self.N)] for __ in range(self.N)]
        self.generate_mines()

    # def show(self):
    #     for row in self.pole:
    #         for cell in row:
    #             if not cell.fl_open:
    #                 print('#', end='')
    #             else:
    #                 if cell.mine:
    #                     print('M', end='')
    #                 else:
    #                     print(cell.around_mines, end='')
    #         print()
