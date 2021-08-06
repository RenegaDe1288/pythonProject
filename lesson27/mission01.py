def func_2(funk, i):
    num = funk(i) * funk(i)
    return num


def func_1(x):
    return x + 10


print(func_2(func_1, 9))
