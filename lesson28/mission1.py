import os, io


class File:

    def __init__(self, file_name: str, method: str):
        self.file = file_name
        self.method = method

    def __enter__(self) -> io:
        try:
            self.r = open(os.path.abspath(self.file), self.method, encoding='utf-8')
            return self.r
        except BaseException:
            self.r = open(os.path.abspath(self.file), 'w', encoding='utf-8')
            print('Файл {} создан. Запись прошла успешно.'.format(self.file))
            return self.r

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.r.close()



with File('example1.txt', 'r') as file:
    try:
        file.write('Всем привет!\n')
    except:
        print('Файл открыт в реЖиме чтения. запись невозмоЖна. Удали файл и снова попытайся')
        pass
