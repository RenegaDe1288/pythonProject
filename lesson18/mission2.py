text = input('Введите текст ').split()
maximum = ''
for word in text:
    if len(word) > len(maximum):
        maximum = word
print('Слово с максимальным количеством букв: {} , букв = {}'.format(maximum, len(maximum)))
