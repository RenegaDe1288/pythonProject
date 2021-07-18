# import random
#
#
# def f(x, y):
#     x += random.randint(0, 10)
#     y += random.randint(0, 5)
#     print('1  ', x, y)
#     try:
#         return x / y
#     except ZeroDivisionError:
#         print('Деление на ноль в первой функции невозможно')
#         return None
#
# def f2(x, y):
#     x -= random.randint(9, 10)
#     y -= random.randint(4, 5)
#     print('2  ', x,y)
#     try:
#         return x / y
#     except ZeroDivisionError:
#         print('Деление на ноль во второй функции невозможно')
#         return None
#
#
# file = open('coordinates.txt', 'r')
# file_2 = open('result.txt', 'w')
# for pos, line in enumerate(file):
#     my_list = []
#     nums_list = line.split()
#     res1 = f(int(nums_list[0]), int(nums_list[1]))
#     res2 = f2(int(nums_list[0]), int(nums_list[1]))
#     number = random.randint(0, 100)
#     try:
#         my_list = sorted([res1, res2, number])
#         print(my_list)
#         file_2.write('\n'+str(my_list))
#     except TypeError:
#         print('В подсчетах строки {} было деление на ноль'.format(pos+1))
# file.close()
# file_2.close()


import random


def f(x, y):
    x += random.randint(0, 10)
    y += random.randint(0, 5)
    return x / y

def f2(x, y):
    x -= random.randint(9, 10)
    y -= random.randint(4, 5)
    return y / x

file = open('coordinates.txt', 'r')
file_2 = open('result.txt', 'w')
for line in file:
    nums_list = line.split()
    try:
        res1 = f(int(nums_list[0]), int(nums_list[1]))
        res2 = f2(int(nums_list[0]), int(nums_list[1]))
        number = random.randint(0, 100)
        my_list = sorted([res1, res2, number])
        print(my_list)
        file_2.write(str(my_list)+'\n')
    except (TypeError, ZeroDivisionError):
        print('Деление на ноль невозможно \nНевозможно сформировать список')
file.close()
file_2.close()

