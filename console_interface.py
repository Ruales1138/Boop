from boop import Boop

class Console:
    def __init__(self):
        self.boop = Boop()
        self.boop.create()
        self.boop.print_table()
        self.option = 0

    def interface(self):
        while self.option != 3:
            print('--------------------------------------------')
            if self.boop.shift == 1:
                pieces = ''
                for _ in range(self.boop.pieces_1):
                    pieces += self.boop.kitten_1
                print(f'Jugador 1 {pieces}')
            if self.boop.shift == 2:
                pieces = ''
                for _ in range(self.boop.pieces_2):
                    pieces += self.boop.kitten_2
                print(f'Jugador 2 {pieces}')
            x = int(input('Ingrese una nueva ubicacion en x:\n'))
            y = int(input('Ingrese una nueva ubicacion en y:\n'))
            print(f'Moviendo a ({x}, {y})')
            self.boop.put((x, y))
            self.boop.print_table()

            


c = Console()
c.interface()