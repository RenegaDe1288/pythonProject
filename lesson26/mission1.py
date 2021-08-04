class CountIterator:

    def __init__(self, num: int):
        self.num = num
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self) -> int:
        if self.num > self.count:
            self.count += 1
            return self.count ** 2
        else:
            raise StopIteration


def generation(num: int):
    for i in range(1, num + 1):
        yield i ** 2


""" метод 1 через итератор"""

my_iter = CountIterator(5)
for i_elem in my_iter:
    print(i_elem, end=' ')
print()

"""метод 2 через генераторное выражение"""

gen = (num ** 2 for num in range(1, 6))
for i in gen:
    print(i, end=' ')
print()

""" метод 3 через генератор"""

list_1 = generation(5)
for i in list_1:
    print(i, end=' ')
