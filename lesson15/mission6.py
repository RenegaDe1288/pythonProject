word = input('Введите слово: ')
lis = list(word)
new = []
for sym in word:
    count = 0
    for i in range(len(lis)):
        if sym == lis[i]:
            count += 1
    if count < 2:
        new.append(sym)

print('Количество уникальных букв: ', len(new))
