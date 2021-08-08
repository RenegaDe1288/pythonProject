import os

class File:

    def __init__(self,file,method):
        self.file = file
        self.method = method

    def __enter__(self):
        try:
            self.r = open(os.path.abspath(self.file),self.method,encoding='utf-8')
            return self.r
        except :
            self.r = open(os.path.abspath(self.file), 'w', encoding='utf-8')
            print('Файл {} создан'.format(self.file))
            return self.r




    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            self.r.close()
        except Exception:
            self.r.close()
            print('Подавлена ошибка!')


with File('example1.txt', 'r') as file:
    try:
      file.write('Всем привет!\n')
    except:
        print('Файл открыт в реЖиме чтенияю запись невозмоЖна. Удали файл и снова попытайся')
        pass
