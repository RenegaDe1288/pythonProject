password = 'Карамба'
count = 0
for num in range(1, 11):
    text = input('Введите слово:  ')
    if text == password:
        count += 1
print('Стали пиратами: ', count)
