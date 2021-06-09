import os
# path = 'E:\Games\Destroy All Humans!'

def size(path):
    total = 0
    for i in os.listdir(path):
        link = os.path.join(path, i)
        if os.path.isdir(link):
            total += size(link)
        elif os.path.isfile(link):
            total += os.path.getsize(link)
    return total


while True:
    my_path = input('Укажите путь: ')
    if os.path.exists(my_path):
        if os.path.isfile(my_path):
            print('Это файл \nРазмер файла: ', os.path.getsize(my_path))
        if os.path.isdir(my_path):
            print('Это папка, \nРазмер папки: ', size(my_path), 'байт')
        if os.path.islink(my_path):
            print('Это ссылка')
    else:
        print('Данный путь не существует')
