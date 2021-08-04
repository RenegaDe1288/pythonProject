import random

class Primes:

    def __init__(self):
        self.list = [1,2,3,4,5]
        self.len = len(self.list)
        self.count = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.len >= self.count:
            self.count += 1
            x = random.randint(1,2)+self.list[-1]
            self.list.append(x)
            return x
        else:
            raise StopIteration


prime_nums = Primes()

for i_elem in prime_nums:
    print(i_elem, end=' ')

print()
print(prime_nums.list)