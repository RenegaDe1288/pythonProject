def decorator(func):
    func.count = 0
    """ создание атрибута функции - счетчика"""

    def wraper(name, age=None):
        """ начало работы счетчика функции"""

        func.count += 1
        print('Функция вызвана в {} раз'.format(func.count))
        print('Вызвана функция: {} и ее аргументы: {} '.format(func.__name__, check(name, age)))
        out = func(name, age)
        print('Функция возвращает: ', out)
        return print(out, '\n')

    return wraper


@decorator
def greeting(name, age=None):
    if age:
        return "Ого, {name}! Тебе уже {age} лет, ты быстро растёшь!".format(name=name, age=age)
    else:
        return "Привет, {name}!".format(name=name)


"""Проверка наличия None элементов"""

def check(*args, **kwargs):
    if args[1] == None:
        return (args[0])
    return args


greeting("Том")

greeting("Миша", age=100)

greeting(name="Катя", age=16)
