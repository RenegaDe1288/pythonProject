try:
    file_1 = open('ages.txt','w+', encoding='utf - 8')
    data = input('Введите данные: ')
    try:
        new = int(data)
    except ValueError:
        print('Нельзя преобразовать данные в целое.')
    except RuntimeError:
        print('Неожиданная ошибка.')
    else:
        file_1.write(data)
    finally:
        file_1.close()
except FileNotFoundError:
    print('Проблема при открытии файла.')
