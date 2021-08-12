"""Вариант решения без говна и палок. Оброт функций  через гетер и сетер """

from datetime import datetime


def call(func):
    def wrapper(*args, **kwargs):
        print('Вызван метод: ', func.__name__)
        func(*args, **kwargs)
        with open('logging.txt', 'a', encoding='utf - 8') as file:
            file.write(str(func) + '\t' + str(datetime.utcnow()) + '\n')
        """Записываем данные о вызове метода в файл"""
        print('Метод: {} записан'.format(func.__name__))

    return wrapper


def logging(func):
    """ Декоратор принимет функцию в качестве аргумента"""

    def wrapper(cls):
        """Обертка принимет класс"""
        print('Запускается класс: ', cls.__name__)
        for i in dir(cls):
            if not i.endswith('__'):
                new = getattr(cls, i)
                new2 = func(new)
                """Оборачиваем каЖдый метод класса"""
                setattr(cls, i, new2)
        return cls

    return wrapper


@logging(call)
class A:
    def test_sum_1(self) -> int:
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


@logging(call)
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Наследник test sum 1")

    def test_sum_2(self):
        print("test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()
