# class СountIterator:
#
#     count = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.count += 1
#         return self.count




def gen():
    count = 0
    while count != 500:
        yield count
        count += 1


my_iter = gen()
for i_elem in my_iter:
    print(i_elem)