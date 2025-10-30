class Boop:
    def __init__(self):
        self.table = []
        self.size = 4
        self.shift = 1

    def create(self):
        for _ in range(self.size):
            self.table.append([' '] * self.size)

    def print_table(self):
        for i in range(self.size):
            print(self.table[i])

    def move(self, location: tuple):
        x, y = location
        if x - 1 > 0:
            pass
        



b = Boop()
b.create()