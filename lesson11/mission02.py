age = int(input('Введите возраст именинника: '))
temp = float(input('Введите температуру тела:  '))
gift = round(1000 * age * temp, 0)
print('Отец подарит сыну : ', gift, 'рублей')
