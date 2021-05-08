def search():
    string = input('Введите текст: ')
    x = input('Какую цифру ищем: ')
    y = input('Какую букву ищем: ')
    countx = 0
    county = 0
    for letter in string:
        if letter == x:
            countx += 1
        if letter == y:
            county += 1
    print('\nЦифр ', x, 'в тексте = ', countx)
    print('Букв ', y, 'в тексте = ', county)

search()
