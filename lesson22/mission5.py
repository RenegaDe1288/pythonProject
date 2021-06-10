import os


def file_path_check():
    while True:
        path = input('Куда хотите сохранить документ?'
                     ' \nВведите последовательность папок (через пробел): ').split()
        link = os.path.join('C:\\', ('\\'.join(path)))
        if os.path.exists(link):
            return link
        else:
            print('Указанный путь не существует.')


def write_text(folder, text_to_write):
    os.chdir(folder)
    print("Текущая директория: ", os.getcwd())
    file = open(name, 'w', encoding='utf-8')
    file.write(text_to_write)
    file.close()
    print('Файл {} успешно перезаписан!'.format(name))


all_path = file_path_check()
text = input('Введите текст для записи: ')

while True:
    name = input('Введите имя файла: ')
    if os.path.exists(os.path.join(all_path, name)):
        answer = input('Файл с таким именем уже существует!'
                       '\nВы действительно хотите перезаписать файл?  ')
        if answer == 'да':
            write_text(all_path, text)
            break
        else:
            all_path = file_path_check()
    else:
        write_text(all_path, text)
        break
