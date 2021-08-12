import time
from _datetime import datetime


def create_time(cls):
    def wrapper(*args, **kwargs):
        print('Дата создания объекта: ', datetime.utcnow())
        instance = cls(*args, **kwargs)
        print('Список методов: ', dir(cls))
        return instance

    return wrapper


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        print('Начало работы таймера: ', start)
        func(*args, **kwargs)
        s = 5435353 ** 433536
        print('Конец работы таймера: ', time.time() - start)

    return wrapper


@create_time
class Hobo:

    def __init__(self):
        self.name = 'Tolik'

    def drink(self):
        print(' {}  наЖрался '.format(self.name))

    @timer
    def dry(self):
        print(self.name, ' протрезвел')


a = Hobo()

print(a)
a.drink()
a.dry()
