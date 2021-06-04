def add_contact(data):
    global tel_book
    for i in tel_book.keys():
        if (data[0], data[1]) == i:
            print('Данный человек уже занесен в телефонную книгу')
            print(i, tel_book[i])
            break
    else:
        tel_book[(data[0], data[1])] = data[2]
        print(tel_book)


def search(sur):
    global tel_book
    list1 = [print(name, tel) for name, tel in tel_book.items() if sur in name]
    if len(list1) == 0:
        print('Человек с данной фамилией не найден в телефонной книге')


tel_book = {}
while True:
    action = int(input('Введите действие: Добавить контакт/Поиск человека по фамилии: (1 или 2) '))
    if action == 1:
        data_all = input('Введите Имя/Фамилию/телефон: ').title()
        add_contact(data_all.split())
    elif action == 2:
        surname = input('Введите Фамилию: ').title()
        search(surname)
