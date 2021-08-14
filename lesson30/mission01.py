# def decotator(func):
#     count = 0
#     def wrapper(*args,**kwargs):
#         nonlocal count
#         count += 1
#         print(func(*args,**kwargs))
#         print(count)
#     return wrapper

def decotator(func):
    def wrapper(*args,**kwargs):
        global count
        count += 1
        print(func(*args,**kwargs))
        print(count)
    return wrapper



@decotator
def mem(x,y):
    return x*y


count = 0
mem(2,3)
mem(2,3)
mem(2,3)
mem(2,3)
mem(2,3)
mem(2,3)


names = globals()['__builtins__'].__dict__.keys()
builtins = sorted([name for name in names if not name.startswith('_')])
print(builtins)

