len = int(input('Введите ширину: '))

for row in range(len):
    for col in range(len):
        if col == row:
            print('^', end='')
        if row == len - col-1:
            print('^', end='')
        else:
            print(' ', end='')

    print(' ')

