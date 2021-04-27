experience = int(input('Введите очки опыта: '))
level = 1
if 0 < experience < 1000:
    print('Ваш уровень: ', level)
elif 1000 <= experience < 2500:
    print('Ваш уровень: ', level + 1)
elif 2500 <= experience < 5000:
    print('Ваш уровень: ', level + 2)
else:
    print('Ваш уровень: ', level + 3)
