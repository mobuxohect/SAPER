import random as r

class Cell:
    def __init__(self, x, y, around_mines=0, mine=False, fl_open=True, flag=False):
        self.x = x
        self.y = y
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
            if self.pole[x][y].mine:
                continue
            else:
                self.pole[x][y].mine = True
                cnt += 1
            indx = (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)
            for i in range(self.N):
                for j in range(self.N):
                    if not self.pole[i][j].mine:
                        mines = sum((self.pole[x+i][y+j].mine for x, y in indx if 0 <= x+i < self.N and 0 <= y+j < self.N))
                        self.pole[i][j].around_mines = mines

    def init(self):
        self.pole = [[Cell(i, j) for j in range(self.N)] for i in range(self.N)]
        self.generate_mines()

    def show(self):
        for row in self.pole:
            for cell in row:
                if not cell.fl_open:
                    print('#', end=' ')
                else:
                    if cell.mine:
                        print('M', end=' ')
                    else:
                        print(cell.around_mines, end=' ')
            print()

pole_game = GamePole(9, 10)
pole_game.show()