nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]



def dig(list):
    total = []
    for i in list:
        total.extend(i)
    return total


# new = [dig(x) for x in nice_list]
# print(new)
total = dig([dig(x) for x in nice_list])

# total = []
# for i in new:
#     total.extend(i)

print(total)