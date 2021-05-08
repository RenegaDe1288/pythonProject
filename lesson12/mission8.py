def gcd(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    print('Наибольший общий делитель = ', a)


a = int(input('Введите превое число: '))
b = int(input('Введите второе число: '))
gcd(a, b)

# count = 0
# count2 = 0
#
# a = int(input('Введите превое число: '))
# b = int(input('Введите второе число: '))
# for num in range(2, a):
#     if a%num == 0:
#         count += 1
#         nod = num
# if count == 0:
#     nod = 1
# print(nod)
# for num in range(2, b):
#     if b%num == 0:
#         count2 += 1
#         nod2 = num
# if count2 == 0:
#      nod2 = 1
# for num in range (a,b,a)
# print(nod2)
