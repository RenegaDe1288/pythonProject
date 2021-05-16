films = [
    'Крепкий орешек', 'Назад в будущее', 'Таксист',
    'Леон', 'Богемская рапсодия', 'Город грехов',
    'Мементо', 'Отступники', 'Деревня',
    'Проклятый остров', 'Начало', 'Матрица'
]

def check(new_film, film_list):
    for new in film_list:
        if new == new_film:
            return True
    return False


my_list = []

while True:
    new_film = input('Введите фильм: ')
    if check(new_film, films):
        comand = input('Введите команду: добавить/удадить/вставить:')
        if comand == 'добавить':
            if check(new_film, my_list):
                print('Такой фильм уже есть:')
            else:
                my_list.append(new_film)
                print(my_list)
        if comand == 'удалить':
            if check(new_film, my_list):
                my_list.remove(new_film)
                print('Фильм удален')
            else:
                print('Такой фильм не существует!')
        if comand == 'вставить':
            if check(new_film, my_list):
                print('Такой фильм уже есть')
            else:
                index = int(input('Введите на какое место поставить: '))
                my_list.insert(index - 1, new_film)
    print('Мой список: ', my_list)
