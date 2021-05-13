def reverse(number):
    x2 = 0
    while number > 0:
        digit = number % 10
        number = number // 10
        x2 = x2 * 10
        x2 = x2 + digit
    return x2



x = int(input('Введите  1 число: '))
y = int(input('Введите  2 число: '))

x = reverse(x)
y = reverse(y)
print(x,y)
summ = x+y
print('Сумма чисел равна: ', reverse(summ))