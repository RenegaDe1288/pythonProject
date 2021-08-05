"""Решение № 1 циклом-рекурсией  без генератора """
#
import os


def size(path):
    for i in os.listdir(path):
        link = os.path.join(path, i)
        if os.path.isfile(link):
            print('Файл: ', link)
        elif os.path.isdir(link):
            if i == 'Movie':
                print('\nНайден каталог: ', link)
                return True
            else:
                if size(link):  # Рекурсия
                    return True


path1 = 'E:\\Games'
size(path1)

"""Решение № 2 с 1 циклом  и с помощью повторного вызова генератора"""


def size(path: str):  # Генератор для проверки имени директории и вывода файлов
    global flag
    for i in os.listdir(path):
        print(i)
        link = os.path.join(path, i)
        if os.path.isfile(link):
            yield link
        elif os.path.isdir(link):
            if i == 'Movie':
                print('\nКаталог найден: ', link)
                flag = 1
                return True
            else:
                if circle(link):  # Создание генератора и цикла для нового каталога
                    return True


def circle(path1: str):  # цикл для повторного запуска генератора
    new_path = size(path1)
    for i in new_path:
        if flag == 0:
            print(i)
        else:
            break


flag = 0  # Для остановки поиска
path1 = 'E:\\Games'
circle(path1)
