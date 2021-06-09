text = open('zen.txt', 'r')
text1 = text.read()

symbols_list =[i.lower() for i in text1 if i.isalpha()]
print('Количество латинских букв: ',  len(symbols_list))
min = len(symbols_list)
for sym in symbols_list:
    if symbols_list.count(sym) < min:
        min = symbols_list.count(sym)
        letter = sym

print('Минимальное количество символов {} : {}'.format(letter,min))


text1 = text1.split('\n')
print('Строк: ', len(text1))

all_words = sum(len(line.split(' ')) for line in text1)
print('Слов: ', all_words)

text.close()

