chair_1 = int(input('Введите стоимость перовго стула: '))
chair_2 = int(input('Введите стоимость второго стула: '))
chair_3 = int(input('Введите стоимость третьего стула: '))
all_chairs = chair_1 + chair_2 + chair_3
if all_chairs > 10000:
    print(' Сумма чека со скидкой: ', all_chairs * 0.9)
else:
    print('Сумма чека: ', all_chairs)