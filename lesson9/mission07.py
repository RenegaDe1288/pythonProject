for geg in range (6):
    if geg == 0 or geg == 5:
        print('-' * 10,)
    str = ''
    if 0 < geg < 5:
        for num in range(1,11):
            if num == 1 or num == 10:
                str += '|'
            else:
                str += '0'
        print(str)

print()
print()

srt_1 = '----------'
str_2 = '|00000000|'
for fer in range(6):
    if fer == 0 or fer == 5:
        print(srt_1)
    else:
        print(str_2)

# for num in range(1,11):
#     print('-')
#     if num == 1 or num == 10:
#         print('|', end= '-')
