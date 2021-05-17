guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

while True:
    print('Всего гостей: ', len(guests))
    print('Введите добавить гостя или удалить: ', end=' ')
    choice = input('')
    if choice == 'добавить':
        if len(guests) == 6:
            print('Дача полная! Добавить гостей невозможно!')
        else:
            new_guest = input('Введите имя гостя: ')
            print('Привет ', new_guest)
            guests.append(new_guest)
    elif choice == 'удалить':
        new_guest = input('Введите имя гостя для удаления: ')
        if new_guest in guests:
            print('Ушел  ', new_guest)
            guests.remove(new_guest)
        else:
            print('Такого гостя нет!')
    elif choice =='спать':
        break

print('Гостей осталось: ', guests)
print('Вечеринка закончилась, все легли спать.')

