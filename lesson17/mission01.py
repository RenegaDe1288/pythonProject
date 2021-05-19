first_num =int(input('Левая граница: '))
second_num =int(input('Правая граница: '))
list_1 = [num**3 for num in range(first_num, second_num+1)]
list_2 = [num**2 for num in range(first_num, second_num+1)]
print('Кубы чисел в диапазоне: ', list_1)
print('Квадраты чисел в диапазоне: ', list_2)