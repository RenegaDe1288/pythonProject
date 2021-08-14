from functools import reduce


# res_2 = list(map(int, range(1000)))
# print(res_2)
#
# res = [print(i, end=', ') for i in range(1000)]


def is_prime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n


my_list = list(filter(is_prime, range(2, 1000)))
print(my_list)

print(list(filter(None, map(lambda y: y * reduce(lambda x, y: x * y != 0,
                                                 map(lambda x, y=y: y % x, range(2, int(y**0.5 + 1))), 1),
                            range(2, 1000)))))
