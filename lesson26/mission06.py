import time

def open_file():
    with open('numbers.txt','r') as file:
        for string in file:
            sum = 0
            string = string.split()
            for i in string:
                if i.isnumeric():
                   sum += int(i)
            yield sum


start = time.time()

m = open_file()
for i in m:
    print(i)


end = time.time()
print(end - start)


# def open_file():
#     list = []
#     with open('numbers.txt','r') as file:
#         for string in file:
#             sum = 0
#             string = string.split()
#             for i in string:
#                 if i.isnumeric():
#                    sum += int(i)
#             list.append(sum)
#     return list
#
#
# start = time.time()
#
# m = open_file()
# print(m)
# for i in m:
#     print(i)
#
#
# end = time.time()
# print(end - start)