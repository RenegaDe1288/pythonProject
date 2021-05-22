n = int(input('Введите целое число: '))
quad_dict = {}
for num in range(1, n+1):
    quad_dict[num] = num ** 2
    print(num, ' - ', quad_dict[num])
