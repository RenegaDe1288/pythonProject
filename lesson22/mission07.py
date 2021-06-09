import os
import random


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
    my_list = find(my_path, file_name)
    num_of_files = len(my_list)
    print('\nКоличество найденных файлов: ', num_of_files)

print()
x = random.randint(0, num_of_files)
print('Открыт файл: ', my_list[x])
print()
text = open(my_list[x], 'r', encoding='utf-8')
print(text.read())
text.close()
