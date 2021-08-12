def repeat(num):
    def decorator(func):
        def wrapper(*args, **kwargs):
            total = 0
            print('Налачо работы декоратора')
            for i in range(num):
                print(func(*args, **kwargs))
                total += func(*args, **kwargs)
            print('Конец декоратора')
            return total

        return wrapper

    return decorator


@repeat(4)
def count(x, y):
    return x * y


print(count(2, 4))
