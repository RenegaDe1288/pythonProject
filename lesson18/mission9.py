text = 'Хотя ,. возм:ожно и нет.'
word = ''
reversed_text = ''


for sym in text:
    if sym.isalpha():
        word += sym
    else:
        reversed_text += word[::-1] + sym
        word = ''
print('Новое сообщение:', reversed_text)
