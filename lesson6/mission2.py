name = input('Введите Ваше имя: ')
debt = int(input('Введите сумму долга: '))
print(' На имя', name, 'найдено долгов на сумму: ', debt)
while debt > 0:
    contribution = int(input('Введите сумму погашения:'))
    debt -= contribution
    if debt >= 0:
        print('Остаток долга :', debt)
print('Вы погасили долг')
if debt < 0:
    debt = debt - debt - debt
    print(' Вы переплатили', debt, 'и они возвращены')
