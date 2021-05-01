len = int(input('Введите ширину: '))
len_2 = int(input('Введите длинну:  '))
for row in range(len):
    for col in range(len_2):
        if col == 0 or col == len_2-1:
            print('|', end='')
        elif row == 0 or row == len-1:
            print('-', end='')
        else:
            print(' ', end='')
    print(' ')

