words = []
counts = [0, 0, 0]
for word in range(3):
    new = input('Введите слово: ')
    words.append(new)
print(words)
text = ''
while text != 'end':
    text = input('Введите слово из рассказа: ')
    for index in range(3):
        if text == words[index]:
            counts[index] += 1

for i in range(3):
    print('слово ', words[i], 'встречается  = ', counts[i], 'раза')
