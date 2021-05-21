def number(password):
    count = len([x for x in password if x.isdigit()])
    return count


while True:
    password = input('Введите пароль: ')
    if len(password) < 8 or sum(map(str.isupper, password)) < 1 or number(password) < 3:
        print('Ошибка ввода')
    else:
        print('DONE')
        break
