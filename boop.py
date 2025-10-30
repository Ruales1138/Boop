class Boop:
    def __init__(self):
        self.table = []
        self.size = 4
        self.shift = 1
        self.space = '  '
        self.kitten_1 = '😈' 
        self.kitten_2 = '😺'
        self.pieces_1 = 6
        self.pieces_2 = 6

    def create(self):
        for _ in range(self.size):
            self.table.append([self.space] * self.size)

    def print_table(self):
        for i in range(self.size):
            print(self.table[i])

    def put(self, location: tuple):
        x, y = location
        if self.shift == 1:
            self.table[x][y] = self.kitten_1
            self.pieces_1 -= 1
        if self.shift == 2:
            self.table[x][y] = self.kitten_2
            self.pieces_2 -= 1
        # Arriba
        if x-1 >= 0 and self.table[x-1][y] != self.space:
            if x-2 >= 0:
                if self.table[x-2][y] == self.space:
                    self.table[x-2][y] = self.table[x-1][y]
                    self.table[x-1][y] = self.space
            else:
                self.table[x-1][y] = self.space
        # Abajo
        if x+1 < self.size and self.table[x+1][y] != self.space:
            if x+2 < self.size:
                if self.table[x+2][y] == self.space:
                    self.table[x+2][y] = self.table[x+1][y]
                    self.table[x+1][y] = self.space
            else:
                self.table[x+1][y] = self.space
        # Izquierda
        if y-1 >= 0 and self.table[x][y-1] != self.space:
            if y-2 >= 0:
                if self.table[x][y-2] == self.space:
                    self.table[x][y-2] = self.table[x][y-1]
                    self.table[x][y-1] = self.space
            else:
                self.table[x][y-1] = self.space
        # Derecha
        if y+1 < self.size and self.table[x][y+1] != self.space:
            if y+2 < self.size:
                if self.table[x][y+2] == self.space:
                    self.table[x][y+2] = self.table[x][y+1]
                    self.table[x][y+1] = self.space
            else:
                self.table[x][y+1] = self.space
        # Esquina superior izquierda
        if x-1 >= 0 and y-1 >= 0 and self.table[x-1][y-1] != self.space:
            if x-2 >= 0 and y-2 >= 0:
                if self.table[x-2][y-2] == self.space:
                    self.table[x-2][y-2] = self.table[x-1][y-1]
                    self.table[x-1][y-1] = self.space
            else:
                self.table[x-1][y-1] = self.space
        # Esquina superior derecha
        if x-1 >= 0 and y+1 < self.size and self.table[x-1][y+1] != self.space:
            if x-2 >= 0 and y+2 < self.size:
                if self.table[x-2][y+2] == self.space:
                    self.table[x-2][y+2] = self.table[x-1][y+1]
                    self.table[x-1][y+1] = self.space
            else:
                self.table[x-1][y+1] = self.space
        # Esquina inferior izquierda
        if x+1 < self.size and y-1 >= 0 and self.table[x+1][y-1] != self.space:
            if x+2 < self.size and y-2 >= 0:
                if self.table[x+2][y-2] == self.space:
                    self.table[x+2][y-2] = self.table[x+1][y-1]
                    self.table[x+1][y-1] = self.space
            else:
                self.table[x+1][y-1] = self.space
        # Esquina inferior derecha
        if x+1 < self.size and y+1 < self.size and self.table[x+1][y+1] != self.space:
            if x+2 < self.size and y+2 < self.size:
                if self.table[x+2][y+2] == self.space:
                    self.table[x+2][y+2] = self.table[x+1][y+1]
                    self.table[x+1][y+1] = self.space
            else:
                self.table[x+1][y+1] = self.space
        # Cambiar turno
        if self.shift == 1:
            self.shift = 2
        else:
            self.shift = 1




b = Boop()
b.create()