text = input('Введите текст: ').lower()

print(text)
sym_dict = dict()
for sym in text:
    if sym in sym_dict:
        sym_dict[sym] += 1
    else:
        sym_dict[sym] = 1
print(sym_dict)
print('максимальное количество повторений: ', max(sym_dict.values()))


