import copy

class Boop:
    def __init__(self):
        self.table = []
        self.size = 4
        self.shift = 1
        self.space = '  '
        self.kitten_1 = '😺'
        self.kitten_2 = '😈' 
        self.cat_1 = '🐯'
        self.cat_2 = '👾'
        self.num_kittens_1 = 6
        self.num_kittens_2 = 6
        self.num_cats_1 = 4
        self.num_cats_2 = 4
        self.total_cats = 4

    def create(self):
        for _ in range(self.size):
            self.table.append([self.space] * self.size)

    def print_table(self):
        for row in self.table:
            print(row)

    def check_promotion(self):
        piece = self.kitten_1 if self.shift == 1 else self.kitten_2
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
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
                                    print(line)
                        if len(line) == 3:
                            promotion_coords = line
                            return promotion_coords
        return promotion_coords
    
    def check_victory(self, silent=False) -> bool:
        if self.num_kittens_1 == 0 or self.num_kittens_2 == 0:
            if not silent:
                print('Empate! No hay más piezas para jugar.')
            return True
        cat = self.cat_1 if self.shift == 1 else self.cat_2
        num_cats = self.num_cats_1 if self.shift == 1 else self.num_cats_2
        if num_cats <= self.total_cats - 2:
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
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

    def put(self, location: tuple, piece_type='kitten', promotion_choice: tuple = None, silent=False) -> bool:
        x, y = location
        if self.table[x][y] != self.space:
            if not silent:
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
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        for dx, dy in directions:
            self.move(x, y, dx, dy)
        promotion_options = self.check_promotion()
        if promotion_options:
            if not silent:
                print(f"🎉 ¡Has formado una línea de 3 gatitos!")
                print("Puedes promocionar uno a gato grande.")
                print("Opciones disponibles:")
                for opt in promotion_options:
                    print(f" - {opt}")
            if promotion_choice and promotion_choice in promotion_options:
                px, py = promotion_choice
            else:
                if self.shift == 1 and not silent:
                    try:
                        px = int(input("Ingresa la coordenada x a promover: "))
                        py = int(input("Ingresa la coordenada y a promover: "))
                        if (px, py) not in promotion_options:
                            print("⚠️ Coordenada no válida, se usará la primera opción disponible.")
                            px, py = promotion_options[0]
                    except Exception:
                        print("⚠️ Entrada no válida, se usará la primera opción disponible.")
                        px, py = promotion_options[0]
                else:
                    px, py = promotion_options[0]
            if self.shift == 1:
                self.table[px][py] = self.cat_1
                self.num_cats_1 -= 1
            else:
                self.table[px][py] = self.cat_2
                self.num_cats_2 -= 1
            if not silent:
                print(f"✅ ¡Promoción exitosa en {px, py}!")
        if self.check_victory():
            return True
        self.shift = 2 if self.shift == 1 else 1
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
                    # if (self.shift == 1 and self.num_cats_1 > 0) or (self.shift == 2 and self.num_cats_2 > 0):
                    #     moves.append({'location': (x, y), 'piece_type': 'cat'})
        return moves
    
    def simulate_move(self, move, promotion_choice=None):
        new_state = self.clone()
        res = new_state.put(move['location'], piece_type=move.get('piece_type', 'kitten'), promotion_choice=promotion_choice, silent=True)
        return new_state, {'ok': res, 'victory': res}

b = Boop()
b.create()