def factorial(number):
    if number == 1:
        return 1
    new = number * (factorial(number - 1))
    return new


n = int(input('Введите число для факториала: '))
fact = factorial(n)
print('Факториал числа {} равен: {}'.format(n, fact))
