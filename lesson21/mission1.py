def count(start, end):
    if end != start:
        print(start, end=' ')
        return count(start+1, end)
    else:
        print(start)


num = int(input('Введите число: '))

count(start=1, end=num)
