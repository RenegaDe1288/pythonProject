import random


class Potato:
    def __init__(self, row, status=1):
        self.num_row = row
        self.status = status

    def check(self, gardener):
        if self.status < 4:
            if gardener.care():
                self.status += 1
        elif 4 <= self.status <= 5:
            if gardener.collect():
                self.status = 10
            else:
                self.status += 1

    def info(self):
        print('Грядка картошки: {} -- {}'.format(self.num_row, status_dict[self.status]))

    def is_rise(self):
        if self.status >= 6:
            return True
        else:
            return False


class Garden:

    def __init__(self, row):
        print('\nКартошка только что посажена')
        self.potatoes = [Potato(row) for row in range(1, row + 1)]

    def grow_all(self):
        gardener = Gardener()
        count = 1
        while not all(potato.is_rise() for potato in self.potatoes):
            print('\nДень : {}. Вся Картошка еще не собрана!\n'.format(count))
            for pot in self.potatoes:
                pot.check(gardener)
                pot.info()
            count += 1
        print('\n\tСадовник {} успел собрать {} грядки картошки \n'.format(gardener.name,len(gardener.collection)))


class Gardener:

    def __init__(self):
        self.name = 'Mike'
        self.collection = []

    def care(self):
        care_choice = random.choice(['Да', 'Нет'])
        if care_choice == 'Да':
            print('   Садовник {} поухаживал за картошкой'.format(self.name))
            return True
        else:
            print('   Садовник {} забил болт на полив картошки'.format(self.name))
            return False

    def collect(self):
        collect_choice = random.choice(['Да', 'Нет'])
        if collect_choice == 'Да':
            print('   Садовник {} собрал картошку'.format(self.name))
            self.collection.append(1)
            return True
        else:
            print('   Садовник {} не успел собрать картошку'.format(self.name))
            return False


status_dict = {1: 'Посажена', 2: 'Росток', 3: 'Зелёная', 4: 'Зрелая', 5: 'Зрелая', 6: 'Сгнила', 10: 'Собрана'}

garden = Garden(3)
garden.grow_all()
