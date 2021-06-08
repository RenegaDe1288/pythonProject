object = (1, 2, 3)
if isinstance(object, list or dict or set):
    print('Объект изменяемый')
else:
    print('Объект неизменяемый')
print('Тип данных:', type(object))
print('Id объекта: ', id(object))
