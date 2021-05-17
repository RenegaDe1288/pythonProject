x, y = 8, 10

while 0 < x < 15 and 0 < y < 20:
    comand = input('\nВведите команду: ')
    if comand == 'w':
        y += 1
    elif comand == 's':
        y -= 1
    elif comand == 'a':
        x -= 1
    elif comand == 'd':
        x += 1
    else:
        print('[Программа]: Нераспознанная команда. Попробуйте еще раз')
    print('[Программа]: Марсоход находится на позиции:', x, y)
print('Марсоход врезался в стену')

