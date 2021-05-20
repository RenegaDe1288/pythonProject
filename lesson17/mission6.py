n = [1, 0, 0, 3, 4, 4, 0, 5, 7]

n = [x for x in n if x != 0] + [0] * n.count(0)

print(n)

n = n = [x for x in n if x != 0]

print(n)

# print(new_list)
# new_list = []
# for i in n[::-1]:
#     if i == 0:
#         new_list.insert(len(new_list)+1,i)
#     else:
#         new_list.insert(0, i)


# print(new_list)
#
# new_list = [x for x in new_list if x != 0]
# print(new_list)
