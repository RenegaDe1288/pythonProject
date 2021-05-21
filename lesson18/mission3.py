path = 'C:/user/docs/folder/new_file.txt'
stoplist = '@№$%^&*()'
stoplist = [x for x in stoplist]

if path[0] in stoplist:
    print('Строка начинается  с непозволительного символа')
elif not path.endswith('.txt') or path.endswith('.docs'):
    print('Неправильное разрешение файла! Ожидалось .txt или .docx')
else:
    print('Путь указан верно!')
