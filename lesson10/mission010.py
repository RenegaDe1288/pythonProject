lent = int(input('Введите размер очереди: '))

for row in range(lent+1):
    print(' В час ', row, 'остались номера: ', end=' ')
    for col in range(lent+1):
        if col <= lent -row:
            print(col+row, end=('\t'))
    print()
