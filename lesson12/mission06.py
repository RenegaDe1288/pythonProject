number = int(input('Введите числовую последовательность: '))

def is_prime():
    if num == 0 or num == 1:
        print(f"Число {num} НЕ ПРОСТОЕ.")
    elif num == 2:
        print(f"Число {num} простое.")
    else:
        for i in range(2, num//2+2):
            if num % i == 0:
                check = "НЕЕЕЕЕ"
                break
            else:
                check = " "
        print(f"Число {num} {check} простое.")

for num in range (1, number+1):
    print(is_prime())