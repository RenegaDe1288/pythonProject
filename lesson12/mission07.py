def summa(a, b):
    sum = 0
    for num in range(a, b + 1):
        sum += num
        print(sum)
    print('среднее ', sum / (b + 1 - a))


while True:
    a = int(input('Введите начало отрезка: '))
    b = int(input('Введите конец отрезка: '))
    if a >= b:
        print('Ошибка ввода. ')
    else:
        summa(a, b)
