lent = int(input('Введите значение стороны: '))
for row in range(lent):
    for col in range(lent):
        if row == 0:
            print('-', end='')
        elif (col == 0 or col == lent - 1) and row > 0:
            print('|', end='')
        else:
            print('', end=(' '))
    print()
