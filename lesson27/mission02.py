import time

def timer (func):
    start = time.time()
    result = func()
    print('Время работы: ',time.time()-start)
    return result

def count():
    result = sum([i**4 for i in range(1000000)])
    return result


def count_2():
    result = 0
    for i in range(1000000):
        result += i**4
    return result

print(timer(count))
print(timer(count_2))


def timer2():
    start = time.time()
    result = count()
    print('Время работы: ',time.time()-start)
    return result

print(timer2())

