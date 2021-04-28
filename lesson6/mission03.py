money = int(input('Какую суммы Вы добавите? '))
balance = 0 + money
while balance < 500000:
    print('Не хватает', (500000 - balance), 'руб. на машину')
    money = int(input('Сколько рубликов добавишь? '))
    balance += money
print('Наконецто ты купил свой Логан')
