from datetime import datetime
import time


def call(func):
    def wrapper(*args, **kwargs):
        print('Вызван метод: ', func)
        func(*args, **kwargs)
        with open('logging.txt', 'a', encoding='utf - 8') as file:
            file.write(str(func) + '\t' + str(datetime.utcnow()) + '\n')
        print('Метод: {} записан'.format(func))

    return wrapper


def logging(func):
    def wrapper(cls):
        print('Список методов: ', dir(cls))
        for i in dir(cls):
            if not i.endswith('__'):
                new = getattr(cls, i)
                new2 = func(new)
                setattr(cls, i, new2)
        return cls

    return wrapper


@logging(call)
class Hobo:

    def __init__(self):
        self.name = 'Tolik'

    def drink(self):
        print(' {}  наЖрался '.format(self.name))

    def dry(self):
        print(self.name, ' протрезвел')


a = Hobo()

print(a.name)
a.drink()
a.dry()
time.sleep(2)
a.dry()
