lent = int(input('Введите ширину '))

for row in range(lent):
    for col in range(lent):
        if col == lent -1 -row:
            print('1', end=('\t'))
        elif col < lent - row -1:
            print('0', end='\t')
        else:
            print('2', end='\t')
    print()