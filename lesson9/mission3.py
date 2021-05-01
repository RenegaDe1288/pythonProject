text = input('Введите слово:  ')
count = 1
for num in text:
    if num != '*':
        count += 1
    else:
        print('Звездочка находится на месте: ', count)
        break
