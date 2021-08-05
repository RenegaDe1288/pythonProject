import os


def count(file):
    with open(file, 'r', encoding='utf-8') as new:
        strings = sum([1 for line in new if line != '\n'])
        print('Количество строк в файле: {} -- {}'.format(file, strings))
        return strings


link = os.listdir('C:/Users/MSI/PycharmProjects/pythonProject/lesson26/')
list1 = (file for file in link if file.endswith('.py'))
total_sum = sum([count(file) for file in list1])
print('\nОбщее количество сток: ', total_sum)
