# самое чокнутое решение

def fibonacci(n):
    if n in (1, 2):
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


n = 7
print('Число с индексом {} равно : {}'.format(n, fibonacci(n)))


# мое 2 решение:

def fibon(fibo1, fibo2, count):
    if num - 1 == count:
        print('Число с индексом {} равно : {}'.format(num, fibo2))
    else:
        fibo1, fibo2 = fibo2, fibo1 + fibo2
        fibon(fibo1, fibo2, count + 1)


num = 6
count = 1
fibon(1, 1, count)

# мое 1 решение:

fib1, fib2 = 1, 1
my_list = [1, 1]
n = 10
for i in range(n - 2):
    fib1, fib2 = fib2, fib1 + fib2
    my_list.append(fib2)

print('Число с индексом {} равно : {}'.format(n, my_list[n - 1]))
