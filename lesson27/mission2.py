import time
from typing import Callable


def timer(func: Callable):
    def wrapper(num):
        """ функция для вызова отсрочки исполнения переданной функции"""
        print('Вызову функцию через 3 секунды:')
        for i in range(3, 0, -1):
            print('Осталось подождать:', i)
            time.sleep(1)
        result = func(num)
        print('Ваш результат: \t', end='')
        return result

    return wrapper


@timer
def count(num: int):
    """функия для посчета суммы каждого числа от 0 до num в степени 4"""
    result = sum([i ** 4 for i in range(num)])
    return result


print(count(10000))
