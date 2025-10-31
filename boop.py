class Boop:
    def __init__(self):
        self.table = []
        self.size = 4
        self.shift = 1
        self.space = '  '
        self.kitten_1 = '😈' 
        self.kitten_2 = '😺'
        self.cat_1 = '👾'
        self.cat_2 = '🐯'
        self.num_kittens_1 = 6
        self.num_kittens_2 = 6
        self.num_cats_1 = 4
        self.num_cats_2 = 4

    def create(self):
        for _ in range(self.size):
            self.table.append([self.space] * self.size)

    def print_table(self):
        for row in self.table:
            print(row)
    
    def move(self, x: int, y: int, dx: int, dy: int):
        nx = x + dx
        ny = y + dy
        nnx = x + 2*dx
        nny = y + 2*dy
        if 0 <= nx < self.size and 0 <= ny < self.size and self.table[nx][ny] != self.space and self.table[nx][ny] != self.cat_1 and self.table[nx][ny] != self.cat_2:
            if 0 <= nnx < self.size and 0 <= nny < self.size:
                if self.table[nnx][nny] == self.space:
                    self.table[nnx][nny] = self.table[nx][ny]
                    self.table[nx][ny] = self.space 
            else:
                self.table[nx][ny] = self.space

    def put(self, location: tuple):
        x, y = location
        if self.table[x][y] != self.space:
            print('Ubicacion ocupada, intente de nuevo.')
            return False
        if self.shift == 1:
            self.table[x][y] = self.kitten_1
            self.num_kittens_1 -= 1
        else:
            self.table[x][y] = self.kitten_2
            self.num_kittens_2 -= 1
        directions = [
            (-1, 0), # Arriba
            (1, 0),  # Abajo
            (0, -1), # Izquierda
            (0, 1),  # Derecha
            (-1, -1),# Esquina superior izquierda
            (-1, 1), # Esquina superior derecha
            (1, -1), # Esquina inferior izquierda
            (1, 1),  # Esquina inferior derecha
        ]
        for dx, dy in directions:
            self.move(x, y, dx, dy)
        self.shift = 2 if self.shift == 1 else 1




b = Boop()
b.create()