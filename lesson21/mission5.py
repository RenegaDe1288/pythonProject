import math


def calculating_math_func(num, book={}):
    if num in book:
        print('Результат по цифре {} найден в библиотеке : {}'.format(num, book[num]))

    else:
        result = (math.factorial(num) / num ** 3) ** 10
        book.update({num: result})
        print('Результат вычислений по цифре {} равен : {}  '.format(num, result))


calculating_math_func(3)
calculating_math_func(4)
calculating_math_func(3)
calculating_math_func(4)
calculating_math_func(5)
calculating_math_func(3)
