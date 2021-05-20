def dig(enclosed):
    total = []
    for i in enclosed:
        total.extend(i)
    return total


nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

opened = dig([dig(x) for x in nice_list])

print(opened)
