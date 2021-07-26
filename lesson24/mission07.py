import random


class Potato:
    def __init__(self, status=1):
        self.status = status

    def check(self):
        if self.status < 6:
            self.status += random.randint(0, 1)


    def info(self,index):
        print('Картошка: {} -- {}'.format(index + 1, list[self.status]))

    def is_rise(self):
        if self.status >= 4:
            return True
        else:
            return False


class Garden:

    def __init__(self, row):
        print('\nКартошка только что посажена')
        self.potatoes = [Potato() for _ in range(1, row + 1)]

    def grow_all(self):
        while not all(potato.is_rise() for potato in self.potatoes):
            print('\nВся Картошка еще не созрела!\n')
            for index, pot in enumerate(self.potatoes):
                pot.check()
                pot.info(index)
        print('\nКартошка Созрела')



list = {1: 'Посажена', 2: 'Росток', 3: 'Зелёная', 4: 'Зрелая', 5: 'Зрелая', 6: 'Сгнила'}

garden = Garden(5)
garden.grow_all()
