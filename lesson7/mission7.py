num_1 = int(input('Введите первое число:'))
num_2 = int(input('Введите второе число:'))
total = 0
count = 0
for number in range(num_1, num_2 + 1):
    if number % 3 == 0:
        total += number
        count += 1
total = total / count
print('Среднее арифметиское отрезка равно ', total)