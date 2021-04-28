import  random
balance = random. randint(1, 9999)
print('Начальная сумма: ', balance)
while balance < 10000:
    points = random. randint(1, 6)
    print('Кубик', points)
    if points != 3:
        balance += 500
        print('Выиграли 500 рублей!')
        print('Всего сейчас ', balance)
    else:
        balance = 0
        print('Вы проиграли всё!')
        print('ИТОГО у вас: ', balance, 'руб')
        break
print('Игра закончена  ')