"""Решение №1 через модуль Itertools"""

from itertools import product

list_1 = [2, 5, 7, 10]
list_2 = [3, 8, 4, 9]

for a, b in product(list_1, list_2):
    if (a * b) == 56:
        print('Найдены числа :', a, b)

""" Решение №2 через генераторное выражение"""


def search(i, y):
    if i * y == 56:
        return i, y


list_1 = [2, 5, 7, 10]
list_2 = [3, 8, 4, 9]
list_3 = (search(i, y) for i in list_1 for y in list_2)

for i in list_3:
    if isinstance(i, tuple):
        print('Найдены числа :', i[0], i[1])

"""Решение №3 через генератор - функцию"""


def search(list_1, list_2):
    for i in list_1:
        for y in list_2:
            if i * y == 56:
                yield i, y


list_1 = [2, 5, 7, 10]
list_2 = [3, 8, 4, 9]
list_3 = search(list_1, list_2)

for i in list_3:
    print('Найдены числа :', i[0], i[1])
