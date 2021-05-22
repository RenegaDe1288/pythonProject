my_string = ' ab1n32kz2'
my_string = [x for x in my_string]
new = set(my_string)
new1 = ''.join([x for x in new if x.isnumeric()])
print('Различные цифры строки: ', new1)
