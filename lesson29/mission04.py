import time

def repeat(num :int= 1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            total = 0
            print('Налачо работы декоратора')
            for i in range(num):
                time.sleep(num)
                print(func(*args, **kwargs))
                total += func(*args, **kwargs)
            print('Конец декоратора')
            return total

        return wrapper

    return decorator


@repeat()
def count(x, y):
    return x * y


print(count(2, 4))