contacts = dict()

while True:
    contact = input('Введите имя и телефон через пробел: ').split()
    if contact[0].isalpha() and contact[1].isdigit():
        if contact[0] not in contacts:
            contacts[contact[0]] = contact[1]
            print(contacts)
        else:
            print('Данное имя уже есть в списке контактов.')
            break
    else:
        print('Введены некорректные данные: ')
