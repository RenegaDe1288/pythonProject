firth_num = int(input('Введите первое число: '))
second_num = int(input('Введите второе число: '))
summ = 0
for number in range(firth_num, second_num + 1):
    summ += number
print(summ)
