from functools import reduce


floats = [12.3554, 4.02, 5.777, 2.12, 3.13, 2, 11.0001]

names = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]

numbers = [22, 33, 10, 6894, 11, 2, 1]

print(list(map(lambda x: round((x ** 3), 3), floats)))

print(list(filter(lambda x: len(x) > 4, names)))

print(reduce(lambda x, y: x * y, numbers))
