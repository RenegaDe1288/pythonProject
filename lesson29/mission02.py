import os
from contextlib import contextmanager

@contextmanager
def in_dir(path):
    my_path = os.getcwd()
    try:
        os.chdir(path)
        print('Мы в каталоге: ', os.getcwd())
        yield
    except Exception as ex:
        print(ex)
    finally:
        os.chdir(my_path)
        print('Мы вернулись в рабочую директорию: ', os.getcwd())





with in_dir('C:\\'):

    print(os.listdir())