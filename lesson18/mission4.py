def up(word):
    new_word = ''.join([x.upper() if word[0] == x else x for x in word])
    return new_word


# text = 'Кажется, я забыл выключить утюг'
# print(text.title())

text = 'Кажется, я забыл выключить утюг'.split()
text_list = ' '.join([up(word) for word in text])
print('Результат:', text_list)
