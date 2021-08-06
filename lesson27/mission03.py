def decorator(func):
    def wrapper(name):
        func(name)
        func(name)
    return wrapper



@decorator
def greeting(name):
    print('Привет, {name}!'.format(name=name))


greeting('Ivan')