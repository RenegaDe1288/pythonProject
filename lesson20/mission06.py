def check(text):
    new_list = []
    try:
        if iter(text):
            new_list = [value for index, value in enumerate(text) if index % 2 == 0]
    except TypeError:
            print('error')
    print(new_list)
    return new_list


text = input('Введите текст: ')

new_list1 = [value for index, value in enumerate(text) if index % 2 == 0]
print(new_list1)
new_list3 = check(text)
new_list4 = check(4)
