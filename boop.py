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
        self.check_promotion()
        if self.check_victory():
            return True
        self.shift = 2 if self.shift == 1 else 1

    def check_promotion(self):
        piece = self.kitten_1 if self.shift == 1 else self.kitten_2
        cat = self.cat_1 if self.shift == 1 else self.cat_2
        icon = self.kitten_1 if self.shift == 1 else self.kitten_2
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
        for x in range(self.size):
            for y in range(self.size):
                if self.table[x][y] == piece:
                    for dx, dy in directions:
                        line = []
                        for i in range(3):
                            nx = x + i*dx
                            ny = y + i*dy
                            if 0 <= nx < self.size and 0 <= ny < self.size:
                                if self.table[nx][ny] == piece:
                                    line.append((nx, ny))
                        if len(line) == 3:
                            print(f"Has formado una línea de 3 gatitos {icon}{icon}{icon}!")
                            print("Puedes promocionar uno a gato grande.")
                            print(f"Posiciones disponibles: {line}")
                            px = int(input("Ingrese la coordenada x del gatito a promocionar: "))
                            py = int(input("Ingrese la coordenada y del gatito a promocionar: "))
                            if (px, py) in line:
                                self.table[px][py] = cat
                                if piece == self.kitten_1:
                                    self.num_cats_1 -= 1
                                else:
                                    self.num_cats_2 -= 1
                                print("🎉 ¡Promoción exitosa!")
                            return True
        return False

    def check_victory(self):
        if (self.num_kittens_1 == 0 and self.num_cats_1 == 0) or (self.num_kittens_2 == 0 and self.num_cats_2 == 0):
            print('Empate! No hay más piezas para jugar.')
            return True
        cat = self.cat_1 if self.shift == 1 else self.cat_2
        num_cats = self.num_cats_1 if self.shift == 1 else self.num_cats_2
        icon = self.kitten_1 if self.shift == 1 else self.kitten_2
        if num_cats < 4:
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
            for x in range(self.size):
                for y in range(self.size):
                    if self.table[x][y] == cat:
                        for dx, dy in directions:
                            line = []
                            for i in range(2):
                                nx = x + i*dx
                                ny = y + i*dy
                                if 0 <= nx < self.size and 0 <= ny < self.size:
                                    if self.table[nx][ny] == cat:
                                        line.append((nx, ny))
                            if len(line) == 2:
                                print('*******************************************')
                                print(f"✅✅✅Jugador {self.shift} {icon} gana! ✅✅✅")
                                print('*******************************************')
                                return True

        return False

b = Boop()
b.create()