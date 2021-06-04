string1 = 'zxclkv'
tup = (1, 2, 3, 4, 5)

generator = ((string1[i], tup[i]) for i, num in enumerate(tup))
print(generator)
generator = [print((string1[i], tup[i])) for i, num in enumerate(tup)]
