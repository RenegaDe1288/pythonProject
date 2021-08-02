class Ship:

    def __init__(self, model):
        self.model = model

    def __str__(self):
        print('Корабль плывет', self.model)


class Warship(Ship):

    def __init__(self, model, gun):
        super().__init__(model)
        self.gun = gun

    def atack(self):
        print("Корабль {}  атакует {}".format(self.model, self.gun))


class Cargoship(Ship):
    def __init__(self, model, load):
        super().__init__(model)
        self.load = 0

    def load_ship(self):
        self.load = 1 if self.load == 0 else 1
        print('Загруженность корабля: ', self.load)

    def empty_ship(self):
        self.load = 0 if self.load == 1 else 0
        print('Загруженность корабля: ', self.load)


ship = Warship('ert', 'lazer')
ship.__str__()
ship.atack()
ship_1 = Cargoship('zzzz', 0)
ship_1.__str__()
ship_1.load_ship()
ship_1.load_ship()
ship_1.__str__()
ship_1.empty_ship()
