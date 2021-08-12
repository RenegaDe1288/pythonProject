from typing import Callable


def decorated_decorator(num_1: int, text_1: str, num_2: int, text_2: str):
    def wrapped_1(func: Callable):
        def wrapped_2(*args, **kwargs):
            print('Переданные арги и кварги в декоратор: ', num_1, text_1, num_2, text_2)
            func(*args, **kwargs)

        return wrapped_2

    return wrapped_1


@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    """ Пример декорируемой функции """
    print("Привет", text, num)


decorated_function("Юзер", 101)
