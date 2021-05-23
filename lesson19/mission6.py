n = int(input('Введите количество пар: '))

sinonims = {}

for i in range(n):
    list = input('Введите пару слов через тире: ').split('-')
    for i in list:
        sinonims[i] = list[list.index(i)-1]
print(sinonims)

while True:
    word = input('Введите слово: ').title()
    if word in sinonims:
        print('Синоним слова {} это {}'.format(word, sinonims[word]))
    else:
        print('Такого слова в словаре нет.')


