text = 'Mama myla ramutttttуууапtt.'
text_list = [sym.lower() for sym in text if sym.isalpha()]

len_text = len(text_list)
letterts = set(text_list)
dict_letters = {}

for sym in letterts:
    percent = round((text_list.count(sym)) / len_text, 3)
    if percent in dict_letters:
        dict_letters[percent].append(sym)
    else:
        dict_letters[percent] = [sym]

file = open('analysis.txt', 'w', encoding='utf-8')

for key in sorted(dict_letters, reverse=True):
    for letter in sorted(dict_letters[key]):
        file.write(letter + ' ' + str(key) + '\n')

file.close()
