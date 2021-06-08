def choise(question, one_more='Неверный ввод. Пожалуйста, введите да или нет.', time=4):
    while time != 0:
        answer1 = input(question)
        if answer1 == 'да':
            print('Сделано')
            break
        elif answer1 == 'нет':
            print('Оставлено')
            break
        else:
            time -= 1
            if time != 0:
                print(one_more)
            print('Осталось попыток: ', time)


question = 'Вы действительно хотите выйти? '
one_more = 'Неверный ввод. Пожалуйста, введите да или нет.'

choise(question, one_more, 4)

choise('Вы хотите удалить файл ')

choise(question='Ты дурочок? ', one_more='Мимо дурачок! Попробуй еще раз! ', time=2)

choise('Как дела? ', 'Промазал', time=3)

choise(question, time=3)

choise(question='dddd', time=5)
