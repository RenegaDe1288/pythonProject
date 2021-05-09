def total(number):
    summ = 0
    for num in range(1, n + 1):
        summ += num
    print('Сумма от 1 до ', n, ' = ', summ)
    return summ


n = int(input('Введите число:  '))


n = total(n)

total(n)