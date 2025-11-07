import copy

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

    def find_promotion_lines(self):
        piece = self.kitten_1 if self.shift == 1 else self.kitten_2
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
        promotion_coords = []
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
                            for p in line:
                                if p not in promotion_coords:
                                    promotion_coords.append(p)
        return promotion_coords
    
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

    def put(self, location: tuple, piece_type='kitten', promotion_choice: tuple = None):
        x, y = location
        if self.table[x][y] != self.space:
            print('Ubicacion ocupada, intente de nuevo.')
            return False
        if self.shift == 1:
            if piece_type == 'kitten':
                self.table[x][y] = self.kitten_1
                self.num_kittens_1 -= 1
            else:
                self.table[x][y] = self.cat_1
                self.num_cats_1 -= 1
        else:
            if piece_type == 'kitten':
                self.table[x][y] = self.kitten_2
                self.num_kittens_2 -= 1
            else:
                self.table[x][y] = self.cat_2
                self.num_cats_2 -= 1
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
        promotion_options = self.find_promotion_lines()
        if promotion_options:
            print(f"🎉 ¡Has formado una línea de 3 gatitos!")
            print("Puedes promocionar uno a gato grande.")
            print("Opciones disponibles:")
            for opt in promotion_options:
                print(f" - {opt}")
            if promotion_choice and promotion_choice in promotion_options:
                px, py = promotion_choice
            else:
                try:
                    entrada = input("Ingresa la coordenada a promover en formato x,y: ")
                    px, py = map(int, entrada.split(","))
                    if (px, py) not in promotion_options:
                        print("⚠️ Coordenada no válida, se usará la primera opción disponible.")
                        px, py = promotion_options[0]
                except Exception:
                    print("⚠️ Entrada no válida, se usará la primera opción disponible.")
                    px, py = promotion_options[0]
            if self.shift == 1:
                self.table[px][py] = self.cat_1
                self.num_cats_1 -= 1
            else:
                self.table[px][py] = self.cat_2
                self.num_cats_2 -= 1
            print(f"✅ ¡Promoción exitosa en {px, py}!")
        if self.check_victory():
            return True
        self.shift = 2 if self.shift == 1 else 1
        return False

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
                                # print('*******************************************')
                                # print(f"✅✅✅Jugador {self.shift} {icon} gana! ✅✅✅")
                                # print('*******************************************')
                                return True
        return False
    
    def clone(self):
        return copy.deepcopy(self)
    
    def get_valid_moves(self):
        moves = []
        for x in range(self.size):
            for y in range(self.size):
                if self.table[x][y] == self.space:
                    if (self.shift == 1 and self.num_kittens_1 > 0) or (self.shift == 2 and self.num_kittens_2 > 0):
                        moves.append({'location': (x, y), 'piece_type': 'kitten'})
                    if (self.shift == 1 and self.num_cats_1 > 0) or (self.shift == 2 and self.num_cats_2 > 0):
                        moves.append({'location': (x, y), 'piece_type': 'cat'})
        return moves
    
    def simulate_move(self, move, promotion_choice=None):
        new_state = self.clone()
        res = new_state.put(move['location'], piece_type=move.get('piece_type', 'kitten'), promotion_choice=promotion_choice)
        return new_state, {'ok': res, 'victory': res}

b = Boop()
b.create()