text = input('Введите шаблон сообщения: с{name} и {age} ')
names_list = input('Введите список имен через запятую: ').split(',')
ages_list = input('Введите список  возростов: ').split()
list = [print
        (text.format(name=names_list[x], age=ages_list[x]))
        for x in range(len(names_list))]

happy = [' '.join([names_list[x], ages_list[x]])
        for x in range(len(names_list))]

happy_str = ','.join(happy)
print('Список именинников: ', happy_str)
