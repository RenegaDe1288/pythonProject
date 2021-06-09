import os


def find(path, file):
    my_list = []
    for i in os.listdir(path):
        link = os.path.join(path, i)
        if os.path.isdir(link):
            my_list.extend(find(link, file))
        elif os.path.isfile(link) and os.path.split(link)[1] == file:
            my_list.append(link)
            print(link)
    return my_list


my_path = os.path.abspath(os.path.join('..', '..', 'pythonProject'))

file_name = 'mission01.py'
if os.path.exists(my_path):
    print('Найдены следущие файлы: ')
    num_of_files = len(find(my_path, file_name))
    print('\nКоличество найденных файлов: ', num_of_files)
