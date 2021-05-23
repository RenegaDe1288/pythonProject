text = input('Введите текст: ')

print(text)
sym_dict = dict()
for sym in text:
    if sym in sym_dict:
        sym_dict[sym] += 1
    else:
        sym_dict[sym] = 1


new_dict = {}
for key in sym_dict:
    if sym_dict[key] in new_dict:
        new_dict[sym_dict[key]].append(key)
    else:
        new_dict[sym_dict[key]] = [key]

print('Инвертированный словарь частот:', )
for i in new_dict:
    print(i, ':', new_dict[i])
