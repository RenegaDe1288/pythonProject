n = [2, 2, 3, 4, 5, 6, 8, 6, 1, 52, 2, 1, 2, 3, 4, 6, 8, 2]
a = 1
b = 7
print(n)

m = [num for num in n[:a]] + [num for num in n[b:]]

print(m)
