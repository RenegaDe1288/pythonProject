text = input('Введите слово:  ')
count = 0
letter = 's'
max = 0
for let in text:
    if letter == let:
        count += 1
        if max < count:
            max += 1
    elif letter != let:
        count = 0
print('Самая длинная последовательность', max)
