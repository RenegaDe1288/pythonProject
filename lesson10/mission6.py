# all = 1
# summ = 0
# lent = int(input('Введите количество чисел:'))
# for num in range(1, lent+1):
#     fact = all*num
#     all = fact
#     summ += all
#     print('Факториал от числа', num, ' равен', fact)
# print('Сумма равна', summ)
#
# all = 1
# summ = 0
# fact =1
# lent = int(input('Введите количество чисел:'))
# for num in range(1, lent+1):
#     for ren in range(num+1, num+2):
#         fact = fact*ren
#     summ += fact
#     print('Факториал от числа', num, ' равен', fact)
# print('Сумма равна', summ)


summ = 0
fact=1
lent = int(input('Введите количество чисел:'))
for num in range(1, lent+1):
    fact = fact*(num)
    summ += fact
    print('Факториал от числа', num, ' равен', fact)
print('Сумма равна', summ)

from random import randint

# n = randint(2, 15)
# total = 0
# for num in range(1, n+1):
#     factorial = 1
#     print(f'{num}! = ', end=' ')
#     for multiplier in range(1, n):
#         if num > multiplier:
#             factorial *= multiplier+1
#     total += factorial
#     print(factorial)
# print(f'Итого: {total}')

