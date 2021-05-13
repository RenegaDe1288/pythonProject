def counter(x):
    count = 0
    while x > 0:
        count += 1
        x = x // 10
    return count


def reverse(x, count):
    last_digit = x % 10
    first_digit = x // 10 ** (count - 1)
    between_digits = x % 10 ** (count - 1) // 10
    first_n = last_digit * 10 ** (count - 1) + between_digits * 10 + first_digit
    return first_n


first_n = int(input("Введите первое число: "))

if counter(first_n) < 3:
    print("В первом числе меньше трёх цифр.")
else:
    count = counter(first_n)
    first_n = reverse(first_n, count)
    print('Изменённое первое число:', first_n)

second_n = int(input("\nВведите второе число: "))

if counter(second_n) < 4:
    print("Во втором числе меньше четырёх цифр.")
else:
    count = counter(second_n)
    second_n = reverse(second_n, count)
    print('Изменённое второе число:', second_n)

print('\nСумма чисел:', first_n + second_n)
