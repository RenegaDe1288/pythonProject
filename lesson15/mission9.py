word = input('ВВедите слово: ')

my_list = list(word)
count = 0
for i in range(len(my_list)):
    if my_list[i] == my_list[-i-1]:
        count += 1
if count == len(my_list):
    print('Слово является паллиндромом')
else:
    print('Не паллиндром')

