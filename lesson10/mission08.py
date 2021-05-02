lent = int(input('Введите ширину '))
lent_2 = int(input('Введите длину '))

for row in range(lent):
    for col in range(lent_2):
        if col == lent_2 // 2 and row != lent//2:
            print('|', end='')
        elif row == lent // 2:
            print('-', end='')
        elif col == lent_2//2 + 5+ row:
            print('\\', end='')
        elif col == lent_2//2- row -5:
            print('/', end='')
        else:
            print(' ', end='')
    print()

