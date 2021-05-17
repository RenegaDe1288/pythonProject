# len = 7
# for row in range(4):
#     for col in range(len):
#         if col==3:
#             print('#', end='')
#         elif col == len//2-row:
#             print('#', end='')
#         elif col == len // 2 + row:
#             print('#', end='')
#
#         else:
#             print('-', end=(''))
#     print()

n = 10
#
# for x in range(1, n + 1):
#     print(' ' * -(x - n) + '$' * (x + x - 1), end='\n')
#
# print('Сначала было так\n')
# for y in range(n):
#     for x in range(n):
#         if x > y:
#             print('$' * 2, end='')
#         else:
#             print(' ', end='')
#     print('$')

print('Сначала было так\n')
for y in range(n):
    for x in range(n):
        if x >= n - y:
            print('$' *2, end='')
        else:
            print(' ', end='')
    print('$')