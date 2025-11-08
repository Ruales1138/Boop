from boop import Boop
from minimax import minimax

class Console:
    def __init__(self):
        self.boop = Boop()
        self.boop.create()
        self.boop.print_table()
        self.option = True

    def interface(self):
        while self.option:
            print('--------------------------------------------')
            if self.boop.shift == 1:
                pieces = ''
                for _ in range(self.boop.num_kittens_1):
                    pieces += self.boop.kitten_1
                for _ in range(self.boop.num_cats_1):
                    pieces += self.boop.cat_1
                print(f'Jugador 1 {pieces}')
            elif self.boop.shift == 2:
                pieces = ''
                for _ in range(self.boop.num_kittens_2):
                    pieces += self.boop.kitten_2
                for _ in range(self.boop.num_cats_2):
                    pieces += self.boop.cat_2
                print(f'Jugador 2 {pieces}')
                # print("🤖 Turno de la IA...")
                # _, best_move = minimax(self.boop, depth=3, alpha=-float('inf'), beta=float('inf'), maximizing=False)
                # print(f"IA elige: {best_move}")
                # self.boop.put(best_move['location'], piece_type=best_move['piece_type'])
                # self.boop.print_table()
                # continue
            try:
                x = int(input('Ingrese una nueva ubicacion en x:\n'))
                y = int(input('Ingrese una nueva ubicacion en y:\n'))
            except ValueError:
                print("Entrada invalida. Por favor ingrese numeros enteros.")
                continue
            print(f'Moviendo a ({x}, {y})')
            if self.boop.put((x, y)):
                self.option = False
            self.boop.print_table()

            
c = Console()
c.interface()