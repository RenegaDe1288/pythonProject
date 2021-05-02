# lent = int(input('Введите ширину '))
#
# for row in range(lent + 1):
#     for col in range(lent + 1):
#         if col <= lent - row:
#             print(col + row, end=('\t'))
#     print()


lent = int(input('Введите ширину '))

for row in range(lent + 1):
    for col in range(row, lent+1):
        print(col, end=('\t'))
    print()
