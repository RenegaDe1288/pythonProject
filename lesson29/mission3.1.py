""" Решение с приемом строки в качестве аргумента декоратора
Ответ выводится согласно условиям """


from datetime import datetime
import time


def call(cls, func, string: str):
    def wrapper(*args, **kwargs):
        start = time.time()
        print('Запускается {}.{}. Дата и время запуска: {} '.format(cls.__name__, func.__name__, string))
        func(*args, **kwargs)
        with open('logging.txt', 'a', encoding='utf - 8') as file:
            file.write(str(func) + '\t' + str(datetime.utcnow()) + '\n')
        print('Метод: {} записан'.format(func.__name__))
        print('Завершение {}.{}. Время работы: {} сек'.format(cls.__name__, func.__name__,
                                                              round((time.time() - start), 3)))

    return wrapper


def logging(string: str):
    def wrapper(cls):
        for i in dir(cls):
            if not i.endswith('__'):
                new = getattr(cls, i)
                new2 = call(cls, new, string)
                setattr(cls, i, new2)
        return cls

    return wrapper


@logging('Apr 23 2021 - 21:50:37')
class A:
    def test_sum_1(self) -> int:
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


@logging('Apr 23 2021 - 21:50:37')
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
