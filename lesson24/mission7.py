import random


class Person:

    def __init__(self, name):
        self.name = name
        self.hunger = 50

    def info(self):
        print('У {} сытость: {} '.format(self.name, self.hunger))

    def eat(self):
        self.hunger += 10
        means.fridge -= 10
        print('{} поел и его сытость теперь: {}'.format(self.name,self.hunger))

    def check_hunger(self):
        if self.hunger <= 0:
            print('{}  помер от голода'.format(self.name))
            persons.remove(person)
        elif 0 < self.hunger <= 20:
            means.check_fridge()
        else:
            means.play()

    def buy(self):
        means.money -= 10
        means.fridge += 10
        self.hunger += 5
        print('{} сходил в магазин и купил {} еды'.format(self.name,10))


    def work(self):
        print(person.name,' заработал 15 $')
        means.money += 25
        self.buy()

class House:

    def __init__(self):
        self.fridge = 50
        self.money = 50

    def info(self):
        print('В холодильнике осталось еды: {} и денег : {}'.format(self.fridge, self.money))

    def check_money(self):
        global cube
        if 0 < self.money <= 50:
            person.work()
        elif self.money > 50:
            person.eat()
        elif cube == 1:
            person.work()
        elif cube == 2 and self.fridge <= 0:
            print('{}  помер от нищеты'.format(person.name))
            persons.remove(person)
        elif cube == 2 and self.fridge > 0:
            person.eat()
        elif self.money < 0:
            print('{}  помер от нищеты'.format(person.name))
            persons.remove(person)
        else:
            self.play()

    def check_fridge(self):
        if 0 < self.fridge <= 10:
            self.check_money()
        elif self.fridge > 10:
            person.eat()
        elif self.fridge <= 0:
            person.work()


    def play(self):
        person.hunger -= 5
        print('{} играл '.format(person.name))


persons = [Person(name) for name in ['Mike', 'Alex']]

means = House()
means.info()
day = 1

while day != 365:
    print('\n\tДень {}\n'.format(day))
    for person in persons:
        cube = random.randint(1, 3)
        print('Выпал кубик: ', cube)
        person.check_hunger()
        person.info()
        means.info()
    day += 1
