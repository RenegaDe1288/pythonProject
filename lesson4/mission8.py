hours = int(input('Введите отработанные часы: '))
rest = int(input('Введите остаток по кредиту: '))
expenses = int(input('Введите траты на еду: '))
money = (200 * hours) / 2**3 + hours
if money >= expenses + rest:
    print('Часов хватает. Можно отдохнуть')
else:
    print('Часов не хватает. Придётся поработать!')
print(' Заработано: ', money)
