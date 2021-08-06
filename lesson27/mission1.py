import time

def how_are_you(func):
    def wrapper():
        answer = input('Как дела?  ')
        print('А у меня не очень! Ладно, держи свою функцию.')
        x = func()
        if x:
            return x
    return wrapper


@how_are_you
def test():
    print('<Тут что-то происходит...>')


@how_are_you
def timer():
    start = time.time()
    result = count()
    print('Время работы: ', time.time() - start)
    return result


@how_are_you
def count():
    result = sum([i ** 4 for i in range(1000000)])
    return result


@how_are_you
def count_2():
    result = 0
    for i in range(1000000):
        result += i ** 4
    return result

test()
print(timer())
print(count())
print(count_2())