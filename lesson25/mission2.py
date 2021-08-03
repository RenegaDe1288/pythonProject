import random


class Carma:
    carma = 0
    day = 0

    def one_day(self):
        new = random.randint(1, 7)
        self.carma += new
        self.day += 1
        return f'День: {self.day}   Карма: {self.carma}'


class MyExceptions(Exception):

    def __init__(self, name):
        self.ex_name = name

    def raise_exception(self, day):
        with open('karma.txt', 'a', encoding='utf-8') as errors_list:
            errors_list.write('\nИсключение: {}  в день: {}'.format(self.ex_name, day))
            print(('\nИсключение: {}  в день: {}\n'.format(self.ex_name, day)))
        raise self.ex_name('Вызвана ошибка')


ex_list = ['KillError', 'DrunkError', 'CarCrashError', 'GluttonyError', 'DepressionError']
buddist = Carma()
errors = [MyExceptions(name) for name in ex_list]

while buddist.carma < 500:
    if random.randint(1, 10) == 1:
        try:
            errors[random.randint(0, 4)].raise_exception(buddist.day)
        except:
            pass
    else:
        print(buddist.one_day())
