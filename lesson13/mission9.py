def factorial(n):
    x = 1
    summa = 1
    while x <= n:
        summa *= x
        x += 1
    return summa


def degree(x, n):
    summa = 1
    for num in range(1, n + 1):
        summa = x * summa
    return summa


# print(degree(2, 4))
#
# print(factorial(5))

precision = 0.001
summ = 1
n = 1
x = 5
y = 1
while abs(y) > precision:
    y = (-1 ** n) * (degree(x, 2 * n)) / factorial(2 * n)
    if n % 2 == 0:
        summ -= y
    else:
        summ += y
    print(y, summ)
    n += 1
print('Сумма ряда = ', summ)
