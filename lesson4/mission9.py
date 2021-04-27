dial = int(input('Введите значение циферблата: '))
number = int(input('Введите число:  '))
total = dial//100 + dial%100//10 + dial%10
if total > number:
    print('Сброс ')
else:
    print('Сегодня не сломался')
print(total)