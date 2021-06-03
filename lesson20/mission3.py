def slice(text, n):
    tuple_1 = tuple([sym for sym in text])
    list_1 = [index for index, value in enumerate(tuple_1) if value == n]
    print('Индексы элементов: {} : {} '.format(n, list_1))
    if len(list_1) >= 2:
        new_tuple = tuple_1[list_1[0]:list_1[1] + 1]
        print('Обнаружено 2 или более  элемента : {} . Новый кортеж {}'.format(n, new_tuple))
    elif len(list_1) == 1:
        new_tuple = tuple_1[list_1[0]:]
        print('Обнаружен 1 элемент : {}. Новый кортеж {}'.format(n, new_tuple))
    else:
        print('Элементов {} не обнаружено. Вывожу пустой котреж {}'.format(n, ()))


n = input('Введите значение для поиска: ')
text = input('Введите строку  в которой ищем: ')
slice(text, n)
