strings = ['a', 'b', 'c', 'd', 'e']

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

n = list(map(lambda x, y: (x, y), strings, numbers))
print(n)
