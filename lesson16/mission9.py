friends = int(input('Введите количество друзей: '))
balance = []
for _ in range(friends):
    balance.append(0)

print(balance)

k = int(input('Введите количество расписок: '))

for _ in range(k):
    debtor = int(input('Кому дал в долг: '))
    creditor = int(input('От кого получил в долг: '))
    money = int(input('Сколько денег: '))
    balance[creditor-1] += money
    balance[debtor-1] -= money

for men in range(len(balance)):
    print('Баланс друга: ', men+1, '=  ', balance[men])
