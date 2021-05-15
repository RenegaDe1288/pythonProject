films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 'Богемская рапсодия', 'Город грехов', 'Мементо', 'Отступники', 'Деревня']
favorite_films = []
search_film = input('Введите фильм: ')
while search_film != '':
    count = 0
    for i in range(len(films)):
        if films[i] == search_film:
            favorite_films.append(films[i])
            print('Фильм добавлен в список любимых')
            count = 1
    if count == 0:
            print('Данного фильма нет в списке')
    search_film = input('Введите фильм: ')
print('Список любимых фильмов: ', favorite_films)
