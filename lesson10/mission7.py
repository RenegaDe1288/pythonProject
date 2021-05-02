lent = int(input('Введите количество цифр: '))
max = 0
for num in range(1, lent + 1):
    number = int(input('\nВведите число:'))
    summ = 0
    while number > 0:
        rest = number % 10
        number = number // 10
        summ += rest
        if summ > max:
            max = summ
            max_number = num
    print('сумма чисел числа', num, ' равен', summ)
print('\nМаксимальная Сумма числа', max_number, ' равна', max)
