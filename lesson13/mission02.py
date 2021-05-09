import math


def gsd(number_1, number_2):
    delif = math.gcd(number_1, number_2)
    return delif


n = int(input('Введите первое число:  '))
x = int(input('Введите второе число:  '))

delif = gsd(n, x)
print('НОД равен ', delif)
