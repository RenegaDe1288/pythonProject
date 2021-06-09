text = open('zen.txt', 'r')
text1 = text.read()

summa = sum(1 for i in text1 if i.isalpha())
print('Количество латинских букв: ',  summa)

text1 = text1.split('\n')
print('Строк: ', len(text1))

all_words = sum(len(line.split(' ')) for line in text1)
print('Слов: ', all_words)

text.close()

