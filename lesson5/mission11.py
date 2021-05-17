clients = int(input('Сколько клиентов в магазине: '))
sellers = int(input('Сколько продавцов: '))
money = int(input('Сколько получает один продавец: '))
average_load = clients/sellers

if average_load > 4:
    print('Слишком мало продавцов')
    if money < 20000:
        print("З/п руб слишком маленькая")
        money += 2000
        print(money, 'руб так то лучше')
else:
    print('Продавцов достаточно')

print(f'Текущая з/п {money} руб')
