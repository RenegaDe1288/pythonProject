import random
import math


class Auto:
    km = 0

    def __init__(self):
        self.x = 0
        self.y = 0
        self.line = random.randint(1, 4)

    def move(self):
        answer = random.randint(0, 361)
        print(answer)
        self.y = round(self.y + self.line * math.sin(math.radians(answer)), 5)
        self.x = round(self.x + self.line * math.cos(math.radians(answer)), 5)
        self.km += self.line
        print(self.__str__())

    def __str__(self):
        return ('\nАвтобус проехал: {} км.  Всего {} '.format(self.line, self.km))

    def total_money(self, passangers):
        return self.line * passangers


class Bus(Auto):
    station = 0
    money = 0

    def __init__(self):
        super().__init__()
        self.pass_in = 0

    def move(self):
        self.station += 1
        super().move()
        self.info()
        self.outcome()
        self.income()
        print('Пассажиров в автобусе: ', self.pass_in)
        self.money_earn()

    def income(self):
        income_pass = random.randint(1, 10)
        self.pass_in += income_pass
        print('Пассажиров вошло: ', income_pass)

    def outcome(self):
        outcome_pass = random.randint(0, self.pass_in)
        self.pass_in -= outcome_pass
        print('Пассажиров вышло: ', outcome_pass)

    def info(self):
        print('И теперь его координаты: {} и {}'.format(self.x, self.y))
        print('Остановка: ', self.station)

    def money_earn(self):
        self.money += super().total_money(self.pass_in)
        print('Денег заработано: ', self.money)


bus = Bus()
while bus.money < 500:
    bus.move()
