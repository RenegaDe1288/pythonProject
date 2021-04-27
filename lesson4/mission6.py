number_1 = int(input('Кубик Кости: '))
number_2 = int(input('Кубик Владельца: '))
if number_1 >= number_2:
    print('Сумма: ', number_1 - number_2)
    print('Костя платит')
else:
    print('Сумма: ', number_2 + number_1)
    print('Владелец платит')
print('Игра окончена')
