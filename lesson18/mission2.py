text = input('Введите текст ').split()
maximum = ''
for word in text:
    if len(word) > len(max):
        maximum = word
print('Слово с максимальным количеством букв: {} , букв = {}'.format(max, len(max)))
