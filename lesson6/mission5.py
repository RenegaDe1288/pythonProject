# 1 решение без цикла
ticket = int(input('Введите номер билетика:'))
part_1 = ticket % 10 + (ticket // 10) % 10 + (ticket // 100) % 10
part_2 = ticket // 100000 + (ticket // 10000) % 10 + (ticket // 1000) % 10
if part_2 == part_1:
    print('Счастливый билетик')
else:
    print('Неудача')

# 2 решение с циклом и обнулением
ticket = int(input('Введите номер билетика:'))
summ_part_1 = 0
summ_part_2 = 0
n = 0
while n < 3:
    number = ticket % 10
    summ_part_1 += number
    ticket = ticket // 10
    n += 1
print('Вторая половинка =', summ_part_1)
n = 0
while n < 3:
    number = ticket % 10
    summ_part_2 += number
    ticket = ticket // 10
    n += 1
print('Первая половинка  = ', summ_part_2)
if summ_part_2 == summ_part_1:
    print('Счастливый билетик')
else:
    print('Неудачник')

# 3 решение с циклом

ticket = int(input('Введите номер билетика:'))
summ_part_1 = 0
summ_part_2 = 0
n = 0
while n < 6:
    if n < 3:
        number = ticket % 10
        summ_part_1 += number
        ticket = ticket // 10
        n += 1
    if n >= 3:
        number = ticket % 10
        summ_part_2 += number
        ticket = ticket // 10
        n += 1
print('Вторая половинка =', summ_part_1)
print('Первая половинка  = ', summ_part_2)
if summ_part_2 == summ_part_1:
    print('Счастливый билетик')
else:
    print('Неудачник')
