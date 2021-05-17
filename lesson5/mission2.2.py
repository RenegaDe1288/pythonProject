a = int(input('Введите число 1: '))
b = int(input('Введите число 2: '))
c = int(input('Введите число 3: '))
if a > b > c:
    print(a)
elif a < b < c:
    print(c)
elif a < b > c:
    print(b)
elif a > b < c:
    if a > c:
        print(a)
    else:
        print(c)

if b < a > c:
  print('Max', a)
elif a < b > c:
  print('Max', b)
elif a < c > b:
  print('Max', c)