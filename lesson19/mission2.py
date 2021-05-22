
numbers = int(input('Введите количество стран: '))
total_dict = {}

for x in range(numbers):
    print('страна номер {} : '.format(x+1), end='')
    country = input('').split()
    dictionary = {country[0]: country[1::]}
    total_dict.update(dictionary)

print(total_dict)

while True:
    town = input('Введите город: ')
    for i in total_dict.keys():
        if town in total_dict[i]:
            print('Город {} расположен в стране {}'. format(town, i))
            break
    else:
        print('Город {} не обнаружен. Попробуйте снова. '.format(town))
