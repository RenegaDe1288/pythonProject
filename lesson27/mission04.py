import time
from typing import Callable


def timer(func: Callable):
    def wrapper(num):
        start = time.time()
        result = func(num)
        print('Время работы: ', time.time() - start)
        return result

    return wrapper


@timer
def count(num: int):
    result = sum([i ** 4 for i in range(num)])
    return result


@timer
def count_2(num: int):
    result = 0
    for i in range(num):
        result += i ** 4
    return result


print(count(1000000))
print(count_2(1000000))
