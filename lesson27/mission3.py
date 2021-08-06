import time
from typing import Callable
from traceback import format_exc


def timer(func: Callable):
    def wrapper(num):
        print('Вызываю функцию: ', func.__name__)
        try:
            result = func(num)
            print('Ваш результат: \t', result)
        except Exception:
            """ запись в лог файл ошибки"""
            print('выполнить функцию {} не удалось: '.format(func.__name__))
            with open('function_errors.txt', 'w', encoding='utf-8') as file:
                file.write(
                    'Дата ошибки: {} \n Имя функции: {} \nКод ошибки: {}'.format(time.strftime("%c", time.localtime()),
                                                                                 func.__name__, format_exc()))

    return wrapper


@timer
def count(num: int):
    """функия для посчета суммы каждого числа от 0 до num в степени 4"""
    result = sum([i ** 4 for i in range(num)])
    return result


@timer
def count2():
    """функия для посчета суммы каждого числа от 0 до num в степени 4"""
    result = sum([i ** 4 for i in range(num)])
    return result


count(10000)
count2(100)
