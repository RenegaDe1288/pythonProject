# n =5
# num =1
#
# print('Сначала было так\n')
# for y in range(1, n+1):
#     for x in range(n*2):
#         if x >= n - y:
#             print(x, end='')
#
#         elif x <n:
#             print(n-x, end='')
#
#         else:
#             print('.', end='')
#     print('')

# from random import randint
#
# n = randint(5, 10)

# for y in range(1, n+1):
#     for x in range(n*2):
#         if x > y-1 and y < -(x-(n*2)):
#             print(".", end='')
#         elif x < n:
#             print(-(x-n), end='')
#         elif x >= n:
#             print(x-(n-1), end='')
#     print()

n = 5
num = 1
int
print('Сначала было так\n')
for y in range(1, n + 1):
    for x in range(n):
        if x < y:
            print(n - x, end='')
    for x in range(n):
        if x >= y:
            print('..', end='')
    for x in range(n, 0,-1):
        if x <= y:
            print(n-x+1, end='')

    print()
