count = 0
positive = 0
negative = 0
while True:
    number_1 = int(input('Введите  оценку:'))
    count += 1
    if number_1 < 0:
        negative += 1
    elif number_1 > 0:
        positive += 1
    elif number_1 == 0:
        break
print('Кол-во отрицательных оценок: ', negative)
print('Кол-во положительных оценок: ', positive)

