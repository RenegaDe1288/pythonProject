import re

numbers = ['9999999999', '999999-999', '99999x9999']

for i, num in enumerate(numbers):
    if re.match(r'\b8|9\d{9}\b', num) != None:
        print('{} Номер подходит: {}'.format(i+1, num))
    else:
        print('{} Номер  НЕ подходит: {}'.format(i+1, num))
