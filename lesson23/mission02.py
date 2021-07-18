import random
import string


ages_file = open('ages.txt','r', encoding= 'utf-8')
try:
    file = input('ВВедите: ')
    result_file = open(file, 'x', encoding='utf - 8')
    for str, line in enumerate(ages_file):
        try:
            age = int(line)
            if age <= 0:
                try:
                    x = 100/(age-age)
                except ZeroDivisionError:
                    print('Некорректное значение в строке: ', str + 1)
                    print(line)
            else:
                result_file.write(random.choice(string.ascii_lowercase) + ' ' + line)
        except ValueError:
            print('Неверный тип данных в строке: ', str + 1)
            print(line)
    ages_file.close()
    result_file.close()
except FileExistsError:
    print('Попытка создания файла, который уже существует.')
except PermissionError:
    print('На чтение ожидался файл, но это оказалась директория.')








