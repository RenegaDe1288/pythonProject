count = 0
message = ''
while count < 4:
    ip = int(input('\nВведите номер: '))
    if 0 <= ip <= 255:
        message += str(ip) + '.'
        count +=1
    else:
        print('Некорректное значение: повторите попытку ')

print(' Адресс компьютера: ', message)





