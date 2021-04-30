text = input('Введите текст: ')
sym_1 = 'Ы'
sym_2 = 'ы'
counts_1 = 0
counts_2 = 0
for symbol in text:
    if symbol == sym_1:
        counts_1 += 1
    if symbol == sym_2:
        counts_2 += 1
print('Букв Ы найдено', counts_1, '. Букв ы найдено', counts_2)
