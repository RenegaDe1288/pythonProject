import timeit

res: float = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)

""" Решение через map"""
res_2 = timeit.timeit('"-".join(map(str, range(100)))', number=10000)

"""Решение через list comprehenshion"""
res_3 = timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)

"""Решение через reduce"""
res_4 = timeit.timeit('reduce(lambda x,y: str(x) + str(y) + "-" , range(100))', number=10000,
                      setup="from functools import reduce")

print(res)
print(res_2)
print(res_3)
print(res_4)
