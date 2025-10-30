from boop import Boop

class Console:
    def __init__(self):
        self.boop = Boop()
        self.boop.create()
        self.boop.print_table()

    def interface(self):
        pass
    

c = Console()