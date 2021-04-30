number = int(input('Введите число: '))
summ = 0
for num in range(1, number + 1, 5):
    summ += num
    print('Номер стула ', num, 'сумма равна ', summ)

