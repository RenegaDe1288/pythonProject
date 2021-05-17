x = int(input('Введите первоначальную сумму: '))
y = int(input('Введите желаемую сумму: '))
p = int(input('Введие процент по вкладу: '))
years = 0
while x < y:
    x += round( x * (p / 100), 2)
    years += 1
print('Потребуется лет: ', years)
print('Сумма на счету будет: ', x)

# x = round(13.5555, 2)
# print(x)
