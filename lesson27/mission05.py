from typing import Callable


def bread(func: Callable):
    def wrapper():
        print('/----------\\')
        func()
        print('<\______/>')

    return wrapper


def vegitebles(func: Callable):
    def wrapper1():
        print('#помидоры#')
        func()
        print('~салат~')

    return wrapper1


@bread
@vegitebles
def ham():
    print('--ветчина--')


ham()
