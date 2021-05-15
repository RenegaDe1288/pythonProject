new_list = list(input('введите строку: '))
count = 0
for index in new_list:
    if index == ':':
        print(';', end='')
        count +=1
    else:
        print(index, end='')
print('\nКоличество замен = ', count)
