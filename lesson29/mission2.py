
def callback(value):
    def decorator (func):
        def wrapper():
            if value == '//':
                result = func()
                return result
        return wrapper
    return decorator



@callback('//')
def route():
    print('Ответ сервера 200')
    return 'OK'


app = {'//': route}

route = app.get('//')

if route:

    response = route()

    print('Ответ:', response)

else:

    print('Такого пути нет')