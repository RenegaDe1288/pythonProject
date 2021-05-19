message = input('Введите строку: ')
symbol = input('ВВедите символ: ')
list_1 = [letter * 2 for letter in message]
list_2 = [letter + symbol for letter in list_1]
print('Список удвоенных символов: ', list_1)
print('Склейка с дополнительным символом: ', list_2)
