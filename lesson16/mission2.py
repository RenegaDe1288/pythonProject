row_1 = list(range(160, 176, 2))
row_2 = list(range(162, 180, 3))
print(row_1)
print(row_2)

row_1.extend(row_2)
print(row_1)

for i in range(len(row_1) - 1):
    for j in range(len(row_1) - i - 1):
        if row_1[j] > row_1[j + 1]:
            row_1[j], row_1[j + 1] = row_1[j + 1], row_1[j]

print(row_1)
