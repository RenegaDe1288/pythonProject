import time

my_dict = {}


def plug_search(func):
    my_dict[func.__name__] = func
    return func


@plug_search
def timer():
    start = time.time()
    result = count()
    print('Время работы: ', time.time() - start)
    return result


@plug_search
def count():
    result = sum([i ** 4 for i in range(1000000)])
    return result


@plug_search
def count_2():
    result = 0
    for i in range(1000000):
        result += i ** 4
    return result


count()
count_2()
timer()
print(my_dict)
