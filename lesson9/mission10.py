password = input('Введите пароль:  ')
text = ''
text_2 = ''
text_3 = ''

count = 0
for letter in password:
    count+=1
    if count %2 == 1:
        text += letter
    if count %2 == 0:
        text_2 += letter
print(text)
for letter in text_2[::-1]:
    text_3 += letter
# text_2 = text_2[::-1]

print(text+text_3)


