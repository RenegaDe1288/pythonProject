import random

size = random.randint(13, 40)
count = 0
print('Размер листа ', size, size)
for count in range(size):
    if size > 12:
        size /= 2
        count += 1
        print('Листок сложе вдвое и равен', size)
        print('Количество сложений листа = ', count)
    else:
        break
print('Лист сложен в конверт')

print()
print()
print()


import random

size = random.randint(40, 140)
count = 0
print('Размер листа ', size, size)
while size > 12:
    size /= 2
    count += 1
    print('Листок сложе вдвое и равен', size)
    print('Количество сложений листа = ', count)
print('Лист сложен в конверт')



