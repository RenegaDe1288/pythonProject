def iteration(list):
    iterator = list.__iter__()
    while True:
        try:
            print(iterator.__next__())
        except:
            StopIteration
            break


list = [1,2,3,4,5]
iteration(list)


a = [1, 2, 3]
s = a.__iter__()
c = next(s)
print(c)