def reverse():
    n = int(input("\nВведите целое число: "))
    if n > 0:
        print('Число  наоборот: ', end='')
        while n > 0:
            rev = n % 10
            n = n // 10
            if rev > 0:
                print(rev, end='')
            elif rev == 0:
                print('', end='')
    elif n == 0:
        print('\nОперация окончена')


while True:
    reverse()
