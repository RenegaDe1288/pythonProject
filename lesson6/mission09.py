balance = int(input('Введите стартовую сумму: '))
while balance < 10000:
    points = int(input('Сколько выпало на кубике?  '))
    if points != 3:
        balance += 500
        print('Выиграли 500 рублей!')
        print('Всего сейчас ', balance)
    else:
        balance = 0
        print('Вы проиграли всё!')
        break
else:
    print('у вас: ', balance, 'руб')
print('Игра закончена  ')