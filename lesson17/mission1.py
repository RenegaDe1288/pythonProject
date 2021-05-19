def count(let):
    for i in letters:
        if i == let:
            return True
    return False


text = input('Введите текст для анализа: ')
letters = ['а', 'у', 'о', 'е', 'и', 'ю', 'я', 'э', 'ы']
new_list = [letter for letter in text if count(letter)]
print('Список гласных букв:  ', new_list, '\nКоличество гласных = ', len(new_list))
