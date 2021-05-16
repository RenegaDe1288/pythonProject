def count(str):
    count = 0
    for sym in str:
        if sym == '!' or sym == '?':
            count += 1
    return count


str1 = input('Введите первую строку: ')
str2 = input('Введите вторую строку: ')


if count(str1) > count(str2):
    print('Новая строка: ', str1+str2)
elif count(str2) > count(str1):
    print('Новая строка: ', str2+str1)
else:
    print('ОЙ')
