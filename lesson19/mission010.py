import random

nums_1 = [29, 17, 10, 15, 13, 22, 12, 22, 7, 24, 26, 3, 11, 2, 3, 16, 19, 21, 2, 3, 8, 27, 2, 17, 2, 20, 12, 21, 3, 1]

nums_2 = [16, 21, 30, 24, 5, 7, 23, 13, 11, 5, 21, 5, 19, 9, 12, 9, 15, 16, 29, 8, 16, 1, 22, 15, 16, 9, 1, 13, 21, 21]

sets1 = set(nums_1)
sets2 = set(nums_2)
print('Минимальный элемент первого множества: ', min(sets1))
print('Минимальный элемент второго множества: ', min(sets2))
sets1.remove(min(sets1))
sets1.add(random.randint(100, 200))
sets2.remove(min(sets2))
sets2.add(random.randint(100, 200))

print('Объединение множеств: ', sets1 | sets2)
print('Пересечение множеств: ', sets1 & sets2)
print('Элементы, входящие в nums_2, но не входящие в nums_1: ', sets2 - sets1)

