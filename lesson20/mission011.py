tel_book = {}
while len(tel_book) < 3:
    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    tel = input('Введите телефон: ')
    if (name,surname) not in tel_book:
        tel_book[(name,surname)] = tel
    else:
        print('Имя уже в списке!')
else:
    print('Телефонная книга преполнена!')
print(tel_book)
