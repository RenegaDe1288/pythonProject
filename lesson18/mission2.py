text  = input('Введите текст ').split()
max = ''
for word in text:
    if len(word) > len(max):
        max = word
print('Слово с максимальным количеством букв: {} , букв = {}'.format(max, len(max)))