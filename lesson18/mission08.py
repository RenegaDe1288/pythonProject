path = input('Введите путь к файлу: ')
if  not path.endswith('.txt'):
    print('Неверное расширение файла. ')
elif not path.startswith('C'):
    print('Директория не обнаружена.')
else:
    print('Верный путь: ', path)