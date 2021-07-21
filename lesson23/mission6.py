while True:
    name = input('Введите Имя: ')
    try:
        answer = int(input(
        'Введите действие \n 1 - Посмотреть текущий текст чата. \n 2 - Отправить сообщение. '
        '\n 3 - Удалить чат. \n 4 - Выйти из программы :\n'))
        if answer == 1:
            with open('chat.txt', 'r', encoding='utf-8') as chat:
                print(chat.read())
        elif answer == 2:
            message = input('Введите сообщение: ')
            with open('chat.txt', 'a', encoding='utf-8') as chat:
                chat.write('{} написал сообщение: {}\n'.format(name, message))
        elif answer == 3:
            with open('chat.txt', 'w', ):
                pass
        elif answer == 4:
            break
        else:
            print('Выбор действия не распознан. Попробуйте еще!')
    except ValueError:
        print('Введено не число!')
