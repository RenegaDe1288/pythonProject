import random

puples = int(input('Введите число учеников:'))
bad = 0
mid = 0
best = 0
for number in range(1, puples + 1):
    score = random.randint(3, 5)
    if score == 3:
        bad += 1
    elif score == 4:
        mid += 1
    elif score == 5:
        best += 1
    print('Ученик: ', number, 'получил ', score)
print(bad, mid, best)
if mid < bad > best:
    print('В классе больше троечников= ', bad)
if bad < mid > best:
    print('В классе больше хорошистов= ', mid)
if mid < best > bad:
    print('В классе больше отличников= ', best)
