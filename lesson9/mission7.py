text = input('Введите текст:  ')
count = 0
max = 0
for let in text:
    if let != ' ':
        count += 1
        if max < count:
            max += 1
    elif let == ' ':
        count = 0
print('Самое длинное слово: ', max)