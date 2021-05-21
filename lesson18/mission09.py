text = input('Введите сообщение: ')

num = [1 if letter.islower() else 0 for letter in text]
if num.count(1) >= num.count(0):
    text = text.lower()
else:
    text = text.upper()

# text_1 = ''.join([letter.lower() if num.count(1) >= num.count(0)
#                   else letter.upper()
#                   for letter in text])

print(text)
